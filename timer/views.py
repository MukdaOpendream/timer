from django.views.generic import TemplateView


class TimerView(TemplateView):
	template_name = 'timer.html'

class TimersView(TemplateView):
	template_name = 'timers.html'

class TimerNoBootstrapView(TemplateView):
	template_name = 'my_css_timer.html'
