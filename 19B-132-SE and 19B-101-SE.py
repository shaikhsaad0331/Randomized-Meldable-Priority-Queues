#!/usr/bin/env python
# coding: utf-8

# # Shaikh Saad (19B-132-SE)
# # Muhammad Zeeshan (19B-101-SE)

# In[183]:


class PriorityQueue(object):

    def __init__(self):
        self.nodes = [None]
        self.insert_counter = 0

    def _is_higher_than(self, a, b):
        return b[1] < a[1] or (a[1] == b[1] and a[2] < b[2])

    def _heapify(self, n_node_index):
        while 1 < n_node_index:
            n_node = self.nodes[n_node_index]
            p_index = n_node_index / 2
            p_node = self.nodes[p_index]

            if self._is_higher_than(p_node, n_node):
                break

            tmp_node = p_node
            self.nodes[p_index] = n_node
            self.nodes[n_node_index] = tmp_node

            n_node_index = p_index

    def add(self, value, priority):
        n_node_index = len(self.nodes)
        self.insert_counter += 1
        self.nodes.append((value, priority, self.insert_counter))

        self._heapify(n_node_index)

    def peek(self):
        if len(self.nodes) == 1:
            return None
        else:
            return self.nodes[1][0]

    def pop(self):

        if len(self.nodes) == 1:
            raise LookupError("Heap is empty")

        f_output = self.nodes[1][0]

        no_space_index = 1
        while no_space_index * 2 < len(self.nodes):

            L_child_index = no_space_index * 2
            R_child_index = no_space_index * 2 + 1

            if (len(self.nodes) <= R_child_index or self._is_higher_than(self.nodes[L_child_index], self.nodes[R_child_index])):
                
                self.nodes[no_space_index] = self.nodes[L_child_index]
                no_space_index = L_child_index

            else:
                self.nodes[no_space_index] = self.nodes[R_child_index]
                no_space_index = R_child_index

        last_node_index = len(self.nodes) - 1
        self.nodes[no_space_index] = self.nodes[last_node_index]
        self._heapify(no_space_index)

        self.nodes.pop()
        return f_output


# In[ ]:




