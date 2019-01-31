from flask import Flask, redirect
import random, conf
#TO-DO: load links from save medium
links = {}

#mode 0 = shorten, mode 1 = sketchify
def generate(mode):
    if mode:
        #TO-DO: make sketchy string
    else:
        while True:
            output = ''.join(random.choice(conf.chars) for _ in range(conf.rand_size))
            if conf.seed_index:
                random.seed(len(links))
                ind = str(random.random() * 100)
                output = ''.join([ind[0], output, ind[1]])
            #guarentees each string is unique
            if not output in links: break
        return output

app = Flask(__name__)
application = app # required for passenger_wsgi
@app.route('/geturl&target=<target>&mode=<mode>')
def geturl():
    if target is None:
        return 'invalid target!'
    try: mode = int(mode)
    except: return 'invalid mode!'
    link = generate(mode)
    links[link] = target
    #TO-DO: save links either to SQL or JSON or some other thing
    return link

#to be ran on 5hl.pw
@app.route('/<destination>')
def redir(destination):
    if destination in links: return redirect(links[destination])
    return redirect(conf.home_url)

# for testing
if __name__ == '__main__': app.run()