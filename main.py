from flask import Flask, redirect, request
import random, conf, json

#loading redirect links
with open('links.json', 'r', encoding='utf-8') as db:
    links = json.load(db)

#mode 0 = shorten, mode 1 = sketchify
def generate(target, mode):
    if mode:
        #TO-DO: make sketchy string
        pass
    else:
        #mode 0 doesn't support generation of multiple URL's pointing to the same target
        for link, val in links.items():
            if target == val: return (link, False)

        while True:
            output = ''.join(random.choice(conf.chars) for _ in range(conf.rand_size))
            if conf.seed_index:
                random.seed(len(links))
                ind = str(random.random() * 100)
                output = ''.join([ind[0], output, ind[1]])
            #guarentees each string is unique
            if not output in links: break
        return (output, True)

app = Flask(__name__)
application = app # required for passenger_wsgi
@app.route('/geturl')
def geturl():
    target = request.args.get('target', default = 'https://reasons-to.live/', type = str)
    mode = request.args.get('mode', default = 0, type = int)
    data = generate(target, mode)
    link = data[0]
    #only saves if a NEW link has been generated
    if data[1]:
        links[link] = target
        with open('links.json', 'w', encoding='utf-8') as db:
            json.dump(links,db,ensure_ascii=False,indent=4)

    return link

#ghetto 'security'
@app.route('/links.json')
def fuckyou():
    return 'excuse me sir stop poking around', 403

#to be ran on 5hl.pw
@app.route('/<destination>')
def redir(destination):
    if destination in links: return redirect(links[destination])
    return redirect(conf.home_url)

# for testing
if __name__ == '__main__': app.run()