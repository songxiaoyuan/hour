#-*- coding:utf8 -*-
import csv
import basic_fun as bf
import os
import cx_Oracle  
import time
import shutil

LASTPRICE = 4
VOLUME = 11
OPENINTEREST = 13
TURNONER = 12
BIDPRICE1 = 22
BIDPRICE1VOLUME = 23
ASKPRICE1 =24
ASKPRICE1VOLUME =25
TIME = 20
LONG =1
SHORT =0

date = time.strftime('%Y%m%d',time.localtime(time.time()))
hour = time.strftime('%H',time.localtime(time.time()))

# 这个是铅的
param_dict_pb = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":5,"file":file,"config_file":310}
# 这个是螺纹钢的
param_dict_rb = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":320}

# 这个是橡胶的
param_dic_ru = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":330}

# 这个是锌的
param_dic_zn = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":5,"file":file,"config_file":340}

param_dic_ni = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":1,"file":file,"config_file":350}

param_dic_al = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":5,"file":file,"config_file":360}

param_dict_cu = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":5,"file":file,"config_file":370}
param_dict_pp = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":5,"file":file,"config_file":380}
param_dict_v = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":5,"file":file,"config_file":390}
param_dict_au = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":1000,"file":file,"config_file":400}
param_dict_ag = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":15,"file":file,"config_file":410}
param_dict_bu = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":420}

param_dict_i = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":100,"file":file,"config_file":430}
param_dict_hc = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":440}
param_dict_j = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":100,"file":file,"config_file":450}
param_dict_jm = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":60,"file":file,"config_file":460}
param_dict_y = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":470}
param_dict_p = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":480}
param_dict_c = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":490}
param_dict_a = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":500}
param_dict_m = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":510}
param_dict_cs = {"rsi_period":14,"limit_ema_tick_5":60,"limit_ema_tick_1":120,
			"multiple":10,"file":file,"config_file":520}

nameDict = {
	"rb1805":{"param":param_dict_rb},
	"ru1801":{"param":param_dic_ru},
	"zn1801":{"param":param_dic_zn},
	"cu1801":{"param":param_dict_cu},
	"ni1805":{"param":param_dic_ni},
	"al1802":{"param":param_dic_al},
	"pp1805":{"param":param_dict_pp},
	"v1805":{"param":param_dict_v},
	"au1806":{"param":param_dict_au},
	"ag1806":{"param":param_dict_ag},
	"bu1806":{"param":param_dict_bu},
	"i1805":{"param":param_dict_i},
	"hc1805":{"param":param_dict_hc},
	"j1801":{"param":param_dict_j},
	"jm1801":{"param":param_dict_jm},
	"y1801":{"param":param_dict_y},
	"p1805":{"param":param_dict_p},
	"c1801":{"param":param_dict_c},
	"a1801":{"param":param_dict_a},
	"m1805":{"param":param_dict_m},
	"cs1801":{"param":param_dict_cs},
	"pb1801":{"param":param_dict_pb}
}

