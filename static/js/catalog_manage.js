
config = {
    init: function () {
        $('#title').text('题目管理表')
        dataurl = 'api/catalog/get/';
        editurl = 'api/catalog/action/';
        function showgrid(data) {
            $("#table_list_2").jqGrid({
                data: data,
                datatype: "local",
                height: 450,
                autowidth: true,
                shrinkToFit: true,
                rowNum: 20,
                rowList: [10, 20, 30],
                colNames: ['编号', '名称', '数量','预览', '编辑'],
                colModel: [
                    { name: 'id', index: 'id', editable: false, width: 60, search: true , searchoptions:{sopt:['eq','ne']},},
                    { name: 'title', index: 'title', editable: true, width: 100, search:true, searchoptions:{sopt:['eq','ne']}},
                    { name: 'count', index: 'count', editable: false,width:100, search:true, searchoptions:{sopt:['eq','ne','lt','le','gt','ge']},},
                    {
                        name: 'id', index: 'id', editable: false, width: 90, search: false,
                        formatter: function (cellvalue, options, rowObject) {

                            return "<a class='btn btn-default btn-xs' href='/customer/qes_body/" + rowObject.id + "' ><i class='fa fa-info'></i> 预览</a> ";

                        }
                    },
                    {
                        name: 'id', index: 'id', editable: false, width: 90,search: false,
                        formatter: function (cellvalue, options, rowObject) {

                            return "<a class='btn btn-default btn-xs' href='admin/qes_body/action/" + rowObject.id + "' ><i class='fa fa-eye'></i> 编辑</a>";

                        },
                    },

                ],
                pager: "#pager_list_2",
                viewrecords: true,//是否要显示总记录数
                hidegrid: true,
                cellEdit: true,//启用或者禁用单元格编辑功能
                cellurl:editurl,
                editurl: editurl,//设置编辑使提交的url
                cellsubmit: 'remote',//定义了单元格内容保存位置

            });
            // Setup buttons
             // Setup buttons
            $("#table_list_2").jqGrid('navGrid', '#pager_list_2',
                { edit:true, add: true, del: true, search: true,
                    searchtext: "查找", addtext: "添加", edittext: "编辑", deltext: "删除",
                    refreshtext:"刷新"},
                {closeAfterEdit:true,
                 afterSubmit: function (response) {
                     var res=JSON.parse(response.responseText)
                     if(res.result){
                         alert(res.message)
                         location.reload()
                     }

                 }
                },
                {closeAfteradd: true,
                 afterSubmit: function (response) {
                     var res=JSON.parse(response.responseText)
                     if(res.result){
                         alert(res.message)
                         location.reload()
                     }
                 }},
                {
                 afterSubmit: function (response) {
                    var res=JSON.parse(response.responseText)
                         if(res.result){
                             alert(res.message)
                             location.reload()
                         }
                    }
                },
                {closeAfterSearch:true}
            );

            // Add responsive to jqGrid
            $(window).bind('resize', function () {
                var width = $('.jqGrid_wrapper').width();
                //$('#table_list_1').setGridWidth(width);
                $('#table_list_2').setGridWidth(width);
            });

            setTimeout(function () {
                $('.wrapper-content').removeClass('animated fadeInRight');
            }, 700);
        }
        $.get(dataurl, function (doc) {
            var data = JSON.parse(doc)
            showgrid(data)
        })
    },

}