#!/usr/bin/env python


__author__ = "nirajKpanda"


import os
import re
import sys
import json
import argparse
import commands
import paramiko


# global variable declarations
CMD = "sudo find {} -type f -printf '%p %s\n'"


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--host",
                        help="The hostname or IP address of the server to connect",
                        required=False)
    parser.add_argument("-u", "--user",
                        help="The remote server username preferably a sudo user",
                        required=False)
    parser.add_argument("-p", "--password",
                        help="The password of the remote server user",
                        required=False)
    parser.add_argument("-f", "--filename",
    	                help="Load server credentials from configuration file, \
    	                				provide absolute path of the config file",
    	                required=False)
    parser.add_argument("-m", "--mountpoint",
    					help="Mount point of the server directory structure",
    					required=True)

    return parser.parse_args()	


def print_diskusage(data, _type="json"):
	"""
		param data: dictionary of file as key and file size in bytes as values
		param _type: print format default as json. 
		           #TODO we can implement other formats like csv, excel

		return None
	"""
	data = json.dumps(data, indent=4)
	print(data)


# not used
def get_all_files_with_path(_dir):
	all_files = []

	for dir_, subdir_, files in os.walk(_dir):
		try:
			for _file in files:
				all_files.append(os.path.join(dir_, _file))
		except OSError as e:
			continue
	return all_files


# preparing output data before jsonifing
def prepare_output(output, mountpoint):
	file_and_size_dict = dict()

	for row in output.split('\n'):
		try:
			_file , _size = row.split(' ')
			_file = re.sub('\.', mountpoint, _file)
			file_and_size_dict[_file] = int(_size)
		except ValueError as e:
			continue # unpacking issue
	
	return file_and_size_dict


# based on the user input collecting disk usage data
def get_file_and_size(host="localhost", user="", password="", mountpoint="."):
    if host == "localhost":
    	print("INFO:User requested to fetch local server file disk usage.....")
    	print("Mount point is : {}".format(mountpoint))
    	cmd = CMD.format(mountpoint)
    	status, output = commands.getstatusoutput(cmd)
    	if status == 0:
    		return prepare_output(output, mountpoint)
    	else:
    		print("ERROR:Command : {} || error status code : {}".format(cmd, status))
    elif host != "localhost" and user != "" and password != "":
    	print("INFO:User requested to fetch from remote server.")
    	print("Mount point is : {}".format(mountpoint))
    	try:
    		file_and_size_dict = dict()
    		s = paramiko.SSHClient()
    		print("SSHClient intialized....")
    		s.connect(host, 22, user, password)
    		print("SSHClient connected....")
    		(stdin, stdout, stderr) = s.exec_command(CMD.format(mountpoint))
    		if not stderr:
    			return prepare_output(stdout, mountpoint)
    		s.close()
    	except Exception as e:
    		print("ERROR:Caught exception while running command:{} in server:{};Exception : {}".
    			format(CMD.format(mountpoint), host, e))


def main():
	opts = parse_command_line()

	if opts.host == "localhost":
		file_and_size_dict = get_file_and_size(host="localhost", \
				user="", password="", mountpoint=opts.mountpoint)
	elif opts.host != "localhost" and opts.user and opts.password:
		file_and_size_dict = get_file_and_size(host=opts.host, \
			user=opts.user, password=opts.password, mountpoint=opts.mountpoint)
	elif opts.filename:
		# load server credentials from config file
		data = open(opts.filename).readlines()
		credentials = dict()
		
		for line in data:
		    key, val = line.split('=')
		    credentials[key] = val.strip()
		if credentials.get('server') and credentials.get('user') and credentials.get('password'):
		    file_and_size_dict = get_file_and_size(host=credentials.get('server'), \
				user=credentials.get('user'), password=credentials.get('password'), \
				mountpoint=opts.mountpoint)
	else:
		print("WARN:Unknown arguments.See usage : {} -h".format(sys.argv[0]))		

	# build json output to show in console
	print_diskusage(file_and_size_dict)	


if __name__ == '__main__':
	main()