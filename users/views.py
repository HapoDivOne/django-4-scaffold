from django.http import JsonResponse
from users.serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.utils.translation import gettext as trans
from rest_framework_simplejwt.tokens import RefreshToken
import csv
from pathlib import Path
from xhtml2pdf import pisa
import pandas as pd

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        
    return not pisa_status.err

class LogoutView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    def logout(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()   
            return JsonResponse({
                    'message': trans('register_success')
                }, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:

            return JsonResponse({
                'message': e,
            }, status=status.HTTP_400_BAD_REQUEST)

class UserRegister(viewsets.ModelViewSet):
     serializer_class = UserSerializer
     def register(self, request):
        if request.method != 'POST':
            return JsonResponse({
                'message': trans('method_not_support'),
            }, status=status.HTTP_400_BAD_REQUEST)
        
        userSerializer = UserSerializer(data=request.data)
        if userSerializer.is_valid():
            userSerializer.validated_data['password'] = make_password(userSerializer.validated_data['password'])
            userSerializer.save()
            return JsonResponse({
                'message': trans('register_success')
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'message': userSerializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        

class UserApi(viewsets.ModelViewSet) :
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]   

    def list(self, request):
        if request.method == 'GET':
            users = User.objects.all()
            users = UserSerializer(users, many=True)
            return JsonResponse({
                'data' : users.data,
                'message' : ""
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': trans('method_not_support'),
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def show(self, request, id):
        if request.method == 'GET':
            user = User.objects.filter(id=id)
            if user.exists():
                return JsonResponse({
                    'data' : user
                }, status=status.HTTP_200_OK)
            else:
                return JsonResponse({
                    'data' : user,
                    'message' : ""
                }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': trans('method_not_support'),
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,id):
        if request.method != 'POST':
            return JsonResponse({
                'message': trans('method_not_support'),
            }, status=status.HTTP_400_BAD_REQUEST)
        
        entity = User.objects.get(id=id)
        userSerializer = UserSerializer(entity, data=request.data)
      
        if userSerializer.is_valid():
            entity.username = request.data.get("username")
            entity.save()

            return JsonResponse({
                'message': trans('update_success')
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'message': userSerializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if request.method == 'DELETE':
            query = User.objects.get(id=id)
            query.delete()
            return JsonResponse({
                'message' : trans('delete_success')
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': trans('method_not_support'),
            }, status=status.HTTP_400_BAD_REQUEST)


class UserExport(viewsets.ModelViewSet) :
    def export_csv(self, request): 
        directory = Path(__file__).resolve().parent.parent
        with open(str(directory) + '/temp.csv', 'w', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC,delimiter=',') 
            writer.writerow(['username', 'firstname', 'lastname', 'email', 'phone_number']) 
        
            users = User.objects.all() 
            for user in users: 
                writer.writerow([user.username, user.firstname, user.lastname, user.email, user.phone_number]) 
        
        return JsonResponse({
            'message' : trans('export_success')
        }, status=status.HTTP_200_OK)


    def export_pdf(self, request):
        html_content = '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>PDF Example</title>
            </head>
            <body>
                <h1>Hello, world!</h1>
            </body>
            </html>
            '''

        # Generate PDF
        directory = Path(__file__).resolve().parent.parent
        pdf_path = str(directory) + '/temp.pdf'
        if convert_html_to_pdf(html_content, pdf_path):
            return JsonResponse({
                'message' : trans('export_success')
                }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message' : trans('export_failed')
                }, status=status.HTTP_400_BAD_REQUEST)

    def export_xlsx(self, request): 
        directory = Path(__file__).resolve().parent.parent
        data = {
            "product_name": ["computer", "printer", "tablet", "monitor"],
            "price": [1200, 150, 300, 450],
        }

        df = pd.DataFrame(data)

        df.to_excel(str(directory) + '/temp.xlsx', index=False)
        
        return JsonResponse({
            'message' : trans('export_success')
        }, status=status.HTTP_200_OK)
