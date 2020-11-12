from django.shortcuts import render
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# POSTS VIEW ENDPOINT
def posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    paginator = Paginator(response, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'blog-listing.html', {'response': paged_listings })


# POST DETAILS VIEW ENDPOINT
def post_details(request, post_id):
    post = requests.get('https://jsonplaceholder.typicode.com/posts/'+ str(post_id)).json()
    comments = requests.get('https://jsonplaceholder.typicode.com/posts/{0}/comments'.format(post_id)).json()
    return render(request, 'blog-post.html', {'post': post, 'comments': comments})
