from flask import Flask, render_template, request, redirect
import mysql.connector
import subprocess
import datetime
import os
import logging
from functools import wraps


#logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="a", format="%(asctime)s  ::  %(levelname)s  ::   %(message)s")



#Initializing flask application
app = Flask(__name__)



#Database details using env variables
host =os.environ.get('MYSQL_HOST')
user =os.environ.get('MYSQL_USER')
password =os.environ.get('MYSQL_PASSWORD')
database =os.environ.get('MYSQL_DB')
port =os.environ.get('DB_PORT')



# Connect to database
mysql = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)





# log actions
def log(logger):
    def wrapper(func):
        @wraps(func)
        def enable(*args, **kwargs):
            logger.info(f"Calling Function < {func.__name__} >")
            return func(*args, **kwargs)
        return enable
    return wrapper






# Route to the main page
@app.route('/')
@log(logger)
def index():
	return render_template('index.html')





# Route to the memory.html page 
@app.route('/memory.html')
@log(logger)
def memoryu():
	cur = mysql.cursor()
	resultValue = cur.execute("SELECT * FROM memoryusage")
	headers =["Time","Used Memory 'M'","Free Memory 'M'"]
	memoryu = cur.fetchall()
	return render_template('memory.html', headers=headers, memoryu=memoryu)






# Route to the disk.html page
@app.route('/disk.html')
@log(logger)
def disk_usage():
	cur = mysql.cursor()
	resultValue = cur.execute("SELECT * FROM diskusage")
	
	#Table headers
	source_disk = subprocess.check_output("df -H --output=source |sed '1d'", shell=True)
	source_disk = source_disk.decode('ascii')
	headers = ["Time ","File System","Size","Used","Available"]
	diskusage = cur.fetchall()
	return render_template('disk.html', headers=headers, diskusage=diskusage)






# Route to the cpu.html page
@app.route('/cpu.html')
@log(logger)
def cpu_usage():
	cur = mysql.cursor()
	resultValue = cur.execute("SELECT * FROM cpuusage")

	#Table headers:
	headers="   Time   CPU   %usr   %nice   %sys    %iowait  %irq   %soft   %steal   %guest   %gnice  %idle"
	cpuusage = cur.fetchall()
	return render_template('cpu.html', headers=headers, cpuusage=cpuusage)







# Collect the memory usage from the host server 
@log(logger)
def memory_us():
        used_memory = subprocess.check_output("free -m |sed '1d'| awk 'NR==1{ printf $3 }'", shell=True)
        return int(used_memory)






# Collect the free memory from the host server
@log(logger)
def memory_fr():
        free_memory = subprocess.check_output("free -m |sed '1d'| awk 'NR==1{ printf $4 }'", shell=True)
        return int(free_memory)





# Collect the time from the host server
@log(logger)
def time():
	time_date = subprocess.check_output("date", shell=True)
	return time_date.decode('ascii')





#Collect the File system structure for the host server
@log(logger)
def disk_source():
	source_disk = subprocess.check_output("df -H --output=source |sed '1d'", shell=True)
	return source_disk.decode('ascii')





#Collect the size of the File system for the host server
@log(logger)
def disk_size():
        size_disk = subprocess.check_output("df -H --output=size |sed '1d'", shell=True)
        return size_disk.decode('ascii')





#Collect the used size in the File system for the host server
@log(logger)
def disk_used():
	used_disk = subprocess.check_output("df -H --output=used |sed '1d'", shell=True)
	return used_disk.decode('ascii')




#Collect the avilable size in the File system for the host server
@log(logger)
def disk_avilable():
	avilable_disk = subprocess.check_output("df -H --output=avail |sed '1d'", shell=True)
	return avilable_disk.decode('ascii')






#Collect the CPU usage
@log(logger)
def cpu_usage():
	cpu_usage = subprocess.check_output("mpstat | sed -n '4p'", shell=True)
	return cpu_usage.decode('ascii')






#Collect the headers information of the CPU usage
@log(logger)
def cpu_usage_header():
	cpu_usage_h = subprocess.check_output("mpstat | sed -n '3p'", shell=True)
	return cpu_usage_h.decode('ascii')





	
# Add CPU statistics to cpuusage table in the database 	
@log(logger)
def add_row_cpudb(cpuUsage):
	cur = mysql.cursor()
	query= "INSERT INTO `cpuusage` (`cpuUsage`) VALUES(%s)"
	cur.execute(query, (cpuUsage,))
	mysql.commit()
	cur.close()






# Collect the CPU usage and add it to cpuusage table in the database
@log(logger)
def addCpuUsage():
	cpuUsage = cpu_usage()
	add_row_cpudb(cpuUsage)






# Add memory statistics to memoryusage table in the database
@log(logger)
def add_row_memorydb(time, usedm, freem):
	cur = mysql.cursor()
	query= "INSERT INTO `memoryusage` (`time`, `usedm`, `freem`) VALUES(%s, %s, %s)"
	cur.execute(query, (time, usedm, freem))
	mysql.commit()
	cur.close()






# Collect the memory usage and add it to memoryusage table in the database
@log(logger)
def addMemoryUsage():
	freem=memory_fr()
	usedm=memory_us()
	time_date=time()
	add_row_memorydb(time_date, usedm, freem)






# Add disk statistics to diskusage table in the database
@log(logger)
def add_row_diskdb(time, filesystem, size, usedDisk, availableDisk):
	cur = mysql.cursor()
	query= "INSERT INTO `diskusage` (`time`, `filesystem`, `size`, `usedDisk`, `availableDisk`) VALUES(%s, %s, %s, %s, %s)"
	cur.execute(query, (time, filesystem, size, usedDisk, availableDisk))
	mysql.commit()
	cur.close()






# Collect the disk usage and add it to diskusage table in the database
@log(logger)
def addDiskUsage():
	time_date=time()
	filesystem=disk_source()
	size=disk_size()
	usedDisk=disk_used()
	availableDisk=disk_avilable()
	add_row_diskdb(time_date, filesystem, size, usedDisk, availableDisk)






# Add current usage
@log(logger)
def add_current_usage():
	addMemoryUsage()	
	addDiskUsage()
	addCpuUsage()





# Add usage by cronjob 
@log(logger)
def collect_statistics():
	addMemoryUsage()
	addDiskUsage()
	addCpuUsage()





if __name__ == '__main__':
	
	# Add current usage
	add_current_usage()

	#Run the flask app
	app.run(debug=False, host="0.0.0.0")
