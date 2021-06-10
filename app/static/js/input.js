$(function () {
    //0.初始化fileinput
    var oFileInput = new FileInput();
    oFileInput.Init("txt_file", "/upload");
});

//初始化fileinput
var FileInput = function () {
    var oFile = new Object();

    //初始化fileinput控件（第一次初始化）
    oFile.Init = function (ctrlName, uploadUrl) {
        var control = $('#' + ctrlName);

        //初始化上传控件的样式
        control.fileinput({
            language: 'zh', //设置语言
            uploadUrl: uploadUrl, //上传的地址
            allowedFileExtensions: ['csv', 'json', 'png','jpg','jpeg'],//接收的文件后缀
            showUpload: true, //是否显示上传按钮
            showCaption: false,//是否显示标题
            uploadAsync:false, 
            browseClass: "btn btn-primary", //按钮样式     
            maxFileCount: 15, //表示允许同时上传的最大文件个数
            enctype: 'multipart/form-data',
            validateInitialCount: true,
            previewFileIcon: "<i class='glyphicon glyphicon-king'></i>",
            msgFilesTooMany: "选择上传的文件数量({n}) 超过允许的最大数值{m}！",
        });

        //导入文件上传完成之后的事件
        $("#txt_file").on("fileuploaded", function (event, data, previewId, index) {
            $("#uploadModal").modal("hide");
            console.log("ss")
            // var ret = data.response.lstOrderImport;
            // if(ret==""){
            //     toastr.error('文件格式类型不正确');
            //     return;
            // }
            // else if (ret == undefined) {
            //     toastr.error('文件格式类型不正确');
            //     return;
            // }
            //1.初始化表格
            // var oTable = new TableInit();
            // oTable.Init(data);
            // $("#div_startimport").show();
        });

        $('#txt_file').on('fileerror', function(event, data, msg) {
            console.log("error")
        });
    }
    return oFile;
};


function Upload(){
    $('#uploadModal').modal('show')
}