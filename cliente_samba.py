import uuid

from smbclient import (
    listdir,
    mkdir,
    register_session,
    rmdir,
    scandir,
)

from smbclient.path import (
    isdir,
)


server = "10.216.177.12"
port = 445
usr = "Administrator"
pwd = "T0r3r0fr"
# share = r"\\%s\ftp_tmp\ps07647" % server

share = r"\\%s\software\ISOS" % server


register_session(server,username=usr,password=pwd)
for filename in listdir(share):
    print(filename)
