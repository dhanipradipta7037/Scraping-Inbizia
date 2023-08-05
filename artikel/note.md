next_page = response.css('a.page-link::attr(href)')[5].get()
artikels = response.css('div.col-8.lh-120')
title = artikels.css('a.font-link::text').get()
link = artikels.css('a.font-link::attr(href)').get()