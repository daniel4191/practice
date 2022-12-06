from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core import validators
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def full_address(self):
        return f"{self.postal_code} {self.city} {self.street}"

    def __str__(self):
        return self.full_address()

    # admin 페이지 상에서 카테고리 명을 꾸며준다.
    class Meta:

        # 복수(2개 이상)
        verbose_name_plural = 'Address Entries'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # 확실하게 여기서 뿐만이 아니라 null=True를 해줘야
    # This is because the database needs something to populate existing rows.
    # 유형의 에러가 안뜬다.

    # 더불어서 address에 OneToOneField를 먹여줬기때문에, 한번 사용중인 주소는 다른 곳에서 사용할 수 없다.
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    # 여기서 만들어준 함수를 아래의 __str__에 활용해준다.
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    # null=True, default=False를 입력하기 전에는 makemigrations를 하는데 있어서
    # prompt가 떴었다. 하지만 지금은 생성이 된다.
    # 한번의 makemigrations마다 migrations 폴더 안에 0001, 0002 이런식으로 늘어가는 것 같다.
    # author = models.CharField(null=True, max_length=100)

    # on_delete는 Foreignkey를 쓸때 사용되며 어느 하나가 죽으면 함께 죽는 개념으로 연결하기 위해 사용된다고 보면 된다.
    # on_delete의 값으로 models.CASCADE로 하면 함께 삭제가 되는거고, 만약 PROTECT로 설정한다면, 삭제한것만 사라지게 된다.
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestseller = models.BooleanField(default=False)

    # Harry Potter 1 => harry-potter-1
    # blank=True를 해줌으로써 관리자페이지에서 빈값 이어도 받아들여지게 설정했다.
    # editable=False를 해줌으로써 관리자페이지에서 아예 slug 값 입력 필드를 삭제했다.
    # 왜냐하면 지금 여기의 설정 만으로도 title을 토대로 자동 생성되니깐.
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, null=False)

    def get_absolute_url(self):
        # 여기의 book_detail도 app 단위의 urls에서 지정된 name으로 부터 비롯되었다.
        return reverse('book_detail', args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
