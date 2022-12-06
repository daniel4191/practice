# views는 기본적으로 app단위의 템플릿과 모델을 연결해주는 다리와도 같은 개념으로 작용한다.
# views, models, templates가 연결이 되어야 비로소 프로젝트 단위에서 사용이 가능한 app으로 구성이 된다.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# 여기에서 설정된 함수들이 결과적으로는 return 이라는 곳에 뿌려진다.
# request는 일종의 '열쇠'의 개념이고, 다음으로 나오는 ~~html은 연결하고자 하는 페이지, 그 다음에 쓰이는 딕셔너리는
# 큰 틀에서 연결된 html에 딕셔너리 데이터를 보내주는 역할을 한다.
# views에서 클래스나 함수를 등록하고 나서는 app단위의 urls에 등록을 해주고, 그 다음으로는 프로젝트 단위의 urls에 등록을 해줘야한다.

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})

def photo_post(request):
    # 요청온 방식이 POST라는것은 누군가 글등록을 했다는 말이다. (게시판의 글 등록기능)
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        # form이 유효하다 라는 뜻은 models에서 정의된 fields의 요구대로 모두 들어왔음을 의미한다. (form.is_valid())
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            # 여기서의 photo_detail은 app단위의 urls.py에서 정의된 name이다. 그 name에 부여된 곳으로 되돌아 간다는 의미다.
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_post.html', {'form':form})

def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)    
    else:
        form = PhotoForm(instance=photo)
    
    return render(request, 'photo/photo_post.html', {'form':form})
        