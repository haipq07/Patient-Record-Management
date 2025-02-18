import graphviz
import csv
from binary_search_tree import BinarySearchTree, Node
class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.diagnosis=diagnosis
        self.blood_pressure=blood_pressure
        self.pulse=pulse
        self.body_temperature=body_temperature
    def __str__(self):
        return (f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
                f"Diagnosis: {self.diagnosis}, Blood Pressure: {self.blood_pressure}, "
                f"Pulse: {self.pulse}, Body Temperature: {self.body_temperature}")


class PatientRecordManagementSystem:
    def __init__(self):
        self.bst = BinarySearchTree()  # Create an empty Binary Search Tree
    
    
    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        new_record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        self.bst.insert(Node(patient_id, new_record))  # Insert new node into the BST

    def search_patient_record(self, patient_id):
        node = self.bst.search(patient_id)
        return node.value if node else None

    def delete_patient_record(self, patient_id):
        self.bst.remove(patient_id)

    def display_all_records(self):
        nodes = self.bst.inorder_traversal(self.bst.root)
        for node in nodes:
            print(node.value)  # This now uses the __str__ method of PatientRecord

    def build_tree_from_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature = row
                self.add_patient_record(int(patient_id), name, int(age), diagnosis, blood_pressure, int(pulse), float(body_temperature))
    def _add_nodes(self, dot, node):
        if node:
            dot.node(str(node.key), f"{node.key}: {node.value.name}")  # Ensure correct label is displayed
            if node.left:
                dot.edge(str(node.key), str(node.left.key))  # Add edge to left child
                self._add_nodes(dot, node.left)  # Correct recursive call for left child
            if node.right:
                dot.edge(str(node.key), str(node.right.key))  # Add edge to right child
                self._add_nodes(dot, node.right)  # Correct recursive call for right child

    def visualize_tree(self):
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
        return dot
    

