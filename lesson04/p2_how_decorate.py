# 用在哪里

# 注册
@route('index',methods=['GET','POST'])
def static_html():
    return  render_templete('index.html')

# 等效于
static_html = route('index',methods=['GET','POST'])(static_html)


def route(rule, **options):
    def decorator(f):
        endpoint = options.pop("endpoint", None)
        # 使用类似字典的结构以'index'为key 以 method static_html  其他参数为value存储绑定关系
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator

