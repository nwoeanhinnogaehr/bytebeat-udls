slides.html : slides.md
	pandoc -s --mathjax -i -t revealjs slides.md  -o slides.html
