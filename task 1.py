class Requisition:
    def __init__(self, req_date, staff_id, staff_name, req_id):
        self.req_date = req_date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.req_id = req_id
        self.item_list = []
        self.total_price = 0.0
        self.status = "Pending"
        self.approval_ref_num = "Not available"

    def requisition_details(self, items):
        self.item_list = items
        self.total_price = 0.0

        for item in self.item_list:
            self.total_price += item["cost"]

        return self.total_price

    def approve_requisition(self):

        if self.total_price < 500:
            self.status = "Approved"
            self.approval_ref_num = self.staff_id + str(self.req_id)[-3:]

        else:
            self.status = "Pending"
            self.approval_ref_num = "Not available"

        return self.status

    def respond_to_requisition(self, decision):

        if self.status != "Pending":
            print("This requisition is already decided.")
            return False

        if decision == "1":
            self.status = "Approved"
            self.approval_ref_num = self.staff_id + str(self.req_id)[-3:]
            print("Requisition approved by manager.")

        elif decision == "2":
            self.status = "Not approved"
            self.approval_ref_num = "Not available"
            print("Requisition not approved.")

        elif decision == "3":
            print("Requisition remains pending.")

        else:
            print("Invalid decision. Please enter 1, 2 or 3.")
            return False

        return True




















       


