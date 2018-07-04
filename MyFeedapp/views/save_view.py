# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import CreateView
#
# from MyFeedapp.models import *
#
# class addStudentView(LoginRequiredMixin,CreateView):
#     login_url = '/login/'
#     form_class = addStudent
#     template_name = 'addStudentTemplate.html'
#     model =
#     def post(self, request, *args, **kwargs):
#         import ipdb
#         ipdb.set_trace()
#         collage = Collage.objects.get(id=int(self.kwargs['id']))
#         student_form = addStudent(request.POST)
#         mock_test_form=addMockTest(request.POST)
#
#         if student_form.is_valid():
#             stu = student_form.save(commit=False)
#             stu.college=collage
#             stu.save()
#
#             if mock_test_form.is_valid():
#                 mckTest = mock_test_form.save(commit=False)
#                 mckTest.calulateTotal()
#                 mckTest.student=stu
#                 mckTest.save()
#         return HttpResponse(reverse_lazy('onlineapp:collages_html'))
#
#
#
from django.http import JsonResponse
import json
import ast
from MyFeedapp.models import *


def save(request):
    import ipdb
    ipdb.set_trace()
    ab=list()
    try:
        for i in request.GET.keys():
            ab.append(i)
        article = ast.literal_eval("".join(ab))
        source = article.pop('source')
        id = article.pop('id')
        articleObj = Article(**article)
        articleObj.user = request.user
        articleObj.save()
        data = {'is_saved': True, }
    except Exception as ex:
        data = {'is_saved': False, }
    return JsonResponse(data)


def remove(request):
    import ipdb
    ipdb.set_trace()
    ab=list()
    for i in request.GET.keys():
        ab.append(i)
    articleId = int(ab[0])
    try:
        articleObj = Article.objects.get(id=articleId)
        articleObj.delete()
        data = {'is_removed': True, }
    except Exception as ex:
        data = {'is_removed': False, }
    return JsonResponse(data)
