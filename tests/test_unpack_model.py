import unittest

from devicemonitor.model.base import PowerSupplyModel, BaseModel
from devicemonitor.model.input import FloatInput, BooleanInput, IntegerInput, StringInput


class MockModel(BaseModel):
    inputA = FloatInput(field_name="similar_to_A")
    inputB = BooleanInput(field_name="similar_to_B")
    inputC = IntegerInput(field_name="similar_to_C")
    inputD = StringInput(field_name="similar_to_D")

    def show(self):
        pass


class TestUnpackModelComplex(unittest.TestCase):
    """
    The simplest unpack test case
    """
    def test_unpack_model_correct(self):
        """
        Test unpack_json_to_model with complex model
        Json has string value and model supports many types
        Should convert to correct type
        """
        # Arrange
        json = {
            "similar_to_A": "0.0",
            "similar_to_B": "True",  # or 1
            "similar_to_C": "1",
            "similar_to_D": "string",
        }
        model = MockModel(json)
        # Assert
        self.assertEqual(model.inputA, 0.0)
        self.assertEqual(model.inputB, True)
        self.assertEqual(model.inputC, 1)
        self.assertEqual(model.inputD, "string")

    def test_unpack_model_not_all_data_key_error(self):
        """
        Test unpack_json_to_model with complex model
        Json has string value and model supports many types
        Should convert to correct type
        """
        # Arrange
        json = {
            "similar_to_A": "0.0",
            "similar_to_B": "True",  # or 1
            "similar_to_C": "1",
            # "similar_to_D": "string",
        }
        try:
            MockModel(json)
        except KeyError:
            self.assertRaises(KeyError)

    def test_unpack_model_value_error(self):
        """
          Test unpack_json_to_model with string
          Json has string value NOT number and model supports only float
          """
        json = {
            "similar_to_A": "notWorking",
            "similar_to_B": "notWorking",
            "similar_to_C": "notWorking",
            "similar_to_D": "working",
        }

        try:
            MockModel(json)
        except ValueError as e:
            print(e)
            self.assertRaises(ValueError)


class TestUnpackModelString(unittest.TestCase):
    """
    The simplest unpack test case
    """
    def test_unpack_model_correct(self):
        """
        Test unpack_json_to_model with string
        Json has string value and model supports only float
        Should convert to float
        """
        # Arrange
        json = {
            "current": "0.0",
            "voltage": "0.1",

        }
        model = PowerSupplyModel(json)
        # Assert
        self.assertEqual(model.output_current, 0.0)
        self.assertEqual(model.output_voltage, 0.1)

    def test_unpack_model_fail(self):
        """
          Test unpack_json_to_model with string
          Json has string value NOT number and model supports only float
          """
        json = {
            "current": "notWorking",
            "voltage": "notWorking",
        }
        try:
            PowerSupplyModel(json)
        except ValueError:
            self.assertRaises(ValueError)


