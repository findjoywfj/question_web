
config = {
    init: function () {
        $('#title').text('测试记录')
        dataurl = '/developer/api/record/get/';
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
                colNames: ['用户','题库名称','题库id', '测试得分', '测试结果','测试时间','详情'],
                colModel: [
                    { name: 'user', index: 'user', editable: false , search: true},
                    { name: 'questions_name', index: 'questions_name', editable: false, width: 60, search: true , searchoptions:{sopt:['eq','ne']},},
                    { name: 'questions_id', index : 'questions_id', editable: false, search:false},
                    { name: 'score', index: 'score', editable: false, width: 100, search:false,},
                    { name: 'content', index: 'content', editable: false,width:100, search:false,},
                    { name: 'found_time', index: 'found_time', editable: false, width: 100,},
                    {
                        name: 'id', index: 'id', editable: false, width: 90, search: false,
                        formatter: function (cellvalue, options, rowObject) {

                            return "<a class='btn btn-default btn-xs' href='/customer/qes_body/"+ rowObject.id + "/developer/' ><i class='fa fa-info'></i> 详情</a> ";

                        }
                    },
                ],
                pager: "#pager_list_2",
                viewrecords: true,//是否要显示总记录数
                hidegrid: true,
                cellEdit: false,//启用或者禁用单元格编辑功能
                cellurl:editurl,
                editurl: editurl,//设置编辑使提交的url
                cellsubmit: 'remote',//定义了单元格内容保存位置

            });
            // Setup buttons
             // Setup buttons
            $("#table_list_2").jqGrid('navGrid', '#pager_list_2',
                {   search: true,
                    refreshtext:"刷新"},

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