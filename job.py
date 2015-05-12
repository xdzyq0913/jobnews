#!/usr/bin/env python 
#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import sys
import re

sys.setrecursionlimit(15000) #用美丽汤而无奈添加这句。。

XDUaddress = 'http://job.xidian.edu.cn/html/zpxx/jobs/'
HDUaddress = 'http://career.hdu.edu.cn/f/l/41'
ZJUTaddress = 'http://job.zjut.edu.cn/job/IndexMotion!ListJobMore?type=2'
XJTUaddress = 'http://job.xjtu.edu.cn/jobmore.do?page=1&ext=&sign=8'
NWPUaddress = 'http://job.nwpu.edu.cn/jobInfoList.do?ext=1'

class Job():
    def GetHtml(self,html):
       req = urllib2.Request(html)
       resp = urllib2.urlopen(req)
       respHtml = resp.read()
       return respHtml
    
    def XDU(self):
       print '=========================='
       print '来自西电的消息：'
       XDUhtml = BeautifulSoup(self.GetHtml(XDUaddress))
       XDUnews = XDUhtml.find_all(name = "a", attrs={"target":"_blank"})      
       for i in range(0,25):
           print XDUnews[i].string

    def HDU(self):
        print '=========================='
        print '来自杭电的消息：'
        reg = r'<a href="/f/v/.*<'
        HDUhtml = self.GetHtml(HDUaddress)
        HDUre = re.compile(reg)
        HDUquery = re.findall(HDUre,HDUhtml)
        i = 1
        HDUlist = []
        while(i <= len(HDUquery)):
            pos = 0
            for j in range(0, len(HDUquery[i])):
                if(HDUquery[i][j] == '>'):
                    pos = j + 1
                    break
            HDUlist.append(HDUquery[i][pos:len(HDUquery[i])-1])
            i += 2
        for i in range(0,len(HDUlist)):
            print HDUlist[i]

    def ZJUT(self):
        print '=========================='
        print '来自浙工大的消息:'
        reg = r'title=.*">'
        ZJUThtml = self.GetHtml(ZJUTaddress)
        ZJUTre = re.compile(reg)
        ZJUTquery = re.findall(ZJUTre,ZJUThtml)
        i = 0
        ZJUTlist = []
        while(i < len(ZJUTquery)):
            print ZJUTquery[i][7:(len(ZJUTquery[i])-2)]
            ZJUTlist.append(ZJUTquery[i][7:(len(ZJUTquery[i])-2)])
            i += 1

    def XJTU(self):
        print'==========================='
        print'来自西交大的消息：'
        reg = r'k".*">'
        XJTUhtml = self.GetHtml(XJTUaddress)
        XJTUre = re.compile(reg)
        XJTUquery = re.findall(XJTUre, XJTUhtml)
        for i in range(0,len(XJTUquery)):
            print XJTUquery[i][10:len(XJTUquery[i])-2]

    def NWPU(self):
        '''待完成'''
        print'==========================='
        print'来自西工大的消息：'
        reg = r'k".*">'
        NWPUhtml = self.GetHtml(NWPUaddress)
        NWPUre = re.compile(reg)
        NWPUquery = re.findall(NWPUre, NWPUhtml)
        for i in range(0,len(NWPUquery) - 1):
            print NWPUquery[i][10:len(NWPUquery[i])-2]

    
if __name__ == "__main__":
    myJob = Job()
    myJob.XDU()
    myJob.XJTU()
    myJob.NWPU()
    myJob.ZJUT()
    myJob.HDU()
