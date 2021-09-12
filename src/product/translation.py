from modeltranslation.translator import translator, TranslationOptions,register
from .models import Product
from modeltranslation.utils import fallbacks

@register(Product)
class NewsTranslationOptions(TranslationOptions):
    fields = ('PRDName', 'PRDDec','PRDVandor_Name','PRDCategory','PRDDec','PRDBrand')
    with fallbacks(True):
        fallback_languages = {'default': ('ar',)}
