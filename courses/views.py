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
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        #
        # course_slug = self.kwargs.get('slug')
        # lesson_slug = self.kwargs.get('lesson_slug')

        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

        lesson.video = lesson.video.split("=")[1]

        ctx['lesson'] = lesson
        ctx['title'] = lesson
        ctx['lesson'] = lesson
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx


class CourseByCategory(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    paginate_by = 6

    def get_queryset(self):
        category = self.kwargs['category']
        if category == 'all':
            return Course.objects.all()
        return Course.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = f"Courses in {self.kwargs['category'].title()}"
        return ctx