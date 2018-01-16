#coding:utf-8
import urllib.request,urllib.parse,json
import http.cookiejar
import ssl
import requests.utils
import re
from chaojiying_Python.chaojiying import Chaojiying_Client
ssl._create_default_https_context = ssl._create_unverified_context

codedict = { '1':'46,42,', '2':'105,45,','3':'184,44,','4':'256,43,','5':'42,117,','6':'112,115,','7':'181,114,','8':'252,111,'} #手工验证码坐标
username = str(input('请输入12306网站的账号')).replace(' ','')
pwd = str(input('请输入12306网站的密码')).replace(' ','')


class Auto12306():
    global codedict,username,pwd
    def __init__(self):
        self.headers = {
        'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3178.0 Safari/537.36',
        'Host':'kyfw.12306.cn',
        'Cookie':'RAIL_DEVICEID=J3KL0MQuTTb1Bs96vKCmO4o1Wa9TyfY5WB014kQAkqd7hB_I8lT3O9WvrLXzCHdxpse-JWO-Pp_lN3DAcWRa7dXm0LVLFLqWzjGb-B0f2RLZKUg5bJNbkISK6rBIFMj6_DdujXExp8hY58fNDPdWZwG5t6y2CC5i',
        }
        self.username = username
        self.pwd = pwd
        self.cj = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))


    def getticket(self):
        godate = '2018-01-22'
        url1 = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date='
        from_station = 'HGH'
        to_station = 'CEH'
        url1 = url1 + godate + '&leftTicketDTO.from_station=' + from_station + '&leftTicketDTO.to_station=' + to_station
        urlquery = url1 + '&purpose_codes=ADULT'
        req = urllib.request.Request(urlquery,headers=self.headers)
        res_data = urllib.request.urlopen(req).read().decode('utf-8')
        res_data = json.loads(res_data)
        city = res_data['data']['map']
        ticketinfo = res_data['data']['result']
        # for i in ticketinfo:
        #     i = i.split('|')
        #     print('-----------------------------------------------分割线------------------------------------')
        #     print(i[0])
        #     print ('车次：%s,出发站：%s,目的站：%s,出发时间：%s,到达时间：%s,历时：%s'%(i[3],city[i[6]],city[i[7]],i[8],i[9],i[10]))
        #     print('商务：%s,一等：%s,二等：%s,软卧：%s,硬卧：%s,硬座：%s,无座：%s' % (i[32], i[31], i[30], i[23], i[28], i[29],i[26]))
        #     print('-----------------------------------------------分割线------------------------------------')
        return ticketinfo[0].split('|')[0]

    # def autocode():
    #     chaojiying = Chaojiying_Client('youidr', '987456', '894198')
    #     im = open('code.jpg', 'rb').read()
    #     codevalue = chaojiying.PostPic(im, 9004)
    #     print(codevalue)
    #     code = codevalue['pic_str']
    #     pic_id = codevalue['pic_id']
    #     code = code.replace('|',',').split(',')
    #     strn = ''
    #     c = 1
    #     for x in code:
    #         if c % 2 == 0:
    #             x = str(int(x) - 20)
    #         strn = strn + x + ','
    #         c += 1
    #     code = strn[:-1]
    #     return code,pic_id
    #
    # def login():
    #     #getticket()
    #     cj = http.cookiejar.CookieJar()
    #     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    #     cookdict = {'RAIL_DEVICEID':"SJbAnnl2bRr42LXu2NxFZPn7ib3pXvFwBfDE0XrxCz3-aFIg9rzTvmBhnPSHnMa_mVWWmOs2nx_fIwKCFMg_Ot9aW0BRHHeNRcpQVorGGsaUL2jhjntqU94nhhadHNk8NRj9kuA6MjUtp6kg4X0gklKZEm3-bmW7"}
    #     requests.utils.add_dict_to_cookiejar(cj, cookdict)
    #     url2 = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.0858224421220557"
    #     req = urllib.request.Request(url2, headers=headers)
    #     code_data = opener.open(req).read()
    #     with open('code.jpg','wb') as fc:
    #         fc.write(code_data)
    #     #手工验证码
    #     code = str(input('请输入验证码'))
    #     strn = ''
    #     for x in code:
    #         strn = strn + codedict[x]
    #     code = strn[:-1]
    #     #手工验证码
    #     #自动验证码
    #     # cjycode = autocode()
    #     # code,pic_id = cjycode[0],cjycode[1]
    #     # 自动验证码
    #     print(code)
    #     url3 = "https://kyfw.12306.cn/passport/captcha/captcha-check"  #验证码验证
    #     data = {
    #         'answer': code,
    #         'login_site':'E',
    #         'rand': 'sjrand',
    #     }
    #     data = urllib.parse.urlencode(data).encode('utf-8')
    #     req = urllib.request.Request(url3,data, headers=headers)
    #     res = opener.open(req).read().decode('utf-8')
    #     res = json.loads(res)
    #     res_code = res['result_code']
    #     res_msg = res['result_message']
    #     if res_code == '4':
    #         print(res_msg)
    #         url4 = 'https://kyfw.12306.cn/passport/web/login'  #账号密码验证
    #         data = {'username':username,'password':pwd, 'appid':'otn'}
    #         data = urllib.parse.urlencode(data).encode('utf-8')
    #         req = urllib.request.Request(url4,data,headers=headers)
    #         res_login = opener.open(req).read().decode('utf-8')
    #         res_login = json.loads(res_login)
    #         login_msg = res_login['result_message']
    #         login_code = res_login['result_code']
    #         if login_code == 0:
    #             print(login_msg)
    #             surl = 'https://kyfw.12306.cn/passport/web/auth/uamtk' #登录一次验证
    #             ldata = {'appid':'otn'}
    #             ldata = urllib.parse.urlencode(ldata).encode('utf-8')
    #             userlogin = urllib.request.Request(surl,ldata,headers=headers)
    #             res_uamtk = opener.open(userlogin).read().decode('utf-8')
    #             res_uamtk = json.loads(res_uamtk)
    #             uamtk_msg = res_uamtk['result_message']
    #             tk = res_uamtk['newapptk']
    #             uamtk_code = res_uamtk['result_code']
    #             if uamtk_code == 0:
    #                 print('登录第一次：',uamtk_msg)
    #                 # cookdict = requests.utils.dict_from_cookiejar(cj)
    #                 # cookdict.pop('uamtk')
    #                 # cj = http.cookiejar.CookieJar()
    #                 # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    #                 # requests.utils.add_dict_to_cookiejar(cj, cookdict)
    #                 uamtkclient = 'https://kyfw.12306.cn/otn/uamauthclient' #登录二次验证
    #                 data = {'tk':tk}
    #                 data = urllib.parse.urlencode(data).encode('utf-8')
    #                 uamauth = urllib.request.Request(uamtkclient,data,headers=headers)
    #                 res_uamauth = opener.open(uamauth)
    #                 res_uamauth = json.loads(res_uamauth.read().decode('utf-8'))
    #                 uamauth_code,uamauth_msg,realname = res_uamauth['result_code'],res_uamauth['result_message'],res_uamauth['username']
    #                 if uamauth_code == 0:
    #                     print('登录第二次：',uamauth_msg)
    #
    #                     # 获取车次安全码
    #                     godate = '2018-01-22'
    #                     url1 = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date='
    #                     from_station = 'HGH'
    #                     to_station = 'CEH'
    #                     url1 = url1 + godate + '&leftTicketDTO.from_station=' + from_station + '&leftTicketDTO.to_station=' + to_station
    #                     urlquery = url1 + '&purpose_codes=ADULT'
    #                     req = urllib.request.Request(urlquery, headers=headers)
    #                     res_data = opener.open(req).read().decode('utf-8')
    #                     res_data = json.loads(res_data)
    #                     city = res_data['data']['map']
    #                     ticketinfo = res_data['data']['result']
    #                     # 获取车次安全码
    #                     ticketinfo = ticketinfo[0].split('|')
    #                     secretStr = ticketinfo[0]
    #                     leftTicketStr = ticketinfo[12]
    #                     print(secretStr)
    #                     secretStr = urllib.parse.unquote(secretStr)
    #                     url5 = "https://kyfw.12306.cn/otn/login/checkUser"  #预定前用户登录状态验证
    #                     data = {'_json_att':''}
    #                     data = urllib.parse.urlencode(data).encode('utf-8')
    #                     checkUser = urllib.request.Request(url5,data, headers=headers)
    #                     res_checkUser = opener.open(checkUser).read().decode('utf-8')
    #                     print(res_checkUser)
    #                     print('预定前用户登录状态验证后的cookie')
    #                     for x in cj:
    #                         print(x)
    #                     url6 = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest' #提交交易请求
    #                     data = {
    #                         'secretStr':secretStr,
    #                         'train_date':'2018-01-22',
    #                         'back_train_date':'2018-01-15',
    #                         'tour_flag':'dc',
    #                         'purpose_codes':'ADULT',
    #                         'query_from_station_name':'杭州',
    #                         'query_to_station_name':'苍南',
    #                         'undefined':'',
    #                     }
    #                     data = urllib.parse.urlencode(data).encode('utf-8')
    #                     submitOrderRequest = urllib.request.Request(url6,data, headers=headers)
    #                     res_submitOrderRequest = opener.open(submitOrderRequest).read().decode('utf-8')
    #                     print(res_submitOrderRequest)
    #                     print('提交交易请求后的cookie')
    #                     for x in cj:
    #                         print(x)
    #
    #                     url7 = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc' #确认交易状态
    #
    #                     data = urllib.parse.urlencode(data).encode('utf-8')
    #                     initDc = urllib.request.Request(url7,data, headers=headers)
    #                     res_initDc = opener.open(initDc).read().decode('utf-8')
    #                     #print(res_initDc)
    #                     prog = re.compile('(?!globalrepeatsubmittoken=)[0-9a-z]{32}')
    #                     REPEAT_SUBMIT_TOKEN = prog.findall(res_initDc)[0]
    #                     prog = re.compile('[0-9A-Z]{56}')
    #                     key_check_isChange = prog.findall(res_initDc)[0]
    #                     print(REPEAT_SUBMIT_TOKEN)
    #                     print(key_check_isChange)
    #                     input('===')
    #                     print('确认交易状态后的cookie')
    #                     for x in cj:
    #                         print(x)
    #                     #passengerTicketStr:O  O是二等座   9是商务座   M是一等座
    #                     url8 = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo' #检查交易信息
    #                     data = {
    #                         'cancel_flag':'2',
    #                         'bed_level_order_num':'000000000000000000000000000000',
    #                         'passengerTicketStr':'O,0,1,许亦元,1,330327198410028479,15558123937,N',
    #                         'oldPassengerStr':'许亦元,1,330327198410028479,1_',
    #                         'tour_flag':'dc',
    #                         'randCode':'',
    #                         'whatsSelect':'1',
    #                         '_json_att':'',
    #                         'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
    #                     }
    #                     data = urllib.parse.urlencode(data).encode('utf-8')
    #                     checkOrderInfo = urllib.request.Request(url8,data, headers=headers)
    #                     res_checkOrderInfo = opener.open(checkOrderInfo).read().decode('utf-8')
    #                     print(res_checkOrderInfo)
    #                     print('检查交易信息后的cookie')
    #                     for x in cj:
    #                         print(x)
    #                     url9 = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'#获取队列计数
    #                     data = {
    #                         'train_date':'Mon Jan 22 2018 00:00:00 GMT+0800 (中国标准时间)',
    #                         'train_no':ticketinfo[2],
    #                         'stationTrainCode':ticketinfo[3],
    #                         'seatType':'O',
    #                         'fromStationTelecode':'HGH',
    #                         'toStationTelecode':'CEH',
    #                         'leftTicket':leftTicketStr,
    #                         'purpose_codes':'00',
    #                         'train_location':ticketinfo[15],
    #                         '_json_att':'',
    #                         'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
    #                     }
    #                     data = urllib.parse.urlencode(data).encode('utf-8')
    #                     getQueueCount = urllib.request.Request(url9,data, headers=headers)
    #                     res_getQueueCount = opener.open(getQueueCount).read().decode('utf-8')
    #                     print(res_getQueueCount)
    #                     print('获取队列计数后的cookie')
    #                     for x in cj:
    #                         print(x)
    #                     urlover = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue' #最后确认
    #                     data = {
    #                         'passengerTicketStr':'O,0,1,许亦元,1,330327198410028479,15558123937,N',
    #                         'oldPassengerStr':'许亦元,1,330327198410028479,1_',
    #                         'randCode':'',
    #                         'purpose_codes':'00',
    #                         'key_check_isChange':key_check_isChange,
    #                         'leftTicketStr':leftTicketStr,
    #                         'train_location':ticketinfo[15],
    #                         'choose_seats':'',
    #                         'seatDetailType':'000',
    #                         'whatsSelect':'1',
    #                         'roomType':'00',
    #                         'dwAll':'N',
    #                         '_json_att':'',
    #                         'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
    #                     }
    #                     data = urllib.parse.urlencode(data).encode('utf-8')
    #                     confirmSingleForQueue = urllib.request.Request(urlover,data, headers=headers)
    #                     res_confirmSingleForQueue  = opener.open(confirmSingleForQueue).read().decode('utf-8')
    #                     print(res_confirmSingleForQueue)
    #
    #                 else:
    #                     print(uamauth_msg)
    #             else:
    #                 print(1,uamtk_msg)
    #         else:
    #             print(login_msg)
    #     else:
    #         print(res_msg)
    #         #print(chaojiying.ReportError(pic_id))





if __name__ == '__main__':
    A = Auto12306()
    print(A.getticket())
