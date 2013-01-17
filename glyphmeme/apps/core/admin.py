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


from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from core.models import Category, Language, Code, Word, Translation

class CodeInline(admin.TabularInline):
	model = Code

class TranslationInline(admin.TabularInline):
	model = Translation

class LanguageAdmin(admin.ModelAdmin):
	inlines = [CodeInline]
	
class WordAdmin(admin.ModelAdmin):
	inlines = [TranslationInline]

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Word, WordAdmin)
