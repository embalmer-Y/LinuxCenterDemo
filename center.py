from app import config
import threading


class PermissionError(KeyError):
    pass


class TaskCenter(object):
    def __init__(self) -> None:
        self._id = ""
        self._user = ""
        self.command = []
        self._permission = ""

    # 将任务参数写入TaskCenter对象
    def reg_task(self, task_id, user_name, command, permission):
        self._id = task_id
        self._user = user_name
        self.command = command
        self._permission = permission

    # 简单鉴权后执行命令对应的函数
    def run_task(self):
        user_level = ""
        for key, user_list in  config.UserLists.items():
            if key == self._permission and self._user in user_list:
                user_level = key

        if user_level == "":
            raise PermissionError("User is not in UserList!")
        else:
            func = config.CommandDescription[user_level][self.command[0]]
            if len(self.command) == 1:
                t = threading.Thread(target=func, name=self._id)
            elif len(self.command) > 1:
                t = threading.Thread(target=func, name=self._id, args=(self.command[1:]))
            t.start()
