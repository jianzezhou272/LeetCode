"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: list[Employee]
        :type id: int
        :rtype: int
        """
        E={}
        for emp in employees:
            E[emp.id]=[emp.importance,emp.subordinates]
        if E[id][1]==[]:
            return E[id][0]
        else:
            s=E[id][0]
            for emp in E[id][1]:
                s+=self.getImportance(employees, emp)
            return s