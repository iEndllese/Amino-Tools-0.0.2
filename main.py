from utils import config
import aminofix
import os

#------------------------------------------------
client = aminofix.Client()
#------------------------------------------------


#------------------------------------------------
print(config.teg_tools)
print(config.script_by)
print(config.table)
inp = int(input("\nВыберите цифру: "))
#------------------------------------------------

#------------------------------------------------
if inp == 0:
	os.system("cls || clear")
	from utils import list
	pass
#------------------------------------------------

#------------------------------------------------
if inp == 1:
	os.system("cls||clear")
	from utils.DeviceId import Device
	pass
#------------------------------------------------

#------------------------------------------------	
elif inp == 2:
	os.system("cls||clear")
	from utils.sid import sid
	pass
#------------------------------------------------

#------------------------------------------------	
elif inp == 3:
	os.system("cls || clear")
	from utils.GenDev import main
	pass
#------------------------------------------------

#------------------------------------------------	
elif inp == 4:
	os.system("cls || clear")
	from utils.InviteChat import Invite
	pass
#------------------------------------------------

#------------------------------------------------
elif inp == 5:
	os.system("cls || clear")
	from utils.VipSend import main
	pass
#------------------------------------------------

#------------------------------------------------
elif inp == 6:
	os.system("cls || clear")
	from utils.TotalAss import ass
	pass
#------------------------------------------------

#------------------------------------------------
elif inp == 7:
	os.system("cls || clear")
	from utils.LikeBlog import like
	pass
#------------------------------------------------

#------------------------------------------------
elif inp == 8:
	os.system("cls || clear")
	from utils.Install import Upgrade
	pass
#------------------------------------------------

#------------------------------------------------
elif inp == 9:
	os.system("cls || clear")
	from utils.ComId import ComId
	pass
#------------------------------------------------

