# _*_ coding: utf-8 _*_
__author__ = 'xbr'
__date__ = '2019/1/11 14:49'

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 用来正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# 获取PM2.5数据
df = pd.read_excel(r'D:\data\20180101PM25-CHINA.xlsx')
# 剔除无效值NAN
df = df.dropna(axis=0, how='any')

lat = np.array(df["lat"][:])  # 获取维度之维度值
lon = np.array(df["lon"][:])  # 获取经度值
PM25 = np.array(df["PM25"][:], dtype=float)
# 画图
fig = plt.figure(figsize=(16, 9))
plt.rc('font', size=15, weight='bold')
ax = fig.add_subplot(111)
# 添加标题,PM2.5下标设置
plt.title(u'2018年01月01日中国地区$\mathrm{PM}_{2.5}$质量浓度分布', size=25, weight='bold')
# 创建底图,等经纬度投影
mp = Basemap(llcrnrlon=73., llcrnrlat=17.,
             urcrnrlon=135., urcrnrlat=55,
             projection='cyl', resolution='h')
# 添加海岸线
mp.drawcoastlines()
# 添加国家行政边界
mp.drawcountries()
# 设置colorbar中颜色间隔个数
levels = np.linspace(0, np.max(PM25), 20)
# cf = mp.scatter(lon, lat, PM25, marker='o', color='r')
# 设置颜色表示数值大小
cf = mp.scatter(lon, lat, PM25, c=PM25, cmap='jet', alpha=0.75)
# 设置上下标以及单位的希腊字母
cbar = mp.colorbar(cf, location='right', format='%d', size=0.3,
                   ticks=np.linspace(0, np.max(PM25), 10),
                   label='$\mathrm{PM}_{2.5}$($\mu$g/$\mathrm{m}^{3}$)')
plt.show()
