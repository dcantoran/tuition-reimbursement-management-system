import unittest

from models.dept_head import DeptHead
from repositories.dept_head_repo import DeptHeadRepo

dhr = DeptHeadRepo()


class TestDeptHeadRepo(unittest.TestCase):

    added_dh = DeptHead()

    def test_get_dept_head_success(self):
        head = dhr.get_dept_head(1)
        self.assertEqual(head, DeptHead(dh_id=1, name="Lisa"))

    def test_create_dept_head_success(self):
        TestDeptHeadRepo.added_dh = dhr.create_dept_head(self.added_dh)

        self.assertEqual(self.added_dh, DeptHead(dh_id=self.added_dh.dh_id, name=""))

        self.assertIsNotNone(dhr.get_dept_head(self.added_dh.dh_id))
        print(self.added_dh)

    # setUp and tearDown will execute before or after each and every test
    # whereas setUpClas and tearDownClass will execute once before or after all tests
    @classmethod
    def tearDownClass(cls):
        if cls.added_dh.dh_id:
            dhr.delete_dept_head(cls.added_dh.dh_id)


if __name__ == '__main__':
    unittest.main()

