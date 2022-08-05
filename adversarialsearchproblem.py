from abc import ABC, abstractmethod
from typing import Generic, Set, Tuple, TypeVar

###############################################################################
# An AdversarialSearchProblem is a representation of a game that is convenient
# for running adversarial search algorithms.
#
# A game can be put into this form by extending the AdversarialSearchProblem
# class. See tttproblem.py for an example of this.
#
# Every subclass of AdversarialSearchProblem has its game states represented
# as instances of a subclass of GameState. The only requirement that of a
# subclass of GameState is that it must implement that player_to_move(.) method,
# which returns the index (0-indexed) of the next player to move.
###############################################################################


class GameState(ABC):
    @abstractmethod
    def player_to_move(self) -> int:

        pass


State = TypeVar("State", bound=GameState)

# Action represents the type of actions that an instance of AdversarialSearchProblem uses to
# cause a transition. It's generic because different games have different actions: TTT requires
# placing a piece on a *2D* grid, while Connect 4 just involves selecting a column.
Action = TypeVar("Action")


class AdversarialSearchProblem(ABC, Generic[State, Action]):
    def get_start_state(self):

        return self._start_state

    def set_start_state(self, state: State):

        self._start_state = state

    @abstractmethod
    def get_available_actions(self, state: State) -> Set[Action]:

        pass

    @abstractmethod
    def transition(self, state: State, action: Action) -> State:

        assert not (self.is_terminal_state(state))
        assert action in self.get_available_actions(state)
        pass

    @abstractmethod
    def is_terminal_state(self, state: State) -> bool:
 
        pass

    # Used to be called evaluate_state
    @abstractmethod
    def evaluate_terminal(self, state: State) -> Tuple[int, int]:

        assert self.is_terminal_state(state)
        pass

    # Used to be called eval_func
    @abstractmethod
    def heuristic_func(self, state: State, player_index: int) -> float:

        pass


###############################################################################
# GameUI is an abstraction that allows you to interact directly with
# an AdversarialSearchProblem (through gamerunner.py). See tttproblem or
# connect4problem for examples.
#
# Utilizing GameUI is NOT necessary for this assignment, although you can use
# it with any ASPs you may decide to create.
###############################################################################


class GameUI(ABC):
    def update_state(self, state: GameState):

        self._state = state

    @abstractmethod
    def render(self):

        pass

    @abstractmethod
    def get_user_input_action(self):

        pass
