import uuid


class HandleCommandId:
    @staticmethod
    def get_command_id():
        return str(uuid.uuid1()).replace('-', '')


if __name__ == '__main__':
    comm = HandleCommandId()
    aa = comm.get_command_id()
    print(aa)
    bb = comm.get_command_id()
    print(bb)


