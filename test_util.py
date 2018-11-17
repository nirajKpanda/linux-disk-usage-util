import unittest
import get_diskusage


class UtilTester(unittest.TestCase):
	def testPrintMehod(self):
		self.assertIsNone(get_diskusage.print_diskusage({'/tmp/a':0}))

	def testListPWDFiles(self):
		data = get_diskusage.get_file_and_size()
		self.assertNotIsInstance(data, list)

	def testLocalHostHappyPath(self):
		data = get_diskusage.get_file_and_size(host="localhost",
			user="", 
			password="", 
			mountpoint="/tmp")
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


if __name__ == '__main__':
	unittest.main()