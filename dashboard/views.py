from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from client.models import Client
from order.models import PurchaseOrder
from invoice.utils import render_to_pdf


def dashboard_index(request):
    clients = Client.objects.all()
    return render(request, 'dashboard/dashboard-index.html', {
        'clients': clients
    })


def dashboard_client(request, slug):
    client = get_object_or_404(Client, slug=slug)
    if request.method == 'POST':
        po_id = request.POST.get('po_number')
        purchases = get_object_or_404(PurchaseOrder, pk=po_id)
        context = {'client': client, 'purchases': purchases}
        return render(request, 'dashboard/dashboard-invoices.html', context)

    return render(request, 'dashboard/dashboard-clients.html', {'client': client})


def pdf_test(request):
    context = {
        "invoice_id": 9045902590348,
        "customer_name": "John Cooper",
        "amount": 1399.99,
        "today": "Today",
    }
    return render(request, 'pdf/invoice.html', context)


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        # template = get_template('pdf/invoice.html')
        context = {
            "invoice_id": 9045902590348,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        # html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
