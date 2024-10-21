import re
from .node import Node

def parse_condition(condition):
    match = re.match(r"(\w+)\s*(>|<|>=|<=|==|!=)\s*([\w']+)", condition)
    if match:
        operand, operator, value = match.groups()
        return Node('operand', value={"operand": operand, "operator": operator, "value": value})
    return None

def create_rule(rule_string):
    tokens = rule_string.split()  # Tokenize rule string
    stack = []
    
    for token in tokens:
        if token.upper() == 'AND' or token.upper() == 'OR':
            right = stack.pop()
            left = stack.pop()
            stack.append(Node('operator', left=left, right=right, value=token.upper()))
        else:
            condition_node = parse_condition(token)
            if condition_node:
                stack.append(condition_node)
    
    return stack[0]  # Return the root node of the AST

def combine_rules(rule_asts, operator):
    root = Node('operator', value=operator)
    root.left = rule_asts[0]
    root.right = rule_asts[1]
    
    for i in range(2, len(rule_asts)):
        new_root = Node('operator', value=operator)
        new_root.left = root
        new_root.right = rule_asts[i]
        root = new_root
    
    return root
