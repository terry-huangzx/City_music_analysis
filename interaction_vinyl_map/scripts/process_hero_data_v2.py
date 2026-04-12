"""Process setlist.fm CSVs into slim JSON with genre assignments for hero viz."""
import pandas as pd, json, os, glob, random

random.seed(42)

data_dir = 'City_music_analysis/setfim_data'
files = sorted(glob.glob(os.path.join(data_dir, '*.csv')))

all_dfs = []
for f in files:
    df = pd.read_csv(f, low_memory=False)
    if len(df) > 0:
        all_dfs.append(df)

df = pd.concat(all_dfs, ignore_index=True)
df['event_date'] = pd.to_datetime(df['event_date'], errors='coerce')
df = df.dropna(subset=['event_date','city_name','artist_name'])
df['month'] = df['event_date'].dt.month

metro = {
    'Toronto': {'lat':43.7,'lon':-79.4,'cities':['Toronto','Mississauga','Oshawa','Pickering','Brampton','Oakville','Markham','Richmond Hill','Vaughan','Ajax','Aurora','Newmarket','Milton','Whitby','Caledon','Thornhill']},
    'Montreal': {'lat':45.5,'lon':-73.6,'cities':['Montreal','Laval','Brossard','Boucherville','Longueuil','Montreal-Est']},
    'Vancouver': {'lat':49.25,'lon':-123.1,'cities':['Vancouver','New Westminster','Surrey','Burnaby','Coquitlam','North Vancouver','West Vancouver','Delta','Langley','Abbotsford','Maple Ridge','Port Moody','White Rock','Richmond']},
    'Calgary': {'lat':51.05,'lon':-114.07,'cities':['Calgary','Airdrie','Cochrane']},
    'Ottawa': {'lat':45.42,'lon':-75.69,'cities':['Ottawa','Gatineau','Carleton Place','Navan','Carp']},
    'New York': {'lat':40.71,'lon':-74.0,'cities':['New York','Brooklyn','Queens','Staten Island','The Bronx','Jersey City','Hoboken','Newark','Yonkers','Bayonne','Weehawken','Secaucus','East Rutherford','Rutherford','Teaneck','Hackensack','Bergenfield','Little Ferry','North Arlington','Clifton','Passaic','Paterson','Kearny','Harrison','Carlstadt','Lyndhurst','Garwood','Elmont','Sayreville','Edison','Metuchen','Dunellen','Port Washington','New Rochelle','Elmsford']},
    'Los Angeles': {'lat':34.05,'lon':-118.24,'cities':['Los Angeles','West Hollywood','Hollywood','Long Beach','Inglewood','Anaheim','Pasadena','Santa Ana','Pomona','Santa Monica','Burbank','Glendale','Culver City','Malibu','Venice','Beverly Hills','Huntington Beach','Fullerton','Garden Grove','Cerritos','Downey','Universal City','San Pedro','Agoura Hills','Topanga','Calabasas','Westlake Village','Thousand Oaks','San Fernando','Hermosa Beach','Redondo Beach','South Pasadena','Eagle Rock','San Dimas','Seal Beach','Santa Clarita','Rancho Palos Verdes','Marina del Rey','Alhambra','Huntington Park','Claremont','Montclair','Lawndale','Hawthorne','Gardena','Ontario','Fontana','Rancho Cucamonga','Upland','Maywood','Mount Washington','Boyle Heights','East Los Angeles','Northridge','Westwood','Century City','San Gabriel','Monterey Park','Pico Rivera','Torrance','Glendora','Commerce','Covina','Chino','Arcadia','Brea','Bellflower','Compton','Norwalk','Azusa','Norco','Riverside','Santa Fe Springs','Moorpark','Fountain Valley','La Mirada']},
    'Chicago': {'lat':41.85,'lon':-87.65,'cities':['Chicago','Evanston','Joliet','Des Plaines','Skokie','West Chicago','Tinley Park','Bridgeview','Rosemont','Highland Park','Berwyn','Forest Park','Naperville','Lisle','Downers Grove','Mundelein','Libertyville','Batavia','Schaumburg','Hoffman Estates','Arlington Heights','Elmhurst','Bolingbrook','Lemont','West Dundee','Highwood','Brookfield','Oak Forest','Wheaton','Lansing','Villa Park','Addison','Darien','Mokena','Frankfort','Vernon Hills','Palatine','Orland Park','Bartlett','Winnetka','Norridge','Lombard','Streamwood','Park Forest','Palos Hills','River Forest','Wheeling','Northbrook','Oakbrook Terrace','Mount Prospect','Oak Lawn','Niles','South Barrington','Glen Ellyn','Elmwood Park','Carol Stream','Willow Springs','Merrionette Park','Country Club Hills','Hammond','La Grange']},
    'Detroit': {'lat':42.33,'lon':-83.05,'cities':['Detroit','Hamtramck','Ferndale','Royal Oak','Pontiac','Clarkston','Sterling Heights','Westland','Wyandotte','Melvindale','Berkley','Hazel Park','Clinton Township','Rochester Hills','Lake Orion','Milford','Chesterfield Township','Taylor','Warren','Dearborn','Canton','Plymouth','Rochester','Grosse Pointe','Romulus','Novi','Northville','Livonia','River Rouge','Farmington','Lincoln Park']},
    'Las Vegas': {'lat':36.17,'lon':-115.14,'cities':['Las Vegas','Henderson','North Las Vegas','Moapa','East Las Vegas']},
    'Miami': {'lat':25.77,'lon':-80.19,'cities':['Miami','Miami Beach','Miami Gardens','North Miami Beach','North Miami','Coral Gables','Hallandale Beach','Cutler Bay','Doral','Aventura','Miami Springs','Miramar','Hialeah','Pembroke Pines','Kendall']},
    'San Francisco': {'lat':37.77,'lon':-122.42,'cities':['San Francisco','Daly City','Menlo Park','Novato','Mill Valley','Pacifica','San Rafael','Redwood City','San Mateo','Corte Madera','Half Moon Bay','Bolinas','Nicasio','Woodside','Ross','Burlingame']},
    'Washington': {'lat':38.90,'lon':-77.04,'cities':['Washington','Silver Spring','Alexandria','Arlington','Falls Church','Tysons Corner','Fairfax','Bristow','North Bethesda','Bethesda','Reston','Manassas','College Park','Hyattsville','Takoma Park','Cheverly','Beltsville','Landover','Bladensburg','University Park','Chevy Chase','Sterling','McLean','Englewood','Vienna','West Springfield']},
}

