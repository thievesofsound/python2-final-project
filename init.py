from textual_serve.server import Server
import selection_menu
server = Server("python selection_menu.py", port=8000)
server.serve(debug=True)
