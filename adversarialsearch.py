from cmath import inf
from typing import Callable
from typing_extensions import Self

from adversarialsearchproblem import (
    Action,
    AdversarialSearchProblem,
    State as GState,
)
from adversarialsearchproblem import GameState
global Alpha
global Beta
Alpha = 0
Beta = 0


def minimax(asp: AdversarialSearchProblem[GState, Action]) -> Action:
    state = asp.get_start_state()
    player = state.player_to_move()
    V2 = float("-inf")
    for A in asp.get_available_actions(state):
        nextstate = asp.transition(state,A)
        V = MinValue(asp,nextstate, player)
        if V > V2:
            best_value = V
            best_move = A
    assert best_move is not None
    return best_move
def MaxValue(asp,state,player):
    if asp.is_terminal_state(state):
        Goal = asp.evaluate_terminal(state)
        return Goal[player]
    V = float("-inf")
    for A in asp.get_available_actions(state):
        nextstate = asp.transition(state,A)
        V = max(V,(MinValue(asp,nextstate,player)))
    return V

def MinValue(asp,state,player):
    if asp.is_terminal_state(state):
        Goal = asp.evaluate_terminal(state)
        return Goal[player]
    V = float("inf")
    for A in asp.get_available_actions(state):
        nextstate = asp.transition(state,A)
        V = min(V,(MaxValue(asp,nextstate,player)))
    return V





def alpha_beta(asp: AdversarialSearchProblem[GState, Action]) -> Action:
    state = asp.get_start_state()
    player = state.player_to_move()
    V2 = float("-inf")
    for A in asp.get_available_actions(state):
        nextstate = asp.transition(state,A)
        V = MinValue(asp,nextstate, player)
        if V > V2:
            best_value = V
            best_move = A
    assert best_move is not None
    return best_move
def MaxValue2(asp,state,player):
    if asp.is_terminal_state(state):
        Goal = asp.evaluate_terminal(state)
        return Goal[player]
    V = float("-inf")
    for A in asp.get_available_actions(state):
        nextstate = asp.transition(state,A)
        Alpha = max(V,(MinValue(asp,nextstate,player)))
    if V >= Beta:
        return Alpha

def MinValue2(asp,state,player):
    if asp.is_terminal_state(state):
        Goal = asp.evaluate_terminal(state)
        return Goal[player]
    V = float("inf")
    for A in asp.get_available_actions(state):
        nextstate = asp.transition(state,A)
        Beta = min(V,(MaxValue(asp,nextstate,player)))
    if V <= Alpha:
        return Beta


def alpha_beta_cutoff(
    asp: AdversarialSearchProblem[GState, Action],
    cutoff_ply: int,
    # See AdversarialSearchProblem:heuristic_func
    heuristic_func: Callable[[GState], float],
) -> Action:
    """
    This function should:
    - search through the asp using alpha-beta pruning
    - cut off the search after cutoff_ply moves have been made.

    Input:
        asp - an AdversarialSearchProblem
        cutoff_ply - an Integer that determines when to cutoff the search and
            use heuristic_func. For example, when cutoff_ply = 1, use
            heuristic_func to evaluate states that result from your first move.
            When cutoff_ply = 2, use heuristic_func to evaluate states that
            result from your opponent's first move. When cutoff_ply = 3 use
            heuristic_func to evaluate the states that result from your second
            move. You may assume that cutoff_ply > 0.
        heuristic_func - a function that takes in a GameState and outputs a
            real number indicating how good that state is for the player who is
            using alpha_beta_cutoff to choose their action. You do not need to
            implement this function, as it should be provided by whomever is
            calling alpha_beta_cutoff, however you are welcome to write
            evaluation functions to test your implemention. The heuristic_func
            we provide does not handle terminal states, so evaluate terminal
            states the same way you evaluated them in the previous algorithms.
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...
