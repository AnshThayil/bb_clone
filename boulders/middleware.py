from django.utils.deprecation import MiddlewareMixin
from users.models import Profile

class GradeMiddleware(MiddlewareMixin):

        
    def process_template_response(self, request, response):
        try:
            profile = Profile.objects.get(user = request.user)
            if profile.grade_format_font:
                format = 'font'
            else:
                format = 'v'

            if response.template_name == ['boulders/boulder_detail.html']:
                response.context_data['boulder'].grade = self.translate(response.context_data['boulder'].grade, format)
            elif response.template_name == ['gyms/gym_detail.html']:
                for boulder in response.context_data['boulders']:
                    boulder.grade = self.translate(boulder.grade, format)
    
        finally:
            return response

    def translate(self, grade, format):
        self.font = ['3', '3+', '4', '4+', '5', '5+', '6A','6A+','6B', '6B+', '6C', '6C+', '7A', '7A+', '7B', '7B+', '7C', '7C+', '8A', '8A+']
        self.v = ['B', '0-', '0', '0+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

        if (format == 'font'):
            return 'fb ' + self.font[int(grade)]
        else:
            return 'V' + self.v[int(grade)]