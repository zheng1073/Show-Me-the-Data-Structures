#Problem 4: Active Directory

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
        
def is_user_in_group(user, group):
    in_group = False
    
    if user in group.get_users():
        in_group = True
        return in_group
    else:
        if len(group.get_groups()) == 0:
            return in_group
        else:
            for orgs in group.get_groups():
                is_user_in_group(user, orgs)
  

#Test
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(parent.is_user_in_group('', parent)) #False
print(parent.is_user_in_group(sub_child_user, child)) #True
print(parent.is_user_in_group(child_user, '')) #False
