import random, string, urllib

swaps = {
    'e': '3',
    'i': '1',
    'o': '0',
}

drugs = [
    'designer',
    'smoke',
    'pipe',
    'insufflated',
    'krokodil',
    'injected',
    'research',
    'chemical',
    'silk road',
    'bitcoin',
    'pharma',
    'black tar',
    'xanax',
    'ritalin',
    'adderall',
    'fentanyl',
    'coke',
    'crack',
    'cocaine',
    'discount',
    'heroin',
    'viagra',
    'shrooms',
    'lsd',
    'meth',
    'pills',
    '6-apb',
    '2-fma',
    'pcp',
    'wax',
    'ice'
]

legal = [
    'syria',
    'isis',
    'border',
    'government',
    'secret',
    'hidden',
    'snowden',
    'illegal',
    'mexican',
    'russian',
    'crypto',
    'nasa',
    'putin',
    'nsa',
    'fbi',
    'iran',
    'bomb',
    'president',
    'kill',
    'bombs',
    'terrorist',
    'sweden',
    'somali',
    'attack',
    'hostage',
    'airline',
    'threat',
]

hentai = [
    'blacked',
    'creampie',
    'mindbreak',
    'bondage',
    'lolicon',
    'shota',
    'hentai',
    'child porn',
    'free porn',
    'bukkake',
    'underage',
    'jailbait',
    'hebe',
    'teen',
    'bondage',
    'hardcore',
    'extreme',
    'violent',
    'anal',
    'rape',
    'twink',
    'gay',
    'bdsm',
    'gagged',
    'dildo',
    'cuckold',
    'femdom',
    'vore',
    'furry',
    'scat',
]

tech = [
    'piratebay',
    'darknet',
    'onion',
    'download',
    'sh',
    'ru',
    'exe',
    'tor',
    'download',
    'executable',
    'keylogger',
    'backtrack',
    'virus',
    'trojan',
    'trojan',
    'payload',
    'application',
    'overflow',
    'tracker',
    'account',
    'torrent',
    'bypass',
    'install',
    'setup',
    'hack',
    'exploit',
    'mp3.exe',
    'robot',
]

normie = [
    'league of legends',
    'minecraft',
    'anti virus',
    'automatic',
    'direct',
    'computer',
    'streaming',
    'music',
    'easy',
    'bootleg',
    'facebook',
    'malicious',
    'signup',
    'forum',
    'hacker',
    'netflix',
    'loser',
    'retard',
    'free',
    'cheap',
    'tv',
    'http',
    'html',
    'php',
    'lol',
]

words = normie + tech + hentai + legal + drugs
chars = (
    '-_' * 8 +
    '+.' * 6 +
    '~' * 4 +
    ';!,'
)

def generate():
    url, past = "", set()
    for i in range(6):
        sel = random.choice(words)
        if sel not in past and random.random() <= 0.85:
            url += urllib.parse.quote(sel)
            past.add(sel)
        else:
            url += ''.join([random.choice(string.ascii_lowercase
                + string.digits) for _ in range(4)])
        if i < 5:
            url += random.choice(chars)
    for x in swaps:
        if x in url and random.random() <= 0.15:
            n = random.choice([i for i, c in enumerate(url) if c == x])
            url = url[:n] + swaps[x] + url[n+1:]
            break
    return url

# for _ in range(20):
#     new = generate()
#     print(len(new), new)
