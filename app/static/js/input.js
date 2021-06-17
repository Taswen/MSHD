$(document).ready(
    () => {
        console.log('jquery func')
        var oFileInput = new FileInput();
        oFileInput.Init("file_uploader", "/upload");
    })

//初始化fileinput
var FileInput = function () {
    const oFile = {};

    //初始化fileinput控件（第一次初始化）
    oFile.Init = function (ctrlName, uploadUrl) {
        var control = $('#' + ctrlName);

        //初始化上传控件的样式
        control.fileinput({
            language: 'zh', //设置语言
            uploadUrl: uploadUrl, //上传的地址
            dropZoneTitle: '可以将数据与图片拖至此处，支持多文件上传',
            allowedFileExtensions: ['csv', 'json', 'png', 'jpg', 'jpeg'],//接收的文件后缀
            showUpload: true, //是否显示上传按钮
            showCaption: false,//是否显示标题
            uploadAsync: false,
            // browseClass: "btn btn-primary", //按钮样式
            maxFileCount: 1, //表示允许同时上传的最大文件个数
            enctype: 'multipart/form-data',
            validateInitialCount: true,
            previewFileIcon: "<i class='fa fa-king'></i>",
            msgFilesTooMany: "选择上传的文件数量({n}) 超过允许的上传{m}个文件！",
        });

        //导入文件上传完成之后的事件
        $("#file_uploader").on("fileuploaded", function (event, data, previewId, index) {
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

        $('#file_uploader').on('fileerror', function (event, data, msg) {
            console.log("error")
        });
    }
    return oFile;
};


function Upload() {
    $('#uploadModal').modal('show')
}