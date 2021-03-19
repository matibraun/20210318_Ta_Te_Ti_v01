type State = Welcome | LoadingPlayers | FinishedLoadingPlayers | LoadingBoard | FinishedLoadingBoard | Playing | FinishedWithWinner | FinishedWithoutWinner | AfterGameOptions | GoodBye

type Welcome = {
    stage: 'Welcome',
}

type LoadingPlayers = {
    stage: 'LoadingPlayers',
    players: Array<Player>
}

type Player = {
    name = 'string',
    symbol = 'string',
}

type FinishedLoadingPlayers = {
    stage: 'FinishedLoadingPlayers',
    players: Array<Player>,
}

type LoadingBoard = {
    stage: 'LoadingBoard',
    players: Array<player>,
    board: Array<Fila>,
    historicBoards: Array<board>,
}

type Fila = Array<'string' | None>,

type FinishedLoadingBoard = {
    stage: 'LoadingBoard',
    players: Array<player>,
    board: Array<Fila>,
    historicBoards: Array<board>,
}

type Playing = {
    stage: 'Playing',
    players: Array<player>,
    board: Array<Fila>,
    historicBoards: Array<board>,
    turn: 'number',
}

type FinishedWithWinner = {
    stage: 'FinishedWithWinner',
    players: Array<player>,
    board: Array<Fila>,
    historicBoards: Array<board>,
    turn: 'number',
}