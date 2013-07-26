from django import forms
from django.forms import Textarea, Select
from directory.models import Image, Sponsor, Vassal, House
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings



class ImageForm(forms.ModelForm):

      class Meta:
          
          model = Image

      def clean_content(self):

            print("called the image validator")
            
            content = self.cleaned_data['content']
          
            content_type = content.content_type.split('/')[0]
          
            if content_type in settings.CONTENT_TYPES:
                
                  if content._size > settings.MAX_UPLOAD_SIZE:
                    
                        raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))

            else:

                  raise forms.ValidationError(_('File type is not supported'))

            return content

class SponsorForm(forms.ModelForm):

      class Meta:
          
          model = Sponsor

class VassalForm(forms.ModelForm):

      class Meta:

            model = Vassal
            widgets = {'title': Select(),}
            
            
class HouseForm(forms.Form):

      field = forms.ModelChoiceField(queryset = House.objects.all())
