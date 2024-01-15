import pytest
import gitcode

def test_get_user_data():
  assert gitcode.get_user_data() != {}

