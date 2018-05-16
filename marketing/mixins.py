from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class CsrfExceptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super(CsrfExceptMixin,self).dispatch(request,*args,**kwargs)

