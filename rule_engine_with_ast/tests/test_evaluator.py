import unittest
from ast_engine.rule_evaluator import evaluate_rule
from ast_engine.rule_parser import create_rule

class TestRuleEvaluator(unittest.TestCase):
    def test_evaluate_true(self):
        rule = create_rule("(age > 30 AND salary > 50000)")
        data = {"age": 35, "salary": 60000}
        self.assertTrue(evaluate_rule(rule, data))

    def test_evaluate_false(self):
        rule = create_rule("(age > 30 AND salary > 50000)")
        data = {"age": 25, "salary": 40000}
        self.assertFalse(evaluate_rule(rule, data))

if __name__ == '__main__':
    unittest.main()
