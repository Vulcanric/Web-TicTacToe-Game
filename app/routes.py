from flask import Blueprint, render_template, request, jsonify, Response
from flask_socketio import emit, join_room, leave_room
from . import socketio
from .models import TicTacToe
from typing import Dict, Any

main = Blueprint('main', __name__)

# Global game instance (not suitable for production; consider using a more robust state management system)
game = TicTacToe()

@main.route('/')
def index() -> str:
    """ 
    Render the index page.
    
    :return: The rendered HTML for the index page (maybe landing page).
    """
    return render_template('index.html')

@main.route('/play-ai', methods=['POST'])
def play_ai() -> Response:
    """ 
    Handles a move by the player and responds with Karaba's move and the winner, if any.
    
    :return: A JSON response with Karaba's move and the winner, if there's one.
    """
    global game
    if not request.json or 'move' not in request.json:
        return jsonify({'error': 'Invalid input'}), 400
    
    player_move: int = int(request.json['move'])
    if not game.make_move(player_move, 'X'):
        return jsonify({'error': 'Invalid move'}), 400

    if game.current_winner:
        return jsonify({'winner': 'X'})

    ai_move: int = game.ai_move()
    game.make_move(ai_move, 'O')
    return jsonify({'ai_move': ai_move, 'winner': game.current_winner})

@socketio.on('join')
def on_join(data: Dict[str, Any]) -> None:
    """
    Handles a player joining a room in the online game.

    :param data: A dictionary containing the room information.
    """
    room: str = data['room']
    join_room(room)
    emit('join_room', {'message': 'Joined room: ' + room}, room=room)

@socketio.on('move')
def on_move(data: Dict[str, Any]) -> None:
    """
    Handles a move made by a player in the online game.

    :param data: A dictionary containing the room and move information.
    """
    room: str = data['room']
    move: int = data['move']
    emit('make_move', move, room=room)
