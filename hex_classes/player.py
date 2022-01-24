class HexPlayer:
    """
    Represents a player in hex game.

    Attributes
    --------
    name: str
        player's name
    char: str
        a single character representing the player
    started_first: bool
        whether the player had the first move
    connections: List[Set[Tuple[int, int]]]
        list containing sets of player's connected hex tiles' coordinates
    is_winner: bool
        whether the player has won the game

    Methods
    --------
    set_name(name)
        sets name attribute to a new given value
    """
    def __init__(self, name: str, started_first: bool) -> None:
        """
        Parameters
        --------
        name: str
            the name of the player
        started_first: bool
            whether the player has/had the first move
        """
        self.name = name
        self.char = '1' if started_first else '2'
        self.started_first = started_first
        self.connections = list()
        self.is_winner = False

    def set_name(self, name: str) -> None:
        """
        sets player's name to a new given value

        Parameters
        --------
        name (str)
            new name to be assigned
        """
        if name:
            self.name = name
        else:
            raise ValueError("Name must not be empty")

    def __str__(self):
        return self.name
