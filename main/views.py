from django.shortcuts import render,HttpResponse,redirect
from main.models import Transaction
from main.models import Customer
from django.contrib import messages
from datetime import datetime
from django import template
register=template.Library()

@register.filter()
def range(min=5):
    return range(min)

# Create your views here.
def home(request):
    return render(request,"index.html")

def Details(request):

    customers = Customer.objects.all().order_by('id')
    return render(request,"second.html",context={'customers':customers})

def RecentTransactions(request):

    transactions = Transaction.objects.all().order_by('-sno')
    return render(request,"third.html",context={'transactions':transactions})

def AllTransactions(request):
    transactions = Transaction.objects.all().order_by('-sno')
    return render(request,"fourth.html",context={'transactions':transactions})

def fifth(request):
    customers = Customer.objects.all()
   
   
    
    

    if request.method == "POST":
        sender = request.POST.get("sender")
        receiver = request.POST.get("receiver")
        Amount = request.POST.get("Amount")
        
        status =False

        if int(sender) > 0 and int(receiver) > 0:
            sender_acc = Customer.objects.get(cid = sender)
            receiver_acc = Customer.objects.get(cid = receiver)
            if float(sender_acc.balance) > float(Amount): 
                sender_acc.balance = float(sender_acc.balance) - float(Amount)
                receiver_acc.balance = float(receiver_acc.balance) + float(Amount)
                sender_acc.save()
                receiver_acc.save()
                status =True
                t = Transaction(sender_acc =sender_acc,receiver_acc=receiver_acc,Amount=Amount,status=status,date=datetime.now() )
                t.save()
                return redirect("/AllTransactions")
            
            else:
                messages.info(request, 'Insufficient Balance ')
                t = Transaction(sender_acc =sender_acc,receiver_acc=receiver_acc,Amount=Amount,status=status,date=datetime.now() )
                t.save()
                return redirect("transfer",customer_id=int(sender))
            
        
        else:
            messages.warning(request, 'Enter Correct users ')
      

   

    
    return render(request,"fifth.html",context={'customers':customers})

def transfer( request,customer_id):
    customers = Customer.objects.all()
    cust=Customer.objects.get(pk=customer_id)
    return render(request,"fifth.html",context={'customers':customers,'cust':cust})


   



#     {
#     "emmet.triggerExpansionOnTab":true,
#     "files.associations": {"*html": "html" },
#     "liveServer.settings.donotShowInfoMsg": true,
#     "emmet.excludeLanguages": [

#         "markdown"
#     ],
#     "C_Cpp.updateChannel": "Insiders",
#     "python.linting.pylintArgs": [
#         "--load-plugins=pylint_django"
#     ],
#     "[python]": {
        
#     }
# }