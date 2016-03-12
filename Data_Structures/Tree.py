from Data_Structures.Queues import QueueByLList as Queue


class ExpressionTree:
    def __init__(self, exp_str):
        self._expTree = None
        self._build_tree(exp_str)

    def evaluate(self, var_map):
        return self._eval_tree(self._expTree, var_map)

    def __str__(self):
        return self._build_string(self._expTree)

    def _build_tree(self, exp_str):
        # Build a queue containing the tokens in the expression string.
        exp_queue = Queue()
        for token in exp_str:
            exp_queue.enqueue(token)

        # Create an empty root node.
        self._expTree = _ExpTreeNode(None)
        # Call the recursive function to build the expression tree.
        self._rec_build_tree(self._expTree, exp_queue)

    def _rec_build_tree(self, cur_node, exp_queue):
        token = exp_queue.dequeue()

        if token == '(':
            cur_node.left = _ExpTreeNode(None)
            self._rec_build_tree(cur_node.left, exp_queue)

            # The next token will be an operator: + - / * %
            cur_node.element = exp_queue.dequeue()
            cur_node.right = _ExpTreeNode(None)
            self._rec_build_tree(cur_node.right, exp_queue)

            # The next token will be a ), remove it.
            exp_queue.dequeue()
        # Otherwise, the token is a digit that has to be converted to an int.
        else:
            cur_node.element = token

    def _build_string(self, tree_node):
        # If the node is a leaf, it's an operand. Otherwise, it's an operator.
        if tree_node.left is None and tree_node.right is None:
            return str(tree_node.element)
        else:
            exp_str = '('
            exp_str += self._build_string(tree_node.left)
            exp_str += str(tree_node.element)
            exp_str += self._build_string(tree_node.right)
            exp_str += ')'
            return exp_str

    def _eval_tree(self, subtree, var_dict):
        # See if the node is a leaf node, in which case return its value.
        if subtree.left is None and subtree.right is None:
            if '0' <= subtree.element <= '9':
                return int(subtree.element)
            else:
                assert subtree.element in var_dict, "Invalid variable."
                return var_dict[subtree.element]
        # Otherwise, it's an operator that needs to be computed.
        else:
            left_value = self._eval_tree(subtree.left, var_dict)
            right_value = self._eval_tree(subtree.right, var_dict)
            return self._compute_op(left_value, subtree.element, right_value)

    @staticmethod
    # Compute the arithmetic operation based on the supplied op string.
    def _compute_op(left, op, right):
        return eval(str(left) + str(op) + str(right))


class _ExpTreeNode:
    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None


if __name__ == '__main__':
    t_exp = '(8*5)'
    t_exp_tree = ExpressionTree(t_exp)
    result = t_exp_tree.evaluate({})
    print result
