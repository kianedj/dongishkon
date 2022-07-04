from rest_framework import generics
from .models import Transaction, DongishGroup
from .serializers import TransactionSerializer, DongishGroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class TransactionListAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    model = Transaction
    serializer_class = TransactionSerializer

class TransactionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    model = Transaction
    serializer_class = TransactionSerializer

class DongishGroupListAPIView(generics.ListCreateAPIView):
    queryset = DongishGroup.objects.all()
    model = DongishGroup
    serializer_class = DongishGroupSerializer

class DongishGroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DongishGroup.objects.all()
    model = DongishGroup
    serializer_class = DongishGroupSerializer

''' get balance the Dongish group's members by suggesting payments with most less transactions '''
@api_view()
def DongishGroupDutchCalculationAPIView(request, pk):
    best_trxs = DongishGroup.objects.get(id=pk).best_trx_to_balance()

    #preparing data and serialization.
    keepmem = {}
    data = list()
    for item in best_trxs:
        keepmem['debtor'] = item[0]
        keepmem['amount'] = item[1]
        keepmem['creditor'] = item[2]
        data.append(keepmem)
        keepmem={}

    return Response(data)


''' show total spends, total members and dutch of user for 
    each Dongish group which user is member of.   '''
@api_view()
def UserProfile(request):
    #queries to bring data needed.
    user_id = request.user.id

    #queryset to receive all user's Dongish groups.     
    groups = DongishGroup.objects.filter(members__id=user_id) 

    #preparing data and serialization.
    keepmem = {}
    data = []
    for group in groups:
        keepmem['group_name'] = group.__str__()
        keepmem['total_spends'] = group.total_spends()
        keepmem['total_members'] = group.total_members()
        keepmem['dutch'] = group.dutch()
        data.append(keepmem)
        keepmem={}

    return Response(data)
