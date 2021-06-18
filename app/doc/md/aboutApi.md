

 
# 查询请求

统一使用 GET 谓词，并捎带限制参数的方式

## 多条地震元信息
### 基本地址

```http
GET /api/earchquaskes
```

### 限制参数

1. 可带 `offset` 和 `limit` 来截取特定偏移量和数量的Json数据。


2. 可带 `orderBy` 和 `order` 来获取按照指定字段顺序排序的Json。


3. 可带 `dateStart` 和 `dateEnd` 来指定时间段范围内的Json数据

# API接口
## 接口说明1
- 方法描述：单条震情数据查询
- URL地址：/api/earthquakes/<<int:id>>
- 请求方式：get
- 返回结果示例：

```json
{
    "Depth": 9.0,
    "Id": 1,
    "Latitude": 39.46, 
    "Level": 4.6, 
    "Location": "\u5409\u5c14\u5409\u65af\u65af\u5766", 
    "Longitude": 73.15
}
```

##接口说明2
- 方法描述：多条震情数据查询
- URL地址：/api/earthquakes/list
- 请求方式：get,patch
- 返回结果示例：

```json
{
  "limit": 0, 
  "rows": [
    {
      "Depth": 5.0, 
      "EarthquakeEncode": "0000394600731502021051417540446", 
      "Id": 1, 
      "Latitude": 39.46, 
      "Level": 4.5, 
      "Location": "\u5409\u5c14\u5409\u65af\u65af\u5766", 
      "Longitude": 73.15, 
      "OccurrenceTime": "2021-05-14 17:54:04"
    }, 
    {
      "Depth": 5.0, 
      "EarthquakeEncode": "CHN0325701052402021051401254929", 
      "Id": 2, 
      "Latitude": 32.57, 
      "Level": 2.9, 
      "Location": "\u56db\u5ddd\u5e7f\u5143\u5e02\u9752\u5ddd\u53bf", 
      "Longitude": 105.24, 
      "OccurrenceTime": "2021-05-14 01:25:49"
    }, 
    {
      "Depth": 420.0, 
      "EarthquakeEncode": "000-16050-1772502021051321313356", 
      "Id": 3, 
      "Latitude": -16.05, 
      "Level": 5.6, 
      "Location": "\u6590\u6d4e\u7fa4\u5c9b\u5730\u533a", 
      "Longitude": -177.25, 
      "OccurrenceTime": "2021-05-13 21:31:33"
    }, 
    {
      "Depth": 10.0, 
      "EarthquakeEncode": "000006800-823502021051317421157", 
      "Id": 4, 
      "Latitude": 6.8, 
      "Level": 5.7, 
      "Location": "\u5df4\u62ff\u9a6c\u4ee5\u5357\u6d77\u57df", 
      "Longitude": -82.35, 
      "OccurrenceTime": "2021-05-13 17:42:11"
    }, 
    {
      "Depth": 8.0, 
      "EarthquakeEncode": "CHN0244300992402021051311423647", 
      "Id": 5, 
      "Latitude": 24.43, 
      "Level": 4.7, 
      "Location": "\u4e91\u5357\u4fdd\u5c71\u5e02\u65bd\u7538\u53bf", 
      "Longitude": 99.24, 
      "OccurrenceTime": "2021-05-13 11:42:36"
    }, 
    {
      "Depth": 10.0, 
      "EarthquakeEncode": "CHN0371200850802021051222370641", 
      "Id": 6, 
      "Latitude": 37.12, 
      "Level": 4.1, 
      "Location": "\u65b0\u7586\u5df4\u97f3\u90ed\u695e\u5dde\u4e14\u672b\u53bf", 
      "Longitude": 85.08, 
      "OccurrenceTime": "2021-05-12 22:37:06"
    }
  ], 
  "total": 6
}
```

## 接口说明3
- 方法描述：单条灾情数据查询
- URL地址：/api/disaster/<<int:id>>
- 请求方式：get
- 返回结果示例：

```json
{
  "Id": 1, 
  "TypeCode": 1
}
```

##接口说明4
- 方法描述：多条灾情数据查询
- URL地址：/api/disaster/list
- 请求方式：get,patch
- 返回结果示例：

```json
{
  "limit": 0, 
  "rows": [
    {
      "Id": 1, 
      "TypeCode": 1
    }, 
    {
      "Id": 2, 
      "TypeCode": 1
    }, 
    {
      "Id": 3, 
      "TypeCode": 1
    }, 
    {
      "Id": 4, 
      "TypeCode": 1
    }, 
    {
      "Id": 5, 
      "TypeCode": 1
    }, 
    {
      "Id": 6, 
      "TypeCode": 1
    }
  ], 
  "total": 6
}
```

## 接口说明5
- 方法描述：单条房屋破坏数据查询
- URL地址：/api/houseDamaged/<<int:id>>
- 请求方式：get
- 返回结果示例：

```json
{
  "BasicallyIntactSquare": 61.0, 
  "Category": "\u697c\u623f\u635f\u574f", 
  "DamagedSquare": 57.0, 
  "Date": "2021-06-02 14:40:56", 
  "DestroyedSquare": 56.0, 
  "EarthquakeId": 1, 
  "Id": 1, 
  "Level": "4", 
  "Location": "\u5409\u5c14\u5409\u65af\u65af\u5766", 
  "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
}
```

##接口说明6
- 方法描述：多条房屋破坏数据查询
- URL地址：/api/houseDamaged/list
- 请求方式：get,patch
- 返回结果示例：

