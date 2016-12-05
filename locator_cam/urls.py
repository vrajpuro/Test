
"""locator_cam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))



    url(r'^leave-channel/$', views.leave_channel, name='leave-channel')
    url(r'^locator_cam/', include('locator_cam.urls')),

"""


from django.conf.urls import patterns, include, url
import django.views.defaults
from . import views

urlpatterns = patterns('',
    url(r'^404/$', django.views.defaults.page_not_found),
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^search-user/$', views.search_user, name='search-user'),
	url(r'^add-friend/$', views.add_friend, name='add-friend'),
	url(r'^logout/$', views.logout_user, name='logout'),
	url(r'^unfriend/$', views.unfriend, name='unfriend'),
	url(r'^upload-moment/$', views.upload_moment, name='upload-moment'),
	url(r'^fetch-moments/$', views.fetch_moments, name='fetch-moments'),
	url(r'^delete-moment/$', views.delete_moment, name='delete-moment'),
	url(r'^fetch-photo/$', views.fetch_photo, name='fetch-photo'),
	url(r'^number-of-friends/$', views.number_of_friends, name='number-of-friends'),
	url(r'^get-all-friends/$', views.get_all_friends, name='get-all-friends'),
	url(r'^fetch-channels/$', views.fetch_channels, name='fetch-channels'),
	url(r'^fetch-channels-count/$', views.fetch_channels_count, name='fetch-channels-count'),
	url(r'^create-channel/$', views.create_channel, name='create-channel'),
	url(r'^add-member-to-channel/$', views.add_member_to_channel, name='add-member-to-channel'),
	url(r'^add-administrator-to-channel/$', views.add_administrator_to_channel, name='add-administrator-to-channel/'),
	url(r'^get-channel-members/$', views.get_channel_members, name='get-channel-members'),
	url(r'^get-channel-administrators/$', views.get_channel_administrators, name='get-channel-administrators'),
	url(r'^remove-member-from-channel/$', views.remove_member_from_channel, name='remove-member-from-channel'),
	url(r'^remove-administrator-from-channel/$', views.remove_administrator_from_channel, name='remove-administrator-from-channel'),
	url(r'^delete-channel/$', views.delete_channel, name='delete-channel'),
                       )


