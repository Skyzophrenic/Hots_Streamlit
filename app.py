 
import streamlit as st
import pandas as pd
import random 

stats = pd.read_csv('Copy of Whisper Drafter -6.0 - hero_stats (1).csv')
comforts = pd.read_csv('Copy of Whisper Drafter -6.0 - Player Comforts (4).csv')
matchups = pd.read_csv('Copy of Whisper Drafter -6.0 - hero_data.csv')

# Convert Series to List and insert 'Default' at the start
column_names = ["Hero0", "Hero1", "Hero2", "Hero3", "Hero4"]



names = stats['Hero Name'].tolist()
names.insert(0, 'Default')
options = names

if 'Blue_Heroes' not in globals():
  Blue_Heroes = pd.DataFrame([["Default"]*len(column_names)], columns=column_names)

if 'Red_Heroes' not in globals():
  Red_Heroes = pd.DataFrame([["Default"]*len(column_names)], columns=column_names)




# Set the page config to wide mode
st.set_page_config(layout="wide")

# CSS for custom column backgrounds
st.markdown(
    """
    <style>
        .appview-container .main .block-container {
            padding-top: 3rem;
            padding-bottom: 3rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_default_name(color, index):
  colname = 'Hero' + str(index)
  if color == 'b':
    return Blue_Heroes.at[0, colname]
  else:
    return Red_Heroes.at[0, colname]

red_list = [Red_Heroes.at[0,'Hero0'],Red_Heroes.at[0,'Hero1'],Red_Heroes.at[0,'Hero2'],Red_Heroes.at[0,'Hero3'],Red_Heroes.at[0,'Hero4'],]
# Initialize session state for dropdown values

if 'b1_dropdown' not in st.session_state:
    st.session_state.b1_dropdown = get_default_name('b',0)
    st.session_state.b2_dropdown = get_default_name('b',1)
    st.session_state.b3_dropdown = get_default_name('b',2)
    st.session_state.b4_dropdown = get_default_name('b',3)
    st.session_state.b5_dropdown = get_default_name('b',4)
    st.session_state.r1_dropdown = red_list[0]
    st.session_state.r2_dropdown = red_list[1]
    st.session_state.r3_dropdown = red_list[2]
    st.session_state.r4_dropdown = red_list[3]
    st.session_state.r5_dropdown = red_list[4]

bp1 = ['Default','Default','Default','Default','Default']
bp2 = ['Default','Default','Default','Default','Default']
bp3 = ['Default','Default','Default','Default','Default']
bp4 = ['Default','Default','Default','Default','Default']
bp5 = ['Default','Default','Default','Default','Default']
bps = [bp1,bp2,bp3,bp4,bp5]

rp1 = ['Default','Default','Default','Default','Default']
rp2 = ['Default','Default','Default','Default','Default']
rp3 = ['Default','Default','Default','Default','Default']
rp4 = ['Default','Default','Default','Default','Default']
rp5 = ['Default','Default','Default','Default','Default']
rps = [rp1,rp2,rp3,rp4,rp5]



def get_stat(hero_name, stat):
    if hero_name in stats['Hero Name'].values:
        return stats[stats['Hero Name'] == hero_name][stat].iloc[0]
    else:
        return 0



# Function to be called when a dropdown is updated
def update_stats():
    Blue_Heroes.at[0,'Hero0'] = st.session_state["b1_dropdown"]
    Blue_Heroes.at[0,'Hero1'] = st.session_state["b2_dropdown"]
    Blue_Heroes.at[0,'Hero2'] = st.session_state["b3_dropdown"]
    Blue_Heroes.at[0,'Hero3'] = st.session_state["b4_dropdown"]
    Blue_Heroes.at[0,'Hero4'] = st.session_state["b5_dropdown"]
    
    Red_Heroes.at[0,'Hero0'] = st.session_state["r1_dropdown"]
    Red_Heroes.at[0,'Hero1'] = st.session_state["r2_dropdown"]
    Red_Heroes.at[0,'Hero2'] = st.session_state["r3_dropdown"]
    Red_Heroes.at[0,'Hero3'] = st.session_state["r4_dropdown"]
    Red_Heroes.at[0,'Hero4'] = st.session_state["r5_dropdown"]

    b1 = Blue_Heroes.at[0,'Hero0']
    b2 = Blue_Heroes.at[0,'Hero1']
    b3 = Blue_Heroes.at[0,'Hero2']
    b4 = Blue_Heroes.at[0,'Hero3']
    b5 = Blue_Heroes.at[0,'Hero4']

    r1 = Red_Heroes.at[0,'Hero0']
    r2 = Red_Heroes.at[0,'Hero1']
    r3 = Red_Heroes.at[0,'Hero2']
    r4 = Red_Heroes.at[0,'Hero3']
    r5 = Red_Heroes.at[0,'Hero4']


########
    btotal_fight = sum(get_stat(hero, 'Fight') for hero in [b1, b2, b3, b4, b5])
    btotal_macro = sum(get_stat(hero, 'Macro') for hero in [b1, b2, b3, b4, b5])
    btotal_artill = sum(get_stat(hero, 'Artillery') for hero in [b1, b2, b3, b4, b5])
    btotal_protect = sum(get_stat(hero, 'Protect') for hero in [b1, b2, b3, b4, b5])
    btotal_pick = sum(get_stat(hero, 'Pick') for hero in [b1, b2, b3, b4, b5])

    rtotal_fight = sum(get_stat(hero, 'Fight') for hero in [b1, b2, b3, b4, b5])
    rtotal_macro = sum(get_stat(hero, 'Macro') for hero in [b1, b2, b3, b4, b5])
    rtotal_artill = sum(get_stat(hero, 'Artillery') for hero in [b1, b2, b3, b4, b5])
    rtotal_protect = sum(get_stat(hero, 'Protect') for hero in [b1, b2, b3, b4, b5])
    rtotal_pick = sum(get_stat(hero, 'Pick') for hero in [b1, b2, b3, b4, b5])
#########
    btotal_wave_clear = sum(get_stat(hero, 'Wave Clear') for hero in [b1, b2, b3, b4, b5])
    btotal_engage = sum(get_stat(hero, 'Engage') for hero in [b1, b2, b3, b4, b5])
    btotal_peel = sum(get_stat(hero, 'Peel') for hero in [b1, b2, b3, b4, b5])
    btotal_sustain = sum(get_stat(hero, 'Team-Sustain') for hero in [b1, b2, b3, b4, b5]) + sum(get_stat(hero, 'Self-Sustain') for hero in [b1, b2, b3, b4, b5])

    waveclear_target = 25
    engage_target = 23
    peel_target = 20
    sustain_target = 20

    waveclear_weight = 1 / (btotal_wave_clear / (waveclear_target + .001))
    engage_weight = 1 / (btotal_engage / (engage_target + .001))
    peel_weight = 1 / (btotal_peel / (peel_target + .001))
    sustain_weight = 1 / (btotal_sustain / (sustain_target + .001))

    weights = [waveclear_weight, engage_weight, peel_weight, sustain_weight]
    min_weight = min(weights)
    max_weight = max(weights)

    waveclear_total_weight = (waveclear_weight - min_weight) / (max_weight - min_weight + .001) * (2 - 0.5) + 0.5
    engage_total_weight = (engage_weight - min_weight) / (max_weight - min_weight + .001) * (2 - 0.5) + 0.5
    peel_total_weight = (peel_weight - min_weight) / (max_weight - min_weight + .001) * (2 - 0.5) + 0.5
    sustain_total_weight = (sustain_weight - min_weight) / (max_weight - min_weight + .001) * (2 - 0.5) + 0.5

    player_stats = pd.merge(stats, comforts, on='Hero Name')
    
    running_stats = player_stats.copy()
    running_stats['Fight'] = running_stats['Fight']*(rtotal_macro+rtotal_artill+.01)/(rtotal_protect+rtotal_pick+.01)
    running_stats['Macro'] = running_stats['Macro']*(rtotal_protect+rtotal_artill+.01)/(rtotal_fight+rtotal_pick+.01)
    running_stats['Artillery'] = running_stats['Artillery']*(rtotal_protect+rtotal_pick+.01)/(rtotal_fight+rtotal_macro+.01)
    running_stats['Protect'] = running_stats['Protect']*(rtotal_pick+rtotal_fight+.01)/(rtotal_macro+rtotal_artill+.01)
    running_stats['Pick'] = running_stats['Pick']*(rtotal_macro+rtotal_fight+.01)/(rtotal_protect+rtotal_artill+.01)

    running_stats['Style'] = running_stats['Fight']+ running_stats['Macro'] +running_stats['Artillery']+running_stats['Protect'] +running_stats['Pick'] 


    running_stats['Wave Clear'] = running_stats['Wave Clear'] * waveclear_total_weight
    running_stats['Engage'] = running_stats['Engage'] * engage_total_weight
    running_stats['Peel'] = running_stats['Peel'] * peel_total_weight
    running_stats['Sustain'] = (running_stats['Team-Sustain'] + running_stats['Self-Sustain'] / 4) * sustain_total_weight
    running_stats['Stats Totals'] = running_stats['Wave Clear'] + running_stats['Engage'] + running_stats['Peel'] + running_stats['Sustain'] 
    

    this_matchup = matchups[['hero', 'matchup_hero', 'Pairing Score']].copy()
    this_matchup = this_matchup[this_matchup['matchup_hero'].isin([b1, b2, b3, b4, b5])]
    this_matchup = this_matchup.groupby('hero').agg({'Pairing Score': 'sum'}).reset_index()
    running_stats = pd.merge(running_stats, this_matchup, left_on='Hero Name', right_on='hero', how='left')
    if([b1, b2, b3, b4, b5].count("Default") !=5):
      if([r1, r2, r3, r4, r5].count("Default") !=5):
        counter_stats = matchups[['hero', 'matchup_hero', 'Counter Score']]
        counter_stats = counter_stats[counter_stats['hero'].isin([r1, r2, r3, r4, r5])]
        counter_stats = counter_stats.groupby('matchup_hero').agg({'Counter Score': 'sum'}).reset_index()
        running_stats = pd.merge(running_stats, counter_stats, left_on='Hero Name', right_on='matchup_hero', how='left')
    
        running_stats['Healer Score'] = (running_stats['Pairing Score']*2+running_stats['Counter Score']) * running_stats['Stats Totals'] * ((running_stats['Healer']/5)**3)
        running_stats['Tank Score'] = (running_stats['Pairing Score']*2+running_stats['Counter Score']) * running_stats['Stats Totals'] * ((running_stats['Tank']/5)**3)
        running_stats['Ranged Score'] = (running_stats['Pairing Score']*2+running_stats['Counter Score']) * running_stats['Stats Totals'] * ((running_stats['RangedDPS']/5)**3)
        running_stats['Flex Score'] = (running_stats['Pairing Score']*2+running_stats['Counter Score']) * running_stats['Stats Totals'] * ((running_stats['Flex']/5)**3)
        running_stats['Offlane Score'] = (running_stats['Pairing Score']*2+running_stats['Counter Score']) * running_stats['Stats Totals'] * ((running_stats['Offlane']/5)**3)
      else:
        running_stats['Healer Score'] = (running_stats['Pairing Score']) * running_stats['Stats Totals'] * ((running_stats['Healer']/5)**3)
        running_stats['Tank Score'] = (running_stats['Pairing Score']) * running_stats['Stats Totals'] * ((running_stats['Tank']/5)**3)
        running_stats['Ranged Score'] = (running_stats['Pairing Score']) * running_stats['Stats Totals'] * ((running_stats['RangedDPS']/5)**3)
        running_stats['Flex Score'] = (running_stats['Pairing Score']) * running_stats['Stats Totals'] * ((running_stats['Flex']/5)**3)
        running_stats['Offlane Score'] = (running_stats['Pairing Score']) * running_stats['Stats Totals'] * ((running_stats['Offlane']/5)**3)
    else:
      if([r1, r2, r3, r4, r5].count("Default") !=5):
        counter_stats = matchups[['hero', 'matchup_hero', 'Counter Score']]
        counter_stats = counter_stats[counter_stats['matchup_hero'].isin([r1, r2, r3, r4, r5])]
        counter_stats = counter_stats.groupby('hero').agg({'Counter Score': 'sum'}).reset_index()
        running_stats = pd.merge(running_stats, counter_stats, left_on='Hero Name', right_on='hero', how='left')

        running_stats['Healer Score'] = (running_stats['Counter Score']**0.5) * running_stats['Stats Totals'] * ((running_stats['Healer']/5)**3)
        running_stats['Tank Score'] = (running_stats['Counter Score']**0.5) *running_stats['Stats Totals'] * ((running_stats['Tank']/5)**3)
        running_stats['Ranged Score'] = (running_stats['Counter Score']**0.5) *running_stats['Stats Totals'] * ((running_stats['RangedDPS']/5)**3)
        running_stats['Flex Score'] =(running_stats['Counter Score']**0.5) * running_stats['Stats Totals'] * ((running_stats['Flex']/5)**3)
        running_stats['Offlane Score'] = (running_stats['Counter Score']**0.5) *running_stats['Stats Totals'] * ((running_stats['Offlane']/5)**3)
      else:
        running_stats['Healer Score'] = running_stats['Stats Totals'] * ((running_stats['Healer']/5)**3)
        running_stats['Tank Score'] = running_stats['Stats Totals'] * ((running_stats['Tank']/5)**3)
        running_stats['Ranged Score'] = running_stats['Stats Totals'] * ((running_stats['RangedDPS']/5)**3)
        running_stats['Flex Score'] = running_stats['Stats Totals'] * ((running_stats['Flex']/5)**3)
        running_stats['Offlane Score'] = running_stats['Stats Totals'] * ((running_stats['Offlane']/5)**3)

    ####### ALLY SEGMENT DONE
    ####### PROCESS ENEMY NOW


    

    rtotal_wave_clear = sum(get_stat(hero, 'Wave Clear') for hero in [r1, r2, r3, r4, r5])
    rtotal_engage = sum(get_stat(hero, 'Engage') for hero in [r1, r2, r3, r4, r5])
    rtotal_peel = sum(get_stat(hero, 'Peel') for hero in [r1, r2, r3, r4, r5])
    rtotal_sustain = sum(get_stat(hero, 'Team-Sustain') for hero in [r1, r2, r3, r4, r5]) + sum(get_stat(hero, 'Self-Sustain') for hero in [r1, r2, r3, r4, r5])

    rwaveclear_weight = 1 / (rtotal_wave_clear / (waveclear_target + .001))
    rengage_weight = 1 / (rtotal_engage / (engage_target + .001))
    rpeel_weight = 1 / (rtotal_peel / (peel_target + .001))
    rsustain_weight = 1 / (rtotal_sustain / (sustain_target + .001))

    rweights = [rwaveclear_weight, rengage_weight, rpeel_weight, rsustain_weight]
    rmin_weight = min(rweights)
    rmax_weight = max(rweights)

    rwaveclear_total_weight = (rwaveclear_weight - rmin_weight) / (rmax_weight - rmin_weight + .001) * (2 - 0.5) + 0.5
    rengage_total_weight = (rengage_weight - rmin_weight) / (rmax_weight - rmin_weight + .001) * (2 - 0.5) + 0.5
    rpeel_total_weight = (rpeel_weight - rmin_weight) / (rmax_weight - rmin_weight + .001) * (2 - 0.5) + 0.5
    rsustain_total_weight = (rsustain_weight - rmin_weight) / (rmax_weight - rmin_weight + .001) * (2 - 0.5) + 0.5







    enemy_stats = pd.merge(stats, comforts, on='Hero Name')

    rrunning_stats = enemy_stats.copy()

    rrunning_stats['Wave Clear'] = rrunning_stats['Wave Clear'] * rwaveclear_total_weight
    rrunning_stats['Engage'] = rrunning_stats['Engage'] * rengage_total_weight
    rrunning_stats['Peel'] = rrunning_stats['Peel'] * rpeel_total_weight
    rrunning_stats['Sustain'] = (rrunning_stats['Team-Sustain'] + rrunning_stats['Self-Sustain'] / 4) * rsustain_total_weight
    rrunning_stats['Stats Totals'] = rrunning_stats['Wave Clear'] + rrunning_stats['Engage'] + rrunning_stats['Peel'] + rrunning_stats['Sustain']
    
    rthis_matchup = matchups[['hero', 'matchup_hero', 'Pairing Score']].copy()
    rthis_matchup = rthis_matchup[rthis_matchup['matchup_hero'].isin([r1, r2, r3, r4, r5])]
    rthis_matchup = rthis_matchup.groupby('hero').agg({'Pairing Score': 'sum'}).reset_index()
    rrunning_stats = pd.merge(rrunning_stats, rthis_matchup, left_on='Hero Name', right_on='hero', how='left')

    if([r1, r2, r3, r4, r5].count("Default") !=5):
      if([b1, b2, b3, b4, b5].count("Default") !=5):
        rcounter_stats = matchups[['hero', 'matchup_hero', 'Counter Score']]
        rcounter_stats = rcounter_stats[rcounter_stats['matchup_hero'].isin([b1, b2, b3, b4, b5])]
        rcounter_stats = rcounter_stats.groupby('hero').agg({'Counter Score': 'sum'}).reset_index()
        rrunning_stats = pd.merge(rrunning_stats, rcounter_stats, left_on='Hero Name', right_on='hero', how='left')
    
        rrunning_stats['Healer Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Healer']/5)**3)
        rrunning_stats['Tank Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Tank']/5)**3)
        rrunning_stats['Ranged Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['RangedDPS']/5)**3)
        rrunning_stats['Flex Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Flex']/5)**3)
        rrunning_stats['Offlane Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Offlane']/5)**3)
      else:
        rrunning_stats['Healer Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Healer']/5)**3)
        rrunning_stats['Tank Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Tank']/5)**3)
        rrunning_stats['Ranged Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['RangedDPS']/5)**3)
        rrunning_stats['Flex Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Flex']/5)**3)
        rrunning_stats['Offlane Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Offlane']/5)**3)
    else:
      if([b1, b2, b3, b4, b5].count("Default") !=5):
        rcounter_stats = matchups[['hero', 'matchup_hero', 'Counter Score']]
        rcounter_stats = rcounter_stats[rcounter_stats['hero'].isin([b1, b2, b3, b4, b5])]
        rcounter_stats = rcounter_stats.groupby('matchup_hero').agg({'Counter Score': 'sum'}).reset_index()
        rrunning_stats = pd.merge(rrunning_stats, rcounter_stats, left_on='Hero Name', right_on='matchup_hero', how='left')

        rrunning_stats['Healer Score'] = (rrunning_stats['Counter Score'])*rrunning_stats['Stats Totals'] * ((rrunning_stats['Healer']/5)**3)
        rrunning_stats['Tank Score'] = (rrunning_stats['Counter Score'])*rrunning_stats['Stats Totals'] * ((rrunning_stats['Tank']/5)**3)
        rrunning_stats['Ranged Score'] = (rrunning_stats['Counter Score'])*rrunning_stats['Stats Totals'] * ((rrunning_stats['RangedDPS']/5)**3)
        rrunning_stats['Flex Score'] = (rrunning_stats['Counter Score'])*rrunning_stats['Stats Totals'] * ((rrunning_stats['Flex']/5)**3)
        rrunning_stats['Offlane Score'] = (rrunning_stats['Counter Score'])*rrunning_stats['Stats Totals'] * ((rrunning_stats['Offlane']/5)**3)
      else:
        rrunning_stats['Healer Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['Healer']/5)**3)
        rrunning_stats['Tank Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['Tank']/5)**3)
        rrunning_stats['Ranged Score'] =rrunning_stats['Stats Totals'] * ((rrunning_stats['RangedDPS']/5)**3)
        rrunning_stats['Flex Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['Flex']/5)**3)
        rrunning_stats['Offlane Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['Offlane']/5)**3)


    enemy_role_reqs = pd.read_csv('Copy of Whisper Drafter -6.0 - Enemy Comforts (5).csv')

    #running_stats['Pairing Score'] = [b1, b2, b3, b4, b5]
    bps[0] = running_stats.sort_values(by='Healer Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    bps[1] = running_stats.sort_values(by='Tank Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    bps[2] = running_stats.sort_values(by='Ranged Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    bps[3] = running_stats.sort_values(by='Flex Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    bps[4] = running_stats.sort_values(by='Offlane Score', ascending=False)['Hero Name'].iloc[:5].tolist()

    rps[0] = rrunning_stats.sort_values(by='Healer Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    rps[1] = rrunning_stats.sort_values(by='Tank Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    rps[2] = rrunning_stats.sort_values(by='Ranged Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    rps[3] = rrunning_stats.sort_values(by='Flex Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    rps[4] = rrunning_stats.sort_values(by='Offlane Score', ascending=False)['Hero Name'].iloc[:5].tolist()

update_stats()

def get_bot_pick():
    Blue_Heroes.at[0,'Hero0'] = st.session_state["b1_dropdown"]
    Blue_Heroes.at[0,'Hero1'] = st.session_state["b2_dropdown"]
    Blue_Heroes.at[0,'Hero2'] = st.session_state["b3_dropdown"]
    Blue_Heroes.at[0,'Hero3'] = st.session_state["b4_dropdown"]
    Blue_Heroes.at[0,'Hero4'] = st.session_state["b5_dropdown"]
    
    Red_Heroes.at[0,'Hero0'] = st.session_state["r1_dropdown"]
    Red_Heroes.at[0,'Hero1'] = st.session_state["r2_dropdown"]
    Red_Heroes.at[0,'Hero2'] = st.session_state["r3_dropdown"]
    Red_Heroes.at[0,'Hero3'] = st.session_state["r4_dropdown"]
    Red_Heroes.at[0,'Hero4'] = st.session_state["r5_dropdown"]

    b1 = Blue_Heroes.at[0,'Hero0']
    b2 = Blue_Heroes.at[0,'Hero1']
    b3 = Blue_Heroes.at[0,'Hero2']
    b4 = Blue_Heroes.at[0,'Hero3']
    b5 = Blue_Heroes.at[0,'Hero4']

    r1 = Red_Heroes.at[0,'Hero0']
    r2 = Red_Heroes.at[0,'Hero1']
    r3 = Red_Heroes.at[0,'Hero2']
    r4 = Red_Heroes.at[0,'Hero3']
    r5 = Red_Heroes.at[0,'Hero4']

    already_selected = [st.session_state["b1_dropdown"], st.session_state["b2_dropdown"], st.session_state["b3_dropdown"], st.session_state["b4_dropdown"], st.session_state["b5_dropdown"], st.session_state["r1_dropdown"], st.session_state["r2_dropdown"], st.session_state["r3_dropdown"], st.session_state["r4_dropdown"], st.session_state["r5_dropdown"]]

    waveclear_target = 25
    engage_target = 23
    peel_target = 20
    sustain_target = 20



    rtotal_wave_clear = sum(get_stat(hero, 'Wave Clear') for hero in [r1, r2, r3, r4, r5])
    rtotal_engage = sum(get_stat(hero, 'Engage') for hero in [r1, r2, r3, r4, r5])
    rtotal_peel = sum(get_stat(hero, 'Peel') for hero in [r1, r2, r3, r4, r5])
    rtotal_sustain = sum(get_stat(hero, 'Team-Sustain') for hero in [r1, r2, r3, r4, r5]) + sum(get_stat(hero, 'Self-Sustain') for hero in [r1, r2, r3, r4, r5])

    rwaveclear_weight = 1 / (rtotal_wave_clear / (waveclear_target + .001))
    rengage_weight = 1 / (rtotal_engage / (engage_target + .001))
    rpeel_weight = 1 / (rtotal_peel / (peel_target + .001))
    rsustain_weight = 1 / (rtotal_sustain / (sustain_target + .001))

    rweights = [rwaveclear_weight, rengage_weight, rpeel_weight, rsustain_weight]
    rmin_weight = min(rweights)
    rmax_weight = max(rweights)

    rwaveclear_total_weight = (rwaveclear_weight - rmin_weight) / (rmax_weight - rmin_weight + .001) * (2 - 0.5) + 0.5
    rengage_total_weight = (rengage_weight - rmin_weight) / (rmax_weight - rmin_weight + .001) * (2 - 0.5) + 0.5
    rpeel_total_weight = (rpeel_weight - rmin_weight) / (rmax_weight - rmin_weight + .001) * (2 - 0.5) + 0.5
    rsustain_total_weight = (rsustain_weight - rmin_weight) / (rmax_weight - rmin_weight + .001) * (2 - 0.5) + 0.5







    enemy_stats = pd.merge(stats, comforts, on='Hero Name')

    rrunning_stats = enemy_stats.copy()

    rrunning_stats['Wave Clear'] = rrunning_stats['Wave Clear'] * rwaveclear_total_weight
    rrunning_stats['Engage'] = rrunning_stats['Engage'] * rengage_total_weight
    rrunning_stats['Peel'] = rrunning_stats['Peel'] * rpeel_total_weight
    rrunning_stats['Sustain'] = (rrunning_stats['Team-Sustain'] + rrunning_stats['Self-Sustain'] / 4) * rsustain_total_weight
    rrunning_stats['Stats Totals'] = rrunning_stats['Wave Clear'] + rrunning_stats['Engage'] + rrunning_stats['Peel'] + rrunning_stats['Sustain']
    
    rthis_matchup = matchups[['hero', 'matchup_hero', 'Pairing Score']].copy()
    rthis_matchup = rthis_matchup[rthis_matchup['matchup_hero'].isin([r1, r2, r3, r4, r5])]
    rthis_matchup = rthis_matchup.groupby('hero').agg({'Pairing Score': 'sum'}).reset_index()
    rrunning_stats = pd.merge(rrunning_stats, rthis_matchup, left_on='Hero Name', right_on='hero', how='left')

    if([r1, r2, r3, r4, r5].count("Default") !=5):
      if([b1, b2, b3, b4, b5].count("Default") !=5):
        rcounter_stats = matchups[['hero', 'matchup_hero', 'Counter Score']]
        rcounter_stats = rcounter_stats[rcounter_stats['matchup_hero'].isin([b1, b2, b3, b4, b5])]
        rcounter_stats = rcounter_stats.groupby('hero').agg({'Counter Score': 'sum'}).reset_index()
        rrunning_stats = pd.merge(rrunning_stats, rcounter_stats, left_on='Hero Name', right_on='hero', how='left')
    
        rrunning_stats['Healer Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Healer']/5)**3)
        rrunning_stats['Tank Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Tank']/5)**3)
        rrunning_stats['Ranged Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['RangedDPS']/5)**3)
        rrunning_stats['Flex Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Flex']/5)**3)
        rrunning_stats['Offlane Score'] = (rrunning_stats['Pairing Score']+rrunning_stats['Counter Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Offlane']/5)**3)
      else:
        rrunning_stats['Healer Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Healer']/5)**3)
        rrunning_stats['Tank Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Tank']/5)**3)
        rrunning_stats['Ranged Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['RangedDPS']/5)**3)
        rrunning_stats['Flex Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Flex']/5)**3)
        rrunning_stats['Offlane Score'] = (rrunning_stats['Pairing Score']) * rrunning_stats['Stats Totals'] * ((rrunning_stats['Offlane']/5)**3)
    else:
      rrunning_stats['Healer Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['Healer']/5)**3) 
      rrunning_stats['Tank Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['Tank']/5)**3)
      rrunning_stats['Ranged Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['RangedDPS']/5)**3)
      rrunning_stats['Flex Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['Flex']/5)**3)
      rrunning_stats['Offlane Score'] = rrunning_stats['Stats Totals'] * ((rrunning_stats['Offlane']/5)**3)

    enemy_role_reqs = pd.read_csv('Copy of Whisper Drafter -6.0 - Enemy Comforts (5).csv')

    r_healer = 10-enemy_role_reqs[enemy_role_reqs['Hero Name'].isin([r1,r2,r3,r4,r5])]['Healer'].sum()
    r_tank = 13-enemy_role_reqs[enemy_role_reqs['Hero Name'].isin([r1,r2,r3,r4,r5])]['Tank'].sum()
    r_ranged = 15-enemy_role_reqs[enemy_role_reqs['Hero Name'].isin([r1,r2,r3,r4,r5])]['RangedDPS'].sum()
    r_flex = 18-enemy_role_reqs[enemy_role_reqs['Hero Name'].isin([r1,r2,r3,r4,r5])]['Flex'].sum()
    r_offlane = 13-enemy_role_reqs[enemy_role_reqs['Hero Name'].isin([r1,r2,r3,r4,r5])]['Offlane'].sum()
    roles = [r_healer, r_tank, r_ranged, r_flex, r_offlane]

    r_healer_s = (r_healer - min(roles)) / (max(roles) - min(roles)+.001) * (2-1)+1
    r_tank_s = (r_tank - min(roles)) / (max(roles) - min(roles)+.001) * (2-1)+1
    r_ranged_s = (r_ranged - min(roles)) / (max(roles) - min(roles)+.001) * (2-1)+1
    r_flex_s = (r_flex - min(roles)) / (max(roles) - min(roles)+.001) * (2-1)+1
    r_offlane_s = (r_offlane - min(roles)) / (max(roles) - min(roles)+.001) * (2-1)+1

    first_pick_df = enemy_role_reqs[['Hero Name', 'First Pick']]
    rrunning_stats = pd.merge(rrunning_stats, first_pick_df, on='Hero Name')

    st.write('Healer sum: ', str(r_healer_s))
    st.write('Tank sum: ', str(r_tank_s))
    st.write('Ranged sum: ', str(r_ranged_s))
    st.write('Flex sum: ', str(r_flex_s))
    st.write('Offlane sum: ', str(r_offlane_s))

    rrunning_stats['Healer Score'] = rrunning_stats['Healer Score'] *( r_healer_s) 
    rrunning_stats['Tank Score'] = rrunning_stats['Tank Score'] *( r_tank_s)
    rrunning_stats['Ranged Score'] = rrunning_stats['Ranged Score']* ( r_ranged_s)
    rrunning_stats['Flex Score'] = rrunning_stats['Flex Score'] *( r_flex_s)
    rrunning_stats['Offlane Score'] = rrunning_stats['Offlane Score'] *( r_offlane_s)

    for name in already_selected:
      rrunning_stats.loc[rrunning_stats['Hero Name'] == name, ['Healer Score', 'Tank Score', 'Ranged Score', 'Flex Score', 'Offlane Score']] = 0
    
    if([st.session_state["r1_dropdown"],st.session_state["r2_dropdown"],st.session_state["r3_dropdown"],st.session_state["r4_dropdown"],st.session_state["r5_dropdown"]].count("Default") ==5):
      rrunning_stats['Total Score'] = (rrunning_stats['Healer Score']+rrunning_stats['Tank Score']+rrunning_stats['Ranged Score']+rrunning_stats['Flex Score']+rrunning_stats['Offlane Score'])*rrunning_stats['First Pick'] 
      top3 = rrunning_stats.sort_values(by='Total Score', ascending=False)['Hero Name'].iloc[:5].tolist()
    else:
      rrunning_stats['Total Score'] = rrunning_stats['Healer Score']+rrunning_stats['Tank Score']+rrunning_stats['Ranged Score']+rrunning_stats['Flex Score']+rrunning_stats['Offlane Score']
      top3 = rrunning_stats.sort_values(by='Total Score', ascending=False)['Hero Name'].iloc[:3].tolist()

    my_sel = random.choice(top3)
    if st.session_state.r1_dropdown == 'Default':
      Red_Heroes.at[0,'Hero0'] = my_sel
      st.session_state.r1_dropdown = Red_Heroes.at[0,'Hero0']
    elif st.session_state.r2_dropdown == 'Default':
      Red_Heroes.at[0,'Hero1'] = my_sel
      st.session_state.r2_dropdown = Red_Heroes.at[0,'Hero1']
    elif st.session_state.r3_dropdown == 'Default':
      Red_Heroes.at[0,'Hero2'] = my_sel
      st.session_state.r3_dropdown = Red_Heroes.at[0,'Hero2']
    elif st.session_state.r4_dropdown == 'Default':
      Red_Heroes.at[0,'Hero3'] = my_sel
      st.session_state.r4_dropdown = Red_Heroes.at[0,'Hero3']
    elif st.session_state.r5_dropdown == 'Default':
      Red_Heroes.at[0,'Hero4'] = my_sel
      st.session_state.r5_dropdown = Red_Heroes.at[0,'Hero4']







# Function to display dropdown and image


# Function to display dropdown and image
def dropdown_with_image(col, idx, side):
    value = 0
    colname = 'Hero'+str(idx)
    if side == 'r':
      value = options.index(Red_Heroes.at[0,colname])
    else:
      value = options.index(Blue_Heroes.at[0,colname])
    selection = col.selectbox(
        f"{side}{idx+1}", 
        options, 
        key=f"{side}{idx+1}_dropdown", 
        on_change=update_stats
    )
    image_path = update_image_path(selection)
    col.image(image_path, use_column_width=True)
    return selection

def update_image_path(hero_name):
    return f'Hero_Pics/{hero_name}_Hero_Portrait.png'


# Create blue, center, and red sections
global blue, center, red
blue, center, red = st.columns([5, 2, 5])

def reset_dropdowns():
    st.write(st.session_state.values)

# Center section
with center:
    if st.button('Bot Pick', use_container_width=True):
      st.write('0')
      get_bot_pick()
      st.write('Dropdowns updated to Default')
    st.write('2')
    map = st.selectbox("map", ("Infernal_Shrines", "Towers_of_Doom", "Tomb_of_the_Spider_Queen"))
    map_picture = st.image(f'Map_Pics/{map}.webp')
    st.write('3')

with blue:
  global b_columns
  b_columns = st.columns(5)
  global b_selections
  b_selections = [dropdown_with_image(col, i, "b") for i, col in enumerate(b_columns)]
  for n, col in enumerate(b_columns):
      with col:
          for i in range(5):
              path = update_image_path(bps[n][i])
              st.image(path, width=100)

# Create red section with 5 dropdowns and images
with red:
    global r_columns
    r_columns = st.columns(5)
    global r_selections
    r_selections = [dropdown_with_image(col, i, "r") for i, col in enumerate(r_columns)]
    for n, col in enumerate(r_columns):
        with col:
            for i in range(5):
                path = update_image_path(rps[n][i])
                st.image(path, width=100)
#r_columns = [st.empty() for i, col in enumerate(r_columns)]




# Display the updated stats below the dropdowns


update_stats()

















