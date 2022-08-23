import random
import traceback

import requests
import json

# ----------配置区----------
address = ""
# 提交时所在定位
cityName = "重庆市"
# 提交城市
schoolName = ""
# 学校名称，必须正确，查看学校名称：
bodyTemperature = True
# 体温情况 为True时是正常，False是>37.3，若填其他则是True
abnormalSymptoms = True
# 新型冠状病毒肺炎主要症状：发热、干咳、乏力、咽痛、嗅(味) 觉减退、腹泻等 为True时是无，False是有，若填其他则是True
healthCodeColor = 0
# 健康码颜色 0绿码，1黄码，2红码，3弹框，4其他
travelCardStatus = True
# 行程卡状态 为True时是正常，False是异常，若填其他则是True
token = ""
# 唯一token,需要抓包,抓包方法：也可联系作者进行付费抓包
Bark = ''

# Bark手机通知。仅限水果手机，水果手机安装Bark应用,格式：https://api.day.app/barkid/推送标题/{}?group=信息采集

class CqgcxxcjXcx:
    def __init__(self):
        self.edu_pre_url = "https://ossc.cqcet.edu.cn/static/edu_pre_url.json"
        # 查可用学校——委员会
        self.findUser = "/api-sys/system/user/findUserByWxCode?code="
        # 查询绑定数据  code get
        self.bindUser = "/api-sys/system/user/bindUser"
        # 绑定 idCardLastSix=11111&name=11111&code=身份证后6，姓名 url编码全。code post
        self.unBindUser = "/api-sys/system/user/unBindUser"
        # 需要token
        # 解绑 code=&loginName=oginName在用户信息里，也在绑定包里,code不是登陆时的，是事实的
        self.saveBatch = "/api-prevention/signinfo/savebatch"
        # 需要token
        # 打卡
        # {"isTravel":0,"isContact":0,"isCohabit":0,"isFatigue":0,"isShortnessBreath":0,"travelInfoVo":{"relationshipInfo":[{"contactInfo":"","name":"","relationship":"","key":0}]},"contactInfo":{},"cohabitInfo":[{"name":"","province,city,disctrict":"","returnTime":"","transType":"","transTypeValue":"","transNumber":"","currentDetailResidence":"","contactInfo":0,"highRiskInfo":0,"governmentQuarantine":0,"homeQuarantine":0,"healthCardInfo":"","healthCardUrl":"","travelInfo":"","travelUrl":"","nucleicAcid":"","nucleicAcidMethod":"","nucleicAcidPointName":"","nucleicAcidSamplingDate":"","nucleicAcidAgency":"","nucleicAcidTime":"","nucleicAcidResult":"","nucleicAcidImg":"","key":0}],"healthCardInfo":"0","healthStatus":0,"travelInfo":"0","locateDetailedAddress":"重庆市江津区鼎山街道金钗井路40号","locateLatitude":29.29014,"locateLongitude":106.25936,"city":"重庆市","disctrict":"江津区","cityCode":"023","disctrictCode":"500116","province":"重庆市"}参数postAuthorization: Bearer 0976e5f2-2dc9-4d7e-9c0c-4aa0a10a3bf4这个参数校验参数,也是token 结果{"data":null,"code":1,"msg":"保存成功"}{"data":null,"code":-1,"msg":"今日已打卡"}
        self.ip = self.camouflage_ip()
        # 伪造ip
        self.jwd = "https://api.map.baidu.com/geocoder?address={}&output=json&key=E4805d16520de693a3fe707cdc962045&city={}".format(
            address, cityName)
        # 获取经纬度
        try:
            res = requests.get(self.jwd, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"})
            res_str = res.content.decode()
            res_json = json.loads(res_str)
            if res_json['status'] != "OK":
                self.whetherAvailable = False
                print("获取经纬度坐标错误，请联系作者或查看更新")
            self.x = res_json["result"]["location"]["lng"]
            self.y = res_json["result"]["location"]["lat"]
        except:
            self.whetherAvailable = False
            print("获取经纬度坐标错误，请联系作者或查看更新")
        self.header = {
            "Referer": "https://servicewechat.com/wx949a64a04ad423d3/20/page-frame.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI "
                          "MiniProgramEnv/Windows WindowsWechat ",
            "Connection": "keep-alive",
            "Client-Ip": self.ip,
            "X-Forwarded-For": self.ip,
            "x-forwarded-for": self.ip,
            "Remote_Addr": self.ip,
            "x-remote-IP": self.ip,
            "x-remote-ip": self.ip,
            "x-client-ip": self.ip,
            "x-client-IP": self.ip,
            "X-Real-IP": self.ip,
            "client-IP": self.ip,
            "x-originating-IP": self.ip,
            "x-remote-addr": self.ip,
        }
        self.city_code = "https://restapi.amap.com/v3/geocode/regeo?output=json&key=232fbfeca6da9d981c79f9f020188f61&radius=1000&extensions=base&location={}".format(
            str(self.x) + "," + str(self.y))
        try:
            res = requests.get(self.city_code, headers=self.header)
            res_str = res.content.decode()
            res_json = json.loads(res_str)
            if res_json['status'] != "1":
                self.whetherAvailable = False
                print("获取城市code错误，请联系作者或查看更新")
            self.adcode = res_json["regeocode"]["addressComponent"]["adcode"]
            self.district = res_json["regeocode"]["addressComponent"]["district"]
            self.citycode = res_json["regeocode"]["addressComponent"]["citycode"]
        except:
            self.whetherAvailable = False
            print("获取城市code错误，请联系作者或查看更新")
        self.school = self.find_school(schoolName)
        self.whetherAvailable = True
        if self.school['code'] == -1:
            self.whetherAvailable = False
            print("无此学校")
        self.host = self.txt_zhongjian(self.school['href'], "https://", "/")
        if self.host is None:
            self.host = self.txt_zhongjian(self.school['href'], "http://", "/")
        if self.host is None:
            self.whetherAvailable = False
            print("无此学校")
        # 请求头
        self.nearlyInfo = "/api-prevention/signinfo/nearlyInfo?userId="
        # 需要token
        # 查询打卡信息，用户信息
        self.findByType = "/api-prevention/fieldsettings/findByType?type=0"
        # 需要token
        # 查询当前打卡页。4条。超过或若有不同有改动，需更新。2022年8月23日09点18分目前为：体温情况healthStatus，新型冠状病毒肺炎主要症状：发热、干咳、乏力、咽痛、嗅(味) 觉减退、腹泻等isFatigue，健康码颜色healthCardInfo，行程卡状态travelInfo。分别的字段信息也在里边data[0].remark。0正常1异常。看提交信息较多，可能以后会更改
        # {"data":[{"id":"001","type":0,"description":"体温情况","sortOrder":1,"isRequired":true,"isShown":true,"delFlag":"0","createBy":"db","createDate":"2022-06-27 10:30:56","updateBy":"db","updateDate":"2022-06-27 10:36:27","remark":"healthStatus"},{"id":"002","type":0,"description":"新型冠状病毒肺炎主要症状：发热、干咳、乏力、咽痛、嗅(味) 觉减退、腹泻等","sortOrder":2,"isRequired":true,"isShown":true,"delFlag":"0","createBy":"db","createDate":"2022-06-27 10:30:56","updateBy":"db","updateDate":"2022-06-27 10:36:27","remark":"isFatigue"},{"id":"004","type":0,"description":"健康码颜色","sortOrder":4,"isRequired":true,"isShown":true,"delFlag":"0","createBy":"db","createDate":"2022-06-27 10:30:56","updateBy":"db","updateDate":"2022-06-27 10:36:27","remark":"healthCardInfo"},{"id":"006","type":0,"description":"行程卡状态","sortOrder":6,"isRequired":true,"isShown":true,"delFlag":"0","createBy":"db","createDate":"2022-06-27 10:30:56","updateBy":"db","updateDate":"2022-06-27 10:36:27","remark":"travelInfo"}],"code":1,"msg":"查询成功"}
        self.token = "Bearer " + token
        self.description = ["体温情况", "新型冠状病毒肺炎主要症状：发热、干咳、乏力、咽痛、嗅(味) 觉减退、腹泻等", "健康码颜色", "行程卡状态"]

    def save_batch(self):
        if not self.whetherAvailable:
            print("无法执行打卡，请查看日志并反应给作者或查看更新")
            return {"code": -2}  # 无法执行打卡，请查看日志并反应给作者或查看更新
        header = {}
        header.update(self.header)
        header.update({"Host": self.host, "Authorization": self.token})
        url = str(self.school['href']) + self.findByType
        res = requests.get(url, headers=header)
        try:
            res_str = res.content.decode()
            res_json = json.loads(res_str)
            if res_json['code'] != 1:
                return {"code": -1}  # 协议失效
            data = res_json['data']
            if len(data) != 4:
                return {"code": 0}  # 打卡页更新
            for i in data:
                description = i['description']
                remark = i['remark']
                if description in self.description == False:
                    return {"code": 0}  # 打卡页更新
            # {"isTravel":0,"isContact":0,"isCohabit":0,"isFatigue":0,"isShortnessBreath":0,"travelInfoVo":{"relationshipInfo":[{"contactInfo":"","name":"","relationship":"","key":0}]},"contactInfo":{},"cohabitInfo":[{"name":"","province,city,disctrict":"","returnTime":"","transType":"","transTypeValue":"","transNumber":"","currentDetailResidence":"","contactInfo":0,"highRiskInfo":0,"governmentQuarantine":0,"homeQuarantine":0,"healthCardInfo":"","healthCardUrl":"","travelInfo":"","travelUrl":"","nucleicAcid":"","nucleicAcidMethod":"","nucleicAcidPointName":"","nucleicAcidSamplingDate":"","nucleicAcidAgency":"","nucleicAcidTime":"","nucleicAcidResult":"","nucleicAcidImg":"","key":0}],"healthCardInfo":"0","healthStatus":0,"travelInfo":"0","locateDetailedAddress":"重庆市江津区鼎山街道金钗井路40号","locateLatitude":29.29014,"locateLongitude":106.25936,"city":"重庆市","disctrict":"江津区","cityCode":"023","disctrictCode":"500116","province":"重庆市"}
            submit_information = {}
            submit_information.update(
                {"isTravel": 0, "isContact": 0, "isCohabit": 0, "isFatigue": 0, "isShortnessBreath": 0,
                 "travelInfoVo": {"relationshipInfo": [{"contactInfo": "", "name": "", "relationship": "", "key": 0}]},
                 "contactInfo": {}, "cohabitInfo": [
                    {"name": "", "province,city,disctrict": "", "returnTime": "", "transType": "", "transTypeValue": "",
                     "transNumber": "", "currentDetailResidence": "", "contactInfo": 0, "highRiskInfo": 0,
                     "governmentQuarantine": 0, "homeQuarantine": 0, "healthCardInfo": "", "healthCardUrl": "",
                     "travelInfo": "", "travelUrl": "", "nucleicAcid": "", "nucleicAcidMethod": "",
                     "nucleicAcidPointName": "", "nucleicAcidSamplingDate": "", "nucleicAcidAgency": "",
                     "nucleicAcidTime": "", "nucleicAcidResult": "", "nucleicAcidImg": "", "key": 0}],
                 "healthCardInfo": "0", "healthStatus": 0, "travelInfo": "0",
                 "locateDetailedAddress": "重庆市江津区鼎山街道金钗井路40号", "locateLatitude": 29.29014, "locateLongitude": 106.25936,
                 "city": "重庆市", "disctrict": "江津区", "cityCode": "023", "disctrictCode": "500116", "province": "重庆市"})
            submit_information.update({
                "locateLatitude": self.x,
                "locateLongitude": self.y,
                "locateDetailedAddress": address,
                "city": cityName,
                "disctrict": self.district,
                "cityCode": self.citycode,
                "disctrictCode": self.district,
                "province": cityName,
                "healthStatus": 0 if bodyTemperature == True else 1,  # 体温情况
                "isFatigue": 0 if abnormalSymptoms == True else 1,  # 是否健康
                "healthCardInfo": 0 if healthCodeColor == True else 1,  # 健康码颜色
                "travelInfo": 0 if travelCardStatus == True else 1,  # 行程卡状态
            })
            submit_information_str = json.dumps(submit_information)
            url = str(self.school['href']) + self.saveBatch
            header.update({"content-type": "application/json"})
            try:
                res = requests.post(url, headers=header, data=submit_information_str)
                res_str = res.content.decode()
                res_json = json.loads(res_str)
                if res_json['code'] != 1 | res_json['code'] != 0:
                    return {"code": -4, "msg": res_json['msg']}
                return {"code": 0, "msg": res_json['msg']}
            except:
                traceback.print_exc()
                return {"code": -3}  # 打卡失败，可能失效，如果打卡失效，可能字段出错，一般和打卡页一起更新，这里应该不可能
        except:
            traceback.print_exc()
            return {"code": -1}  # 协议失效

    def find_school(self, school_name):
        header = {}
        header.update(header)
        header.update({"Host": "ossc.cqcet.edu.cn", "content-type": "application/json"})
        res = requests.get(self.edu_pre_url, headers=header)
        try:
            res_str = res.content.decode()
            res_json = json.loads(res_str)
            name_list = []
            href_list = []
            for data in res_json:
                name_list.append(data['label'])
                href_list.append(data['value'])
            list = name_list.index(school_name)
            return {"name": name_list[list], "href": href_list[list], "code": 1}
        except:
            # traceback.print_exc()
            return {"name": "", "href": "", "code": -1}

    def txt_zhongjian(self, str, light, right):
        # 查找左边文本的结束位置
        start_pos = str.find(light)
        if start_pos == -1:
            return None
        start_pos += len(light)
        # 查找右边文本的起始位置
        stop_pos = str.find(right, start_pos)
        if stop_pos == -1:
            return None

        # 通过切片取出中间的文本
        return str[start_pos:stop_pos]

    def camouflage_ip(self):  # 暂时只能伪装电信ip,伪装其他地区ip更改106.84.
        return "106.84." + str(random.randint(146, 254)) + "." + str(random.randint(1, 254))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    gc = CqgcxxcjXcx()
    sc = gc.save_batch()
    if sc['code'] != 0:
        if "msg" in sc:  # msg不在返回里，在里边已经输出
            print(sc['msg'])
            print("code:" + str(sc['code']))
            if Bark != "":
                requests.get(Bark.format("打卡失败，请到服务器查看日志"))
    else:
        print(sc['msg'])
        if Bark != "":
            requests.get(Bark.format(sc['msg']))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
