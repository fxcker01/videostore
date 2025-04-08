from django.db import models
from django.urls import reverse


COURSE_CATEGORIES = [
    ('all', 'All'),
    ('games', 'Games'),
    ('web', 'Websites'),
    ('design', 'Design'),
    ('languages', 'Languages'),
    ('other', 'Other'),
    ('paid', 'Paid'),
]

class Course(models.Model):
    # slug, title, desc, image
    slug = models.SlugField('Unique course slug', unique=True)
    title = models.CharField('Course title', max_length=120)
    desc = models.TextField('Course description')
    image = models.ImageField('Image', default='default.jpg', upload_to='course_images')
    is_free = models.BooleanField('Free?', default=True)
    category = models.CharField('Category', max_length=50, choices=COURSE_CATEGORIES, default='all')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    # slug, title, desc, course, number, video_url
    slug = models.SlugField('Unique lesson slug')
    title = models.CharField('Lesson title', max_length=120)
    desc = models.TextField('Lesson description')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Which course?')
    number = models.IntegerField('Lesson number')
    video = models.CharField('Video URL', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})
