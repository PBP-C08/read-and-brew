import json
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from main.models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email



@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "id": user.id,
                "user_status": user.profile.status,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali username atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)


    
@csrf_exempt
def create_user_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if (len(data['password1']) < 8):
            return JsonResponse({"status": "error", "messages":"Password minimal 8 karakter!"}, status=401)
        elif (data['password1'] != data['password2']):
            return JsonResponse({"status": "error", "messages":"Konfirmasi password tidak sama!"}, status=401)
        elif (User.objects.filter(username=data['username']).exists()):
            return JsonResponse({"status": "error", "messages":"Username telah digunakan!"}, status=401)
        elif (User.objects.filter(email=data['email']).exists()):
            return JsonResponse({"status": "error", "messages":"Email telah digunakan!"}, status=401)
        else:
            try:
                validate_email(data['email'])
            except ValidationError:
                return JsonResponse({"status": "error", "messages":"Format email salah!"}, status=401)
            new_user = User.objects.create_user(
                username = data['username'],
                email = data['email'],
                password = data['password1'],
                )
            Profile.objects.create(
                user = new_user,
                status = data['status'],
                full_name = data['full_name'],
                email = data['email']
                )
            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "messages":"Terdapat kesalahan pengisian, silahkan coba lagi!"}, status=401)