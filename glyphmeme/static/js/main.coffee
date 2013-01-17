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


# "domain" variable from config.js or other file is needed

$ ->
	form1 = $ '#form1'
	button = $ '#button'
	guess = $ '#guess'

	translationsDIV = $ '#translations'	
	categoryDIV = $ '#category'
	
	numberCorrectSPAN = $ '#number-correct'
	numberTriedSPAN = $ '#number-tried'

	numberCorrect = 0
	numberTried = 0

	language = null
	codes = null
	word = null
	translations = null
	
	answers = null

	getRandomWord = ->
		$.getJSON (domain + 'ajax/random-word/'), null, (data, response) ->
			data = data[0]
	
			language = data.language[0]
			codes = data.codes
			word = data.word[0]
			translations = data.translations
			
			categoryText = ''
			
			for c, i in word.fields.categories
				categoryText += c.fields.name + ', '
			
			categoryDIV.html 'Category: ' + categoryText.slice 0, -2
	
			$('.translation').remove()	
	
			answers = translations.filter (x) -> x.fields.language.pk == language.pk
			
			$('.translation').remove()
	
			for t, i in translations
				if t.fields.language.pk == language.pk
					continue
	
				if not t.fields.primary
					continue
	
				newDIV = '<div class="translation fluid-row">' +
					'<div class="span6"><h4>' +
					t.fields.language.fields.name +
					'</h4></div>' +
					'<div class="span6"><h4>' +
					t.fields.spelling +
					'</h4></div>' +
					'</div>'
	
				translationsDIV.append(newDIV)
				
		guess.val ''
		guess.focus()

	
	normalize = (text, language) -> text.toLowerCase()
	
	
	fixButton = -> button.html 'Submit'
	
	
	checkGuess = (guess, answers, language) ->
		for a, i in answers
			if (normalize a.fields.spelling, language) == (normalize guess, language)
				return true

		return false
	
		
	processGuess = (guess, answers, language) ->
		correct = false
	
		numberTried += 1
		numberTriedSPAN.html numberTried	
	
		if checkGuess guess, answers, language
			correct = true
		
			numberCorrect += 1
			numberCorrectSPAN.html numberCorrect		
	
		if correct
			button.html 'Correct :)'
		else
			button.html 'Incorrect :('
	
		setTimeout (->
			fixButton()
			getRandomWord()
		), 2000


	getRandomWord()


	form1.submit (event) ->
		event.preventDefault()
		processGuess guess.val(), answers, language
		return false
