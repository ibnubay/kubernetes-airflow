import unittest
from airflow.models import DagBag


class TestAirflowDAG(unittest.TestCase):
    def setUp(self):
        self.dagbag = DagBag()

    def test_import_dags(self):
        self.dag = self.dagbag.get_dag(dag_id='sample_dag')
        self.assertFalse(len(self.dagbag.import_errors), f'DAG Import failures: {self.dagbag.import_errors}')
        self.assertIsNotNone(self.dag)
        self.assertEqual(len(self.dag.tasks), 1)

    def test_send_email_error(self):
        for dag_id, dag in self.dagbag.dags.items():
            email = dag.default_args.get('email', [])
            msg = f"Alert email not set for DAG '{dag_id}'"
            self.assertIn('your@mail.com', email, msg)


if __name__ == '__main__':
    unittest.main()
