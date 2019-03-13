#!/usr/local/bin/python3

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
v_name = form.getvalue('name')
v_email = form.getvalue('email')
v_age = form.getvalue('age')
v_occupation = form.getvalue('occupation')
v_feedback = form.getvalue('feedback')
v_levelsPlayed = form.getvalue('levels-played')
v_updates = form.getvalue('updates')
V_comments = form.getvalue('comments')

	pass
# send an html response.
print("""
<html>
  <body>
   <h1>Thanks, {v_name}.format</h1><br><br>
   <p>Your email {v_email}.format has been received.</p><br>
   <p>Thank you for sharing your age ({v_age}.format) , you preserve well for being so old!</p>
   

  </body>
</html>
""")


