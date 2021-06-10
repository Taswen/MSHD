import csv
from app.models import Earthquake
from ftplib import FTP 


# 疑似废弃
def csv2EarthQuakes(file):
    start_id = 1
    ref_start_id = 1
    with open("file", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['Id'] = str(start_id)
            row['ReferenceId'] = str(ref_start_id)
            obj = Earthquake(row)
            print(obj.gen_sql())
            start_id += 1
            ref_start_id += 1

def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect(ftpHost, ftpUser, ftpPass)
    downloadfile(ftp, "Faint.mp4", "C:/Users/Administrator/Desktop/test.mp4")
    #调用本地播放器播放下载的视频
    os.system('start "C:\Program Files\Windows Media Player\wmplayer.exe" "C:/Users/Administrator/Desktop/test.mp4"')
    uploadfile(ftp, "C:/Users/Administrator/Desktop/test.mp4", "test.mp4")

    ftp.quit()