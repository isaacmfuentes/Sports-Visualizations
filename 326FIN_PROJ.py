import pandas as pd
import matplotlib.pyplot as plt

messi_data = {
    'Year': list(range(2010, 2021)),
    'Goals': [60, 59, 91, 45, 58, 52, 59, 54, 51, 50, 27],
    'Games': [60, 70, 69, 47, 66, 61, 62, 64, 54, 58, 48],
}

ronaldo_data = {
    'Year': list(range(2010, 2021)),
    'Goals': [48, 60, 63, 69, 61, 57, 55, 53, 49, 39, 44],
    'Games': [59, 60, 71, 59, 60, 57, 57, 60, 53, 50, 45],
}

suarez_data = {
    'Year': list(range(2010, 2021)),
    'Goals': [24, 9, 19, 29, 13, 30, 37, 26, 25, 19, 14],
    'Games': [29, 31, 32, 28, 27, 34, 35, 34, 35, 33, 23],
}

lewandowski_data = {
    'Year': list(range(2010, 2021)),
    'Goals': [5, 15, 20, 25, 16, 25, 27, 33, 24, 31, 32],
    'Games': [28, 34, 33, 32, 31, 32, 32, 34, 29, 34, 26],
}

benzema_data = {
    'Year': list(range(2010, 2021)),
    'Goals': [4, 22, 17, 15, 17, 18, 17, 9, 9, 27, 17],
    'Games': [29, 32, 34, 32, 32, 28, 26, 30, 36, 37, 34],
}

ronaldo_df = pd.DataFrame(ronaldo_data)
ronaldo_df['Player'] = 'Ronaldo'

messi_df = pd.DataFrame(messi_data)
messi_df['Player'] = 'Messi'

suarez_df = pd.DataFrame(suarez_data)
suarez_df['Player'] = 'Suarez'

lewandowski_df = pd.DataFrame(lewandowski_data)
lewandowski_df['Player'] = 'Lewandowski'

benzema_df = pd.DataFrame(benzema_data)
benzema_df['Player'] = 'Benzema'

def generate_goals_graph(player_name):
    players = {
        'Ronaldo': ronaldo_df,
        'Messi': messi_df,
        'Suarez': suarez_df,
        'Lewandowski': lewandowski_df,
        'Benzema': benzema_df
    }

    if player_name in players:
        player_data = players[player_name]
        plt.figure(figsize=(10, 8))
        plt.plot(player_data['Year'], player_data['Goals'], marker='o')
        plt.xlabel('Year')
        plt.ylabel('Goals')
        plt.title(f"{player_name} Goals per Year")
        plt.grid(True)

        total_goals = player_data['Goals'].sum()
        total_games = player_data['Games'].sum()
        overall_goals_per_game = total_goals / total_games

        x_pos = player_data['Year'].iloc[-1]
        y_pos = player_data['Goals'].iloc[+3]

        plt.text(x_pos, y_pos, f"Average Goals Per Game: {overall_goals_per_game:.2f}", ha='right', va='top', fontsize=10, color='black', bbox=dict(facecolor='white', alpha=0.8))

        plt.show()
    else:
        print("Player not found. Please enter a valid player name.")

player_name = input("Enter player name (Ronaldo, Messi, Suarez, Lewandowski, Benzema): ")
generate_goals_graph(player_name)
