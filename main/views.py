from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Banner,Project,Role,Employee,EmployeeAttribute
from django.template.loader import render_to_string
# Home Page
def home(request):
	banners=Banner.objects.all().order_by('-id')
	data=Employee.objects.filter(is_featured=True).order_by('-id')
	return render(request,'main/index.html',{'data':data,'banners':banners})

# Category
def project_list(request):
	data=Project.objects.all().order_by('-id')
	project_count=str(Project.objects.filter(active=True).count())
	project_counts=str(Project.objects.filter(active=False).count())
	return render(request,'main/project_list.html',{'data':data, 'project_count':project_count, 'project_counts':project_counts})

# Brand
def role_list(request):
	data=Role.objects.all().order_by('-id')
	#project_count=str(Project.objects.filter(active=True).count())
	return render(request,'main/role_list.html',{'data':data})

# Product List
def employee_list(request):
	data=Employee.objects.all().order_by('-id')
	return render(request,'main/employee_list.html',
		{
			'data':data,
		}
		)

# Product List According to Category
def project_employee_list(request,cat_id):
	project=Project.objects.get(id=cat_id)
	data=Employee.objects.filter(project=project).order_by('-id')
	return render(request,'main/project_employee_list.html',{
			'data':data,
			})

# Product List According to Brand
def role_employee_list(request,brand_id):
	role=Role.objects.get(id=brand_id)
	data=Employee.objects.filter(role=role).order_by('-id')
	return render(request,'main/role_employee_list.html',{
			'data':data,
			})

# Product Detail
def employee_detail(request,slug,id):
	employee=Employee.objects.get(id=id)
	return render(request, 'main/employee_detail.html',{'data':employee})

# Search
def search(request):
	q=request.GET['q']
	data=Employee.objects.filter(title__icontains=q).order_by('-id')
	return render(request,'main/search.html',{'data':data})


def search_project(request):
	q=request.GET['s']
	data=Project.objects.filter(title__icontains=q).order_by('-id')
	return render(request,'main/search_project.html',{'data':data})

def search_ongoingproject(request):
	data=Project.objects.filter(active=True)
	return render(request,'main/search_ongoingproject.html',{'data':data})

def search_completedproject(request):
	data=Project.objects.filter(active=False)
	return render(request,'main/search_completedproject.html',{'data':data})