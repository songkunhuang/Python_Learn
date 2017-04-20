# -*- coding: utf-8 -*-
"""
Created on  17:27 2017/4/17 
@author: Song
@E-mail: songkunhuang@163.com

"""
"""
import suds

url = "http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl"
client = suds.client.Client(url)
print client
res = client.service['IpAddressSearchWebServiceSoap12'].getCountryCityByIp('8.8.8.8')
print res
"""


def func_a(func):
    def func_b(func):
        print ("before func_a")
        return func
    return func_b(func)

@func_a
def func_a():
    print "func runing"

func_a()

"""
from suds.xsd.doctor import ImportDoctor, Import
import suds
imp = Import('http://www.w3.org/2001/XMLSchema')
imp.filter.add('urn:ClientServices')
doctor = ImportDoctor(imp)
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = suds.Client(url, doctor=doctor, cache=None)
"""
