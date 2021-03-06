'''
/******************************************************************************
 * 0000-5000年间 二十四节气详细时间推算程序 
 * ============================================================================
 * 程序作者 ：德充符  QQ:277839096  (2010/8/14)
 * 网站地址: www.liuv.net & www.zuijin.net
 * ----------------------------------------------------------------------------
 * 本程序主要采用PHP语言实现。功能是推算0000年到5000年间二十四节气的详细更迭时间。
 * 本程序提供的推算时间最大误差在20分钟左右，平均误差在6分钟左右。
 * 所有结果仅供参考，欢迎提出意见，相互交流。
 * ============================================================================
 * $name   : 配置程序
 * $Author : 德充符
 * $contact: mustdone@163.com $
------------------------------二十四节气介绍-----------------------------------------
 * 二十四节气是中国古代订立的一种用来指导农事的补充历法，是在春秋战国时期形成的。
-由于中国农历是一种“阴阳合历”，即根据太阳也根据月亮的运行制定的，因此不能完全
-反映太阳运行周期，但中国又是一个农业社会，农业需要严格了解太阳运行情况，农事完
-全根据太阳进行，所以在历法中又加入了单独反映太阳运行周期的“二十四节气”，用作
-确定闰月的标准。二十四节气能反映季节的变化，指导农事活动，影响着千家万户的衣食
-住行。二十四节气是根据太阳在黄道（即地球绕太阳公转的轨道）上的位置来划分的。
------------------------------二十四节气介绍-----------------------------------------
立春,雨水,惊蛰,春分,清明,谷雨,立夏,小满,芒种,夏至,小暑,大暑
秋分,寒露,霜降,立冬,小雪,大雪,冬至,小寒,大寒,立秋,处暑,白露
*******************************************************************************/
'''

def jieqiming(num):
    names = ('立春', '雨水', '惊蛰', '春分', '清明', '谷雨', '立夏', '小满', '芒种', '夏至', '小暑',
             '大暑', '立秋', '处暑', '白露', '秋分', '寒露', '霜降', '立冬', '小雪', '大雪', '冬至', '小寒', '大寒')
    return names[int(num)]


