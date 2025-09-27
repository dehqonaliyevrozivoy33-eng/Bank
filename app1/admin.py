
from django.contrib import admin
from .models import Transaction, BankCard, Customer



admin.site.register(Customer)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('card','amount','transaction_type' )

@admin.register(BankCard)
class BankCardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'balance', 'expiry_date')