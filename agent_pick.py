from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Ajan listesi
AGENTS = [
    "Brimstone", "Viper", "Omen", "Killjoy", "Sage", "Cypher",
    "Reyna", "Jett", "Phoenix", "Raze", "Breach", "Sova",
    "Astra", "KAY/O", "Yoru", "Skye", "Gekko", "Chamber",
    "Neon", "Fade", "Harbor", "Deadlock", "Vyse", "Iso",
    "Waylay", "Clove", "Veto", "Tejo"
]


def get_safe_filename(agent_name):

    return agent_name.lower().replace("/", "").replace(" ", "")


@app.route('/', methods=['GET', 'POST'])
def index():
    selected_agent = None
    agent_filename = None

    if request.method == 'POST':
        selected_agent = random.choice(AGENTS)
        # Seçilen ajanın dosya ismini (örn: kayo) hesapla
        agent_filename = get_safe_filename(selected_agent)

    return render_template('index.html', agent=selected_agent, filename=agent_filename)


if __name__ == '__main__':
    app.run(debug=True)
