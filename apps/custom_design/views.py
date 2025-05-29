from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import SurveyQuestion,MainModel
from .forms import SurveyQuestionForm, SurveyOptionFormSet,AboutUsForm,HeruSectionForm,CardForm,FooterUpperSectionForm,TrainVideoForm,FAQForm
from .serializers import CardSerializer
from rest_framework.generics import ListAPIView
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
        heru_section, _ = MainModel.objects.get_or_create(pk=1)
        form = HeruSectionForm(instance=heru_section)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        heru_section, _ = MainModel.objects.get_or_create(pk=1)
        form = HeruSectionForm(request.POST, request.FILES, instance=heru_section)
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



class CardListView(ListView):
    model = MainModel
    template_name = 'manage_cards.html'
    context_object_name = 'cards'

    def get_queryset(self):
        return MainModel.objects.filter(page_name='home', page_section='card')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class CardCreateView(CreateView):
    model = MainModel
    form_class = CardForm
    template_name = 'card_form.html'
    success_url = reverse_lazy('manage_cards')

    def dispatch(self, request, *args, **kwargs):
        if MainModel.objects.filter(page_name='home', page_section='card').count() >= 3:
            return redirect('manage_cards')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.page_name = 'home'
        form.instance.page_section = 'card'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Add'
        context = TemplateLayout.init(self, context)
        return context

class CardUpdateView(UpdateView):
    model = MainModel
    form_class = CardForm
    template_name = 'card_form.html'
    success_url = reverse_lazy('manage_cards')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Edit'
        context = TemplateLayout.init(self, context)
        return context

class CardDeleteView(DeleteView):
    model = MainModel
    template_name = 'card_confirm_delete.html'
    success_url = reverse_lazy('manage_cards')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class CustomAdminFooterUpeer(View):
    template_name = 'footer_upper_edit.html'

    def get(self, request):
        cus_up_footer, _ = MainModel.objects.get_or_create(
            page_name='home', page_section='footer_upper'
        )
        form = FooterUpperSectionForm(instance=cus_up_footer)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        cus_up_footer, _ = MainModel.objects.get_or_create(
            page_name='home', page_section='footer_upper'
        )
        form = FooterUpperSectionForm(request.POST, request.FILES, instance=cus_up_footer)
        context = self.get_context_data(form=form)
        if form.is_valid():
            form.save()
            return redirect('survey_admin_list')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = kwargs
        context = TemplateLayout.init(self, context)
        return context

from .serializers import VideoSerializer
class CardViewApi(ListAPIView):
    queryset = MainModel.objects.filter(page_name='home', page_section='card')
    serializer_class = CardSerializer
class VideoViewApi(ListAPIView):
    queryset = MainModel.objects.filter(page_name='train&FAQ', page_section='hero')
    serializer_class = VideoSerializer



class TrainVideoListView(View):
    template_name = 'train_video_list.html'

    def get(self, request):
        videos = MainModel.objects.filter(page_name='train&FAQ', page_section='video')
        context = {'videos': videos}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

class TrainVideoCreateView(View):
    template_name = 'train_video_form.html'

    def get(self, request):
        form = TrainVideoForm()
        context = {'form': form}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

    def post(self, request):
        form = TrainVideoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.page_name = 'train&FAQ'
            instance.page_section = 'video'
            instance.save()
            return redirect('train_video_list')
        context = {'form': form}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

class TrainVideoUpdateView(View):
    template_name = 'train_video_form.html'

    def get(self, request, pk):
        video = MainModel.objects.get(pk=pk)
        form = TrainVideoForm(instance=video)
        context = {'form': form}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        video = MainModel.objects.get(pk=pk)
        form = TrainVideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('train_video_list')
        context = {'form': form}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

class TrainVideoDeleteView(DeleteView):
    model = MainModel
    template_name = 'train_video_confirm_delete.html'
    success_url = reverse_lazy('train_video_list')

    def get_queryset(self):
        return MainModel.objects.filter(page_name='train&FAQ', page_section='video')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context
    


from django.core.paginator import Paginator
class FAQListView(View):
    template_name = 'faq_list.html'
    faqs= MainModel.objects.filter(page_name='train&FAQ', page_section='down')
    paginate_by = 5

    def get(self, request):
        faqs = MainModel.objects.filter(page_name='train&FAQ', page_section='down')
        context = {'faqs': faqs}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

class FAQCreateView(View):
    template_name = 'faq_form.html'

    def get(self, request):
        form = FAQForm()  # or your MainModel-based form
        context = {'form': form}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

    def post(self, request):
        form = FAQForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.page_name = 'train&FAQ'
            instance.page_section = 'down'
            instance.save()
            return redirect('faq_list')
        context = {'form': form}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

class FAQUpdateView(View):
    template_name = 'faq_form.html'

    def get(self, request, pk):
        faq = MainModel.objects.get(pk=pk, page_name='train&FAQ', page_section='down')
        form = FAQForm(instance=faq)
        context = {'form': form}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        faq = MainModel.objects.get(pk=pk, page_name='train&FAQ', page_section='down')
        form = FAQForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
        context = {'form': form}
        context = TemplateLayout.init(self, context)
        return render(request, self.template_name, context)

class FAQDeleteView(DeleteView):
    model = MainModel
    template_name = 'faq_confirm_delete.html'
    success_url = reverse_lazy('faq_list')

    def get_queryset(self):
        return MainModel.objects.filter(page_name='train&FAQ', page_section='down')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context
    




