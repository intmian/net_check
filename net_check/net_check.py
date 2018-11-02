import pycurl
import certifi
import threading
from io import BytesIO
import os
import threading
def clear():os.system('cls')
import time
import json
import sys

threads_information = []
dict_code = {100: "Continue",
             101: "Switching Protocols",
             102: "Processing",
             200: "OK",
             201: "Created",
             202: "Accepted",
             203: "Non-Authoritative Information",
             204: "No Content",
             205: "Reset Content",
             206: "Partial Content",
             207: "Multi-Status",
             300: "Multiple Choices",
             301: "Moved Permanently",
             302: "Move temporarily",
             303: "See Other",
             304: "Not Modified",
             305: "Use Proxy",
             306: "Switch Proxy",
             307: "Temporary Redirect",
             400: "Bad Request",
             401: "Unauthorized",
             402: "Payment Required",
             403: "Forbidden",
             404: "Not Found",
             405: "Method Not Allowed",
             406: "Not Acceptable",
             407: "Proxy Authentication Required",
             408: "Request Timeout",
             409: "Conflict",
             410: "Gone",
             411: "Length Required",
             412: "Precondition Failed",
             413: "Request Entity Too Large",
             414: "Request-URI Too Long",
             415: "Unsupported Media Type",
             416: "Requested Range Not Satisfiable",
             417: "Expectation Failed",
             421: "too many connections",
             422: "Unprocessable Entity",
             423: "Locked",
             424: "Failed Dependency",
             425: "Unordered Collection",
             426: "Upgrade Required",
             449: "Retry With",
             451: "Unavailable For Legal Reasons",
             500: "Internal Server Error",
             501: "Not Implemented",
             502: "Bad Gateway",
             503: "Service Unavailable",
             504: "Gateway Timeout",
             505: "HTTP Version Not Supported",
             506: "Variant Also Negotiates",
             507: "Insufficient Storage",
             509: "Bandwidth Limit Exceeded",
             510: "Not Extended",
             600: "Unparseable Response Headers"
             }

test_urls = None
# TODO read it by read set
thread_num = None
port = None
work_add = None
config_add = None

def test_website_whole(url,mode):
    print("正在检测网站:", url)
    c = pycurl.Curl()
    buffer = BytesIO()  # 创建缓存对象
    if mode == 1:
       c.setopt(c.PROXY, '127.0.0.1:' + port)
    c.setopt(pycurl.CONNECTTIMEOUT, 10)
    c.setopt(pycurl.TIMEOUT, 15)
    c.setopt(c.WRITEDATA, buffer)  # 设置资源数据写入到缓存对象
    c.setopt(c.URL, url)  # 指定请求的URL
    c.setopt(c.MAXREDIRS, 5)  # 指定HTTP重定向的最大数
    c.setopt(pycurl.FORBID_REUSE, 1)
    c.setopt(pycurl.SSL_VERIFYPEER, 1)
    c.setopt(pycurl.SSL_VERIFYHOST, 2)
    c.setopt(pycurl.CAINFO, certifi.where())
    c.perform()  # 执行

    http_code = c.getinfo(pycurl.HTTP_CODE)  # 返回的HTTP状态码
    dns_resolve = c.getinfo(pycurl.NAMELOOKUP_TIME)  # DNS解析所消耗的时间
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)  # 建立连接所消耗的时间
    http_pre_trans = c.getinfo(pycurl.PRETRANSFER_TIME)  # 从建立连接到准备传输所消耗的时间
    http_start_trans = c.getinfo(pycurl.STARTTRANSFER_TIME)  # 从建立连接到传输开始消耗的时间
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)  # 传输结束所消耗的总时间
    http_size_download = c.getinfo(pycurl.SIZE_DOWNLOAD)  # 下载数据包大小
    http_size_upload = c.getinfo(pycurl.SIZE_UPLOAD)  # 上传数据包大小
    http_header_size = c.getinfo(pycurl.HEADER_SIZE)  # HTTP头部大小
    http_speed_downlaod = c.getinfo(pycurl.SPEED_DOWNLOAD)  # 平均下载速度
    http_speed_upload = c.getinfo(pycurl.SPEED_UPLOAD)  # 平均上传速度
    http_redirect_time = c.getinfo(pycurl.REDIRECT_TIME)  # 重定向所消耗的时间

    print('HTTP响应状态： %d[%s]' % (int(http_code), dict_code[http_code]))
    print('DNS解析时间：%.2f ms' % (dns_resolve * 1000))
    print('建立连接时间： %.2f ms' % (http_conn_time * 1000))
    print('准备传输时间： %.2f ms' % (http_pre_trans * 1000))
    print("传输开始时间： %.2f ms" % (http_start_trans * 1000))
    print("传输结束时间： %.2f ms" % (http_total_time * 1000))
    print("重定向时间： %.2f ms" % (http_redirect_time * 1000))
    print("上传数据包大小： %d bytes" % http_size_upload)
    print("下载数据包大小： %d bytes" % http_size_download)
    print("HTTP头大小： %d bytes" % http_header_size)
    print("平均上传速度： %d kb/s" % (http_speed_upload / 1024))
    print("平均下载速度： %d kb/s" % (http_speed_downlaod / 1024))

