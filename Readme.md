# 重庆信息采集——小程序自动采集
> 重庆部分单位采用了新的信息采集,小程序采集,本程序可以帮助自动采集
# 可用单位(学校)
> ['重庆市教育委员会', '西南大学', '西南政法大学', '重庆医科大学', '重庆师范大学', '重庆邮电大学', '重庆交通大学', '重庆工商大学', '四川外国语大学', '重庆理工大学', '重庆三峡学院', '重庆文理学院', '长江师范学院', '重庆科技学院', '重庆第二师范学院', '重庆人文科技学院', '重庆工程学院', '重庆对外经贸学院', '重庆财经学院', '重庆工商大学派斯学院', '重庆外语外事学院', '重庆移通学院', '重庆城市科技学院', '重庆机电职业技术大学', '重庆开放大学（重庆工商职业学院）', '重庆电子工程职业学院', '重庆电力高等专科学校', '重庆三峡医药高等专科学校', '重庆医药高等专科学校', '重庆幼儿师范高等专科学校', '重庆航天职业技术学院', '重庆工业职业技术学院', '重庆城市管理职业学院', '重庆工程职业技术学院', '重庆三峡职业学院', '重庆工贸职业技术学院', '重庆水利电力职业技术学院', '重庆城市职业学院', '重庆青年职业技术学院', '重庆财经职业学院', '重庆建筑工程职业学院', '重庆商务职业学院', '重庆化工职业学院', '重庆旅游职业学院', '重庆安全技术职业学院', '重庆文化艺术职业学院', '重庆传媒职业学院', '重庆信息技术职业学院', '重庆建筑科技职业学院', '重庆应用技术职业学院', '重庆科创职业学院', '重庆电讯职业学院', '重庆能源职业学院', '重庆交通职业学院', '重庆公共运输职业学院', '重庆艺术工程职业学院', '重庆电信职业学院', '重庆科技职业学院', '重庆经贸职业学院', '重庆资源与环境保护职业学院', '重庆智能工程职业学院', '重庆健康职业学院', '重庆工信职业学院', '中国科学院大学重庆学院', '重庆五一职业技术学院']
# 使用方法
> 在配置区内填写：单位(学校)。本人(使用者)每日所在地(若使用者每日所在地不同，请勿使用本程序)。小程序token。小程序要求的信息(健康码状态，行程卡状态，是否健康，温度是否正常等)。  
> 随后将本程序放入linux服务器，输入:crontab -e编辑 python3 脚本位置\脚本名称.py >> 脚本位置\log.log  
> token提取方法：电脑打开抓包工具，例如：Fiddler。打开微信，进入信息采集小程序，点击 我的 进入抓包工具查看xxx.edu.xx 查看请求头,你会看到：Authorization: Bearer xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx，你只需要复制xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx即可，图文教程https://www.kancloud.cn/amen12138/cqxxcjtoken/content
# 声明
> 此程序仅用于特别忙的人群，禁止用本程序非法自动采集(乱填地区，乱填城市，乱填任何信息) 否则导致的信息异常，本程序作者概不负责。若你填写的是健康，但实际本人不健康，应立即停用或更新配置，否则造成的信息异常，作者本人概不负责
# 作者有话说
> 脚本本人也会使用，因为本人常在某楼,并且会随时关注自己的健康状态(可随时更新配置)，并填写信息这种繁琐的事情，通常采用自动，若本程序触犯了 某单位 的原则(并非利益) 本人将立即将此仓库变为私人仓库(并不会下架，此程序是本人的辛苦成功)