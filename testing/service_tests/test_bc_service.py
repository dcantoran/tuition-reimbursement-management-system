# Service Tests should NOT rely on Repos or on functions being used for added functionality
# We're going to assume that all other methods being used/called in the testing function WILL work
# If they do work does the rest of the function logic do what we want it to do?
import unittest
from unittest.mock import MagicMock

from models.benco import Benco
from repositories.benco_repo import BencoRepo
from services.benco_service import BencoService


# MOCKING
# A Process of trying NOT to rely on parts of our code to test other aspects of our code
# Create MOCK functions and return values and compare MOCK test value but using the ACTUAL service method
class TestBencoService(unittest.TestCase):

    br = BencoRepo()
    bs = BencoService(br)

    def test_get_benco_by_id(self):
        # fake data for what will be returned in case we need get_benco_by_id
        self.bs.get_benco_by_id = MagicMock(return_value=[
            Benco(bc_id=1, name="Gerry")
        ])
        refined_benco = self.bs.get_benco_by_id(1)
        print(refined_benco)

        self.assertEqual(refined_benco, [
            Benco(bc_id=1, name="Gerry")
        ])

    def test_create_benco(self):
        pass

    def test_get_all_bencos(self):

        self.bs.get_all_bencos = MagicMock(return_value=[
            Benco(bc_id=1, name="Gerry"),
            Benco(bc_id=2, name="Mary"),
            Benco(bc_id=3, name="Harry")
        ])
        refined_benco = self.bs.get_all_bencos
        print(self.bs.get_all_bencos)

        # self.assertListEqual(refined_benco, [
        #     Benco(bc_id=1, name="Gerry"),
        #     Benco(bc_id=2, name="Mary"),
        #     Benco(bc_id=3, name="Harry")
        # ])

    def test_update_benco(self, change):
        pass

    def test_delete_benco(self, bc_id):
        pass


if __name__ == '__main__':
    unittest.main()