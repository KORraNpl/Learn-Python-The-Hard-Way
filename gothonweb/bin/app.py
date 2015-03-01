import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        greeting = None
        return render.foo()

if __name__ == "__main__":
    app.run()
