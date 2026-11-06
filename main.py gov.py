
# ============================================
# CITIZEN COMPLAINT MANAGEMENT SYSTEM
# Course: PROG211 - Object-Oriented Programming 1
# Domain: Government
# ============================================


# CLASS 1: CITIZEN
class Citizen:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def submit_complaint(self, category, description):
        """Create a complaint for this citizen."""
        complaint = Complaint(
            self.name,
            category,
            description
        )
        return complaint

    def display_info(self):
        print("Citizen Name:", self.name)
        print("Contact:", self.contact)


# CLASS 2: COMPLAINT
class Complaint:

    total_complaints = 0

    # Class constructor
    def __init__(self, citizen_name, category, description):
        Complaint.total_complaints += 1

        self.complaint_id = "CMP" + str(Complaint.total_complaints)
        self.citizen_name = citizen_name
        self.category = category
        self.description = description
        self.status = "Pending"

    # INSTANCE METHOD
    def update_status(self, new_status):
        self.status = new_status
        print("Complaint status updated successfully!")

    # INSTANCE METHOD
    def display_complaint(self):
        print("\n-----------------------------")
        print("COMPLAINT INFORMATION")
        print("-----------------------------")
        print("Complaint ID:", self.complaint_id)
        print("Citizen:", self.citizen_name)
        print("Category:", self.category)
        print("Description:", self.description)
        print("Status:", self.status)
        print("-----------------------------")

    # CLASS METHOD
    @classmethod
    def get_total_complaints(cls):
        return cls.total_complaints

    # STATIC METHOD
    @staticmethod
    def validate_category(category):
        allowed_categories = [
            "Roads",
            "Water Supply",
            "Electricity",
            "Sanitation",
            "Public Services"
        ]

        return category in allowed_categories


# PYTHON DATA STRUCTURE: DICTIONARY
complaints = {}


# FUNCTION TO ADD A COMPLAINT
def add_complaint():

    print("\n===== REGISTER CITIZEN COMPLAINT =====")

    name = input("Enter citizen name: ")
    contact = input("Enter contact information: ")

    print("\nAvailable Complaint Categories:")
    print("1. Roads")
    print("2. Water Supply")
    print("3. Electricity")
    print("4. Sanitation")
    print("5. Public Services")

    category = input("Enter complaint category: ")

    # Validate complaint category
    if not Complaint.validate_category(category):
        print("Invalid category. Please try again.")
        return

    description = input("Enter complaint description: ")

    # Create citizen object
    citizen = Citizen(name, contact)

    # Create complaint object through citizen
    complaint = citizen.submit_complaint(
        category,
        description
    )

    # Store complaint in dictionary
    complaints[complaint.complaint_id] = complaint

    print("\nComplaint submitted successfully!")
    print("Your Reference Number:", complaint.complaint_id)


# FUNCTION TO DISPLAY ALL COMPLAINTS
def display_complaints():

    print("\n===== ALL REGISTERED COMPLAINTS =====")

    if not complaints:
        print("No complaints have been registered.")
        return

    for complaint in complaints.values():
        complaint.display_complaint()


# FUNCTION TO SEARCH FOR A COMPLAINT
def search_complaint():

    complaint_id = input("Enter complaint reference number: ")

    if complaint_id in complaints:
        complaints[complaint_id].display_complaint()
    else:
        print("Complaint not found.")


# FUNCTION TO UPDATE COMPLAINT STATUS
def update_complaint():

    complaint_id = input("Enter complaint reference number: ")

    if complaint_id not in complaints:
        print("Complaint not found.")
        return

    print("\n1. Pending")
    print("2. In Progress")
    print("3. Resolved")

    choice = input("Select new status: ")

    statuses = {
        "1": "Pending",
        "2": "In Progress",
        "3": "Resolved"
    }

    if choice in statuses:
        complaints[complaint_id].update_status(
            statuses[choice]
        )
    else:
        print("Invalid status selection.")


# MAIN PROGRAM
def main():

    while True:

        print("\n================================")
        print(" GOVERNMENT OF SIERRA LEONE")
        print(" CITIZEN COMPLAINT MANAGEMENT")
        print("================================")

        print("1. Register a Complaint")
        print("2. View All Complaints")
        print("3. Search Complaint")
        print("4. Update Complaint Status")
        print("5. Total Complaints")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_complaint()

        elif choice == "2":
            display_complaints()

        elif choice == "3":
            search_complaint()

        elif choice == "4":
            update_complaint()

        elif choice == "5":
            print(
                "Total Complaints:",
                Complaint.get_total_complaints()
            )

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")


# RUN APPLICATION
if __name__ == "__main__":
    main()
