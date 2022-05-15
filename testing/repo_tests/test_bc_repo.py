import unittest

from models.benco import Benco
from repositories.benco_repo import BencoRepo

br = BencoRepo()


class TestBencoRepo(unittest.TestCase):

    added_benco = Benco()
    # Creating a Benco to update it?
    deleted_benco = Benco()

    def test_get_benco_success(self):
        benco = br.get_benco(1)
        self.assertEqual(benco, Benco(bc_id=1, name="Frank"))

    def test_create_benco_success(self):
        TestBencoRepo.added_benco = br.create_benco(self.added_benco)

        self.assertEqual(self.added_benco, Benco(bc_id=self.added_benco.bc_id, name=""))

        self.assertIsNotNone(br.get_benco(self.added_benco.bc_id))
        print(self.added_benco)

    def test_all_bencos_success(self):
        # Still prone to errors - If I add more Bencos = I must manually update the test list
        bencos = br.all_bencos()
        self.assertListEqual(bencos, [
            Benco(bc_id=1, name="Frank"),
            Benco(bc_id=2, name="Carl"),
            Benco(bc_id=3, name="Pamela"),
            Benco(bc_id=4, name="Ali"),
            Benco(bc_id=5, name="Stephanie")
        ])

    def test_update_benco_success(self):
        # I don't want to make the update permanent
        TestBencoRepo.added_benco = br.create_benco(self.added_benco)
        TestBencoRepo.added_benco.name = "Update"
        TestBencoRepo.added_benco = br.update_benco(TestBencoRepo.added_benco)
        self.assertEqual(self.added_benco, Benco(bc_id=self.added_benco.bc_id, name="Update"))
        self.assertIsNotNone(br.get_benco(self.added_benco.bc_id))
        print(self.added_benco)

    def test_delete_benco_success(self):
        # I don't want to make the delete permanent
        # Prone to errors since List of bencos can still be updated. This is hard coded
        # How do I make mock test list dynamic (update and added bencos handled properly)?
        bencos = br.all_bencos()
        TestBencoRepo.deleted_benco = br.create_benco(self.deleted_benco)
        br.delete_benco(self.deleted_benco.bc_id)
        self.assertListEqual(bencos, [
            Benco(bc_id=1, name="Frank"),
            Benco(bc_id=2, name="Carl"),
            Benco(bc_id=3, name="Pamela"),
            Benco(bc_id=4, name="Ali"),
            Benco(bc_id=5, name="Stephanie")
        ])

    # setUp and tearDown will execute before or after each and every test
    # whereas setUpClas and tearDownClass will execute once before or after all tests
    @classmethod
    def tearDownClass(cls):
        if cls.added_benco.bc_id:
            br.delete_benco(cls.added_benco.bc_id)


if __name__ == '__main__':
    unittest.main()

