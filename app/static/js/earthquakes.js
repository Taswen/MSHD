const baseUrl = "http://127.0.0.1:5123/"

// 生成表格
$('#earthquakesTable').bootstrapTable({
    url: baseUrl + 'api/earthquakes/list', //请求后台的URL（*）
    method: 'get', //请求方式（*）
    toolbar: '#toolbar',
    pagination: true, //是否显示分页（*）
    sortable: true,
    sortName: 'Id',
    sortOrder: 'asc',


    paginationLoop: false, 				//设置为 true 启用分页条无限循环的功能。
    sidePagination: "server", //分页方式：client客户端分页，server服务端分页（*）
    pageList: [10, 15, 20], //可供选择的每页的行数（*）
    showRefresh: true, //是否显示刷新按钮
    showToggle: true,                    //是否显示详细视图和列表视图的切换按钮
    showColumns: true,
    cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
    columns: [
        {
            field: 'Id',
            title: '序号(I)',
            sortable: true
        },
        {
            field: 'Level',
            title: '震级(M)',
            sortable: true,
            formatter: function (value, row, index, field) {
                let des = ""
                if (value < 1) {
                    des = ' <sup style="color:#f3f1fe">超微震</sup>'
                } else if (value < 3) {
                    des = ' <sup style="color:#b2eaed">弱震</sup>'
                } else if (value < 4.5) {
                    des = ' <sup style="color:#0142fc">有感地震</sup>'
                } else if (value < 6) {
                    des = ' <sup style="color:#fce794">中强震</sup>'
                } else if (value < 7) {
                    des = ' <sup style="color:#fee600">强震</sup>'
                } else if (value < 8) {
                    des = ' <sup style="color:#fd2901">大地震</sup>'
                } else {
                    des = ' <sup style="color:#b9006d">巨大地震</sup>'
                }
                return value + des
            }
        },
        {
            field: 'OccurrenceTime',
            title: '发震时刻(UTC+8)',
            sortable: true
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
            sortable: true
        },

        {
            field: 'Location',
            title: '参考位置',
        }, {
            title: '操作',
            align: "center",
            formatter: function (value, row, index) {
                return '<div><button type="button" class="btn btn-sm btn-outline-warning" onclick="editEq(' + row.Id + ')">修改</button>&nbsp;&nbsp;' +
                    '<button type="button" class="btn btn-sm btn-outline-danger" onclick="deleteEq(' + row.Id + ')">删除</button></div>'
            }
        }
    ],
    onLoadError: function () {
        showTips("数据加载失败！");
    },
    onDblClickRow: function (row, $element) {
        window.location.href = baseUrl + "earthquakes/" + row.Id
    },
    //得到查询的参数
    queryParams: function (params) {
        //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
        var temp = {
            "limit": params.limit, //页面大小
            "offset": params.offset, //页码
            "orderBy": params.sort,
            "order": params.order, //排序列名

        };
        return temp;
    },
    locale: "zh-CN",
    responseHandler: function (res, jqXHRs) {
        $('#count').html(res["total"])
        return res
    }
});

// 删除数据
function deleteEq(id) {
    $('#delModal #delContext').val(id)
    $('#delModal').modal('show');
}

