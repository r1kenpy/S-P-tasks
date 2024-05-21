class WrongNumberOfPlayersError(BaseException): ...


class NoSuchStrategyError(BaseException): ...


WINNER_OPTIONS = {'P': 'R', 'R': 'S', 'S': 'P'}
POSSIBLE_FIGURES = ('P', 'R', 'S')


def rps_game_winner(players):

    if len(players) != 2:
        raise WrongNumberOfPlayersError('Количество игроков не равно 2')

    player1, player2 = players
    player1_move, player2_move = player1[1], player2[1]

    if (
        player1_move not in POSSIBLE_FIGURES
        or player2_move not in POSSIBLE_FIGURES
    ):
        raise NoSuchStrategyError(
            'Указан неправильный фигура.'
            f'Возможные варианты: {POSSIBLE_FIGURES}'
        )

    if (
        WINNER_OPTIONS[player1_move] == player2_move
        or player1_move == player2_move
    ):
        return ' '.join(player1)
    else:
        return ' '.join(player2)
