from django.shortcuts import render
from django.views.generic import RedirectView,TemplateView

# Create your views here.
class GeekyRedirectView(RedirectView):
    url ="https://www.geekyshows.com/"


class GeekRedirectView(RedirectView):
    pattern_name ="homewithkwargs"
    query_string = True
    permanent    = True

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['pk']=17
        return super().get_redirect_url(*args, **kwargs)