function submitDel() {
    var id = $('#delModal #delContext').val();
    $.ajax({
        url: baseUrl + "api/earthquakes/" + id,
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


// 编辑地震信息
function editEq(index) {
    var jobj = $('#earthquakesTable').bootstrapTable('getData')[index-1];
    if (jobj == undefined) {
        alert("错误！数据不存在！")
        return false;
    } else {
        // 不可更改
        $('#eqId').val(jobj.Id).prop('disabled', true);
        $('#eqLevel').val(jobj.Level);
        $('#eqTime').val(jobj.OccurrenceTime)
        $('#eqLongitude').val(jobj.Longitude)
        $('#eqLatitude').val(jobj.Latitude)
        $('#eqDepth').val(jobj.Depth)
        $('#eqLocation').val(jobj.Location)
        // $('#taskName').val(jobj.taskName).prop('disabled', true);
        // // 隐藏
        // $('#taskState').hide();
        // // 可更改
        // $('#taskInterval').val(jobj.taskInterval);
        // endpicker.data('DateTimePicker').minDate(new Date());


        // $('#editId').val(jobj.id);
        // $('#flag').val("edit");

        $('#editModalLabel').html("编辑震情数据");
        $('#editModal').modal('show');
    }

}


function submitEdit() {
    // 检查名字
    var eqId = $('#eqId').val();
    var eqLevel = $('#eqLevel').val();
    var eqTime = $('#eqTime').val();
    var eqLongitude = $('#eqLongitude').val();
    var eqLatitude = $('#eqLatitude').val();
    var eqDepth = $('#eqDepth').val();
    var eqLocation = $('#eqLocation').val();

    
    $.ajax({
        headers : { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }, 
        url: baseUrl + "api/earthquakes/" + eqId,
        type: "PATCH",
        data: JSON.stringify({"Level":eqLevel,"Time":eqTime,"Longitude":eqLongitude,"Latitude":eqLatitude,"Depth":eqDepth,"Location":eqLocation}),
        dataType: "json",

        success: function (response, status, xhr) {
            console.log("hello");
            $('#editModal').modal('hide');
            $('#earthquakesTable').bootstrapTable('refresh'); //刷新  
        },
        error: function (j, q, x) {
            console.log("hello");
            $('#editModal').modal('hide');
            $('#earthquakesTable').bootstrapTable('refresh'); //刷新  
        }
        // readyState: {
        //     {

        //     }
        // }
    });

    // if (eqId == "") {
    //     alert("任务名称不能为空！");
    //     return;
    // }
    // if (movieName == "") {
    //     alert("电影名称不能为空！");
    //     return;
    // }
    // // 检查间隔
    // var taskInterval = $('#taskInterval').val();
    // if (taskInterval == "") {
    //     alert("任务时间间隔不能为空！");
    //     // taskInterval = "48"
    //     return;
    // }
    // // 开始时间
    // var taskStartTime = $('#taskStartTime').val();
    // // 结束时间
    // var taskEndTime = $('#taskEndTime').val();

    // var flag = $('#flag').val();
    // var urlFor = ""
    // var param = "?"
    // // 修改
    // if (flag == "edit") {
    //     urlFor = "editTask"
    //     param += "taskName=" + taskName + "&"
    //     if (taskEndTime != "") {
    //         param += "endTime=" + encodeURIComponent(taskEndTime) + "&"
    //     }
    //     if (taskInterval != "") {
    //         param += "interval=" + encodeURIComponent(taskInterval)
    //     }
    // }
    // // 新建
    // else if (flag == "add") {
    //     urlFor = "addTask"
    //     param += "movieName=" + movieName + "&"
    //     param += "startTime=" + encodeURIComponent(taskStartTime) + "&"
    //     param += "endTime=" + encodeURIComponent(taskEndTime) + "&"
    //     param += "interval=" + encodeURIComponent(taskInterval)
    // }
    // // var corpId = $('#editCorpId').val();
    // $.ajax({
    //     url: baseUrl + urlFor + param,
    //     type: "get",
    //     success: function (result) {
    //         $('#editModal').modal('hide');
    //         // window.location.reload();
    //     }
    // });
}

// 初始化时间选择器
var picker1 = $('#eqTimePicker').datetimepicker({

    format: 'YYYY-MM-DD HH:mm:ss',
    locale: moment.locale('zh-cn')
});

$.extend(true, $.fn.datetimepicker.defaults, {
    icons: {
        time: 'far fa-clock',
        date: 'far fa-calendar',
        up: 'fas fa-arrow-up',
        down: 'fas fa-arrow-down',
        previous: 'fas fa-chevron-left',
        next: 'fas fa-chevron-right',
        today: 'fas fa-calendar-check',
        clear: 'far fa-trash-alt',
        close: 'far fa-times-circle'
    }
});


function onblurEqIdEvent(){}
function onblurEqLevelEvent(){}