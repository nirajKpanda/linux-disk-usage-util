import os
import unittest
import get_diskusage


class BasicTests(unittest.TestCase):
	def test_local_host_happyPath(slef):
		data = get_diskusage.get_file_and_size(host="localhost",
			user="", 
			password="", 
			mountpoint="/tmp")
		self.assertNotIsInstance(data, list)

	def test_path_not_accessible(slef):
		data = get_diskusage.get_file_and_size(host="localhost",
			user="", 
			password="", 
			mountpoint="/root")
		self.assertRaises(Exception, data)

	def test_directory_not_found(self):
		data = get_diskusage.get_file_and_size(host="localhost",
			user="", 
			password="", 
			mountpoint="/tmp1")
		self.assertRaises(Exception, data)

	def test_boundry_values(self):
		pass


class UtilTester(unittest.TestCase):
	def testPrintMehod(self):
		self.assertIsNone(get_diskusage.print_diskusage({'/tmp/a':0}))

	def testListPWDFiles(self):
		data = get_diskusage.get_file_and_size()
		self.assertNotIsInstance(data, list)

	def testRemoteSSHFail(self):
		data = get_diskusage.get_file_and_size(host="1.2.3.4",
			user="abcd", 
			password="abcd", 
			mountpoint="/tmp")
		self.assertRaises(Exception, data)

	def testTypeError(self):
		data = get_diskusage.prepare_output('ABCD', '.')
		self.assertRaises(TypeError, data)


class PerformaceTest(unittest.TestCase):
	def test_recursive(self):
		for obj in os.listdir(os.path.expanduser('~')):
			_dir = os.path.expanduser('~') + '/' + obj
			if os.path.isdir(obj):
				data = get_diskusage.get_file_and_size(host="localhost",
					user="", 
					password="", 
					mountpoint=_dir)
				self.assertNotIsInstance(data, list)
			else:
				data = get_diskusage.get_file_and_size(host="localhost",
					user="", 
					password="", 
					mountpoint=_dir)
				self.assertRaises(Exception, data)


if __name__ == '__main__':
	unittest.main()