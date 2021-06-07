function addMarker(point, index){  // 创建图标对象   
    var myIcon = new BMapGL.Icon("markers.png", new BMapGL.Size(23, 25), {    
        // 指定定位位置。   
        // 当标注显示在地图上时，其所指向的地理位置距离图标左上    
        // 角各偏移10像素和25像素。您可以看到在本例中该位置即是   
        // 图标中央下端的尖角位置。    
        anchor: new BMapGL.Size(10, 25),    
        // 设置图片偏移。   
        // 当您需要从一幅较大的图片中截取某部分作为标注图标时，您   
        // 需要指定大图的偏移位置，此做法与css sprites技术类似。    
        imageOffset: new BMapGL.Size(0, 0 - index * 25)   // 设置图片偏移    
    });      
    // 创建标注对象并添加到地图   
    var marker = new BMapGL.Marker(point, {icon: myIcon});    
    map.addOverlay(marker);    
}   
marker.addEventListener("click", function(){    
    alert("您点击了标注");    
});  