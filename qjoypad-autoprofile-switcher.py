#!/usr/bin/python3
# -*- encoding: utf-8 -*-
''' This module launchs and kills automatically qjoypad when a joystick 0 is plugged or unplugged.
	it iterates every 10 seconds to check the joystick 0

	it can also change between qjoypad profiles upon a running process name,
	so give this script a dictionary of procesess and qjoypad profiles, and this script
	will change from the default profile to the process specified profile if the process is running

	'''

import os, time  # Checks if joystick is registered in the system.
from subprocess import check_output  # Checks if a process is active or not

## User Variables ##
AppProfileDict = {'process_name':'profilename',}  # dictionary of process and profiles
DefaultProfile = 'Kodi Cursors'  # Default profile when Joystick 0 is present
Shutdownqjoypad = True  # This option will shudown qjoypad if no joystick 0 is found.



## Internal Script variables ##
joydevice = '/dev/input/js0' # Device to supervise
sleepseconds = 10			 # seconds to sleep on every iteration
qjoypad = 'qjoypad'			 # qjoypad process

def get_pid (app):
	''' returns None if the aplication is not running, or
		returns application PID if the aplication is running 
		'''
	try:
		pids = check_output(["pidof", app ])
	except:
		#logging.debug('no %s app is currently running'%(app))
		return None
	pidlist = pids.split()
	la = lambda x : int(x)
	pidlist = list (map (la , pidlist))
	return pidlist

def getappstatus (app):
	''' Given a list of proces's names, it checks if there is any instance running
		DefTest >> OK'''
	state = False
	if not (app == None or app == ''):
		for entry in app:
			if get_pid (entry) != None:
				state = True
	return state


if __name__ == '__main__':
	activeapp = None
	while True:
		if os.path.exists (joydevice):
			if not getappstatus ([activeapp]):
				assigned = False
				for app in AppProfileDict:
					if getappstatus([app]) and app != activeapp:
						activeapp = app
						assigned = True
						break
				if activeapp == None or (not assigned and activeapp != ''):
					selectprofile = '"'+DefaultProfile+'"'
					activeapp = ''
					assigned = True
					#print ('Default profile selected')
				elif activeapp != '':
					selectprofile = '"'+AppProfileDict[activeapp]+'"'
					#print ('{} profile selected ({})'.format(app,AppProfileDict[app]))
				if assigned:
					cmdline = ' '.join([qjoypad,selectprofile]) + ' &'
					os.system (cmdline)
					#print ('Changed qjoypad profile: {}'.format(cmdline))
					time.sleep (sleepseconds)
		else:
			#print ('No joystick is attached.')
			if getappstatus ([qjoypad]) and Shutdownqjoypad:
				qjoypad_pid = get_pid (qjoypad)
				os.system ('kill {}'.format(qjoypad_pid[0]))
				#print ('qjoypad has been killed so no joystick is attached.')
				activeapp = None
		#print ('Waitting {} seconds'.format (sleepseconds),'\n\n')
		time.sleep (sleepseconds)