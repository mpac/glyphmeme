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


from django.contrib.auth.models import User
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
		name = models.CharField(max_length=100, unique=True, null=False, blank=False)
		parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
		
		created = models.DateTimeField(auto_now_add=True)
		modified = models.DateTimeField(auto_now=True)
		
		creator = models.ForeignKey(User, null=True, editable=False, related_name="+")
		modifier = models.ForeignKey(User, null=True, editable=False, related_name="+")
		
		class Meta:
				verbose_name_plural = 'Categories'

		class MPTTMeta:
				level_attr = 'mptt_level'
				order_insertion_by=['name']

		def __unicode__(self):
				return self.name


class BaseModel(models.Model):
	class Meta:
		abstract = True

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	creator = models.ForeignKey(User, null=True, editable=False, related_name='+')
	modifier = models.ForeignKey(User, null=True, editable=False, related_name='+')


class Language(BaseModel):
	name = models.CharField(max_length=100, null=False, blank=False)
	region = models.CharField(max_length=100, null=False, blank=True)
	
	default = models.BooleanField(null=False, default=False)
	
	def __unicode__(self):
		return "%s (%s)" % (self.name, self.region)


# Codes can be used to combine regions, such as en-us and en-gb

class Code(BaseModel):
	name = models.CharField(max_length=10, null=False, blank=False)
	primary = models.BooleanField(null=False, default=False)
	
	language = models.ForeignKey(Language)

	def __unicode__(self):
			return self.name


class Word(BaseModel):
	name = models.CharField(max_length=100, unique=True, null=False, blank=False)
	
	categories = TreeManyToManyField(Category)
	approved = models.BooleanField(null=False, default=False)

	def __unicode__(self):
		return self.name
	

class Translation(BaseModel):
	word = models.ForeignKey(Word)
	language = models.ForeignKey(Language)

	spelling = models.CharField(max_length = 100, null=False, blank=False)

	position = models.IntegerField(null=False, default=0)
	primary = models.BooleanField(null=False, default=False)
	approved = models.BooleanField(null=False, default=False)

	def __unicode__(self):
		return self.spelling
