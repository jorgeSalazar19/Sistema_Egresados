from django.shortcuts import redirect
from django.contrib.auth import logout

def closeSession(request):
	if request.user is not None:
		logout(request)

	return redirect('/')