# Genre distributions per city (same as original prototype)
GENRE_DIST = {
    'Toronto':       {'Rock':.22,'Pop':.20,'Hip-Hop':.18,'Jazz':.08,'Classical':.05,'EDM':.12,'Country':.05,'R&B':.10},
    'Montreal':      {'Rock':.18,'Pop':.15,'Hip-Hop':.12,'Jazz':.20,'Classical':.10,'EDM':.10,'Country':.03,'R&B':.12},
    'Vancouver':     {'Rock':.20,'Pop':.22,'Hip-Hop':.15,'Jazz':.06,'Classical':.04,'EDM':.18,'Country':.06,'R&B':.09},
    'Calgary':       {'Rock':.25,'Pop':.15,'Hip-Hop':.10,'Jazz':.05,'Classical':.05,'EDM':.10,'Country':.22,'R&B':.08},
    'Ottawa':        {'Rock':.20,'Pop':.18,'Hip-Hop':.12,'Jazz':.10,'Classical':.12,'EDM':.10,'Country':.08,'R&B':.10},
    'New York':      {'Rock':.15,'Pop':.18,'Hip-Hop':.22,'Jazz':.12,'Classical':.08,'EDM':.08,'Country':.02,'R&B':.15},
    'Los Angeles':   {'Rock':.14,'Pop':.25,'Hip-Hop':.20,'Jazz':.05,'Classical':.03,'EDM':.15,'Country':.04,'R&B':.14},
    'Chicago':       {'Rock':.16,'Pop':.14,'Hip-Hop':.18,'Jazz':.18,'Classical':.06,'EDM':.10,'Country':.06,'R&B':.12},
    'Detroit':       {'Rock':.18,'Pop':.12,'Hip-Hop':.20,'Jazz':.08,'Classical':.04,'EDM':.14,'Country':.04,'R&B':.20},
    'Las Vegas':     {'Rock':.15,'Pop':.25,'Hip-Hop':.12,'Jazz':.05,'Classical':.05,'EDM':.20,'Country':.08,'R&B':.10},
    'Miami':         {'Rock':.08,'Pop':.20,'Hip-Hop':.18,'Jazz':.05,'Classical':.03,'EDM':.18,'Country':.03,'R&B':.25},
    'San Francisco': {'Rock':.22,'Pop':.18,'Hip-Hop':.12,'Jazz':.10,'Classical':.06,'EDM':.16,'Country':.04,'R&B':.12},
    'Washington':    {'Rock':.16,'Pop':.16,'Hip-Hop':.18,'Jazz':.12,'Classical':.10,'EDM':.10,'Country':.06,'R&B':.12},
}

GENRES = ['Rock','Pop','Hip-Hop','Jazz','Classical','EDM','Country','R&B']

def assign_genre(city):
    dist = GENRE_DIST.get(city, GENRE_DIST['New York'])
    r = random.random()
    cum = 0
    for g in GENRES:
        cum += dist[g]
        if r <= cum:
            return g
    return 'Rock'

city_to_metro = {}
for m, info in metro.items():
    for c in info['cities']:
        city_to_metro[c] = m

df['metro'] = df['city_name'].map(city_to_metro)
df = df.dropna(subset=['metro'])

result = {}
for m, info in metro.items():
    mdf = df[df['metro'] == m]
    if len(mdf) == 0:
        continue

    # Genre distribution (from our predefined)
    gd = GENRE_DIST.get(m, GENRE_DIST['New York'])

    # Top 8 venues
    tv = mdf['venue_name'].value_counts().head(8)
    top_venues = [[k, int(v)] for k, v in tv.items()]

    # Top 10 artists
    ta = mdf['artist_name'].value_counts().head(10)
    top_artists = [[k, int(v)] for k, v in ta.items()]

    # Sample events — 120 per city, with genre assigned
    sample_n = min(120, len(mdf))
    sampled = mdf.sample(n=sample_n, random_state=42)
    events = []
    for _, r_row in sampled.iterrows():
        g = assign_genre(m)
        events.append([
            r_row['artist_name'][:40],
            r_row['venue_name'][:40],
            r_row['event_date'].strftime('%m-%d'),
            g,
        ])

    result[m] = {
        'a': info['lat'],
        'o': info['lon'],
        'e': len(mdf),
        'v': mdf['venue_name'].nunique(),
        'r': mdf['artist_name'].nunique(),
        'gd': gd,
        'tv': top_venues,
        'ta': top_artists,
        's': events,
    }

compact = json.dumps(result, ensure_ascii=False, separators=(',', ':'))
with open('api/hero_data_v2.json', 'w', encoding='utf-8') as f:
    f.write(compact)

print(f'JSON size: {len(compact)} chars ({len(compact)/1024:.1f} KB)')
for m, d in result.items():
    print(f'  {m}: {d["e"]} events, sample={len(d["s"])}')
