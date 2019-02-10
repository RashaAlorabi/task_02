from django.shortcuts import render

# Create your views here.
def print_template(request):
	context ={
	'msg': 'Hello World !'

	}
	return render(request,'index.html',context)
