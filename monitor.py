from ConnectionScreen import ConnectionScreen
from CommandScreen import CommandScreen

if __name__ == "__main__":
    connection_screen = ConnectionScreen()
    if (connection_screen.ser != -1):
        CommandScreen(connection_screen.ser)