detailjieqi = (
    {
        "name": "立春",
        "ename": "the Beginning of Spring",
        "time": "2月3~5日",
        "sanhou": "东风解冻、蛰虫始振、鱼上冰。",
        "content": "斗指东北。太阳黄经为315度。是二十四个节气的头一个节气。其含意是开始进入春天，“阳和起蛰，品物皆春”，过了立春，万物复苏生机勃勃，一年四季从此开始了。"
    },
    {
        "name": "雨水",
        "ename": "Rain Water",
        "time": "2月18~20日",
        "sanhou": "獭祭鱼、鸿雁来、草木萌动。",
        "content": "斗指壬。太阳黄经为330°。这时春风遍吹，冰雪融化，空气湿润，雨水增多，所以叫雨水。人们常说：“立春天渐暖，雨水送肥忙”。"},
    {
        "name": "惊蛰",
        "ename": "the Waking of Insects",
        "time": "3月5~7日",
        "sanhou": "桃始花、仓庚鸣、鹰化为鸠。",
        "content": "斗指丁。太阳黄经为345°。这个节气表示“立春”以后天气转暖，春雷开始震响，蛰伏在泥土里的各种冬眠动物将苏醒过来开始活动起来，所以叫惊蛰。这个时期过冬的虫排卵也要开始孵化。我国部分地区过入了春耕季节。谚语云：“惊蛰过，暖和和，蛤蟆老角唱山歌。”“惊蛰一犁土，春分地气通。”“惊蛰没到雷先鸣，大雨似蛟龙。“ "},
    {
        "name": "春分",
        "ename": "the Spring Equinox",
        "time": "3月20~21日",
        "sanhou": "玄鸟至、雷乃发声、始电。",
        "content": "斗指壬。太阳黄经为0°。春分日太阳在赤道上方。这是春季90天的中分点，这一天南北两半球昼夜相等，所以叫春分。这天以后太阳直射位置便向北移，北半球昼长夜短。所以春分是北半球春季开始。我国大部分地区越冬作物进入春季生长阶段。各地农谚有：“春分在前，斗米斗钱”（广东）、“春分甲子雨绵绵，夏分甲子火烧天”（四川）、“春分有雨家家忙，先种瓜豆后插秧”（湖北）、“春分种菜，大暑摘瓜”（湖南）、“春分种麻种豆，秋分种麦种蒜”（安徽）。 "},
    {
        "name": "清明",
        "ename": "Pure Brightness",
        "time": "4月4~6日",
        "sanhou": "桐始华、鼠化为鴽、虹始见。",
        "content": "斗指丁。太阳黄经为15°。此时气候清爽温暖，草木始发新枝芽，万物开始生长，农民忙于春耕春种。从前，在清明节这一天，有些人家都在门口插上杨柳条，还到郊外踏青，祭扫坟墓，这是古老的习俗。"},
    {
        "name": "谷雨",
        "ename": "Grain Rain",
        "time": "4月19~21日",
        "sanhou": "萍始生、鸣鸠拂其羽、戴胜降于桑。",
        "content": "斗指癸。太阳黄经为30°。就是雨水生五谷的意思，由于雨水滋润大地五谷得以生长，所以，谷雨就是“雨生百谷”。谚云“谷雨前后，种瓜种豆”。 "},
    {
        "name": "立夏",
        "ename": "the Beginning of Summer",
        "time": "5月5~7日",
        "sanhou": "蝼蝈鸣、蚯蚓出、王瓜生。",
        "content": "斗指东南。太阳黄经为45°。是夏季的开始，从此进入夏天，万物旺盛大。习惯上把立夏当作是气温显著升高，炎暑将临，雷雨增多，农作物进入旺季生长的一个最重要节气。"},
    {
        "name": "小满",
        "ename": "Lesser Fullness of Grain",
        "time": "5月20~22日",
        "sanhou": "苦菜秀、靡草死、小暑至。",
        "content": "斗指甲。太阳黄经为60°。从小满开始，大麦、冬小麦等夏收作物，已经结果、籽粒饱满，但尚未成熟，所以叫小满。"},
    {
        "name": "芒种",
        "ename": "Grain in Beard",
        "time": "6月5~7日",
        "sanhou": "螳螂生、鵙始鸣、反舌无声。",
        "content": "北斗指向已。太阳黄经为75°。这时最适合播种有芒的谷类作物，如晚谷、黍、稷等。如过了这个时候再种有芒和作物就不好成熟了。同时，“芒”指有芒作物如小麦、大麦等，“种”指种子。芒种即表明小麦等有芒作物成熟。芒种前后，我国中部的长江中、下游地区，雨量增多，气温升高，进入连绵阴雨的梅雨季节，空气非常潮湿，天气异常闷热，各种器具和衣物容易发霉，所以在我国长江中、下游地区也叫“霉雨”。"},
    {
        "name": "夏至",
        "ename": "the Summer Solstice",
        "time": "6月21~22日",
        "sanhou": "鹿角解、蜩始鸣、半夏生。",
        "content": "北斗指向乙。太阳黄经为90°。太阳在黄经90°“夏至点”时，阳光几乎直射北回归线上空，北半球正午太阳最高。这一天是北半球白昼最长、黑夜最短的一天，从这一天起，进入炎热季节，天地万物在此时生长最旺盛。所心以古时候又把这一天叫做日北至，意思是太阳运生到最北的一日。过了夏至，太阳逐渐向南移动，北半球白昼一天比一天缩短，黑夜一天比一天加长。"},
    {
        "name": "小暑",
        "ename": "Lesser Heat",
        "time": "7月6~8日",
        "sanhou": "温风至、蟋蟀居辟、鹰乃学习。",
        "content": "斗指辛。太阳黄经为105°。天气已经很热，但不到是热的时候，所以叫小暑。此时，已是初伏前后。"},
    {
        "name": "大暑",
        "ename": "Greater Heat ",
        "time": "7月22~24日",
        "sanhou": "腐草化为萤、土润溽暑、大雨时行。",
        "content": "斗指丙。太阳黄经为120°。大暑是一年中最热的节气，正值勤二伏前后，长江流域的许多地方，经常出现40℃高温天气。要作好防暑降温工作。这个节气雨水多，在“小暑、大暑，淹死老鼠”的谚语，要注意防汛防涝。"},
    {
        "name": "立秋",
        "ename": "the Beginning of Autumn",
        "time": "8月7~9日",
        "sanhou": "凉风至、白露降、寒蝉鸣。",
        "content": "北斗指向西南。太阳黄经为135°。从这一天起秋天开始，秋高气爽，月明风清。此后，气温由最热逐渐下降。"},
    {
        "name": "处暑",
        "ename": "the End of Heat ",
        "time": "8月22~24日",
        "sanhou": "鹰乃祭鸟、天地始肃、禾乃登。",
        "content": "斗指戊。太阳黄经为150°。这时夏季火热已经到头了。暑气就要散了。它是温度下降的一个转折点。是气候变凉的象征，表示暑天终止。"},
    {
        "name": "白露",
        "ename": "White Dew",
        "time": "9月7~9日",
        "sanhou": "鸿雁来、玄鸟归、群鸟养羞。",
        "content": "斗指癸。太阳黄经为165°。天气转凉，地面水汽结露最多。"},
    {
        "name": "秋分",
        "ename": "the Autumn Equinox",
        "time": "9月22~24日",
        "sanhou": "雷始收声、蛰虫培户、水始涸。",
        "content": "斗指已。太阳黄经为180°。秋分这一天同春人一样，阳光几乎直射赤道，昼夜几乎相等。从这一天起，阳光直射位置继续由赤道向南半球推移，北半球开始昼短夜长。依我国旧历的秋季论，这一天刚好是秋季九十天的一半，因而称秋分。但在天文学上规定，北半球的秋天是从秋分开始的。"},
    {
        "name": "寒露",
        "ename": "Cold Dew",
        "time": "10月8~10日",
        "sanhou": "鸿雁来宾、雀攻大水为蛤、菊有黄花。",
        "content": "斗指甲。太阳黄经为195°。白露后，天气转凉，开始出现露水，到了寒露，则露水日多，且气温更低了。所以，有人说，寒是露之气，先白而后寒，是气候将逐渐转冷的意思。而水气则凝成白色露珠。"},
    {
        "name": "霜降",
        "ename": "Frost\'s Descent",
        "time": "10月23~24日",
        "sanhou": "豺乃祭兽、草木黄落、蛰虫咸俯。",
        "content": "太阳黄经为210°。天气已冷，开始有霜冻了，所以叫霜降。"},
    {
        "name": "立冬",
        "ename": "the Beginning of Winter",
        "time": "11月7~8日",
        "sanhou": "水始冰、地始冻、雉入大水为蜃。",
        "content": "太阳黄经为225°。习惯上，我国人民把这一天当作冬季的开始。冬，作为终了之意，是指一年的田间操作结束了，作物收割之后要收藏起来的意思。立冬一过，我国黄河中、下游地区即将结冰，我国各地农民都将陆续地转入农田水利基本建设和其他农事活动中。"},
    {
        "name": "小雪",
        "ename": "Lesser Snow",
        "time": "11月22~23日",
        "sanhou": "虹藏不见、天气上腾、闭塞而成冬。",
        "content": "太阳黄经为240°。气温下降，开始降雪，但还不到大雪纷飞的时节，所以叫小雪。小雪前后，黄河流域开始降雪（南方降雪还要晚两个节气）；而北方，已进入封冻季节。"},
    {
        "name": "大雪",
        "ename": "Greater Snow",
        "time": "12月6~8日",
        "sanhou": "鴠鸟不鸣、虎始交、荔挺生。",
        "content": "太阳黄经为255°。大雪前后，黄河流域一带渐有积雪；而北方，已是“千里冰封，万里雪飘荡”的严冬了。"},
    {
        "name": "冬至",
        "ename": "the Winter Solstice",
        "time": "12月21~23日",
        "sanhou": "蚯蚓结、麋角解、水泉动。",
        "content": "太阳黄经为270°。冬至这一天，阳光几乎直射南回归线，我们北半球白昼最短，黑夜最长，开始进入数九寒天。天文学上规定这一天是北半球冬季的开始。而冬至以后，阳光直射位置逐渐向北移动，北半球的白天就逐渐长了，谚云：吃了冬至面，一天长一线。"},
    {
        "name": "小寒",
        "ename": "Lesser Cold",
        "time": "1月5~7日",
        "sanhou": "雁北向、鹊始巢、雉始雊。",
        "content": "太阳黄经为285°。小寒以后，开始进入寒冷季节。冷气积久而寒，小寒是天气寒冷但还没有到极点的意思。"},
    {
        "name": "大寒",
        "ename": "Greater Cold",
        "time": "1月20~21日",
        "sanhou": "鸡始乳、鸷鸟厉疾、水泽腹坚。",
        "content": "太阳黄经为300°。大寒就是天气寒冷到了极点的意思。大寒前后是一年中最冷的季节。大寒正值三九刚过，四九之初。谚云：“三九四九冰上走”。 "},
)
