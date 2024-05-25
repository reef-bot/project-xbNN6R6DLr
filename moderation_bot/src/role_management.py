# role_management.py

class RoleManagement:
    def __init__(self):
        self.roles = {}

    def add_role(self, role_name):
        if role_name not in self.roles:
            self.roles[role_name] = []
        else:
            print("Role already exists.")

    def remove_role(self, role_name):
        if role_name in self.roles:
            del self.roles[role_name]
        else:
            print("Role does not exist.")

    def assign_role(self, user_id, role_name):
        if role_name in self.roles:
            if user_id not in self.roles[role_name]:
                self.roles[role_name].append(user_id)
                print(f"Assigned role {role_name} to user {user_id}.")
            else:
                print("User already has the role.")
        else:
            print("Role does not exist.")

    def remove_role_from_user(self, user_id, role_name):
        if role_name in self.roles:
            if user_id in self.roles[role_name]:
                self.roles[role_name].remove(user_id)
                print(f"Removed role {role_name} from user {user_id}.")
            else:
                print("User does not have the role.")
        else:
            print("Role does not exist.")