class BandAndTrigger(object):
	"""docstring for BandAndTrigger"""
	def __init__(self,param_dic):
		super(BandAndTrigger, self).__init__()

		self._write_to_csv_data = []

		self._pre_md_price = []
		self._now_md_price = []
		self._lastprice_array = []


		self._pre_ema_val_60 = 0
		self._now_middle_60 =0

		self._pre_ema_val_5 = 0
		self._now_middle_5 = 0
		self._now_ema_tick_5 = 0
		self._limit_ema_tick_5 = param_dic["limit_ema_tick_5"]

		self._pre_ema_val_1 = 0
		self._now_middle_1 = 0
		self._now_ema_tick_1 = 0
		self._limit_ema_tick_1 = param_dic["limit_ema_tick_1"]

		self._ema_period = 20
		self._minute_num = 0
		self._limit_minute_num = 60
		self._current_minute = -1

		self._multiple = param_dic["multiple"]

		self._rsi_period = param_dic["rsi_period"]
		self._rsi_val = 0

		self._file = param_dic["file"]
		self._config_file = param_dic["config_file"]

		if len(self._lastprice_array) ==0:
			print "this is init function " + str(self._config_file)
			tmp_pre_ema_array_60 = []
			tmp_pre_ema_array_5 = []
			tmp_pre_ema_array_1 = []
			config_file = "../hour_config/config/"+str(self._config_file)
			bf.get_config_info(tmp_pre_ema_array_60,tmp_pre_ema_array_5,tmp_pre_ema_array_1,self._lastprice_array,config_file)
			if len(tmp_pre_ema_array_60)==0:
				self._pre_ema_val_60 = 0
				self._pre_ema_val_5 = 0
				self._pre_ema_val_1 = 0
			else:
				self._pre_ema_val_60 = tmp_pre_ema_array_60[0]
				self._pre_ema_val_5 = tmp_pre_ema_array_5[0]
				self._pre_ema_val_1 = tmp_pre_ema_array_1[0]
		# print self._pre_ema_val_60
		print len(self._lastprice_array)
		# print "the length of lastprice is: " +str(len(self._lastprice_array))


	# get the md data ,every line;
	def get_md_data(self,md_array,lastone):
		# tranfer the string to float
		# md_array[LASTPRICE] = float(md_array[LASTPRICE])
		# md_array[VOLUME] = float(md_array[VOLUME])
		# md_array[OPENINTEREST] = float(md_array[OPENINTEREST])
		# md_array[TURNONER] = float(md_array[TURNONER])
		# md_array[BIDPRICE1] = float(md_array[BIDPRICE1])
		# md_array[ASKPRICE1] = float(md_array[ASKPRICE1])

		self._pre_md_price = self._now_md_price
		self._now_md_price = md_array

		lastprice = self._now_md_price[LASTPRICE]
		# self._lastprice_array.append(lastprice)
		# print lastprice
		if len(self._pre_md_price) ==0:
			# "the is the first line data"
			return

		if self._pre_ema_val_60 ==0:
			self._pre_ema_val_60 = lastprice
			self._pre_ema_val_5 = lastprice
			self._pre_ema_val_1 = lastprice
		self._now_middle_60 = bf.get_ema_data(lastprice,self._pre_ema_val_60,self._ema_period)
		self._now_middle_5 = bf.get_ema_data(lastprice,self._pre_ema_val_5,self._ema_period)
		self._now_middle_1 = bf.get_ema_data(lastprice,self._pre_ema_val_1,self._ema_period)
		
		self._sd_val = bf.get_sd_data(lastprice,self._lastprice_array,self._ema_period)
		self._rsi_val = bf.get_rsi_data(lastprice,self._lastprice_array,self._rsi_period)

		if lastone == True:
			self._pre_ema_val_60 = self._now_middle_60
			self._lastprice_array.append(lastprice)
			return True
		minute = int(self._now_md_price[TIME].split(':')[1])
		if minute != self._current_minute:
			self._current_minute = minute
			self._minute_num +=1
			if self._minute_num >= self._limit_minute_num:
				self._minute_num =0
				self._pre_ema_val_60 = self._now_middle_60
				self._lastprice_array.append(lastprice)
		if self._now_ema_tick_1 >= self._limit_ema_tick_1:
			self._now_ema_tick_1 = 0
			self._pre_ema_val_1 = self._now_middle_1
		else:
			self._now_ema_tick_1 +=1
		if self._now_ema_tick_5 >= self._limit_ema_tick_5:
			self._now_ema_tick_5 = 0
			self._pre_ema_val_5 = self._now_middle_5
		else:
			self._now_ema_tick_5 +=1

		diff_volume = self._now_md_price[VOLUME] - self._pre_md_price[VOLUME]
		diff_interest = self._now_md_price[OPENINTEREST] - self._pre_md_price[OPENINTEREST]
		diff_turnover = self._now_md_price[TURNONER] - self._pre_md_price[TURNONER]

		if diff_volume != 0 and (self._pre_md_price[ASKPRICE1] - self._pre_md_price[BIDPRICE1]) !=0:
			avg_price = float(diff_turnover)/diff_volume/self._multiple
			spread = 100*(avg_price - self._pre_md_price[BIDPRICE1])/(self._pre_md_price[ASKPRICE1] - self._pre_md_price[BIDPRICE1])
		else:
			spread = 50


		tmp_to_csv = [self._now_md_price[TIME],self._now_md_price[LASTPRICE],
					round(self._now_middle_60,2),round(self._now_middle_5,2),round(self._now_middle_1,2),round(self._sd_val,2),
					round(self._rsi_val,2),round(diff_volume,2),round(spread,2)]
		# print tmp_to_csv
		self._write_to_csv_data.append(tmp_to_csv)

		return True

	def get_to_csv_data(self):
		return self._write_to_csv_data


