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


import random

from core.models import Language, Code, Category, Word, Translation

from django.core import serializers
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def get_language(request):
	
	return Language.objects.get(pk=1)	


def index(request):
	
	return render_to_response(
		'core/index.html',
		{},
		context_instance=RequestContext(request)
	)


def ajax_random_word(request):
	
	language = get_language(request)
	
	count = Word.objects.all().count()
	random_index = random.randint(0, count - 1)
	
	word = Word.objects.all()[random_index]
	translation = Translation.objects.filter(word=word)
	
	language_json = serializers.serialize(
		'json',
		[language],
		indent=4,
	)
	
	codes_json = serializers.serialize(
		'json',
		Code.objects.filter(language=language),
		indent=4,
	)
	
	word_json = serializers.serialize(
		'json',
		[word],
		indent=4,
		relations=('categories',)
	)
		
	translations_json = serializers.serialize(
		'json',
		Translation.objects.filter(word=word),
		indent=4,
		relations=('word', 'language')
	)	
	
	json = '[{"language": %s, "codes": %s, "word": %s, "translations": %s}]' % (
		language_json, codes_json, word_json, translations_json
	)
	
	return HttpResponse(json, mimetype='application/json')
