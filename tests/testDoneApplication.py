import DoneApplication
import unittest

from DoneApplication import DoneApplication

class testDoneApplication(unittest.TestCase):
  def test_Execute_When_NoParams_Then_ProposeDisplayingHelp(self):
    done = DoneApplication()
    text = done.Execute(["done"]);
    self.assertEqual("Use done help to display commands available", text)