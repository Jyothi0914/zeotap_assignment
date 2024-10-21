from flask import Flask, request, jsonify
import logging
from ast_engine.rule_parser import create_rule, combine_rules
from ast_engine.rule_evaluator import evaluate_rule
from database.db import store_rule, fetch_rule

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    try:
        rule_string = request.json.get('rule_string')
        if not rule_string:
            return jsonify({"error": "rule_string is required"}), 400

        rule_ast = create_rule(rule_string)
        store_rule(rule_string, rule_ast)
        return jsonify({"ast": rule_ast.__repr__()})

    except Exception as e:
        logging.error(f"Error creating rule: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    try:
        rules = request.json.get('rules')
        operator = request.json.get('operator', 'AND')

        if not rules or not isinstance(rules, list):
            return jsonify({"error": "rules must be a list of rule strings"}), 400

        rule_asts = [create_rule(r) for r in rules]
        combined_ast = combine_rules(rule_asts, operator)

        return jsonify({"combined_ast": combined_ast.__repr__()})

    except Exception as e:
        logging.error(f"Error combining rules: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/evaluate', methods=['POST'])
def evaluate_rule_api():
    try:
        rule_id = request.json.get('rule_id')
        user_data = request.json.get('data')

        if not rule_id or not user_data:
            return jsonify({"error": "rule_id and data are required"}), 400

        rule_string, ast = fetch_rule(rule_id)
        result = evaluate_rule(ast, user_data)
        return jsonify({"result": result})

    except Exception as e:
        logging.error(f"Error evaluating rule: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
