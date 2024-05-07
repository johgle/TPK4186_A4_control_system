from gate import Gate
from project import Project

class Checker:

    """Class to check that there is only one start node and one end node in the project"""

    def check_start_node(self, project):
        # No constraint has the gate "begin" as their target node
        gates = []
        for key, value in project.nodes.items(): #dict
            if isinstance(value, Gate):
                gates.append(value)
        # print(gates)

        target_nodes = []
        for node in gates:
            for con in project.constraints:
                target_node = con.get_target_node()
                if target_node == node:
                    target_nodes.append(target_node)
            
        start_gates = []
        for node in gates:
            if node not in target_nodes:
                start_gates.append(node)
        
        # print("start gates: ", start_gates)
        if len(start_gates) == 1:
            return True, start_gates[0]
        return False

    def check_end_node(self, project):
        # No constrain has the gate "end" as their source node.
        gates = []
        for key, value in project.nodes.items(): #dict
            if isinstance(value, Gate):
                gates.append(value)
        # print("Gates:", gates)

        source_nodes = []
        for node in gates:
            for con in project.constraints:
                source_node = con.get_source_node()
                if source_node == node:
                    source_nodes.append(source_node)

        end_gates = []
        for node in gates:
            if node not in source_nodes:
                end_gates.append(node)
        
        # print("end gates: ", end_gates)
        if len(end_gates) == 1:
            return True, end_gates[0]
        return False

    def check_start_node_dict(self, node_dict):
        for key, node in node_dict.items():
            if isinstance(node, Gate):
                if len(node.get_in_constraints()) == 0: # no constraint has this as their target node
                # the node is a gate and has no presuccessors.
                    # print("Fungerer, her er id til start node:", node.id)
                    return True, node
        return False

    def check_end_node_dict(self, node_dict):
        for key, node in node_dict.items():
            if isinstance(node, Gate):
                if len(node.get_out_constraints()) == 0: # no constraint has this as their source node
                # the node is a gate and has no successors.
                    # print("Fungerer, her er id til end node:", node.id)
                    return True, node
        return False