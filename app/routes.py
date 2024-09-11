from flask import Blueprint, render_template, request, jsonify, Response
from . import socketio
from .models import TicTacToe
from typing import Dict, Any

main = Blueprint('main', __name__)

# Global game instance
game = TicTacToe()

@main.route('/')
def index() -> str:
    """Render the index page."""
    return render_template('index.html')

@main.route('/play-ai', methods=['POST'])
def play_ai() -> Response:
    """Handles a move by the player and responds with Karaba's move and the winner, if any."""
    global game
    if not request.json or 'move' not in request.json:
        return jsonify({'error': 'Invalid input'}), 400
    
    player_move = int(request.json['move'])
    if not game.make_move(player_move, 'X'):
        return jsonify({'error': 'Invalid move'}), 400

    if game.current_winner:
        return jsonify({'winner': 'X'})

    if game.is_full():
        return jsonify({'draw': True})

    ai_move = game.ai_move()
    game.make_move(ai_move, 'O')

    if game.current_winner:
        return jsonify({'ai_move': ai_move, 'winner': 'O'})

    return jsonify({'ai_move': ai_move})

@main.route('/reset', methods=['POST'])
def reset() -> Response:
    """Resets the game board."""
    global game
    game.reset_board()
    return jsonify({'status': 'reset'})

@socketio.on('join')
def on_join(data: Dict[str, Any]) -> None:
    """Handles a player joining a room in the online game."""
    room = data['room']
    join_room(room)
    emit('join_room', {'message': 'Joined room: ' + room}, room=room)

@socketio.on('move')
def on_move(data: Dict[str, Any]) -> None:
    """Handles a move made by a player in the online game."""
    room = data['room']
    move = data['move']
    emit('make_move', move, room=room)
