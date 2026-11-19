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
            print("This requisition is not pending. Status cannot be changed.")
            return
        if decision == "1":
            self.status = "Approved"
            self.approval_ref_num = self.staff_id + str(self.req_id)[-3:]
            print("Requisition approved by manager.")

        elif decision == "2":
            self.status = "Not approved"
            self.approval_ref_num = "Not available"
            print("Requisition not approved by manager.")

        elif decision == "3":
            print("Requisition is pending.")

        else:
            print("Invalid decision. Please choose 1, 2 or 3.")

    def display_requisition(self):
        print("Date:", self.req_date)
        print("Requisition ID:", self.req_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + format(self.total_price, ))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_ref_num)
class RequisitionSystem:

    def __init__(self):
        self.requisition_list = []
        self.next_id = 10001
    def add_requisition(self):
        print("--- Add Requisition ---")

        req_date = input("Date (DD/MM/YYYY): ").strip()

        while req_date == "":
            print("Date cannot be empty.")
            req_date = input("Date (DD/MM/YYYY): ").strip()

        staff_id = input("Staff ID: ").strip()

        while staff_id == "":
            print("Staff ID cannot be empty.")
            staff_id = input("Staff ID: ").strip()

        staff_name = input("Staff Name: ").strip()

        while staff_name == "":
            print("Staff Name cannot be empty.")
            staff_name = input("Staff Name: ").strip()

        items = []

        print("Add requested items; enter 'done' when finished.")

        while True:
            item_name = input("Item name (or done): ").strip()

            if item_name.lower() == "done":
                if len(items) > 0:
                    break

                print("Please add at least one item.")

            elif item_name == "":
                print("Item name cannot be empty.")

            else:
                while True:
                    try:
                        item_cost = float(input("Item cost ($): "))

                        if 0 <= item_cost < float("inf"):
                            break

                        print("Cost must be zero or a positive finite number.")

                    except ValueError:
                        print("Please enter a valid number.")

                items.append({
                    "name": item_name,
                    "cost": item_cost
                })
        requisition = Requisition(
            req_date,
            staff_id,
            staff_name,
            self.next_id
        )

        total = requisition.requisition_details(items)

        requisition.approve_requisition()

        self.requisition_list.append(requisition)

        self.next_id += 1

        print("Requisition submitted successfully.")
        print("Requisition ID:", requisition.req_id)
        print("Total: $" + format(total, ".2f"))
        print("Status:", requisition.status)
        print("Approval Reference Number:", requisition.approval_ref_num)

        return total
    def respond_to_requisition(self):
        entered_id = input("Enter Requisition ID: ").strip()

        if not entered_id.isdigit():
            print("Requisition ID must be numeric.")
            return

        for requisition in self.requisition_list:

            if requisition.req_id == int(entered_id):

                if requisition.status != "Pending":
                    print("Only pending requisitions can be changed.")
                    return

                print("1: Approved")
                print("2: Not approved")
                print("3: Leave pending")

                decision = input("Manager decision: ").strip()

                requisition.respond_to_requisition(decision)
                return

        print("Requisition ID not found.")

    def display_requisitions(self):

        if len(self.requisition_list) == 0:
            print("No requisitions have been submitted.")
            return

        print("Displaying Requisitions")

        for requisition in self.requisition_list:
            requisition.display_requisition()

    # Question 5(f): Requisition statistics
    def requisition_statistics(self):
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in self.requisition_list:

            if requisition.status == "Approved":
                approved += 1

            elif requisition.status == "Pending":
                pending += 1

            elif requisition.status == "Not approved":
                not_approved += 1

        submitted = len(self.requisition_list)

        print("\nDisplaying the Requisition Statistics")
        print("The total number of requisitions submitted:", submitted)
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)

        return {
            "submitted": submitted,
            "approved": approved,
            "pending": pending,
            "not_approved": not_approved
        }
    def menu(self):

        while True:
            print("\n===== REQUISITION MENU =====")
            print("1: Add Requisition")
            print("2: Manager Response")
            print("3: Display Requisitions")
            print("4: Requisition Statistics")
            print("5: Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_requisition()

            elif choice == "2":
                self.respond_to_requisition()

            elif choice == "3":
                self.display_requisitions()

            elif choice == "4":
                self.requisition_statistics()

            elif choice == "5":
                print("Exiting program.")
                break

            else:
                print("Invalid choice! Enter a number between 1 and 5.")
            if __name__ == "__main__":
                system = RequisitionSystem()
                system.menu()











































