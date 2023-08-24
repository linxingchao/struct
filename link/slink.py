
class SinggleLink:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
def showData(head):
    info = ""
    while head is not None:
        info += "{}->".format(head.data)
        head = head.next
    info += "None"
    print(info)
        
def reserve(head:SinggleLink):
    if head == None or head.next == None:
        return head
    first = None
    mid = head
    last = head.next
    
    while last is not None:
        mid.next = first
        first = mid
        mid = last
        last = last.next
        if last is None:
            mid.next = first
    head = mid
    return head 
    
    
    
    