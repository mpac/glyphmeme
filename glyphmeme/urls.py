# Copyright 2013, Michael Pacchioli.
#  
# This file is part of GlyphMeme.
# 
# GlyphMeme is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 3,
# as published by the Free Software Foundation.
# 
# GlyphMeme is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GlyphMeme.  If not, see <http://www.gnu.org/licenses/>.


from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
 
	(r'^$', 'core.views.index'),   
	(r'^ajax/random-word/$', 'core.views.ajax_random_word'),	
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(
			r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}
		),
	)

