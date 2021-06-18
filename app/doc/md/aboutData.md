# 站点数据

本站存储多源的震情和与之相关的灾情文件



# 数据编码说明

## 灾害信息类型编码

基本震情数据编码：`51`

房屋损伤数据编码：`21`

人员伤亡数据编码：`11`

## 单条地震信息编码
(国家)3位    (位置)16位     (时间)14位    (震级)2位

**其中**
- 国家
        使用三位英文字母缩写，如
    - CHN 中国
    - 000 外国(暂定)



- 位置
        使用经纬度（一位表示正负（正0负1），三位表示整数位，三位小数精度）进行编码，如
    - 23.1, 45.2  =>   00231000045200



- 时间 
        分配如下：4位年 2位月 2位日 2位时 2位分 2位秒，如
    - 2021.5.31 21:22:32   =>   20210531212232



- 震级
        按照标准地震震级，保留一位小数精度，如
    - 7.2  => 7.2  

# 数据存储

- Earthquake表（字段）
    - ID                 地震数据的id
    - OccurrenceTime     地震发生时间
    - Longitude          地震发生经度
    - Latitude           地震发生纬度
    - Depth              震源深度
    - Location           地震地点
    - Level              地震等级
    - EarthquakeEncode   地震编码
    - Source             数据来源
    - ReportingUnit      报告单位

- HouseDamaged表（字段）
    - ID                 房屋破坏数据的id
    - Category           房屋破坏种类
    - Date               破坏发生时间
    - Location           破坏发生位置
    - BasicallyIntactSquare   基本完好面积
    - DamagedSquare      破坏面积            
    - DestroyedSquare    毁坏面积
    - ReportingUnit      报告单位
    - EarthquakeId       对应的地震数据ID
    - Level              破坏等级
    
- InjuredStatistics表（字段）
    - Id                 人员伤亡数据id
    - Date               人员伤亡时间
    - Location           伤亡发生位置
    - DeathNumber        死亡人数
    - InjuredNumber      受伤人数            
    - MissingNumber      失踪人数
    - ReportingUnit      报告单位
    - EarthquakeId       对应的地震数据ID
    
三个表关系：  
Earthquake表与HouseDamaged表和InjuredStatistics表为一对多关系，通过外键EarthquakeId联系，一条地震数据会包含多个房屋毁坏数据和多个人员伤亡数据。

    







