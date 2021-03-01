from django.shortcuts import render

posts = [
  {
    'author': 'Rickesh Khilnani',
    'title': 'Im a dog',
    'content': 'First',
    "date_posted": 'August 27, 2020'
  },
  {
    'author': 'Corey in the House',
    'title': 'Im Corey',
    'content': 'Second omegalul',
    "date_posted": 'August 28, 2020'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)


def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})