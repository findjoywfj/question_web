# -*- coding: utf-8 -*-
def mysetting(request):
    return {

        'STATIC_URL': "/static/",                    # 本地静态文件访问
        'APP_CODE': "question_web",                        # 在蓝鲸系统中注册的  "应用编码"
        'SITE_URL': "/",                        # URL前缀
        'STATIC_VERSION': "2.0",            # 静态资源版本号,用于指示浏览器更新缓存

    }