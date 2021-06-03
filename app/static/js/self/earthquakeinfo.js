const path = window.location.pathname; // =/earthquakes/1

const id = path.split('/')[2];
//TODO(qizozp) pick method, get data
var map = new AMap.Map('map', {
    zoom: 11,//级别
    center: [116.397428, 39.90923],//中心点坐标
    viewMode: '3D'//使用3D视图
});