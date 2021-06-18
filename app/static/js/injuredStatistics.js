const baseUrl = "http://127.0.0.1:5123/"

// 生成表格
$('#InjuredStatisticsTable').bootstrapTable({
    url: baseUrl + 'api/InjuredStatistics/list', //请求后台的URL（*）
    method: 'get', //请求方式（*）
    // toolbar: '#toolbar',
    buttons:function(){
        return {
            btnAdd: {
                text: 'Add new InjuredStatistics',
                icon: 'fa-plus',
                event: function () {
                  alert('Do some stuff to e.g. add a new row')
                },
                attributes: {
                  title: 'Add a new row to the table'
                }
              }
        }
    },
    // data:baseUrl+"query",
    // showFullscreen: true,
    pagination: true, //是否显示分页（*）
    sortable:true,
    sortName: 'Id',
    sortOrder: 'asc',
    // search: true, //开启搜索文本框
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
    columns: [
    {
        field: 'Id',
        title: '序号(I)',
        sortable : true 
    },
    {
        field: 'Date',
        title: '发震时刻(UTC+8)',
        sortable : true 
    },
    {
        field: 'Location',
        title: '参考位置',
    },
     {
        field: 'DeathNumber',
        title: '死亡人数',
    },{
        field: 'InjuredNumber',
        title: '受伤人数',
    }, {
        field: 'MissingNumber',
        title: '失踪人数',
    },
        {
        title: '操作',
        align: "center",
        formatter: function (value, row, index) {
            // switch (row.taskState) {
                return '<div><button type="button" class="btn btn-sm btn-outline-warning" onclick="editEq(' + row.Id + ')">修改</button>&nbsp;&nbsp;'+
                            '<button type="button" class="btn btn-sm btn-outline-danger" onclick="deleteEq(' + row.Id + ')">删除</button></div>'
            // }
        }
    }
    ],
    // onLoadError: function() {
    //     showTips("数据加载失败！");
    // },
    onDblClickRow: function (row, $element) {
        // $("#taskNameForCheck").val(row.taskName)
        // $("#taskDetails_").click()
        window.location.href=baseUrl+"injuredStatistics/"+row.Id
    },
    //得到查询的参数
    queryParams : function (params) {
        //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
        var temp = {
            "limit": params.limit, //页面大小
            "offset": params.offset, //页码
            "orderBy": params.sort,
            "order":params.order, //排序列名

        };
        return temp;
    },
    locale: "zh-CN",
    responseHandler: function (res,jqXHRs) {
        $('#count').html(res["total"])
        return res
    }
});

// 删除数据
function deleteEq(id){
    $('#delModal #delContext').val(id)
    $('#delModal').modal('show');
}

function submitDel() {
    var id = $('#delModal #delContext').val();
    $.ajax({
        url: baseUrl + "api/InjuredStatistics/"+id,
        type: "DELETE",
        success: function (data, textStatus) {
            $('#delModal').modal('hide');
            $('#earthquakesTable').bootstrapTable('refresh'); //刷新  
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            $('#delModal .modal-body').html("" + XMLHttpRequest.status + " " + errorThrown + "<hr/>发生错误, 是否重试")
        }
    });
}