#Import the application file app.py && unittest module
try:
        from app import *
        import unittest
except Exception as e:
        print(f"Modules are missing :{e}")


class AppTest(unittest.TestCase):


        #Check The Response for index page:
        def test_index(self):
                """ Check if the Response is 200 for index page"""
                index_test = app.test_client(self)
                response = index_test.get('/')
                statuscode = response.status_code
                self.assertEqual(statuscode, 200)



        #Check The Response for cpu page:
        def test_cpu_page(self):
                """ Check if the Response is 200 for cpu page"""
                cpu_test = app.test_client(self)
                response = cpu_test.get('/cpu.html')
                statuscode = response.status_code
                self.assertEqual(statuscode, 200)




        #Check The Response for disk page:
        def test_disk_page(self):
                """ Check if the Response is 200 for disk page"""
                disk_test = app.test_client(self)
                response = disk_test.get('/disk.html')
                statuscode = response.status_code
                self.assertEqual(statuscode, 200)




        #Check The Response for memory page:
        def test_memory_page(self):
                """ Check if the Response is 200 for memory page"""
                memory_test = app.test_client(self)
                response = memory_test.get('/memory.html')
                statuscode = response.status_code
                self.assertEqual(statuscode, 200)



        #Check function memory_us():
        def test_memory_us(self):
                """used memory should be an integer value"""
                self.assertEqual(type(memory_us()),int)



        #Check function memory_fr():
        def test_memory_fr(self):
                """free memory should be an integer value"""
                self.assertEqual(type(memory_fr()),int)



        #Check function time():
        def test_time(self):
                """ time shouldn't be a None value"""
                self.assertIsNotNone(time())



        #Check function disk_source():
        def test_disk_source(self):
                """ disk source shouldn't be a None value"""
                self.assertIsNotNone(disk_source())



        #Check function disk_size():
        def test_disk_size(self):
                """ disk size shouldn't be a None value"""
                self.assertIsNotNone(disk_size())



        #Check function disk_used():
        def test_disk_used(self):
                """ Used disk shouldn't be a None value"""
                self.assertIsNotNone(disk_used())



        #Check function disk_avilable():
        def test_disk_avilable(self):
                """ Avilable disk size  shouldn't be a None value"""
                self.assertIsNotNone(disk_avilable())



        #Check function cpu_usage():
        def test_cpu_usage(self):
                """ Cpu usage  shouldn't be a None value"""
                self.assertIsNotNone(cpu_usage())


        #Check function cpu_usage_header():
        def test_cpu_usage_header(self):
                """ Cpu usage header shouldn't be a None value"""
                self.assertIsNotNone(cpu_usage_header())



        #setUp Method for memory usage:
        def setUpMemory(self):
                """setUpMemory Method to add a test recorde to memoryusage Table"""
                add_row_memorydb(time=0, usedm=0, freem=0)


        #setUp Method for cpu usage:
        def setUpCpu(self):
                """setUpCpu Method to add a test recorde to cpuusage Table"""
                add_row_cpudb(cpuUsage=0)



        #setUp Method for disk usage:
        def setUpDisk(self):
                """setUpDisk Method to add a test recorde to diskusage Table"""
                add_row_diskdb(time=0, filesystem=0, size=0, usedDisk=0, availableDisk=0)



        #tearDown for memory usage:
        def tearDownMemory(self):
                """tearDown Method to delete the test recorde from the memoryusage Table """
                cur = mysql.cursor()
                cur.execute("Delete FROM memoryusage where time='0' and usedm=0 and freem=0")
                mysql.commit()
                cur.close()



        #tearDown for cpu usage:
        def tearDownCpu(self):
                """tearDown Method to delete the test recorde from the cpuusage Table """
                cur = mysql.cursor()
                cur.execute("Delete FROM cpuusage where cpuUsage='0'")
                mysql.commit()
                cur.close()



        #tearDown for disk usage:
        def tearDownDisk(self):
                """tearDown Method to delete the test recorde from the diskusage Table """
                cur = mysql.cursor()
                cur.execute("Delete FROM diskusage where time='0' and filesystem='0' and size='0' and usedDisk='0' and availableDisk='0'")
                mysql.commit()
                cur.close()




        #Test the adding to the memoryusage Table in the database
        def test_memoryadd(self):
                self.setUpMemory()
                test_recorde=('0',0,0)
                cur = mysql.cursor()
                resultValue = cur.execute("SELECT time,usedm,freem FROM memoryusage")
                memoryu = cur.fetchall()
                self.assertIn(test_recorde, memoryu)
                self.tearDownMemory()


        #Test the adding to the cpuusage Table in the database
        def test_cpuadd(self):
                self.setUpCpu()
                test_recorde=('0',)
                cur = mysql.cursor()
                resultValue = cur.execute("SELECT cpuUsage FROM cpuusage")
                cpuu = cur.fetchall()
                self.assertIn(test_recorde, cpuu)
                self.tearDownCpu()



        #Test the adding to the diskusage Table in the database
        def test_diskadd(self):
                self.setUpDisk()
                test_recorde=('0','0','0','0','0')
                cur = mysql.cursor()
                resultValue = cur.execute("SELECT time, filesystem, size, usedDisk, availableDisk FROM diskusage")
                disku = cur.fetchall()
                self.assertIn(test_recorde, disku)
                self.tearDownDisk()





if __name__ == "__main__":
        #run the unittest
        unittest.main()
