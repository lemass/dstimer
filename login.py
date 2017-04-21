# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.
# SecureCRT 登录脚本, 新密码登录失败后,自动用老密码登录, 并且把密码改正为新密码.


old_admin_pwd = "Ywjn123xylz!@#"
new_admin_pwd = "yRtMHiNc0A5JNnz#"

old_root_pwd = "Ywsz098xylz!@#"
new_root_pwd = "Ywsz098xylz!@#"

crt.Screen.IgnoreCase = True
timeout = 10

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.WaitForString("Username: ", timeout)
	crt.Screen.Send("admin\r")
	crt.Screen.WaitForString("Password: ", timeout)
	crt.Screen.Send(new_admin_pwd + "\r")
	outPut = crt.Screen.WaitForStrings(["[admin@", "Authentication fail"], timeout)
        index = crt.Screen.MatchIndex
        if (index == 0):
                crt.Dialog.MessageBox ( "admin用户登录超时Timed out!")
                return
        elif (index == 1):
                pass
        elif (index == 2):
            crt.Screen.Send(old_admin_pwd + "\r")
            if (crt.Screen.WaitForString("[admin@", timeout) !=True ):
                crt.Dialog.MessageBox ( "admin登录失败")
                return
            crt.Screen.Send("export LC_ALL='C'\r")
            crt.Screen.Send("passwd\r")
            crt.Screen.WaitForString("current", timeout)
            crt.Screen.Send(old_admin_pwd + "\r")
            crt.Screen.WaitForString("New")
            crt.Screen.Send(new_admin_pwd + "\r")
            crt.Screen.WaitForString("Retype", timeout)
            crt.Screen.Send(new_admin_pwd + "\r")
            crt.Screen.WaitForString("updated", timeout)
	crt.Screen.Send("export LC_ALL='C'\r")
        
	crt.Screen.Send("su -\r")
	crt.Screen.WaitForString("Password: ", timeout)
	crt.Screen.Send(new_root_pwd + "\r")
	outPut = crt.Screen.WaitForStrings(["[root@", "Authentication fail"], timeout)
        index = crt.Screen.MatchIndex
        if (index == 0):
            crt.Dialog.MessageBox ( "Timed out!")
            return
        elif (index == 1):
                pass
        elif (index == 2):
	    crt.Screen.Send("su -\r")
	    crt.Screen.WaitForString("Password: ", timeout)
            crt.Screen.Send(old_root_pwd + "\r")
            if (crt.Screen.WaitForString("[root@", timeout) != True):
                crt.Dialog.MessageBox("不能su到root!")
                return
            crt.Screen.Send("export LC_ALL='C'\r")
            crt.Screen.Send("passwd\r")
            crt.Screen.WaitForString("current")
            crt.Screen.Send(old_root_pwd + "\r")
            crt.Screen.WaitForString("New", timeout)
            crt.Screen.Send(new_root_pwd + "\r")
            crt.Screen.WaitForString("Retype", timeout)
            crt.Screen.Send(new_root_pwd + "\r")
            crt.Screen.WaitForString("updated", timeout)
        crt.Screen.Send("export LC_ALL='zh_CN.UTF-8'\r")
Main()