```json
{
  "limit": 0, 
  "rows": [
    {
      "BasicallyIntactSquare": 61.0, 
      "Category": "\u697c\u623f\u635f\u574f", 
      "DamagedSquare": 57.0, 
      "Date": "2021-06-02 14:40:56", 
      "DestroyedSquare": 56.0, 
      "EarthquakeId": 1, 
      "Id": 1, 
      "Level": "4", 
      "Location": "\u5409\u5c14\u5409\u65af\u65af\u5766", 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "BasicallyIntactSquare": 36.0, 
      "Category": "\u623f\u5c4b\u6bc1\u574f", 
      "DamagedSquare": 57.0, 
      "Date": "2021-06-02 14:42:33", 
      "DestroyedSquare": 5.0, 
      "EarthquakeId": 1, 
      "Id": 2, 
      "Level": "3", 
      "Location": "\u53f0\u6e7e\u82b1\u83b2\u53bf", 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "BasicallyIntactSquare": 45.0, 
      "Category": "\u697c\u623f\u635f\u574f", 
      "DamagedSquare": 57.0, 
      "Date": "2021-06-02 14:44:01", 
      "DestroyedSquare": 5.0, 
      "EarthquakeId": 1, 
      "Id": 3, 
      "Level": "3", 
      "Location": "\u53f0\u6e7e\u82b1\u83b2\u53bf", 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "BasicallyIntactSquare": 254.0, 
      "Category": "\u697c\u623f\u635f\u574f", 
      "DamagedSquare": 57.0, 
      "Date": "2021-06-02 14:47:24", 
      "DestroyedSquare": 55.0, 
      "EarthquakeId": 1, 
      "Id": 4, 
      "Level": "9", 
      "Location": "\u53f0\u6e7e\u82b1\u83b2\u53bf", 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "BasicallyIntactSquare": 245.0, 
      "Category": "\u697c\u623f\u635f\u574f", 
      "DamagedSquare": 57.0, 
      "Date": "2021-06-02 14:46:42", 
      "DestroyedSquare": 5.0, 
      "EarthquakeId": 1, 
      "Id": 5, 
      "Level": "3", 
      "Location": "\u53f0\u6e7e\u82b1\u83b2\u53bf", 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "BasicallyIntactSquare": 245.0, 
      "Category": "\u697c\u623f\u635f\u574f", 
      "DamagedSquare": 57.0, 
      "Date": "2021-06-02 14:40:23", 
      "DestroyedSquare": 5.0, 
      "EarthquakeId": 6, 
      "Id": 6, 
      "Level": "3", 
      "Location": "\u4e91\u5357\u5927\u7406\u5dde\u6d31\u6e90\u53bf", 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }
  ], 
  "total": 6
}
```

## 接口说明7
- 方法描述：单条人员伤亡数据查询
- URL地址：/api/InjuredStatistics/<<int:id>>
- 请求方式：get
- 返回结果示例：

```json
{
  "Date": "2021-06-10 20:40:48", 
  "DeathNumber": 45, 
  "EarthquakeId": 2, 
  "Id": 1, 
  "InjuredNumber": 68, 
  "Location": "\u65b0\u7586\u4f0a\u7281\u5dde\u5bdf\u5e03\u67e5\u5c14\u53bf", 
  "MissingNumber": 9, 
  "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
}
```

##接口说明8
- 方法描述：多条人员伤亡数据查询
- URL地址：/api/InjuredStatistics/list
- 请求方式：get,patch
- 返回结果示例：

```json
{
  "limit": 0, 
  "rows": [
    {
      "Date": "2021-06-10 20:40:48", 
      "DeathNumber": 45, 
      "EarthquakeId": 2, 
      "Id": 1, 
      "InjuredNumber": 68, 
      "Location": "\u65b0\u7586\u4f0a\u7281\u5dde\u5bdf\u5e03\u67e5\u5c14\u53bf", 
      "MissingNumber": 9, 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "Date": "2021-06-10 20:40:48", 
      "DeathNumber": 12, 
      "EarthquakeId": 2, 
      "Id": 2, 
      "InjuredNumber": 68, 
      "Location": "\u65b0\u7586\u4f0a\u7281\u5dde\u5bdf\u5e03\u67e5\u5c14\u53bf", 
      "MissingNumber": 9, 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "Date": "2021-06-10 20:40:48", 
      "DeathNumber": 10, 
      "EarthquakeId": 2, 
      "Id": 3, 
      "InjuredNumber": 68, 
      "Location": "\u65b0\u7586\u4f0a\u7281\u5dde\u5bdf\u5e03\u67e5\u5c14\u53bf", 
      "MissingNumber": 9, 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "Date": "2021-06-10 20:40:48", 
      "DeathNumber": 41, 
      "EarthquakeId": 2, 
      "Id": 4, 
      "InjuredNumber": 68, 
      "Location": "\u65b0\u7586\u4f0a\u7281\u5dde\u5bdf\u5e03\u67e5\u5c14\u53bf", 
      "MissingNumber": 9, 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "Date": "2021-06-10 20:40:48", 
      "DeathNumber": 32, 
      "EarthquakeId": 4, 
      "Id": 5, 
      "InjuredNumber": 68, 
      "Location": "\u65b0\u7586\u4f0a\u7281\u5dde\u5bdf\u5e03\u67e5\u5c14\u53bf", 
      "MissingNumber": 9, 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }, 
    {
      "Date": "2021-06-10 20:40:48", 
      "DeathNumber": 12, 
      "EarthquakeId": 2, 
      "Id": 6, 
      "InjuredNumber": 68, 
      "Location": "\u65b0\u7586\u4f0a\u7281\u5dde\u5bdf\u5e03\u67e5\u5c14\u53bf", 
      "MissingNumber": 9, 
      "ReportingUnit": "\u56fd\u5bb6\u5730\u9707\u5c40"
    }
  ], 
  "total": 6
}
```
