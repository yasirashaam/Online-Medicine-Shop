from django.shortcuts import render, get_object_or_404
from .models import Medicine

def medicine_list(request):
    query = request.GET.get('q')
    
    if query:
        medicines = Medicine.objects.filter(name__icontains=query, stock_quantity__gt=0)
    else:
        medicines = Medicine.objects.filter(stock_quantity__gt=0)

    return render(request, 'medicines/medicine_list.html', {'medicines': medicines})


def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'medicines/medicine_detail.html', {'medicine': medicine})