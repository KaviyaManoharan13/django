from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import InsurancePolicy, Customer, CustomerPolicy

@login_required
def policy_list(request):
    policies = InsurancePolicy.objects.all()
    return render(request, 'insurance/policy_list.html', {'policies': policies})

@login_required
def register_policy(request, policy_id):
    policy = InsurancePolicy.objects.get(id=policy_id)
    customer, created = Customer.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        customer_policy = CustomerPolicy(customer=customer, policy=policy, start_date=start_date, end_date=end_date)
        customer_policy.save()
        return redirect('policy_list')
    return render(request, 'insurance/register_policy.html', {'policy': policy})

@login_required
def my_policies(request):
    customer = Customer.objects.get(user=request.user)
    customer_policies = CustomerPolicy.objects.filter(customer=customer)
    return render(request, 'insurance/policy.html', {'customer_policies': customer_policies})
