import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.email
import anvil.server


from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def send_feedback(name, email, feedback,recommendation):
  # Send yourself an email each time feedback is submitted
  app_tables.feedback.add_row(name=name,email=email,feedback=feedback,created=datetime.now(),recommendation=recommendation)
  