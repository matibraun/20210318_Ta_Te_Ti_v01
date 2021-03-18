type State = Welcome | LoadingPlayers | FinishedLoadingPlayers | LoadingBoard | FinishedLoadingBoard | Playing | FinishedWithWinner | FinishedWithoutWinner | AfterGameOptions | GoodBye

type Welcome = {
    stage: 'Welcome',
}

type LoadingPlayers = {
    stage: 'LoadingPlayers',
    players: Array<player>
}

type player = {
    name = 'string',
    symbol = 'string',
}

type FinishedLoadingPlayers = {
    stage: 'FinishedLoadingPlayers',
    players: Array<player>
}

