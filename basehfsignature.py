#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-11 9:49
#@Author  : hcj
#获取签名加密结果
import base64
import hashlib
import json
import random

import pymysql
import redis
from requests_toolbelt import MultipartEncoder

signFuncID="100"
SECRET_KEY="7bae14bab426"
def get_signature(**kwargs):
    #剔除不参与加密的apisequence和time参数
    pop_apisequence=kwargs.pop('apiSequence')
    pop_time=kwargs.pop('time')
    #加密signature
    str_md5='data={'
    #提取dict中key拼接的时候需要将key强制转换str
    for i in range(0,len(sorted(kwargs.keys()))):
        str_md5=str_md5+'"'+sorted(kwargs.keys())[i]+'":"'+str(kwargs[sorted(kwargs.keys())[i]])+'",'
        str_md5=str_md5[:-1]+'}$time='+pop_time+'$apiSequence='+pop_apisequence+'$signFuncID='+signFuncID+SECRET_KEY
        #print(str_md5)
        signature=hashlib.mdt(str_md5.encode()).hexdigest()
        return signature
#图片生成base64码
def file2base64(filepath):
    with open(filepath,"rb") as f:
        base64_data=base64.b64encode(f.read())
        return base64_data
def m_encoder(sname,filename,filepath):
    fields={sname:(filename,open(filepath,'rb'),'image/jpg')}
    MultipartEncoder(fields)
    print()
 #获取随机数
def get_rendom_num(isstat,isend):
    return random.randint(isstat,isend)
#md5加密
def encryptMD5():
    reStr=hashlib.md5(str.encode()).hexdigest()
    return reStr

# md5加密密码
def password(str):
    sPassword = encryptMD5(password)
    rPassword = sPassword[::-1]
    tPasswword = rPassword + "paf"
    return encryptMD5(tPasswword)


#截取指定文本
def cutTXT(value,sstr,estr):
    start_num=value.find(sstr)+len(sstr)
    end_num=value.find(estr)
    return value[start_num:end_num]

#解锁登陆状态 清除redis缓存
def isacctlocked(response,mobile):
    rjson=response.headers
    print("ccs",rjson)
    jsobj=json.loads(response.text)
    icode=jsobj['code']
    if icode==200007:
        print("用户名密码错误")
    elif icode==200104:
        print("已输错4次，再次输错会锁定账号")
    elif icode==200017:
        print("账户已被锁定")
        reset_loginacct('paf:member:login:locker:',mobile)
        print("解锁账户成功")
    else:
       print("登陆成功")
    print(icode)
def reset_loginacct(skey,mobile):
    host='st-redis.a.pa.com'
    port=6379
    db=0
    key=skey+mobile
    conn=redis.Redis(host=host,port=port,db=db)
    val=conn.exists(key)
    if val==False:
        print("Key not found")
    else:
        conn.delete(key)
        print("key deleted!")

def comparator_str(check,expect):
    if(expect[-1]==','):
         assert str(check)==str(expect[:-1])
    else:
        assert str(check)==str(expect)

def select_values_from_db(insql):
    host='st-mysql-m.a.pa.com'
    user='hfqa'
    passwd='qn3p@I0QG'
    db='server_db'
    conn=pymysql.connect(host=host,user=user,passwd=passwd,db=db)
    cur=conn.cursor()
    cur.execute(insql)
    sms=str(cur.fetchone())
    values=sms[2:len(sms)-3].replace("'","").split(',')
    return  values