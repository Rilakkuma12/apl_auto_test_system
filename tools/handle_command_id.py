import uuid


class HandleCommandId:
    @staticmethod
    def get_command_id():
        return str(uuid.uuid1()).replace('-', '')


my_comm_id = HandleCommandId()
if __name__ == '__main__':
    # comm = HandleCommandId()
    aa = my_comm_id.get_command_id()
    print(aa)
    bb = my_comm_id.get_command_id()
    print(bb)


