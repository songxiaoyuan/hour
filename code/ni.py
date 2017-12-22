# -*- coding:utf8 -*-
import csv
import basic_fun as bf
import os
import shutil

TIME = 0
LASTPRICE = 1
MIDDLE = 2
SD = 3
RSI = 4
DIFF_VOLUME = 5
SPREAD = 6
LONG =1
SHORT =0

def main():
	# ni
	shutil.copy('../hour_config/config/350', '../hour_config/real_server/540')
	shutil.copy('../hour_config/config/350', '../hour_config/real_server/541')
	shutil.copy('../hour_config/config/350', '../hour_config/config/351')

	# pp
	shutil.copy('../hour_config/config/380', '../hour_config/real_server/544')
	shutil.copy('../hour_config/config/380', '../hour_config/real_server/545')
	shutil.copy('../hour_config/config/380', '../hour_config/config/381')

	# v
	shutil.copy('../hour_config/config/390', '../hour_config/real_server/546')
	shutil.copy('../hour_config/config/390', '../hour_config/real_server/547')
	shutil.copy('../hour_config/config/390', '../hour_config/config/391')

	# bu
	shutil.copy('../hour_config/config/420', '../hour_config/real_server/542')
	shutil.copy('../hour_config/config/420', '../hour_config/real_server/543')
	shutil.copy('../hour_config/config/420', '../hour_config/config/421')

	# al
	shutil.copy('../hour_config/config/360', '../hour_config/real_server/538')
	shutil.copy('../hour_config/config/360', '../hour_config/real_server/539')
	shutil.copy('../hour_config/config/360', '../hour_config/config/361')

	# cu
	shutil.copy('../hour_config/config/370', '../hour_config/real_server/536')
	shutil.copy('../hour_config/config/370', '../hour_config/real_server/537')
	shutil.copy('../hour_config/config/370', '../hour_config/config/371')
	shutil.copy('../hour_config/config/370', '../hour_config/config/372')
	shutil.copy('../hour_config/config/370', '../hour_config/config/373')
	shutil.copy('../hour_config/config/370', '../hour_config/config/374')
	shutil.copy('../hour_config/config/370', '../hour_config/config/375')

	# zn
	shutil.copy('../hour_config/config/340', '../hour_config/real_server/528')
	shutil.copy('../hour_config/config/340', '../hour_config/real_server/529')
	shutil.copy('../hour_config/config/340', '../hour_config/config/341')

	# pb
	shutil.copy('../hour_config/config/310', '../hour_config/real_server/532')
	shutil.copy('../hour_config/config/310', '../hour_config/real_server/533')
	shutil.copy('../hour_config/config/310', '../hour_config/config/311')

	# hc
	shutil.copy('../hour_config/config/440', '../hour_config/real_server/548')
	shutil.copy('../hour_config/config/440', '../hour_config/real_server/549')
	shutil.copy('../hour_config/config/440', '../hour_config/config/441')

	# rb
	shutil.copy('../hour_config/config/320', '../hour_config/real_server/530')
	shutil.copy('../hour_config/config/320', '../hour_config/real_server/531')
	shutil.copy('../hour_config/config/320', '../hour_config/config/321')

	# au
	shutil.copy('../hour_config/config/400', '../hour_config/real_server/550')
	shutil.copy('../hour_config/config/400', '../hour_config/real_server/551')
	shutil.copy('../hour_config/config/400', '../hour_config/config/401')

	# ag
	shutil.copy('../hour_config/config/410', '../hour_config/real_server/552')
	shutil.copy('../hour_config/config/410', '../hour_config/real_server/553')
	shutil.copy('../hour_config/config/410', '../hour_config/config/411')

if __name__=='__main__': 
	main()