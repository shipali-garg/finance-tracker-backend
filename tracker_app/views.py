from http.client import HTTPResponse

from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import Transaction
from .serializers import TransactionSerializer
from .permissions import RolePermission
# Create your views here.

def home(request):
    return HttpResponse("Finance Tracker API is running")

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, RolePermission]

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)

        category = self.request.query_params.get('category')
        t_type = self.request.query_params.get('type')

        if category:
            queryset = queryset.filter(category=category)
        if t_type:
            queryset = queryset.filter(type=t_type)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def summary(request):
    transactions = Transaction.objects.filter(user=request.user)

    income = transactions.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = transactions.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    category_data = transactions.values('category').annotate(total=Sum('amount'))

    return Response({
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense,
        "category_breakdown": category_data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def monthly_summary(request):
    transactions = Transaction.objects.filter(user=request.user)

    data = transactions.annotate(month=TruncMonth('date')) \
        .values('month', 'type') \
        .annotate(total=Sum('amount')) \
        .order_by('month')

    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recent_transactions(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')[:5]

    data = [
        {
            "amount": t.amount,
            "type": t.type,
            "category": t.category,
            "date": t.date,
            "notes": t.notes
        }
        for t in transactions
    ]

    return Response(data)