import unittest
from google.appengine.ext import ndb

# theses are the stuff we're going to test
import gae_env
from gae_env.constants import INIT_KEY, NOT_SET_VALUE
from gae_env.errors import ValueNotSetError


class SetValueTestCase(unittest.TestCase):
    nosegae_datastore_v3 = True
    nosegae_memcache = True

    key_foo, value_bar = 'key_foo', 'value_bar'

    def setUp(self):
        ndb.get_context().clear_cache()

    def testDummyValueInitialised(self):
        gae_env.init()  # should set a value for key: INIT_KEY
        dummy_value = gae_env.get(
            INIT_KEY, raise_value_not_set_error=False, return_none_for_not_set_value=False)
        self.assertNotEqual(dummy_value, None)

    def testSetValue(self):
        gae_env.set_value(self.key_foo, self.value_bar)
        retrieved_value = gae_env.get(self.key_foo)
        self.assertEqual(retrieved_value, self.value_bar)

    def testSetValueInCustomNamespace(self):
        custom_namespace = 'custom_namespace'
        gae_env.set_value(self.key_foo, self.value_bar, gae_namespace=custom_namespace)
        retrieved_value = gae_env.get(self.key_foo, gae_namespace=custom_namespace)
        self.assertEqual(retrieved_value, self.value_bar)


class GetValueTestCase(unittest.TestCase):
    nosegae_datastore_v3 = True
    nosegae_memcache = True

    key1, key_foo, key_2_dot_5 = 'one', 'foo', '2_dot_5'
    value1, value_bar, value_2_dot_5 = 1, 'bar', 2.5
    random_key = 'random'
    custom_namespace = 'custom_namespace'

    def setUp(self):
        ndb.get_context().clear_cache()
        gae_env.set_value(self.key1, self.value1)
        gae_env.set_value(self.key_foo, self.value_bar)
        gae_env.set_value(self.key_2_dot_5, self.value_2_dot_5)
        gae_env.set_value(self.key_foo, self.value_bar, gae_namespace=self.custom_namespace)

    def testGetValue(self):
        # GIVEN that key_foo is previously set to value_bar

        # WHEN we get the value stored at key_foo
        retrieved_value = gae_env.get(self.key_foo)

        # THEN it should be the same as value_bar
        self.assertEqual(retrieved_value, self.value_bar)

    def testGetValueFromCustomNamespace(self):
        # GIVEN that key_foo is set to value_bar in custom_namespace

        # WHEN we get the value for key_foo in custom_namespace
        retrieved_value = gae_env.get(self.key_foo, gae_namespace=self.custom_namespace)

        # THEN it should be the same as value_bar
        self.assertEqual(retrieved_value, self.value_bar)

    def testGetValueAsString(self):
        # GIVEN that key_foo was previously set to the value_bar (a string)

        # WHEN we get the value store at key_foo as a string
        retrieved_value = gae_env.get(self.key_foo, converter_class=str)

        # THEN is should be equal to value_bar
        self.assertEqual(retrieved_value, self.value_bar)
        self.assertIsInstance(retrieved_value, str)  # and it should be a string instance

    def testGetValueAsInt(self):
        # GIVEN that key_1 was previously set to value_1 (an integer)

        # WHEN we get the value stored at key1
        retrieved_value = gae_env.get(self.key1, converter_class=int)

        # THEN it should be equal to value1
        self.assertEqual(retrieved_value, self.value1)
        self.assertIsInstance(retrieved_value, int)  # and it should be an integer instance

    def testGetValueAsFloat(self):
        # GIVEN that key_2_dot_5 was previously set to value_2_dot_5 (a float)

        # WHEN we get the value stored at key_2_dot_5
        retrieved_value = gae_env.get(self.key_2_dot_5, converter_class=float)

        # THEN it should be equal to value_2_dot_5
        self.assertEqual(retrieved_value, self.value_2_dot_5)
        self.assertIsInstance(retrieved_value, float)  # and it should be a float

    def testRaisesValueErrorForInvalidConverterClass(self):
        # GIVEN any state

        # WHEN we get a value, and pass converter_class to anything not within (str, int, float)
        # THEN should raise ValueError
        self.assertRaises(
            ValueError, gae_env.get, name=self.key_foo, converter_class=dict
        )

    def testRaisesValueNotSetError(self):
        # GIVEN that no value has been set for key random_key

        # WHEN we get the value stored at random_key and passes raise_value_not_set_error=True
        # THEN should raise a ValueNotSetError
        self.assertRaises(
            ValueNotSetError, gae_env.get, name=self.random_key, raise_value_not_set_error=True
        )

    def testDoesNotRaiseValueNotSetError(self):
        # GIVEN that no value has been set for key random_key

        # WHEN we get the value stored at random_key and passes raise_value_not_set_error=False
        gae_env.get(
            self.random_key, raise_value_not_set_error=False, return_none_for_not_set_value=False)

        # THEN should not raise a ValueNotSetError

    def test_returns_none_if_value_of_key_is_not_set_and_kwargs_passed(self):
        # GIVEN no value has been set for random_key

        # WHEN return_none_for_not_set_value is True and raise_value_not_set_error is False
        # and we get value stored at random_key
        retrieved_value = gae_env.get(
            self.random_key, raise_value_not_set_error=False, return_none_for_not_set_value=True)

        # THEN value should be None
        self.assertEqual(retrieved_value, None)

    def test_returns_NOT_SET_VALUE_if_value_of_key_is_not_set_and_kwargs_passed(self):
        # GIVEN no value has been set for random_key

        # WHEN return_none_for_not_set_value is False and raise_value_not_set_error is False
        # and we get value stored at random_key
        retrieved_value = gae_env.get(
            self.random_key, raise_value_not_set_error=False, return_none_for_not_set_value=False)

        # THEN value should be equal to NOT_SET_VALUE
        self.assertEqual(retrieved_value, NOT_SET_VALUE)


if __name__ == '__main__':
    unittest.main()
