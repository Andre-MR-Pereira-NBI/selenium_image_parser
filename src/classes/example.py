#STUB - Tags
class Worker:
    def __init__(self, input_name, input_id):
        self.name = input_name
        self.id = input_id
    
    def tuplePayload(self):
        return (self.name,self.id)
    
def example_object():
    intern = Worker("Matthew",3)
    return intern.tuplePayload()