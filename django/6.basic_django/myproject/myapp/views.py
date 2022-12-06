from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''

# ()안에는 여러가지 자료가 들어오게 되어있다. 일종의 **kwargs과 같은 개념인것같다
# 그리고 request든 뭐든 써도 사실상 기능엔 동일한 효과를 미치지만, request라고 보편적으로 써준다고 한다.
def index(request):
    # 방법1
    # 페이지를 출력할 때마다 랜덤한 숫자를 추가해준다. 하지만 str으로 씌우지 않으면
    # python에서는 str + int는 사용이 되지 않기 때문에 str으로 씌워준다.
    # return HttpResponse('<h1>Random</h1>' + str(random.random()))
    article = '''
    <h2>Welcome</h2> 
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        # 만약에 read에 사용된 id인자가 topic내부에 있는 id값과 같다면
        # 그리고 받아온 id인자는 다시 int로 감싸주어야한다. 이유는 topic에서 지정된
        # id는 int지만, read에서 인자로 쓰이는 id는 마지막 과정인 HTMLTemplate
        # 속에 들어가서 나오는 과정 속에서 str으로 타입이 변환되게 된다. (출력을 위해서)
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    global nextId
    # 원하는 path로 전달하기 위해서 form태그로 감싸준 것이다.
    # method방식을 post로 설정한 이유는, create페이지의 경우에는 이 설정을 안하게되면
    # 각 입력값마다 url이 부여되는데, 그러면 추후 해당 링크로 들어오는 사람의 수만큼 추가로 중복데이터가 증가되기 때문에
    # 이를 방지하기 위해서 써준다.
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)
        nextId = nextId + 1
        return redirect(url)

@csrf_exempt
def update(request,id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')



@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')