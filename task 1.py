class Requisition:
    def __init__(self, req_id,req_date,stuff_id,stuff_name):
        self.req_date=req_date
        self.req_date=req_date
        self.stuff_id=stuff_id
        self.stuff_name=stuff_name
        self.item_list=[]
        self.total_calculating=0.0
        self.status="pending"
        self.approval_ref_num="Not Available"


    def requisition_details(self,items):
        self.item_list=items
        self.total_calculating=0.0
        for item in self.item_list:

            self.total_calculating+=item["cost"]
        return self.total_calculating
    def response_to_requisition(self, decision ):
        if self.status ="pending"









       


