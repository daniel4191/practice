from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image':'books1.jpeg',
        'author' : 'Daniel',
        'date': date(2022, 10, 19),
        'title' : 'Mountain Hiking',
        'excerpt': 'when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries',
        'content': '''
        but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

        but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

        but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
        '''
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    # 날자를 가지기 위해서 -3으로 슬라이드 해준것
    latest_posts = sorted_posts[-3:]
    # templates는 settings에서 등록이 되어있기에 생략이 가능하다.
    return render(request, 'blog/index.html',{
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })