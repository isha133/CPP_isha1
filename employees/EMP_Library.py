from .models import Employee
from django.shortcuts import render, redirect
# from employeemanagementsystem.models import Employee
# from employeemanagementsystem.form import EmployeeForm


def delete(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('read')
        
    return render(request, 'employee/read.html')

    