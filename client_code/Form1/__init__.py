from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    email = self.email_box.text
    feedback=self.feedback_box.text
    recommendation = self.dropdown_list.selected_value
    print(recommendation)
    anvil.server.call('send_feedback', name, email, feedback,recommendation)
    Notification("Feedback submitted!").show()
    self.clear_inputs()
  
  def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""
    self.dropdown_list.selected_value = "Very unlikely"