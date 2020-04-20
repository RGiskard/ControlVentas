import os
class SenderSMS:
	def __init__(self,version):
		self.__comandsBaseLeft={\
		6:"adb shell service call isms 7 i32 1 s16 \"com.android.mms\" s16 \"",\
		7:"adb shell service call isms 7 i32 1 s16 \"com.android.mms\" s16 \"",\
		8:"adb shell service call isms 7 i32 0 s16 \"com.android.mms.service\" s16 \""}
		self.__comandsBaseRight={\
		6:"\" s16 \"null\" s16 \"null\"",\
		7:"\" s16 \"null\" s16 \"null\"",\
		8:"\" s16 \"null\" s16 \"null\""}
		self.__comandsBasemiddle={\
		6:"\" s16 \"null\" s16 \"",\
		7:"\" s16 \"null\" s16 \"",\
		8:"\" s16 \"null\" s16 \""}
		self.__androidVersion=version;
		self.__versionkey=int(version[0:version.find('.')])
	def sendSMS(self,number,body):
		comand=self.__comandsBaseLeft[self.__versionkey]+number+self.__comandsBasemiddle[self.__versionkey]\
		+body+self.__comandsBaseRight[self.__versionkey]
		os.system(comand)


def prepareSMS(smsbody):
	smsPrepared=smsbody.replace(' ','\32')
	return smsPrepared

