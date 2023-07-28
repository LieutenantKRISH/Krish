from enum import Enum

class MapSite:
    def Enter(self):
        raise NotImplementedError('Abstract Base Class method')

class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

class Room(MapSite):
    def __init__(self, roomNo):
        self._sides = [MapSite() for _ in range(4)]
        self._roomNumber = int(roomNo)

    def GetSide(self, direction):
        return self._sides[direction.value]

    def SetSide(self, direction, mapSite):
        self._sides[direction.value] = mapSite

    def Enter(self):
        print('You have entered room:', self._roomNumber)

class Wall(MapSite):
    def Enter(self):
        print('You ran into a wall......')

class Door(MapSite):
    def __init__(self, room1=None, room2=None):
        self._room1 = room1
        self._room2 = room2
        self._isOpen = False

    def OtherSideFrom(self, room):
        print(f'Door object: This door is a side of Room: {room._roomNumber}')
        if room == self._room1:
            return self._room2
        else:
            return self._room1

    def Enter(self):
        if self._isOpen:
            print('********You have passed through this door....')
        else:
            print('****This door needs to be opened before you can pass through it.....')

class Main:
    def __init__(self):
        self._rooms = {}

    def AddRoom(self, room):
        self._rooms[room._roomNumber] = room

    def RoomNo(self, room_number):
        return self._rooms.get(room_number)

class Maze:
    def __init__(self):
        self._rooms = {}

    def AddRoom(self, room):
        self._rooms[room._roomNumber] = room

    def RoomNo(self, room_number):
        return self._rooms.get(room_number)

class MazeFactory:
    @classmethod
    def MakeMaze(cls):
        return Maze()

    @classmethod
    def MakeWall(cls):
        return Wall()

    @classmethod
    def MakeRoom(cls, n):
        return Room(n)

    @classmethod
    def MakeDoor(cls, r1, r2):
        return Door(r1, r2)

class MazeGame:
    def CreateMaze(self, factory=MazeFactory):
        aMaze = factory.MakeMaze()
        r1 = factory.MakeRoom(1)
        r2 = factory.MakeRoom(2)
        aDoor = factory.MakeDoor(r1, r2)

        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)

        r1.SetSide(Direction.North, factory.MakeWall())
        r1.SetSide(Direction.East, aDoor)
        r1.SetSide(Direction.South, factory.MakeWall())
        r1.SetSide(Direction.West, factory.MakeWall())

        r2.SetSide(Direction.North, factory.MakeWall())
        r2.SetSide(Direction.East, factory.MakeWall())
        r2.SetSide(Direction.South, factory.MakeWall())
        r2.SetSide(Direction.West, aDoor)

        return aMaze

if __name__ == "__main__":
    def find_maze_rooms(maze_obj):
        maze_rooms = []
        for room_number in range(1,3):  # Update the range to match the number of rooms you want to create (e.g., 3 in this case).
            try:
                room = maze_obj.RoomNo(room_number)
                print('\n*** Maze has room:', room_number)
                print('     Entering the room.....')
                room.Enter()
                maze_rooms.append(room)
                for idx in range(4):
                    side = room.GetSide(Direction(idx))
                    side_str = str(side.__class__).replace("<class '__main__.", "").replace("'>", "")
                    print('   Room:', room_number, f'{Direction(idx):<15s}', ', Type:', side_str)
                    print('    Trying to enter:', Direction(idx))
                    side.Enter()
                    if isinstance(side, Door):
                        door = side
                        if not door._isOpen:
                            print('     ****Opening the door.....')
                            door._isOpen = True
                            door.Enter()
                        print('\t', door)
                        other_room = door.OtherSideFrom(room)
                        print(f'\ton the other side of the door is Room: {other_room._roomNumber}\n')

            except KeyError:
                print('No room:', room_number)

    print('*' * 21)
    print('*****The Maze Gate******')
    print('*' * 21)

    factory = MazeFactory
    maze_obj = MazeGame().CreateMaze(factory)
    find_maze_rooms(maze_obj)
  """ EXPALANTION

1. Import necessary modules and classes:
   - The code starts by importing the `Enum` class from the `enum` module. This is used to create enumerations for the `Direction` class.
   

2. Define the `MapSite` class:
   - This class defines an abstract base class with an `Enter` method that raises a `NotImplementedError`. The `MapSite` class is
   meant to be a base class for different components in the maze (e.g., rooms, walls, doors).

3. Define the `Direction` enumeration:
   - This enumeration defines the four cardinal directions: `North`, `East`, `South`, and `West`, with corresponding integer
   values (0, 1, 2, 3).

4. Define the `Room` class:
   - The `Room` class is a subclass of `MapSite` and represents a room in the maze. It has attributes to store the room number and 
   an array (`_sides`) to hold the four sides (north, east, south, west) of the room.
   - The `GetSide` method retrieves the side of the room based on the provided `Direction`.
   - The `SetSide` method sets the side of the room with a given `MapSite`.
   - The `Enter` method prints a message when a player enters the room.

5. Define the `Wall` class:
   - The `Wall` class is a subclass of `MapSite` and represents a wall in the maze. It has an `Enter` method that prints a
   message when a player tries to enter a wall.

6. Define the `Door` class:
   - The `Door` class is a subclass of `MapSite` and represents a door between two rooms in the maze. It has attributes to 
   store the connected rooms (`_room1` and `_room2`) and a flag to indicate whether the door is open (`_isOpen`).
   - The `OtherSideFrom` method returns the room object that is on the other side of the door when given one of the connected rooms.
   - The `Enter` method prints a message depending on whether the door is open or not.

7. Define the `Main` class:
   - The `Main` class is used to manage the rooms in the maze. It has a dictionary (`_rooms`) to store the rooms with their
   respective room numbers.
   - The `AddRoom` method adds a room to the `_rooms` dictionary using the room number as the key.
   - The `RoomNo` method retrieves a room object based on the provided room number.

8. Define the `Maze` class:
   - The `Maze` class is similar to the `Main` class and is used to manage the rooms in the maze.

9. Define the `MazeFactory` class:
   - The `MazeFactory` class is used to create maze components. It has class methods for creating a maze, wall, room, and door.
   - The `MakeMaze`, `MakeWall`, `MakeRoom`, and `MakeDoor` methods return instances of `Maze`, `Wall`, `Room`, and `Door`, respectively.

10. Define the `MazeGame` class:
    - The `MazeGame` class is used to create the maze. It has a `CreateMaze` method that initializes a maze, creates two rooms
    (`r1` and `r2`), and a door (`aDoor`) between them. The maze is then populated with the rooms and their connections.

11. In the `__main__` block:
    - The `find_maze_rooms` function is defined to print details about the maze.
    - The `factory` variable is assigned the `MazeFactory` class.
    - A maze object (`maze_obj`) is created using the `CreateMaze` method from the `MazeGame` class.
    - The `find_maze_rooms` function is called with the `maze_obj` to display information about the maze's rooms, walls,
    and doors.

Overall, this code implements a basic representation of a maze using creational design patterns. It demonstrates how to create a maze
, rooms, walls, and doors and how they are interconnected. The `MazeFactory` class uses the abstract factory pattern to create maze 
components without specifying their concrete classes, allowing for flexibility in creating different types of mazes."""
