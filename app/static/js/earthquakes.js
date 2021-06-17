const baseUrl = "http://127.0.0.1:5123/"

// 生成表格
$('#earthquakesTable').bootstrapTable({
    url: baseUrl + 'api/earthquakes/', //请求后台的URL（*）
    method: 'get', //请求方式（*）
    // toolbar: '#toolbar',
    // data:baseUrl+"query",
    // showFullscreen: true,
    // striped: true, //是否显示行间隔色
    pagination: true, //是否显示分页（*）

    search: true, //开启搜索文本框
    // searchText:"流浪地球",
    // searchOnEnterKey:true, //回车后执行搜索
    // strictSearch: true, //完全匹配
    // trimOnSearch: true, // 去除关键词空格
    // searchAlign: "left", // 搜索框位置
    // customSearch: function customSearch(data, text) { //自定义搜索，比如只搜索ID字段
    //     return data.filter(function(row) {
    //         return (row.Id + "").indexOf(text) > -1
    //     })
    // },


    // height:"",
    paginationLoop:false, 				//设置为 true 启用分页条无限循环的功能。
    sidePagination: "server", //分页方式：client客户端分页，server服务端分页（*）
    // pageNumber:1,                       //初始化加载第一页，默认第一页
    // pageSize: 10,                       //每页的记录行数（*）
    pageList: [10, 15, 20], //可供选择的每页的行数（*）
    // sortable: false,                     //是否启用排序
    showRefresh: true, //是否显示刷新按钮
    // showToggle:true,                    //是否显示详细视图和列表视图的切换按钮
    showColumns: true,
    cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
    // clickToSelect: true,                //是否启用点击选中行
    // rowStyle: function (row, index) {
    //     //这里有5个取值代表5中颜色['active', 'success', 'info', 'warning', 'danger'];
    //     var strclass = "";
    //     if (row.taskState == "完成") {
    //         strclass = 'active';
    //     }
    //     // else if (row.taskState == "完成") {
    //     // 	strclass = 'success';
    //     // }
    //     else if (row.taskState == "错误") {
    //     	strclass = 'danger';
    //     }
    //     else {
    //         return {};
    //     }
    //     // console.log(strclass);
    //     return { classes: strclass };
    // },
    columns: [{
        checkbox: true,
        align: "center",
    },
    {
        field: 'Id',
        title: '序号(I)'
    },
    {
        field: 'Level',
        title: '震级(M)'
    },
    {
        field: 'OccurrenceTime',
        title: '发震时刻(UTC+8)'
    },
    {
        field: 'Longitude',
        title: '经度(°)'
    },
    {
        field: 'Latitude',
        title: '纬度(°)'
    },
    {
        field: 'Depth',
        title: '深度(km)',
        // formatter: function (value, row, index) {

        //     return value + " 小时"
        // }
    },

    {
        field: 'Location',
        title: '参考位置',
        // align: "center",
        // formatter: function (value, row, index) {
        //     var state = new Map([
        //         ["运行", "info"],
        //         ["完成", "success"],
        //         ["挂起", "warning"],
        //         ["错误", "danger"],
        //         ["终止", "default"]
        //     ]);
        //     var result = '<span class="label label-' + state.get(value) + '">' + value + '</span>'
        //     return result
        // }
    }, {
        title: '操作',
        align: "center",
        // formatter: function (value, row, index) {
        //     switch (row.taskState) {
        //         case "运行":
        //             return '<button id="btn_edit" type="button" class="btn btn-sm" onclick="editTask(' + index + ')"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> 修改</button>&nbsp;'+
        //                     '<button id="btn_delete" type="button" class="btn btn-sm" onclick="deleteOneTask(' + index + ')"><span class="glyphicon glyphicon-ban-circle" aria-hidden="true"></span> 终止</button>'

        //         case "挂起":
        //             return '<button id="btn_edit" type="button" class="btn btn-sm" onclick="editTask(' + index +')"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> 修改</button>&nbsp;'+
        //                     '<button id="btn_delete" type="button" class="btn btn-sm" onclick="deleteOneTask(' + index + ')"><span class="glyphicon glyphicon-ban-circle" aria-hidden="true"></span> 终止</button>'
        //         case "错误":
        //             return '<button id="btn_edit" type="button" class="btn btn-sm" onclick="editTask(' + index + ')"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> 修改</button>&nbsp;'+
        //                     '<button id="btn_delete" type="button" class="btn btn-sm" onclick="deleteOneTask(' + index + ')"><span class="glyphicon glyphicon-ban-circle" aria-hidden="true"></span> 终止</button>'
        //         case "完成":
        //         case "终止":
        //         default:
        //             return "-"
        //     }
        // }
    }
    ],
    // onLoadError: function() {
    //     showTips("数据加载失败！");
    // },
    onDblClickRow: function (row, $element) {
        // $("#taskNameForCheck").val(row.taskName)
        // $("#taskDetails_").click()
        window.location.href=baseUrl+"earthquakes/"+row.Id
    },
    //得到查询的参数
    queryParams: function (params) {
        //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
        var temp = {
            limit: params.limit, //页面大小
            offset: params.offset, //页码
            order: params.order, //排序列名
        };
        return temp;
    },
});