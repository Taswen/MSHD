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
- 方法描述：单条数据查询
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
- 方法描述：多条数据查询
- URL地址：/api/earthquakes/list
- 请求方式：get
- 返回结果示例：

```json
{
    "limit": 0, 
    "rows": [
    {
      "Depth": 9.0, 
      "EarthquakeEncode": "0000394600731502021051417540446", 
      "Id": 1, 
      "Latitude": 39.46, 
      "Level": 4.6, 
      "Location": "\u5409\u5c14\u5409\u65af\u65af\u5766", 
      "Longitude": 73.15
    }, 
    {
      "Depth": 9.0, 
      "EarthquakeEncode": "CHN0325701052402021051401254929", 
      "Id": 2, 
      "Latitude": 32.57, 
      "Level": 2.9, 
      "Location": "\u56db\u5ddd\u5e7f\u5143\u5e02\u9752\u5ddd\u53bf", 
      "Longitude": 105.24
    }, 
    {
      "Depth": 420.0, 
      "EarthquakeEncode": "000-16050-1772502021051321313356", 
      "Id": 3, 
      "Latitude": -16.05, 
      "Level": 5.6, 
      "Location": "\u6590\u6d4e\u7fa4\u5c9b\u5730\u533a", 
      "Longitude": -177.25
    }, 
    {
      "Depth": 10.0, 
      "EarthquakeEncode": "000006800-823502021051317421157", 
      "Id": 4, 
      "Latitude": 6.8, 
      "Level": 5.7, 
      "Location": "\u5df4\u62ff\u9a6c\u4ee5\u5357\u6d77\u57df", 
      "Longitude": -82.35
    }, 
    {
      "Depth": 8.0, 
      "EarthquakeEncode": "CHN0244300992402021051311423647", 
      "Id": 5, 
      "Latitude": 24.43, 
      "Level": 4.7, 
      "Location": "\u4e91\u5357\u4fdd\u5c71\u5e02\u65bd\u7538\u53bf", 
      "Longitude": 99.24
    }, 
    {
      "Depth": 10.0, 
      "EarthquakeEncode": "CHN0371200850802021051222370641", 
      "Id": 6, 
      "Latitude": 37.12, 
      "Level": 4.1, 
      "Location": "\u65b0\u7586\u5df4\u97f3\u90ed\u695e\u5dde\u4e14\u672b\u53bf", 
      "Longitude": 85.08
    }, 
    ],
    "total":6
}
```