def test_website_simple(url,mode):
    c = pycurl.Curl()
    buffer = BytesIO()  # 创建缓存对象
    c.setopt(pycurl.CONNECTTIMEOUT, 10)
    c.setopt(pycurl.TIMEOUT, 15)
    c.setopt(c.WRITEDATA, buffer)  # 设置资源数据写入到缓存对象
    c.setopt(c.URL, url)  # 指定请求的URL
    if mode == 1:
       c.setopt(c.PROXY, '127.0.0.1:' + port)    
    c.setopt(c.MAXREDIRS, 5)  # 指定HTTP重定向的最大数
    c.setopt(pycurl.FORBID_REUSE, 1)
    c.setopt(pycurl.SSL_VERIFYPEER, 1)
    c.setopt(pycurl.SSL_VERIFYHOST, 2)
    c.setopt(pycurl.CAINFO, certifi.where())
    try:
        c.perform()  # 执行
    except(pycurl.error):
         return -1  # 代表不能连接
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    http_total_time = round(http_total_time * 1000,1)
    http_code = c.getinfo(pycurl.HTTP_CODE)
    return  http_total_time # ms
    #print("%s \n 直连\n 响应时间： %.2f ms\n 响应状态： %d[%s]" % (url, http_total_time *
                               #1000,int(http_code), dict_code[http_code]))

# return ∞ ms or n ms
def test_website_simple_start(url,mode):
    time_ = test_website_simple(url,mode)
    threads_information.append(time_)

def test_website_withThread(url,mode):
    total_time = 0
    success_time = 0  # 成功响应
    fail_time = 0
    threads_information.clear()
    for i in range(thread_num):
        t = threading.Thread(target=test_website_simple_start,args=(url,mode))
        t.start()
    while len(threads_information) < thread_num:
        time.sleep(0.1)  # 减少系统资源占用
        
    for time_ in threads_information:
        if time_ == -1:
            fail_time += 1
        else:
            success_time +=1 
            total_time += time_
    if success_time >= 2:
        return str(round(total_time / success_time,1)) + " ms"
    elif success_time < 2:
        return "∞ ms"
        
def GetSet():
    global test_urls
    global thread_num
    global port
    with open(config_add+"\\websites.json","r",encoding='utf-8') as f:
        test_urls = json.load(f)
        print("网址已读入")
    with open(config_add+"\\limit.json","r",encoding='utf-8') as f:
        thread_num = int(json.load(f))
        print("线程数已读入")
    with open(config_add+"\\port.json","r",encoding='utf-8') as f:
        port = str(json.load(f))
        print("线程数已读入")

def PushSetToFile():
    with open(config_add+"\\websites.json","w") as f:
        json.dump(test_urls,f)
        print("网址已写入设置")
    with open(config_add+"\\limit.json","w") as f:
        json.dump(thread_num,f)
        print("线程数已写入设置")
    with open(config_add+"\\port.json","w+") as f:
        json.dump(port,f)
        print("端口已写入设置")
#写入配置至文件

def showUrl():
    print("当前网站有:")
    for i in range(len(test_urls)):
        print("    ",i,":",test_urls[i])

def Set():
    global thread_num
    global test_urls
    global port
    clear()
    mode = int(input("1.更改测试网站\n2.更改线程数\n3.更改端口\n4.查看配置\n选择：_\b"))
    if mode == 1:
        while True:
            clear()
            showUrl()
            mode = int(input("1.添加2.删除3.更改4.退出\n选择：_\b"))
            if mode == 4:
                break
            if mode == 1:
                newWeb = input("新的网址:__________\b\b\b\b\b\b\b\b\b\b")
                test_urls.append(newWeb)
            if mode == 2:
                index = int(input("想要删除的网址"))
                del test_urls[index]
            if mode == 3:
                index = int(input("想要替换的网址"))
                newWeb = input("新的网址:__________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
                test_urls[index] = newWeb
    if mode == 2:
        newNum = int(input("当前线程数为：%d\n更改为：_\b"%thread_num))
        thread_num = newNum
    if mode == 3:
        newPort = input("当前端口为：%d\n更改为：_\b"%port)
        port = newPort
    if mode == 4:
        clear()
        showUrl()
        print("--------------------\n当前线程数：", thread_num)
        print("--------------------\n当前端口：", port)
        return
    clear()
    PushSetToFile()

if __name__ == '__main__':
    clear()
    work_add = sys.argv[0]
    work_add = work_add.replace("\\net_check.py","")
    config_add = work_add + "\\config"
    print("读入设置中")
    GetSet()
    clear()
    mode = int(input("1.常用测试\n2.特殊测试\n3.设置\n选择：_\b"))
    if mode == 2:
        url = input("输入网址:___________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
        clear()
        try:
            print("正在尝试直连")
            test_website_whole(url,0)
        except(pycurl.error):
            print("%s\n链接超时" % (url))
            print("正在尝试通过代理")
            try:
                test_website_whole(url,1)
            except(pycurl.error):
                print("连接失败")
    if mode == 1:
        clear()
        con_baidu = test_website_withThread("https://www.baidu.com",0)
        print("直连墙内延迟",con_baidu)
        con_baidu_proxy = test_website_withThread("https://www.baidu.com",1)
        print("代理墙内延迟",con_baidu_proxy)
        con_google = test_website_withThread("https://www.google.com",0)
        print("直连墙外已ban延迟",con_google)
        con_google_withProxy = test_website_withThread("https://www.google.com",1)
        print("代理墙外已ban延迟",con_google_withProxy)
        con_google = test_website_withThread("https://www.wikipedia.org/",0)
        print("直连墙外未ban延迟",con_google)
        con_google_withProxy = test_website_withThread("https://www.wikipedia.org/",1)
        print("代理墙外未ban延迟",con_google_withProxy)

        print("常用网站：")
        for url in test_urls:
            print(url,":")
            con = test_website_withThread(url,0)
            print("    直连:",con)
            if con == "∞ ms":
                con_withProxy = test_website_withThread(url,1)
                print("    代理:",con_withProxy)

    if mode == 3:
        Set()
