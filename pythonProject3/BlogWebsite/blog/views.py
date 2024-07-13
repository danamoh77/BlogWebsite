from django.http import HttpResponse
from django.template import loader




def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
def users(request):
    template = loader.get_template('users.html')
    return HttpResponse(template.render())

def blogs(request):
    template = loader.get_template('blogs.html')
    return HttpResponse(template.render())
def comments(request):
    template = loader.get_template('comments.html')
    return HttpResponse(template.render())

def categories(request):
    template = loader.get_template('categories.html')
    return HttpResponse(template.render())

def blogdetails(request, blog_id):
    template = loader.get_template('blogdetails.html')
    return HttpResponse(template.render())
