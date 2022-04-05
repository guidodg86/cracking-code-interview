class listNode:
    def __init__(self, value):
        self.next = -1
        self.value = value
    
    def append(self, new_item):
        self.next = new_item


class myList:
    def __init__(self, items_to_link):
        listRoot = listNode(items_to_link[0])
        self.root=listRoot
        prev_pointer = listRoot
        for item in items_to_link[1:]:
            listItem = listNode (item)
            prev_pointer.append(listItem)
            prev_pointer=listItem
    
    def __str__(self):
        list_pointer = self.root
        result = ""
        while list_pointer.next != -1:
            result = result + list_pointer.value + " -> "
            list_pointer = list_pointer.next
        result = result + list_pointer.value + " -|"
        return result


