import unittest
from ast_engine.rule_parser import create_rule, combine_rules
from ast_engine.node import Node

class TestASTCreation(unittest.TestCase):
    def test_create_rule(self):
        rule_string = "(age > 30 AND department == 'Sales')"
        ast = create_rule(rule_string)
        self.assertIsInstance(ast, Node)
    
    def test_combine_rules(self):
        rule1 = create_rule("(age > 30)")
        rule2 = create_rule("(salary > 50000)")
        combined_ast = combine_rules([rule1, rule2], "AND")
        self.assertEqual(combined_ast.value, "AND")

if __name__ == '__main__':
    unittest.main()
