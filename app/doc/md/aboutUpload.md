# 本站数据系统

本站使用 FTP+数据库 的形式存储数据

## FTP相关

FTP地址：`ftp://47.93.229.92/`
账户名：`dataput` 密码：`114514`


### FTP文件结构

用户能够登录FTP系统直接上传文件，其中upload是其放置上传文件的地方

```bash
├─error      # 非法文件放在这里
├─scanned
│  └─...     # 扫描后的文件放在这里
└─upload     # 上传文件夹，定时对其扫描

```


## 上传文件格式

### 震情数据

```json
{
"disasters": [
        {
            "TypeCode": 51,
            "Category": "基本震情",
            "OccurrenceTime": "2021-04-21 10:15:57",
            "Longitude": 116.63,
            "Latitude": 40.16,
            "Depth": 15,
            "Level": 7.0,
            "Location":"China",
            "ReportingUnit": "北京地震局",
            "Images": [
                "1.png",
                "2.png"
            ]
        },
        {
            "TypeCode": 51,
            "Category": "基本震情",
            "OccurrenceTime": "2022-04-21 10:15:57",
            "Longitude": 117.63,
            "Latitude": 41.16,
            "Depth": 16,
            "Level": 8.0,
            "Location":"China",
            "ReportingUnit": "北京地震局",
            "Images": [
                "3.png",
                "4.png"
            ]
        }
    ]
}
```

或者选择如下格式的CSV文件
```text
TypeCode, Category, OccurrenceTime, Longitude, Latitude, Depth, Level, Location, ReportingUnit, Images

25, 1, 2021-04-21 10:15:57, 116.63, 40.16, 15, 7.0, China, 北京地震局, 1.png;2.png
```

### 灾情数据

#### 房屋损伤
```json
{
"disasters": [
        {
            "TypeCode": 21,
            "Category": "房屋损伤",
            "Date": "2021-04-21 10:15:57",
            "Location": "北京市东城区东华门街道多福巷社区居委会",
            "BasicallyIntactSquare": 40.16,
            "DamagedSquare": 15,
            "DestroyedSquare": 7.2,
            "Level":"严重",
            "ReportingUnit": "多福巷社区居委会",
            "EarthquakeEncode":"CHN0102000055002021042110155734",
            "Images": [
                "1.png",
                "2.png"
            ]
        }
    ]
}

```


或者选择如下格式的CSV文件
```text
TypeCode, Category, Date, Location, BasicallyIntactSquare, DamagedSquare, DestroyedSquare,Level, ReportingUnit, EarthquakeId, Images

21, "房屋损伤", 2021-04-21 10:15:57, 北京市东城区东华门街道多福巷社区居委会, 40.16, 15, 7.0, 严重, 多福巷社区居委会,CHN0102000055002021042110155734, 1.png;2.png
```



#### 人员伤亡
```json
{
"disasters": [
        {
            "TypeCode": 11,
            "Category": "人员伤亡",
            "Date": "2021-04-21 10:15:57",
            "Location": "北京市东城区东华门街道多福巷社区居委会",
            "DeathNumber": 0,
            "InjuredNumber": 150,
            "MissingNumber": 0,
            "ReportingUnit": "多福巷社区居委会",
            "EarthquakeEncode":"CHN0102000055002021042110155734",
            "Images": [
                "1.png",
                "2.png"
            ]
        }
    ]
}

```


或者选择如下格式的CSV文件
```text
TypeCode, Category, Date, Location, DeathNumber, InjuredNumber, MissingNumber, ReportingUnit, EarthquakeEncode, Images

11, 人员伤亡, 2021-04-21 10:15:57, 北京市东城区东华门街道多福巷社区居委会, 0, 150, 0, 多福巷社区居委会,CHN0102000055002021042110155734, 1.png;2.png
```


## 通过网站直接上传

提供了上传的快捷方式。不用登录FTP系统，用户可以通过网站直接上传文件，这些文件也会被放入FTP系统内的upload文件夹内以供扫描。