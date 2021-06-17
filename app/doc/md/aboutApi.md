

 
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

