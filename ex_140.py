class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, router):
        self.path = path
        self.router = router

    def __call__(self, func):
        self.router.add_callback(self.path, func)
        return func


@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)