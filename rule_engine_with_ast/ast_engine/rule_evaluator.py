def evaluate_rule(node, data):
    if node.type == 'operand':
        operand = node.value['operand']
        operator = node.value['operator']
        value = node.value['value']
        
        if operand not in data:
            return False
        
        if operator == '>':
            return data[operand] > int(value)
        elif operator == '<':
            return data[operand] < int(value)
        # Add more comparisons (==, !=, >=, etc.)
    
    elif node.type == 'operator':
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)
        
        if node.value == 'AND':
            return left_result and right_result
        elif node.value == 'OR':
            return left_result or right_result
    
    return False
