import cgi
form = cgi.FieldStorage()
text = form.getvalue("name")
surename = form.getvalue("surname")
mail = form.getvalue("mail")
phone = form.getvalue("phone")
subject = form.getvalue("subject")
consult = form.getvalue("consult")


