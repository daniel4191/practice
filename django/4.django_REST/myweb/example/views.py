from this import d
from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

'''
# @가 붙는 것을 '데코레이터'라고 하는데, 함수를 감싸서 다른 곳과 연결시키는 기능을 한다.
# 보통의 경우에 API로써 기능하고 싶을때 사용된다.

# 이거는 FBV - function based views
@api_view(['GET'])
def HelloAPI(request):
    return Response('hello, world')


# 이거는 CBV - class based views
class HelloAPI(APIView):
    def get(self, request):
        return Response('hello, world')

# 위의 FBV와 CBV는 형태가 다르지만 동일한 기능을 가지고 있다.
'''


# FBV 버전

@api_view(['GET'])
def HelloAPI(request):
    return Response('hello, world')


@api_view(['GET', 'POST']) # GET/POST 요청을 처리하게 만들어주는 데코레이터
def booksAPI(request):      # /book/
    if request.method == 'GET': # GET 요청(도서 전체 정보)
        books = Book.objects.all() # Book 모델로 부터 전체 데이터 가져오기
        serializer = BookSerializer(books, many=True) # 시리얼라이저에 전체 데이터를 한번에 집어넣기 (직렬화, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) # return Response
    
    elif request.method == 'POST': # POST 요청(도서 정보 등록)
        serializer = BookSerializer(data=request.data) # POST 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        if serializer.is_valid(): # 유효한 데이터라면
            serializer.save() # 시리얼라이저의 역직렬화를 통해 save(), 모델 시리얼라이저의 기본 create()함수가 동작
            return Response(serializer.data, status = status.HTTP_201_CREATED)  # 201 메세지를 보내며 성공
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) # 잘못된 요청

@api_view(['GET'])
def bookAPI(request, bid): # /book/bid/
    book = get_object_or_404(Book, bid = bid) # bid = id 인 데이터를 Book에서 가져오고, 없으면 404에러
    serializer = BookSerializer(book) # 시리얼라이저에 데이터를 집어넣기(직렬화)
    return Response(serializer.data, status=status.HTTP_200_OK) # return Response


# CBV 버전

class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status = status.HTTP_200_OK)

# 도서 정보 API mixins

class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs): # GET 메소드 처리 함수(전체 함수)
        return self.list(request, *args, **kwargs) # mixins.ListModelMixin과 연결
    
    def post(self, request, *args, **kwargs): # POST 메소드 처리 함수
        return self.create(request, *args, **kwargs) # mixins.CreateModelMixin과 연결

class BookAPIMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "bid"  # 이미 django 기본모델인 pk가 아니라 bid를 pk로 사용하고 있으니 이것으로 lookup_field에 설정한다.
    
    def get(self, request, *args, **kwargs):    # GET 메소드 처리 함수 
        return self.retrieve(request, *args, **kwargs) # mixins.RetrieveModelMixin과 연결
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) # mixins.UpdateModelMixin과 연결
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) # minxins.DestroyModelMixin과 연결

# generics 영역

class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'