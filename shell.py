import shlex
import os
import sys
import subprocess

def main():
    while True:

        try:
            command = input("$ ").strip()
            if not command:
                continue

            args = shlex.split(command)

            if args[0] == "ls":

                try:
                    # Use the argument if provided, else current directory
                    dir_path = args[1] if len(args) > 1 else "."
                    for item in os.listdir(dir_path):
                        print(item)
                except FileNotFoundError:
                    print(f"ls: {dir_path}: No such file or directory")
                except NotADirectoryError:
                    print(f"ls: {dir_path}: Not a directory")
                continue

            if args[0] == "exit":
                break

            if args[0] == "cd":
                try:
                    os.chdir(args[1])
                except IndexError:
                    print("cd: missing argument")
                except FileNotFoundError:
                    print("cd: directory not found")
                continue

            if args[0] == "pwd":
                print(os.getcwd())
                continue

            if args[0] == "echo":
                print(" ".join(args[1:]))
                continue

            if args[0] == "mkdir":
                try:
                    os.mkdir(args[1])
                except IndexError:
                    print("mkdir: missing argument")
                except FileExistsError:
                    print(f"mkdir: {args[1]} already exists")
                continue

            if args[0] == "rmdir":
                try:
                    dir_path = args[1]
                    os.rmdir(dir_path)  # Only removes empty directories
                except IndexError:
                    print("rmdir: missing argument")
                except FileNotFoundError:
                    print(f"rmdir: {dir_path}: No such directory")
                except OSError:
                    print(f"rmdir: {dir_path}: Directory not empty or cannot remove")
                continue


            if args[0] == "rm":
                try:
                    os.remove(args[1])
                except IndexError:
                    print("rm: missing argument")
                except FileNotFoundError:
                    print(f"rm: {args[1]} not found")
                continue

            if args[0] == "touch":
                try:
                    file_path = args[1]
                    # APPEND -> CLOSE
                    with open(file_path, "a"):
                        pass
                except IndexError:
                    print("touch: missing argument")
                except Exception as e:
                    print(f"touch: error creating file: {e}")
                continue
            

            if args[0] == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            subprocess.run(args)

        except FileNotFoundError:
            print(f"{args[0]}: command not found")

        except EOFError:
            print()
            break

        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    main()
