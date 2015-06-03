#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET

section_area = {'zoin':0.0, 'sanmin':0.0, 'gusun':0.0, 'fonsun':0.0,
                'nanzi':0.0, 'linya':0.0, 'chenzen':0.0, 'zenwu':0.0,
                'sinsin':0.0, 'shougun':0.0, 'daliao':0.0, 'niaoso':0.0,
                'chenchi':0.0, 'gunshan':0.0, 'menon':0.0, 'daser':0.0,
                'chiaoto':0.0, 'yunchen':0.0, 'dasu':0.0, 'yenchao':0.0,
                'hune':0.0, 'chishan':0.0, 'linyuan':0.0, 'singuan':0.0,
                'luzu':0.0, 'alian':0.0, 'sunlin':0.0, 'liugue':0.0,
                'gasan':0.0, 'nemen':0.0, 'chedin':0.0, 'mito':0.0,
                'chizin':0.0, 'tenliao':0.0, 'uonan':0.0, 'taouan':0.0,
                'namacha':0.0, 'maolin':0.0}
section_price = {'zoin':0, 'sanmin':0, 'gusun':0, 'fonsun':0,
                'nanzi':0, 'linya':0, 'chenzen':0, 'zenwu':0,
                'sinsin':0, 'shougun':0, 'daliao':0, 'niaoso':0,
                'chenchi':0, 'gunshan':0, 'menon':0, 'daser':0,
                'chiaoto':0, 'yunchen':0, 'dasu':0, 'yenchao':0,
                'hune':0, 'chishan':0, 'linyuan':0, 'singuan':0,
                'luzu':0, 'alian':0, 'sunlin':0, 'liugue':0,
                'gasan':0, 'nemen':0, 'chedin':0, 'mito':0,
                'chizin':0, 'tenliao':0, 'uonan':0, 'taouan':0,
                'namacha':0, 'maolin':0}
i = 0

zoin = u"左營區"
sanmin = u"三民區"
gusun = u"鼓山區"
fonsun = u"鳳山區"
nanzi = u"楠梓區"
linya = u"苓雅區"
chenzen = u"前鎮區"
zenwu = u"仁武區"
sinsin = u"新興區"
shougun = u"小港區"
daliao = u"大寮區"
nialso = u"鳥松區"
chenchi = u"前金區"
gunshan = u"岡山區"
menon = u"美濃區"
daser = u"大社區"
chiaoto = u"橋頭區"
yunchen = u"鹽埕區"
dasu = u"大樹區"
yenchao = u"燕巢區"
hune = u"湖內區"
chishan = u"旗山區"
linyuan = u"林園區"
singuan = u"梓官區"
luzu = u"路竹區"
alian = u"阿蓮區"
sunlin = u"杉林區"
liugue = u"六龜區"
gasun = u"甲仙區"
nemen = u"內門區"
chedin = u"茄萣區"
mito = u"彌陀區"
chizin = u"旗津區"
tenliao = u"田寮區"
uonan = u"永安區"
taouan = u"桃源區"
namacha = u"那瑪夏區"
maolin = u"茂林區"

