from django.urls import re_path

from dojo.product import views

urlpatterns = [
    #  product
    re_path(r'^product$', views.product, name='product'),
    re_path(r'^product/(?P<pid>\d+)$', views.view_product,
        name='view_product'),
    re_path(r'^product/(?P<pid>\d+)/components$', views.view_product_components,
        name='view_product_components'),
    re_path(r'^product/(?P<pid>\d+)/engagements$', views.view_engagements,
        name='view_engagements'),
    re_path(r'^product/(?P<pid>\d+)/import_scan_results$',
        views.import_scan_results_prod, name='import_scan_results_prod'),
    re_path(r'^product/(?P<pid>\d+)/metrics$', views.view_product_metrics,
        name='view_product_metrics'),
    re_path(r'^product/(?P<pid>\d+)/async_burndown_metrics$', views.async_burndown_metrics,
        name='async_burndown_metrics'),
    re_path(r'^product/(?P<pid>\d+)/edit$', views.edit_product,
        name='edit_product'),
    re_path(r'^product/(?P<pid>\d+)/delete$', views.delete_product,
        name='delete_product'),
    re_path(r'^product/add', views.new_product, name='new_product'),
    re_path(r'^product/(?P<pid>\d+)/new_engagement$', views.new_eng_for_app,
        name='new_eng_for_prod'),
    re_path(r'^product/(?P<pid>\d+)/new_technology$', views.new_tech_for_prod,
         name='new_tech_for_prod'),
    re_path(r'^technology/(?P<tid>\d+)/edit$', views.edit_technology,
        name='edit_technology'),
    re_path(r'^technology/(?P<tid>\d+)/delete$', views.delete_technology,
        name='delete_technology'),
    re_path(r'^product/(?P<pid>\d+)/new_engagement/cicd$', views.new_eng_for_app_cicd,
        name='new_eng_for_prod_cicd'),
    re_path(r'^product/(?P<pid>\d+)/add_meta_data$', views.add_meta_data,
        name='add_meta_data'),
    re_path(r'^product/(?P<pid>\d+)/edit_notifications$', views.edit_notifications,
        name='edit_notifications'),
    re_path(r'^product/(?P<pid>\d+)/edit_meta_data$', views.edit_meta_data,
        name='edit_meta_data'),
    re_path(r'^product/(?P<pid>\d+)/ad_hoc_finding$', views.ad_hoc_finding,
        name='ad_hoc_finding'),
    re_path(r'^product/(?P<pid>\d+)/engagement_presets$', views.engagement_presets,
        name='engagement_presets'),
    re_path(r'^product/(?P<pid>\d+)/engagement_presets/(?P<eid>\d+)/edit$', views.edit_engagement_presets,
        name='edit_engagement_presets'),
    re_path(r'^product/(?P<pid>\d+)/engagement_presets/add$', views.add_engagement_presets,
        name='add_engagement_presets'),
    re_path(r'^product/(?P<pid>\d+)/engagement_presets/(?P<eid>\d+)/delete$', views.delete_engagement_presets,
        name='delete_engagement_presets'),
    re_path(r'^product/(?P<pid>\d+)/add_member$', views.add_product_member,
        name='add_product_member'),
    re_path(r'^product/member/(?P<memberid>\d+)/edit$', views.edit_product_member,
        name='edit_product_member'),
    re_path(r'^product/member/(?P<memberid>\d+)/delete$', views.delete_product_member,
        name='delete_product_member'),
    re_path(r'^product/(?P<pid>\d+)/add_api_scan_configuration$', views.add_api_scan_configuration,
        name='add_api_scan_configuration'),
    re_path(r'^product/(?P<pid>\d+)/view_api_scan_configurations$', views.view_api_scan_configurations,
        name='view_api_scan_configurations'),
    re_path(r'^product/(?P<pid>\d+)/edit_api_scan_configuration/(?P<pascid>\d+)$', views.edit_api_scan_configuration,
        name='edit_api_scan_configuration'),
    re_path(r'^product/(?P<pid>\d+)/delete_api_scan_configuration/(?P<pascid>\d+)$', views.delete_api_scan_configuration,
        name='delete_api_scan_configuration'),
    re_path(r'^product/(?P<pid>\d+)/add_group$', views.add_product_group,
        name='add_product_group'),
    re_path(r'^product/group/(?P<groupid>\d+)/edit$', views.edit_product_group,
        name='edit_product_group'),
    re_path(r'^product/group/(?P<groupid>\d+)/delete$', views.delete_product_group,
        name='delete_product_group'),
]