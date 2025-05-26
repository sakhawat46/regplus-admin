from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import SurveyQuestion,MainModel
from .forms import SurveyQuestionForm, SurveyOptionFormSet,AboutUsForm,HeruSectionForm

from django.views import View

# List all questions
class SurveyQuestionListView(ListView):
    model = SurveyQuestion
    template_name = 'survey_list.html'
    context_object_name = 'questions'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject layout_path for template inheritance
        context = TemplateLayout.init(self, context)
        return context


class SurveyQuestionCreateView(CreateView):
    model = SurveyQuestion
    form_class = SurveyQuestionForm
    template_name = 'survey_form.html'
    success_url = reverse_lazy('survey_admin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

    def get(self, request, *args, **kwargs):
        self.object = None  # required for CBV
        form = self.form_class()
        formset = SurveyOptionFormSet()
        context = self.get_context_data(form=form, formset=formset)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST)
        formset = SurveyOptionFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form, formset=formset)
        return self.render_to_response(context)



# Update question + options
class SurveyQuestionUpdateView(UpdateView):
    model = SurveyQuestion
    form_class = SurveyQuestionForm
    template_name = 'survey_form.html'
    success_url = reverse_lazy('survey_admin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object)
        formset = SurveyOptionFormSet(instance=self.object)
        context = self.get_context_data(form=form, formset=formset)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        formset = SurveyOptionFormSet(request.POST, instance=self.object)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form, formset=formset)
        return self.render_to_response(context)

from web_project import TemplateLayout
# Delete question
class SurveyQuestionDeleteView(DeleteView):
    model = SurveyQuestion
    template_name = 'survey_confirm_delete.html'
    success_url = reverse_lazy('survey_admin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject layout_path for template inheritance
        context = TemplateLayout.init(self, context)
        return context


class CustomAdminAboutUsView(View):
    template_name = 'about_us_edit.html'

    def get(self, request):
        about_us, _ = MainModel.objects.get_or_create(pk=1)
        form = AboutUsForm(instance=about_us)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        about_us, _ = MainModel.objects.get_or_create(pk=1)
        form = AboutUsForm(request.POST, request.FILES, instance=about_us)
        context = self.get_context_data(form=form)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_about_us')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = kwargs
        context = TemplateLayout.init(self, context)
        return context

class CustomAdminHeruSection(View):
    template_name = 'home_edit.html'

    def get(self, request):
        about_us, _ = MainModel.objects.get_or_create(pk=1)
        form = HeruSectionForm(instance=about_us)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        about_us, _ = MainModel.objects.get_or_create(pk=1)
        form = HeruSectionForm(request.POST, request.FILES, instance=about_us)
        context = self.get_context_data(form=form)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_about_us')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = kwargs
        context = TemplateLayout.init(self, context)
        return context


# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import SurveyQuestion

def survey_question_view(request, question_order=1):
    question = get_object_or_404(SurveyQuestion, order=question_order)

    if request.method == 'POST':
        selected_option = request.POST.get('option')
        request.session[f'answer_{question_order}'] = selected_option

        # Redirect to next question if it exists
        next_question = SurveyQuestion.objects.filter(order=question_order + 1).first()
        if next_question:
            return redirect('survey_question', question_order=next_question.order)
        else:
            return redirect('survey_result')

    return render(request, 'question.html', {'question': question})
   
def survey_result_view(request):
    answers = {}
    for question in SurveyQuestion.objects.all().order_by('order'):
        selected_option_id = request.session.get(f'answer_{question.order}')
        if selected_option_id:
            selected_text = question.options.get(id=selected_option_id).option_text
            answers[question.question_text] = selected_text
        else:
            answers[question.question_text] = "No answer"

    return render(request, 'result.html', {'answers': answers})
