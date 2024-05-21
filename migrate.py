import subprocess

def run_commands():
    commands = [
        'alembic revision --autogenerate -m "migration"',
        'alembic upgrade head'
    ]

    for command in commands:
        try:
            print(f"Executing command: {command}")
            subprocess.run(command, shell=True, check=True)
            print("Command executed successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {command}")
            print(e)
            return

if __name__ == "__main__":
    run_commands()