tree = ET.parse('E_LVR_LAND_A.XML')
root = tree.getroot()
for child in root:
    if child[0].text == zoin:
        area_tmp = section_area['zoin']
        area_tmp = area_tmp + float(child[15].text)
        section_area['zoin'] = area_tmp
        price_tmp = section_price['zoin']
        price_tmp = price_tmp + int(child[21].text)
        section_price['zoin'] = price_tmp
    elif child[0].text == sanmin:
        area_tmp = section_area['sanmin']
        area_tmp = area_tmp + float(child[15].text)
        section_area['sanmin'] = area_tmp
        price_tmp = section_price['sanmin']
        price_tmp = price_tmp + int(child[21].text)
        section_price['sanmin'] = price_tmp
    elif child[0].text == gusun:
        area_tmp = section_area['gusun']
        area_tmp = area_tmp + float(child[15].text)
        section_area['gusun'] = area_tmp
        price_tmp = section_price['gusun']
        price_tmp = price_tmp + int(child[21].text)
        section_price['gusun'] = price_tmp
    elif child[0].text == fonsun:
        area_tmp = section_area['fonsun']
        area_tmp = area_tmp + float(child[15].text)
        section_area['fonsun'] = area_tmp
        price_tmp = section_price['fonsun']
        price_tmp = price_tmp + int(child[21].text)
        section_price['fonsun'] = price_tmp
    elif child[0].text == linya:
        area_tmp = section_area['linya']
        area_tmp = area_tmp + float(child[15].text)
        section_area['linya'] = area_tmp
        price_tmp = section_price['linya']
        price_tmp = price_tmp + int(child[21].text)
        section_price['linya'] = price_tmp
    elif child[0].text == chenzen:
        area_tmp = section_area['chenzen']
        area_tmp = area_tmp + float(child[15].text)
        section_area['chenzen'] = area_tmp
        price_tmp = section_price['chenzen']
        price_tmp = price_tmp + int(child[21].text)
        section_price['chenzen'] = price_tmp
    elif child[0].text == sinsin:
        area_tmp = section_area['sinsin']
        area_tmp = area_tmp + float(child[15].text)
        section_area['sinsin'] = area_tmp
        price_tmp = section_price['sinsin']
        price_tmp = price_tmp + int(child[21].text)
        section_price['sinsin'] = price_tmp
    elif child[0].text == shougun:
        area_tmp = section_area['shougun']
        area_tmp = area_tmp + float(child[15].text)
        section_area['shougun'] = area_tmp
        price_tmp = section_price['shougun']
        price_tmp = price_tmp + int(child[21].text)
        section_price['shougun'] = price_tmp
    elif child[0].text == chenchi:
        area_tmp = section_area['chenchi']
        area_tmp = area_tmp + float(child[15].text)
        section_area['chenchi'] = area_tmp
        price_tmp = section_price['chenchi']
        price_tmp = price_tmp + int(child[21].text)
        section_price['chenchi'] = price_tmp
    elif child[0].text == yunchen:
        area_tmp = section_area['yunchen']
        area_tmp = area_tmp + float(child[15].text)
        section_area['yunchen'] = area_tmp
        price_tmp = section_price['yunchen']
        price_tmp = price_tmp + int(child[21].text)
        section_price['yunchen'] = price_tmp
        
print u"左營區單價==", (section_price['zoin'] / (section_area['zoin'] * 0.3025))
print u"三民區單價==", (section_price['sanmin'] / (section_area['sanmin'] * 0.3025))
print u"鼓山區單價==", (section_price['gusun'] / (section_area['gusun'] * 0.3025))
print u"鳳山區單價==", (section_price['fonsun'] / (section_area['fonsun'] * 0.3025))
print u"苓雅區單價==", (section_price['linya'] / (section_area['linya'] * 0.3025))
print u"前鎮區單價==", (section_price['chenzen'] / (section_area['chenzen'] * 0.3025))
print u"新興區單價==", (section_price['sinsin'] / (section_area['sinsin'] * 0.3025))
print u"小港區單價==", (section_price['shougun'] / (section_area['shougun'] * 0.3025))
print u"前金區單價==", (section_price['chenchi'] / (section_area['chenchi'] * 0.3025))
print u"鹽埕區單價==", (section_price['yunchen'] / (section_area['yunchen'] * 0.3025))


query_area = u"建物移轉總面積平方公尺"
query_money = u"總價元"
total_area = 0.0
total_ping = 0.0
total_money = 0

tree = ET.parse('E_LVR_LAND_A.XML')
root = tree.getroot()

for area in root.iter(query_area):
    total_area = total_area + float(area.text)

print u"總平方公尺==", total_area
total_ping = total_area * 0.3025
print u"總坪數==", total_ping

for money in root.iter(query_money):
    total_money = total_money + int(money.text)

print u"總價累加==", total_money
print u"每坪單價==", (total_money / total_ping)