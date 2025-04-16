from flask import Flask,  render_template, request
import random

app = Flask(__name__)

quotes = ["Every tree is a playground to the spirited squirrel.",
          "Dance like a squirrel leaping from branch to branch.",
          "A squirrel's playfulness reminds us that joy can be found in the simple things.",
          "Stay curious, for that's how the squirrels find the best acorns.",
          "A squirrel always plans with the foresight of winter in mind.",
          "Embrace change with a squirrel's resilience - flexible but steadfast.",
          "In every chirp and chatter, squirrel communities find strength in unity.",
          "Chase happiness with the enthusiasm of a squirrel in autumn.",
          "A squirrel knows that nature's abundance lies in resourcefulness.",
          "Success is calculated risk, like a squirrel's leap across the expanse of air."]

@app.route('/quote', methods=['GET', 'POST'])

def quote():
    selected_quote = None
    if request.method == 'POST':
        selected_quote = random.choice(quotes)
    return render_template('quote.html', quote=selected_quote)

if __name__ == "__main__":
    app.run(debug=True)




