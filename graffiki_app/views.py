from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import CommentForm, UploadFileForm, ProfileImageForm
from .models import Comment, Graffiti, ProfileImage
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, DetailView, ListView
from pykml import parser
from django.template import RequestContext

import urllib.request
import string

graffitis = [] 

def index(request):
	comments = Comment.objects.all
	return render(request, 'graffiki_app/index.html', {'comments': comments})

	

@login_required
def add_comment_to_graffiti(request):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.save()
			return redirect('graffiki_app.views.index')
	else:
		form = CommentForm()
	return render(request, 'comments/add_comment_to_graffiti.html', {'form': form})
			
@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('graffiki_app.views.index')

@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.delete()
	return redirect('graffiki_app.views.index')

			
class KmlLink(generic.TemplateView):
    template_name = 'graffiki_app/kml.html'

# kml parser
def parse(request):

	context = RequestContext(request)
	context_dict = {'graffitis': graffitis}

	if not graffitis:

		url = 'http://blueberrynfig.pythonanywhere.com/static/graffiki_app/graffiti.kml'
		fileobject = urllib.request.urlopen(url)
		doc = parser.parse(fileobject).getroot()
		coordinates = doc.findall('.//{http://www.opengis.net/kml/2.2}coordinates')

		for coordinate in coordinates:
			coordArray = str(coordinate).split(',')
			graffiti = Graffiti()
			graffiti.lon = float(coordArray[0])
			graffiti.lat = float(coordArray[1])
			graffiti.save()
			graffitis.append(graffiti)

	
		return render_to_response('graffiki_app/index.html', context_dict, context)

	return render_to_response('graffiki_app/index.html', context_dict, context)



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Graffiti(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


# image upload stuff
class ProfileImageView(FormView):
    template_name = 'graffiki_app/profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile_image', kwargs={'pk': self.id})

class ProfileDetailView(DetailView):
    model = ProfileImage
    template_name = 'graffiki_app/profile_image.html'
    context_object_name = 'image'


class ProfileImageIndexView(ListView):
    model = ProfileImage
    template_name = 'graffiki_app/profile_image_view.html'
    context_object_name = 'images'
    queryset = ProfileImage.objects.all()
	