def getSortedData(data):
	ret = []
	night = []
	zero = []
	day = []
	nightBegin = 21*3600
	nightEnd = 23*3600+59*60+60
	zeroBegin = 0
	zeroEnd = 9*3600 - 100
	dayBegin = 9*3600
	dayEnd = 15*3600

	for line in data:
		# print line
		timeLine = line[20].split(":")
		# print timeLine
		try:
			nowTime = int(timeLine[0])*3600+int(timeLine[1])*60+int(timeLine[2])
		except Exception as e:
			nowTime = 0

		if nowTime >= zeroBegin and nowTime <zeroEnd:
			zero.append(line)
		elif nowTime >= dayBegin and nowTime <= dayEnd:
			day.append(line)
		elif nowTime >=nightBegin and nowTime <=nightEnd:
			night.append(line)
		# if int(line[22]) ==0 or int(line[4]) ==3629:
		# 	continue
	night = sorted(night, key = lambda x: (x[20], int(x[21])))
	zero = sorted(zero, key = lambda x: (x[20], int(x[21])))
	day = sorted(day, key = lambda x: (x[20], int(x[21])))
	if int(hour) >= 15:
		print "this is afternoon dont need the night data"
	else:	
		for line in night:
			ret.append(line)
		for line in zero:
			ret.append(line)
	for line in day:
		ret.append(line)

	return ret

def start_create_config(instrumentid,data):
	print "start create the config file of " + instrumentid
	if instrumentid not in nameDict:
		print "the instrument id " + instrumentid + " is not in the dict"
	param =  nameDict[instrumentid]["param"]
	bt = BandAndTrigger(param)
	if len(data) <=0:
		return
	for row in data[0:-1]:
		bt.get_md_data(row,0)
		# tranfer the string to float\
	row = data[-1]
	bt.get_md_data(row,1)
	# bt.create_config_file()

	# if int(hour)>=15:
	data = bt.get_to_csv_data()

	path_new = "../everydayoutdata/"+instrumentid+'_'+date+ "_band_data"+".csv"
	bf.write_data_to_csv(path_new,data)


def copy_file_one_to_one(from_path,to_path):
	for root, dirs, files in os.walk(from_path):
	    for file in files:
    		tmp_path = os.path.join(root,file)
    		# print tmp_path
    		shutil.copy(tmp_path, to_path+file)

def copy_file_to_save():
	path = "../hour_config/save_config_file/"
	new_path = os.path.join(path, date)
	if not os.path.isdir(new_path) and os.path.isdir(path):
	    os.mkdir(new_path)
	copy_file_one_to_one("../hour_config/config/",new_path+'/')

def main():
	# instrumentid_array = ["pb1801","bu1712"]
	# instrumentid_array1 = ["rb1805","ru1801","zn1801","cu1801","al1802","ni1805","pp1805","v1805","au1806","ag1806","pb1801","bu1806"]
	# instrumentid_array2 = ["j1801","jm1801","m1805","cs1801","c1801","a1801","i1805","hc1805","y1801","p1805"]
	# instrumentid_array = instrumentid_array1 + instrumentid_array2

	conn = cx_Oracle.connect('hq','hq','114.251.16.210:9921/quota')    
	# conn = cx_Oracle.connect('hyqh','hyqh','192.168.1.15:1521/asp')    

	cursor = conn.cursor()

	
	for instrumentid in instrumentid_array:
		# first get the sql data
		mysql="select * from hyqh.quotatick where TRADINGDAY = '%s' AND INSTRUMENTID = '%s'" % (str(date),instrumentid)
		# mysql="select *from hyqh.test where TRADINGDAY = '%s' AND INSTRUMENTID = '%s' " % (str(date),instrumentid)

		print mysql
		cursor.execute (mysql)  
		icresult = cursor.fetchall()

		cleandata = getSortedData(icresult)
		start_create_config(instrumentid,cleandata)

	cursor.close ()  
	conn.close () 

	copy_file()
	if int(hour)<9:
		copy_file_to_save()


if __name__=='__main__':
	main()
	# copy_file()