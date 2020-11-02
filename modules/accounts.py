import re

import dateparser


def get_eating_account(from_user, description, time=None):
    if time == None or not hasattr(time, 'hour'):
        return 'Expenses:Eating:Others'
    elif time.hour <= 3 or time.hour >= 21:
        return 'Expenses:Eating:Nightingale'
    elif time.hour <= 10:
        return 'Expenses:Eating:Breakfast'
    elif time.hour <= 16:
        return 'Expenses:Eating:Lunch'
    else:
        return 'Expenses:Eating:Supper'


def get_credit_return(from_user, description, time=None):
    for key, value in credit_cards.items():
        if key == from_user:
            return value
    return "Unknown"


public_accounts = [
    'Liabilities:CreditCard:花呗'
]

credit_cards = {
    '中信银行': 'Liabilities:CreditCard:CITIC',
}

accounts = {
    "余额宝": 'Assets:Company:Alipay:MonetaryFund',
    '余利宝': 'Assets:Bank:MyBank',
    '花呗': 'Liabilities:CreditCard:Huabei',
    '建设银行': 'Liabilities:CreditCard:CCB',
    '招商银行(7033)': 'Liabilities:CreditCard:招商银行',
    '招商银行(1386)': 'Assets:Bank:招商银行',
    '零钱': 'Assets:Balances:WeChat',
}

descriptions = {
    #'滴滴打车|滴滴快车': get_didi,
    '余额宝.*收益发放': 'Assets:Company:Alipay:MonetaryFund',
    '转入到余利宝': 'Assets:Bank:MyBank',
    '花呗收钱服务费': 'Expenses:Fee',
    '自动还款-花呗.*账单': 'Liabilities:CreditCard:Huabei',
    '信用卡自动还款|信用卡还款': get_credit_return,
    '外卖订单': get_eating_account,
    '美团订单': get_eating_account,
    '上海交通卡发行及充值': 'Expenses:Transport:Card',
    '地铁出行': 'Expenses:Transport:City',
    '火车票': 'Expenses:Travel:Transport',
    '深圳地铁': 'Expenses:Traffic:地铁',
}

incomes = {
    '余额宝.*收益发放': 'Income:Trade:PnL',
}

