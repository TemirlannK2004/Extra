import os
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} выполнено за {end_time - start_time:.4f} сек")
        return result
    return wrapper

class CommandPrompt:
    def __init__(self):
        self.current_directory = os.getcwd()

    @timing_decorator
    def print_current_directory(self):
        dir =  os.getcwd()
        print(f"Текущая директория: {dir}")

    @timing_decorator
    def list_directories(self):
        try:
            files = os.listdir(self.current_directory)
            directories = [f for f in files if os.path.isdir(os.path.join(self.current_directory, f))]
            print("Директории:", directories)
        except Exception as e:
            print(f"Ошибка: {e}")

    @timing_decorator
    def change_directory(self, new_directory):
        try:
            os.chdir(os.path.join(self.current_directory, new_directory))
            self.current_directory = os.getcwd()
            print(f"Текущая директория: {self.current_directory}")
        except Exception as e:
            print(f"Ошибка: {e}")

    @timing_decorator
    def create_directory(self, directory_name):
        try:
            os.mkdir(os.path.join(self.current_directory, directory_name))
            print(f"Создана директория: {directory_name}")
        except Exception as e:
            print(f"Ошибка: {e}")

    @timing_decorator
    def delete_directory(self, directory_name):
        try:
            os.rmdir(os.path.join(self.current_directory, directory_name))
            print(f"Директория удалена: {directory_name}")
        except Exception as e:
            print(f"Ошибка: {e}")

    @timing_decorator
    def rename_directory(self, old_name, new_name):
        try:
            os.rename(os.path.join(self.current_directory, old_name), os.path.join(self.current_directory, new_name))
            print(f"Директория переименована: {old_name} -> {new_name}")
        except Exception as e:
            print(f"Ошибка: {e}")

    @timing_decorator
    def view_file(self, file_name):
        try:
            with open(os.path.join(self.current_directory, file_name), 'r') as file:
                content = file.read()
                print(f"Содержимое файла {file_name}:\n{content}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    cmd = CommandPrompt()

    command_methods = {
        'pwd':cmd.print_current_directory,
        'ls': cmd.list_directories,
        'cd': cmd.change_directory,
        'mkdir': cmd.create_directory,
        'rm': cmd.delete_directory,
        'mv': cmd.rename_directory,
        'cat': cmd.view_file,
        'help': lambda: print("Доступные команды: pwd, ls, cd, mkdir, rm, mv, cat, help, exit")
    }

    while True:
        user_input = input("Введите команду (для справки введите 'help'): ").split()
        command = user_input[0]

        if command == 'exit':
            break
        else:
            try:
                command_methods.get(command, lambda: print("Неизвестная команда. Введите 'help' для списка команд."))(*user_input[1:])
            except Exception as e:
                print(f"Ошибка выполнения команды: {e}")
