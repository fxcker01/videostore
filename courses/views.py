from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import CourseForm
from .models import Course, Lesson

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.core.paginator import Paginator
# from cloudipsp import Api, Checkout
# from django.contrib.auth.decorators import user_passes_test
# import time


# @user_passes_test(lambda u: u.is_superuser)
@login_required
def add_course(request):
    if not request.user.is_staff:  # Перевірка чи користувач є адміністратором
        return HttpResponseForbidden("403: Forbidden")

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Після успішного додавання перенаправляємо на головну сторінку
    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form, 'title': 'Add course'})


def tarrifsPage(request):
    # api = Api(merchant_id=1396424,
    #           secret_key='test')
    # checkout = Checkout(api=api)
    # data = {
    #     "currency": "USD",
    #     "amount": 500,
    #     "order_description": "Покупка подписки на сайте",
    #     "order_id": str(time.time())
    # }
    # url = checkout.url(data).get('checkout_url')
    return render(request, 'courses/tarrifs.html', {'title': 'Subscription Plans'}) #, 'url': url}) """



class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Home Page'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()
        lessons = Lesson.objects.filter(course=course).order_by('number')

        # Обробка YouTube чи Vimeo
        video_url = lesson.video

        if 'youtube.com' in video_url:
            try:
                lesson.video_embed = video_url.split('=')[1]
                ctx['video_source'] = 'youtube'
            except IndexError:
                lesson.video_embed = ''
                ctx['video_source'] = 'unknown'

        elif 'vimeo.com' in video_url:
            try:
                parts = video_url.split('/')
                video_id = parts[3]  # ID після vimeo.com/
                token = parts[4] if len(parts) > 4 else ''
                if token:
                    lesson.video_embed = f"{video_id}?h={token}"
                else:
                    lesson.video_embed = video_id
                    ctx['video_source'] = 'vimeo'
            except IndexError:
                lesson.video_embed = ''
                ctx['video_source'] = 'unknown'

        else:
            lesson.video_embed = ''
            ctx['video_source'] = 'unknown'


        ctx['lesson'] = lesson
        ctx['title'] = lesson.title
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx

# course_slug = self.kwargs.get('slug')
# lesson_slug = self.kwargs.get('lesson_slug')

#------

# lesson.video = lesson.video.split("=")[1]
class CourseByCategory(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']
    paginate_by = 6

    def get_queryset(self):
        category = self.kwargs['category']
        if category == 'all':
            return Course.objects.all().order_by('-id')
        return Course.objects.filter(category=category).order_by('-id')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = f"Courses in {self.kwargs['category'].title()}"
        return ctx