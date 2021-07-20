import struct
import socket
import ctypes
import time

class ComProtocol(object):
    CarID = 1
    Tem_Left_Front = 400
    Tem_Left_Back = 100
    Tem_Right_Front = 200
    Tem_Right_Back = 300
    CO_param = 25

    def __init__(self,ID,TLF,TLB,TRF,TRB,COP):
        self.CarID = ID
        self.Tem_Left_Front = TLF
        self.Tem_Left_Back = TLB
        self.Tem_Right_Front = TRF
        self.Tem_Right_Back = TRB
        self.CO_param = COP

    def ReturnAllData(self):
        return (self.CarID, self.Tem_Left_Front, self.Tem_Left_Back, self.Tem_Right_Front, self.Tem_Right_Back, self.CO_param)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.8', 6000))
print("LinkSuc")

while True:
    DataP = ComProtocol(ID=1, TLF=10, TLB=20, TRF=40, TRB=40, COP=25)
    Values = DataP.ReturnAllData()
    StructF = struct.Struct('iiiiii')
    data = StructF.pack(*Values)
    # 发送数据
    client.send(data)
    time.sleep(1)

client.close()