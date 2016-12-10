import sys,os
import zipfile
import random
import time
from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, password,*args, **kwargs):
    	if(password != "ankisaif"):
    		return
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

    def run_this_veryimp_function(self):
    	print("Please don't use this class it is for internal use")


class unzipbomb():

	def __init__(self):
		self.__rootfolder = None
		self.__error_log = []
		self.__count = 0
		self.__destination = None
		self.__password = "1234"
		self.__start_time = 0
		self.__timer = 0
		self.__option = True
		self.__timerpass = "ankisaif"

	def __countdowntimer(self):
		print(str(self.__timer)+"\r")
		self.__timer += 1
	
	def showroot(self):
		if(self.__rootfolder is None):
			print("No root folder is set")
			return
		return self.__rootfolder

	def suppresstimer(self,option=True):
		self.__option = False

	def showerrorlog(self):
	
		if len(self.__error_log) == 0:
			print("No errors are there to display")
			return
		return self.__error_log

	def clearerrorlog(self):
		self.__error_log = []

	def __adderror(self,pwd,filename,e):
		if(pwd != "1234"):
			return
		temp = {"filename":filename, "error":e}
		self.__error_log.append(temp)

	def showdestination(self):

		if self.__destination is None:
			print("No Destination set")
			return
		return self.__destination

	def showcount(self):
		return self.__count

	def resetcount(self):
		self.__count = 0

	def setrootfolder(self,rootfolder):

		if os.path.exists(rootfolder):
			self.__rootfolder = rootfolder
			return rootfolder + " was set as the root folder"
		else:
			return "No such path exists"

	def setdestinationfolder(self,destination):
		self.__destination = destination
		return destination + " was set as the destination folder"


	def __isrootfolderset(self):
		if self.__rootfolder is None:
			return False
		else:
			return True
	def __isdestinationset(self):
	 	if self.__destination is None:
	 		return False
	 	else:
	 		return True

	def unzipbomb(self):
		if self.__isrootfolderset() == False:
			return "No root folder set"
		if self.__isdestinationset() == False:
			return "No destination folder set"
		print("---------------starting---------------")
		outpath = self.__destination
		self.__start_time = time.time()
		if(self.__option == True):
			rt = RepeatedTimer(1, self.__countdowntimer,self.__timerpass)
		try:
			for path, subdirs, files in os.walk(self.__rootfolder):
				for name in files:
					k=os.path.join(path, name)
					fh = open(k, 'r')
					try:
						z=zipfile.ZipFile(fh)
					except Exception as e:
						self.__adderror(self.__password,fh.name,str(e))
						continue
					self.__count += len(z.namelist()) - 1
					listnames = z.namelist()
					listnames.pop(0)
					for n in listnames:
						if n.split('.')[-1]=="zip":
							try:
								z.extract(n,self.__rootfolder)
								files.append(n)
							except Exception as e:
								self.__adderror(self.__password,fh.name,str(e))
						else:
							try:
								z.extract(n, outpath)
							except Exception as e:
								self.__adderror(self.__password,fh.name,str(e))
								continue

			
					fh.close()
		except:
			rt.stop()
			print("some error occured try again please")
			return
		if(self.__option == True):
			rt.stop()
		a = str(time.time() - self.__start_time)
		self.__timer = 0
		print("---------------time elapsed "+a +" ---------------" )

