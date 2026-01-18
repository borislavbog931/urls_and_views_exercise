from django.shortcuts import render, get_object_or_404

from review.models import Review

DEFAULT_REVIEW_COUNT = 5

def recent_reviews(request):
    review_count = request.GET.get('review_count', default=DEFAULT_REVIEW_COUNT)
    reviews = Review.objects.filter(is_published = True).order_by('-created_at')[:int(review_count)]
    context = {'reviews': reviews,
               'page_title': 'Recent Reviews'}
    return render (request, 'review/list.html', context)


def review_detail(request, pk:int):
    review = get_object_or_404(Review, pk=pk)
    context = {'review': review,
               'page_title': f'{review.author}\'s Review on {review.destination.name}'}
    return render(request, 'review/detail.html', context)

def reviews_by_year(request, year:int):
    reviews = Review.objects.filter(created_at__year= year)
    context = {'reviews': reviews,
               'page_title': f'Reviews from {year}'}
    return render(request, 'review/list.html', context)