from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.template import loader

from .models import Auteur, Pub, Demande, Contacte, Videos

from .form import Nscontacte

import random

from django.contrib import messages

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def index(request):
    pubs=Pub.objects.all()

    pubs_l = list(pubs)

    random.shuffle(pubs_l)

    pubs_aleatoire = pubs_l[:3]

    pubs_aleatoire = random.choices(pubs_l,k=3)

    context = {'pubs_aleatoire':pubs_aleatoire}

    return render(request,'blog/index.html',context)



def listing(request):
    pubs = Pub.objects.all()

    formatted_pubs = ["<li> {} </li>".format(pub.titre)for pub in pubs]

    message = """ <ul> {} </ul>""".format("\n".join(formatted_pubs))

    return HttpResponse(message)


def blog(request):
    likes={}

    pubs = Pub.objects.all()

    for pub in pubs:

        likes[pub] = len(pub.likeur.all())


    pubs_l = list(pubs)

    pubs_r = pubs_l[::-1]
    
    context ={'pubs_r':pubs_r,"likes":likes}

    return render(request,'blog/blog.html',context)


def ncontacte(request):
    if request=="POST":

        form_c = Nscontacte(request.POST).save()

        messages.success(request,"le messages que vous avez rediger a bien été envoyé.")

        return redirect('index')
    else:
        form_c = Nscontacte()

    context ={'form_c':form_c}
    
    return render(request,'blog/ncontacte.html',context)


class PubDetail(DetailView):
    model = Pub
    templates_name = "blog/detail.html"


def predication(request):
    videos = Videos.objects.all()

    videos = list(videos)

    videos_r = videos[::-1]

    context ={'videos_r':videos_r}

    return render(request,'blog/predications.html',context)


@login_required
def add_favorite_pub(request,pub_id):
    lpub = Pub.objects.filter(id=pub_id).first()

    user = request.user

    if lpub in user.profile.pubs.all():
        messages.warning(request,"la publications {} est déjà dans vos favoris".format(lpub))
    else:
        user.profile.pubs.add(lpub)

        user.profile.save()

        messages.success(request,"la publiction {} à a bien été ajouter dans vos favoris".format(lpub.titre))
    return redirect('blog-app')


@login_required
def mylist_pub(request):
    pubs = Pub.objects.filter(profile=request.user.profile)

    pubs = list(pubs)

    taille_mylist = len(pubs)

    context={"pubs":pubs,"taille_mylist":taille_mylist}

    return render(request,"blog/mylist_pub.html",context)


@login_required
def remove_favorite_pub(request,pub_id):
    lpub=Pub.objects.filter(id=pub_id).first()

    user=request.user

    user.profile.pubs.remove(lpub)

    user.profile.save()

    messages.success(request,"la publication {} a bien été suprimer de vos favoris".format(lpub.titre))
    return redirect('blog-app')


@login_required
def liker(request,pub_id):
    lpub=Pub.objects.filter(id=pub_id).first()
    user = request.user
    if user in lpub.likeur.all():
        messages.warning(request,"vous avez déjà liké cette publication {}".format(lpub.titre))
    else:
        lpub.likeur.add(user)
        lpub.save()
        messages.success(request,"vous avez bien liké la publication nommée {}".format(lpub.titre))
    return redirect('blog-app')




class PubCreatView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Pub
    fields = ['titre','description','image']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class PubvCreatView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Videos
    fields = ['video']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
