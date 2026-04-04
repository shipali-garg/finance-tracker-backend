from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, summary, monthly_summary, recent_transactions

router = DefaultRouter()
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', summary),
    path('monthly-summary/', monthly_summary),
    path('recent-transactions/', recent_transactions),
]
