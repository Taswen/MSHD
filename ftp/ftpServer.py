import os
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

from .config.setting import *



class MyFTPHandler(FTPHandler):  
    def on_connect(self):#链接时调用 
        print("%s:%s connected" % (self.remote_ip, self.remote_port)) 

    def on_disconnect(self):#关闭连接是调用 
        # do something when client disconnects 
        pass 

    def on_login(self, username):#登录时调用 
        # do something when user login 
        pass 

    def on_logout(self, username):#登出时调用 
        # do something when user logs out 
        pass 

    def on_file_sent(self, file):#文件下载后调用 
        # do something when a file has been sent 
        pass 

    def on_file_received(self, file):#文件上传后调用 
        # do something when a file has been received 
        pass 

    def on_incomplete_file_sent(self, file):#下载文件时调用 
        # do something when a file is partially sent 
        pass 

    def on_incomplete_file_received(self, file):#上传文件时调用 
        # remove partially uploaded files 
        import os 
        os.remove(file) 




class MyFTPServer():
    def __init__(self) -> None:
        # 实例化用户授权管理 
        self.__authorizer = DummyAuthorizer() 
        self.__authorizer.add_user('user', '12345', './', perm='elradfmwMT')#添加用户 参数:username,password,允许的路径,权限 
        #这里是允许匿名用户,如果不允许删掉此行即可 
        self.__authorizer.add_anonymous(os.getcwd())

        # 实例化FTPHandler 
        self.__handler = MyFTPHandler 
        self.__handler.authorizer = self.__authorizer 


        #handler.masquerade_address = '151.25.42.11'#指定伪装ip地址 
        #handler.passive_ports = range(60000, 65535)#指定允许的端口范围 

        self.__address = ("0.0.0.0", 21)#FTP一般使用21,20端口 
        self.__server = FTPServer(self.__address, self.__handler)#FTP服务器实例 

        # set a limit for connections 
        self.__server.max_cons = 256
        self.__server.max_cons_per_ip = 5
        
    def run(self):
        # 开启服务器 
        self.__server.serve_forever()

    def loadSetting(self):
        # 设定一个客户端链接时的标语 
        self.__handler.banner = WEB_BANNER


if __name__ == "__main__":
    server = MyFTPServer()
    server.run()

# authorizer = DummyAuthorizer()
# authorizer.add_user('admin', '123456', 'F:\\Working~Study', perm='elradfmwM')
# handler = FTPHandler
# handler.authorizer = authorizer

# server = FTPServer(('0.0.0.0', 8888), handler)
# server.serve_forever()