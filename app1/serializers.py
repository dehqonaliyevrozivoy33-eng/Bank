from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        card = data.get('card')
        amount = data.get('amount')
        transaction_type = data.get('transaction_type')

        if transaction_type == 'withdraw' and amount > card.balance:
            raise serializers.ValidationError("Withdraw summasi balansdan katta bo‘lishi mumkin emas!")
        return data