anothers = {
    '福万家百货': 'Expenses:DailyNecessities',
    '白鹿塬油泼面（宝华店）': get_eating_account,
    '永丰店': 'Expenses:DailyNecessities',
    '廣式脆皮烧腊': get_eating_account,
    '黄焖鸡米饭云南过桥米线': get_eating_account,
    '龙光大厦店': 'Expenses:DailyNecessities',
    '原味汤粉王': get_eating_account,
    '美宜佳（11880店）': 'Expenses:DailyNecessities',
    '滴滴出行': 'Expenses:Traffic:滴滴',
    '中国电信': 'Expenses:通讯:话费充值',
    '叁无粉蒸（科华店）': get_eating_account,
    '马路边边麻辣烫': get_eating_account,
    '茶百道': get_eating_account,
    '饿了么': get_eating_account,
    '馥饮咖啡成都科华北路店': 'Expenses:Drink:Coffee',
    '上海蒜芽信息科技有限公司': 'Expenses:Traffic:Transport',
    '中国铁路网络有限公司': 'Expenses:Traffic:Transport',
    '享道出行': 'Expenses:Traffic:高德打车',
    '成都黄师傅烤鸡腿春熙路店': get_eating_account,
    '锦江区国良良友服饰店': 'Expenses:服饰',
    '大熊抄手（大食代IFS店）': get_eating_account,
    '炸货铺（大食代IFS）': get_eating_account,
    '福熹生煎(大食代IFS店)': get_eating_account,
    '万源市大麦服装店': 'Expenses:服饰',
    '群光大陆实业（成都）有限公司': get_eating_account,
    '雷门拉面（群光广场店）': get_eating_account,
    '天猫小店福家超市成都棕南西街店': get_eating_account,
    '奔腾上海专卖店': 'Expenses:DailyNecessities',
    '北京瓦力网络科技有限公司': 'Expenses:Internet:虚拟消费',
    '阿啦山口': get_eating_account,
    '茶百道（武侯来福士店）': 'Expenses:Drink:奶茶',
    '青羊区程氏宫廷糕点铺': 'Expenses:Eating:零食',
    '成都甜甜香红星路店': 'Expenses:Eating:零食',
    '味绝美蛙鱼头（科华店）': 'get_eating_account',
    '婷': 'Expenses:家人消费',
    '东方航空电子商务有限公司': 'Expenses:Traffic:Transport',
    '潮之味': get_eating_account,
    '中国兰州拉面': get_eating_account,
    '蚂蚁会员（北京）网络技术服务有限公司': 'Expenses:相互宝分摊',
    '鹅宗族': get_eating_account,
    '深圳市安全区新鲜物语便捷超市': 'Expenses:DailyNecessities',
    '东润便利店': 'Expenses:DailyNecessities',
    '王氏果业(深圳宝安区)': 'Expenses:DailyNecessities',
    '唐氏锅贴': get_eating_account,
    '大润华生鲜超市新洲店': 'Expenses:DailyNecessities',
    '心所向必有成': 'Expenses:Internet:虚拟消费',
    #'*洁萍': 'Expenses:House:房租',
    '宝安永丰社区美宜佳': 'Expenses:DailyNecessities',
    '秦都一面': get_eating_account,
    '深圳南山双喜重庆小面': get_eating_account,
    '遵义虾子羊肉粉': get_eating_account,
    '一绝烤面筋深圳坪洲店': get_eating_account,
    '湘岳城市蒸菜': get_eating_account,
    '深圳市龙岗区坂田王威民间瓦罐煨汤餐厅': get_eating_account,
    '聚福缘营养自选快餐': get_eating_account,
    'App Store & Apple Music': 'Expenses:Internet:虚拟消费',
    '宝安大仟里店': 'Expenses:DailyNecessities',
    '婷(王婷)': 'Expenses:Transfer:转账',
    '广州酷狗计算机科技有限公司': 'Expenses:Internet:虚拟消费',
    #'*思尧': 'Expenses:DailyNecessities',
    '7-Eleven(龙光世纪)': 'Expenses:DailyNecessities',
    '王氏果业': 'Expenses:DailyNecessities',
    '百佳兴': 'Expenses:DailyNecessities',
    '丛林的鱼': get_eating_account,
    '湘岳城市蒸菜深圳西乡店': get_eating_account,
    '韬缘轩(宝华旺店)': get_eating_account,
    '晗宝儿e商城': 'Expenses:DailyNecessities',
    '慕乐家居旗舰店': 'Expenses:DailyNecessities',
    '宝安轻铁西九巷美宜佳': 'Expenses:DailyNecessities',
    '公牛仪乐专卖店': 'Expenses:DailyNecessities',
    '中国联通': 'Expenses:通讯:话费充值',
    '重庆麻辣烫': get_eating_account,
    '财富港店': 'Expenses:DailyNecessities',
    '益禾堂': 'Expenses:Drink:奶茶',
    'zhanyuehao': get_eating_account,
    '维客佳唯一店': 'Expenses:DailyNecessities',
    "家乐购连锁超市(华凯店)": 'Expenses:DailyNecessities',
    '大东北首席烤冷面': get_eating_account,
    '嘉盛果业': 'Expenses:Eating:零食',
    '深圳市人人乐商业有限公司': 'Expenses:DailyNecessities',
    '中国电信电渠中心': 'Expenses:通讯:话费充值',
    '麻辣凉菜': get_eating_account,
    '味之缘深圳秀海路店': get_eating_account,
    '深圳市康福万家医药连锁有限公司': 'Expenses:医疗',
    '腾杨数码配件': 'Expenses:ELectronic',
    '佳豆御坊': get_eating_account,
    '深圳市宝安区西乡钻石（皇冠蛋糕店）': 'Expenses:Eating:零食',
    '深圳市罗湖区深惠烟行': 'Expenses:DailyNecessities',
    '宝安坪洲地铁口美宜佳': 'Expenses:DailyNecessities',
    '虾子羊肉粉深圳宝华店': get_eating_account,
    '义贤': 'Expenses:DailyNecessities',
    '中业爱民10786店': 'Expenses:DailyNecessities',
    '袁红贵': 'Expenses:DailyNecessities',
    '深圳市宝安区西乡铭汇港商行': 'Expenses:DailyNecessities',
    '小碗菜': get_eating_account,
    'luckincoffee': 'Expenses:Drink:Coffee',
    '老上海馄饨铺龙光店': get_eating_account,
    '铭': 'Expenses:DailyNecessities',
    '家乐购连锁超市(华凯店4816)': 'Expenses:DailyNecessities',
    '小米姑娘深圳宝安店': get_eating_account,
    '老上海馄饨铺(龙光店)': get_eating_account,
}

description_res = dict([(key, re.compile(key)) for key in descriptions])
another_res = dict([(key, re.compile(key)) for key in anothers])
income_res = dict([(key, re.compile(key)) for key in incomes])
