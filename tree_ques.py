"""
Uber DSA Round 1

You are given an organizational structure hierarchy. The CEO is at the top and then there are reports. 
There are n employees numbered from 0 to n-1
You are given two arrays manager and fun_rating both of length n
manager[i] means the manager of the ith employee. manager[0] = -1 meaning the CEO has no manager.
fun_rating[i] means the rfun ating of the ith employee.

You want to organize a fun event where you want to maximize the total fun of the event.
Total fun is defined as the sum of fun_ratings of all the employees participating. 

There is one constraint. You cannot have an employee and their direct manager participate together.

Find the max total fun of the event and also give the list of employees participating (employee IDs). If there are mutiple such solutions, provide any.
"""

class TreeNode:
    def __init__(self, id, val):
        self.id = id
        self.val = val
        self.children = []

def get_max_fun_rating(root: TreeNode) -> tuple(int, list[int]):
    memo = {}
    def travel_tree(node: TreeNode, can_pick: bool, bitmask: int) -> int:
        if not node:
            return 0, bitmask
        key = (node.id, can_pick)
        if key in memo:
            return memo[key]

        ans_cant_pick = 0
        bitmask_cant_pick = bitmask
        for child in node.children:
            resp, btmsk = travel_tree(child, True, bitmask)
            ans_cant_pick += resp
            bitmask_cant_pick |= btmsk
        
        final_ans = ans_cant_pick
        final_bitmask = bitmask_cant_pick
        if can_pick:
            ans_can_pick = node.val
            bitmask_can_pick = bitmask | 1 << node.id
            for child in node.children:
                resp, btmsk = travel_tree(child, False, bitmask_can_pick)
                ans_can_pick += resp
                bitmask_can_pick |= btmsk
            
            if final_ans < ans_can_pick:
                final_ans = ans_can_pick
                final_bitmask = bitmask_can_pick

        memo[key] = (final_ans, final_bitmask)
        return memo[key]
    
    max_fun_rating, employees = travel_tree(root, True, 0)
    employees_list = []
    idx = 0
    while employees:
        if employees & 1:
            employees_list.append(idx)
        employees >>= 1
        idx += 1
    return max_fun_rating, employees_list


def build_tree(manager: list[int], fun_rating: list[int]) -> TreeNode:
    n = len(manager)
    id_to_node = [None] * n
    for i in range(n):
        node = TreeNode(id = i, val = fun_rating[i])
        id_to_node[i] = node
    
    for i in range(1, n):
        parent_node = id_to_node[manager[i]]
        node = id_to_node[i]
        parent_node.children.append(node)
    
    return id_to_node[0]

if __name__ == "__main__":
    manager = [-1, 0, 0, 1, 1, 2, 2]
    fun_rating = [5, 2, 4, 7, 2, 10, 9]

    root = build_tree(manager=manager, fun_rating=fun_rating)
    max_fun_rating, employee_ids = get_max_fun_rating(root = root)
    print("Max Fun Rating:", max_fun_rating)
    print("Employees participating:", employee_ids)