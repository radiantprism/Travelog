from django.db import models

# Create your models here.

class Attraction(models.Model):
    #id는 TripAdvisor의 장소 id.
    id = models.IntegerField()
    #name은 TripAdvisor의 관광장소의 이름.
    name = models.CharField(max_length = 200)
    # star는 트립어드바이저의 별점에 10을 곱한 수
    star = models.IntegerField()
    #cat1, 2는 TourAPI의 대분류, 중분류를 사용함.
    cat1 = models.CharField(max_length = 100)
    cat2 = models.CharField(max_length = 100)
    #type은 TripAdvisor의 분류 타입을 사용함.
    type = models.CharField(max_length = 50)
    #url는 
    url = models.URLField('', max_length = 400, blank = True)
    #image는 TourAPI에서 나오는 사진 or 개별적으로 구한 사진
    image = models.ImageField(upload_to = '', blank = True)
    #id는 트립어드바이저의 id
    #id_trip = models.CharField(max_length = 100)
    #id_tour = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Review(models.Model):
    #여행장소 하나당 리뷰가 0개부터 2개 이상이므로,
    attraction = models.ForeignKey(Attraction, on_delete = models.CASCADE)
    #리뷰 내용은 TextField로
    content = models.TextField()
