# _*_ coding: utf-8 _*_
__author__ = 'xbr'
__date__ = '2019/1/11 14:09'

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

maps = Basemap(projection='cyl', lat_0=0, lon_0=0)
# 首先给地球涂上蓝色
maps.drawmapboundary(fill_color='aqua')
# 再给大陆涂上橘黄色,给江河湖泊涂上大海一样的颜色
maps.fillcontinents(color='coral', lake_color='blue')
maps.drawcoastlines()
plt.show()
# plt.savefig('test.png')
