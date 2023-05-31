from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import DespesaForm, ReceitaForm
from .models import Despesa, Receita
from django.db.models import Sum



# Create your views here.
def projetofinancas(request):
    return render(request, 'projetofinancas.html')

def financas(request):
    despesas = Despesa.objects.all()
    receitas = Receita.objects.all()
    total_despesas = despesas.aggregate(total=Sum('valor'))['total']
    total_receitas = receitas.aggregate(total=Sum('valor'))['total']
    saldo = total_receitas - total_despesas

    if request.method == 'POST':
        if 'despesa_submit' in request.POST:
            form_despesa = DespesaForm(request.POST)
            if form_despesa.is_valid():
                form_despesa.save()
                return redirect('financas')
        elif 'receita_submit' in request.POST:
            form_receita = ReceitaForm(request.POST)
            if form_receita.is_valid():
                form_receita.save()
                return redirect('financas')
        
        # Processar dados dos formulários table-form2 e table-form3
        valor_despesa = request.POST.get('valor_despesa')
        categoria_despesa = request.POST.get('categoria_despesa')
        data_despesa = request.POST.get('data_despesa')

        valor_receita = request.POST.get('valor_receita')
        categoria_receita = request.POST.get('categoria_receita')
        data_receita = request.POST.get('data_receita')

        # Criar instâncias de Despesa e Receita e salvá-las no banco de dados
        despesa = Despesa(categoria_despesa=categoria_despesa, valor=valor_despesa, data=data_despesa)
        despesa.save()

        receita = Receita(categoria_receita=categoria_receita, valor=valor_receita, data=data_receita)
        receita.save()

        return redirect('financas')

    else:
        form_despesa = DespesaForm()
        form_receita = ReceitaForm()

    context = {
        'despesas': despesas,
        'receitas': receitas,
        'total_despesas': total_despesas,
        'total_receitas': total_receitas,
        'saldo': saldo,
        'form_despesa': form_despesa,
        'form_receita': form_receita,
    }

    return render(request, 'projetofinancas.html', context)