
import pycurl
import certifi
from io import BytesIO
import os
def clear():os.system('cls')

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

test_urls = ["https://www.baidu.com",
             "https://www.intmian.com",
             "https://github.com",
             "https://www.youku.com",
             "https://store.steampowered.com/",
             "api.warframe.com",
             "https://www.google.com",
             "https://www.youtube.com"]


def test_website_whole(url,mode):
    print("正在检测网站:", url)
    c = pycurl.Curl()
    buffer = BytesIO()  # 创建缓存对象
    if mode == 1:
       c.setopt(c.PROXY, '127.0.0.1:2333')
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
       c.setopt(c.PROXY, '127.0.0.1:2333')    
    c.setopt(c.MAXREDIRS, 5)  # 指定HTTP重定向的最大数
    c.setopt(pycurl.FORBID_REUSE, 1)
    c.setopt(pycurl.SSL_VERIFYPEER, 1)
    c.setopt(pycurl.SSL_VERIFYHOST, 2)
    c.setopt(pycurl.CAINFO, certifi.where())
    try:
        c.perform()  # 执行
    except(pycurl.error):
         return "∞ ms"
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    http_code = c.getinfo(pycurl.HTTP_CODE)
    return  str(http_total_time * 1000)+" ms"
    #print("%s \n    直连\n    响应时间： %.2f ms\n    响应状态： %d[%s]" % (url, http_total_time * 1000,int(http_code), dict_code[http_code]))


if __name__ == '__main__':
    mode = int(input("输入1进入常用测试，输入2进入特殊测试:_\b"))
    if mode == 2:
        url = input("输入网址:___________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
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
        con_baidu = test_website_simple("https://www.baidu.com",0)
        print("墙内延迟",con_baidu)
        con_proxy = test_website_simple("45.76.105.14",0)
        print("代理延迟",con_proxy)
        con_google = test_website_simple("https://www.google.com",0)
        print("直连墙外延迟",con_google)
        con_google_withProxy = test_website_simple("https://www.google.com",1)
        print("代理墙外延迟",con_google_withProxy)
        print("常用网站：")
        for url in test_urls:
            print(url,":")
            con = test_website_simple(url,0)
            print("    直连:",con)
            if con == "∞ ms":
                con_withProxy = test_website_simple(url,1)
                print("    代理:",con_withProxy)
