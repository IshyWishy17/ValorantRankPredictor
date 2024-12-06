import csv

def find_rank(soup):
    '''
    Finds the rank from the parsed HTML soup
    '''
    spans = soup.find_all("span", {"class": "stat__label"})
    for span in spans:
        if span.text == 'Rating':
            return span.find_next_sibling("span").text
        
def find_highlighted_stats(soup):
    '''
    Finds the mentioned stats from the parsed HTML soup
    '''
    spans = soup.find_all("span", {"class": "value", "data-v-01072c71": ""})
    res = {}
    stat_idx = 0
    stat_names = ['Damage/Round', 'K/D Ratio', 'Headshot %', 'Win %',\
                'Wins', 'KAST', 'DDΔ/Round', 'Kills', 'Deaths', 'Assists',\
                'ACS', 'KAD Ratio', 'Kills/Round', 'First Bloods',\
                'Flawless Rounds', 'Aces']
    for span in spans[3:]:
        res[stat_names[stat_idx]] = span.text
        stat_idx+= 1
    return res

def should_stop(rank_counts):
    '''
    Specifies the stopping condition
    '''
    return all(rank_count == 5000 for rank_count in rank_counts.values())

def write_to_stats_csv(stats, rank):
    '''
    Writes a single player's stats as a row, after removing commas and percentage symbols.
    '''
    with open('stats.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        stats = [stat.replace('%', '').replace(',', '') for stat in stats.values()]
        writer.writerow(stats + [rank])
