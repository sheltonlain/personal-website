Question 1. Choose one test from the provided suite and name it. In plain English, what does that test confirm about your site? Then name one thing your site could get wrong that this test would not catch.

Answer: 
test_page_shows_both_status_labels
This goal of this test is to make sure that our to-do list displays the correct status labels for finished and unfinished tasks. It does so by searching our home page for the displayed text "Completed" and "In progress". This is a quick way to make sure that our program is iteratiing through the list correctly. However, since this test is simply searching to make sure the text is displayed on the page, it would still pass if "Completed" and "In progress" were written anywhere on the page. For example, if my heading read "Completed and In progress Tasks" but my for loop or if statements did not run properly, this test would still pass.



Question 2. You built three pages that share one navigation bar. If you added a fourth link to your navigation, how many files would you edit? How many would you have edited if you had not used base.html, and why?

Answer: 
If a fourth link was added, I would have to edit 4 files: pages/views.py, pages/urls.py, templates/base.html, and the template for the additional nav link (for example, templates/help.html if I was adding a help page). 

If I had not used base.html, I would have had to edit 6 files, as the new nav link would have needed to be added to each template. This would have included pages/views.py, pages/urls.py, the about.html, contact.html, and home.html files from the templates folder, and the new template file. Let's say I forgot to edit the nav link on the contact template. If that were the case, we would no longer have a way to navigate to the new link we created from the Contact page. This would make our website buggy and difficult to navigate, especially if it had more pages. 