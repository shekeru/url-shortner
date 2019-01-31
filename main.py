from flask import Flask, redirect, request
import random, conf, json

#loading redirect links
with open('links.json', 'r', encoding='utf-8') as db:
    links = json.load(db)

#mode 0 = shorten, mode 1 = sketchify
def generate(target, preview, mode):
    if mode:
        #TO-DO: make sketchy string
        pass
    else:
        #mode 0 doesn't support generation of multiple URL's pointing to the same target
        for link, vals in links.items():
            if target == vals[0] and preview == vals[1]: return (link, False)

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
application = app #required for passenger_wsgi
#example: reasons-to.live/geturl?target=doin-your.mom&preview=1&mode=0
@app.route('/geturl')
def geturl():
    target = request.args.get('target', default = 'https://reasons-to.live/', type = str)
    preview = request.args.get('preview', default = 0, type = int)
    mode = request.args.get('mode', default = 0, type = int)
    #easier to do this on the backend tbh
    if not 'http://' or not 'https://' in target:
        target = ''.join(['http://', target])

    data = generate(target, preview, mode)
    link = data[0]
    #only saves if a NEW link has been generated
    if data[1]:
        links[link] = [target, preview]
        with open('links.json', 'w', encoding='utf-8') as db:
            json.dump(links,db,ensure_ascii=False,indent=4)

    return ''.join(['5hl.pw/', link])

#ghetto 'security'
@app.route('/links.json')
def fuckyou():
    return 'excuse me sir stop poking around', 403

@app.route('/<destination>')
def redir(destination):
    if not destination in links: return redirect(conf.home_url)
    data = links[destination]
    #checks if preview is true or false
    if data[1]: return redirect(data[0])
    #sneaky JS redirect so it can't be previewed as easily
    return ''.join(['<html><head><script>window.location="', data[0], '"</script></head></html>'])
        
# for testing
if __name__ == '__main__': app.run()