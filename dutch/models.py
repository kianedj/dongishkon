from django.db import models
from accounts.models import CustomUser
from .helper import who_debt_owe_balance, who_pay_to_who

class DongishGroup(models.Model):
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=True)
    creator = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.CASCADE,
        related_name= 'creator')
    members = models.ManyToManyField(
        CustomUser,
        blank=True,
        related_name='members')
    explain = models.TextField(
        null=True,
        blank=True)

    def __str__(self):
        return self.name

    def total_spends(self):
        queryset = Transaction.objects.values('amount').filter(group__id=self.id)
        answer = 0
        for object in queryset:
            answer += object['amount']
        return answer

    def total_members(self):
        return self.members.all().count()

    def dutch(self):
        try:
            return self.total_spends() / self.total_members()
        except:
            return 0

    def admin_name(self):
        return str(self.creator.username)

    def best_trx_to_balance(self):
        #queries to bring members and all transactions has been done by them in the group.
        members = self.members.all()
        transactions = Transaction.objects.filter(group__id=self.id)
        
        #all transactions of each person should be sum and sit in dictionery.
        all_members_spends = {}
        for trx in transactions:
            if trx.owner.username in all_members_spends.keys():
                all_members_spends[trx.owner.username] += trx.amount
            else:
                all_members_spends[trx.owner.username] = trx.amount

        #for members who did not spend in group adding -0- as their spend.
        for member in members:
            if member.username in all_members_spends.keys():
                continue
            else:
                all_members_spends[member.username] = 0
        
        #note: the function who_debt_owe_balance(*can only accept list*) so we needed to convert it. 
        all_members_spends = list(map(list,all_members_spends.items()))

        debtors, creditors, balanced = who_debt_owe_balance(
            allpersons_spend=all_members_spends,average_spend=self.dutch())
        data = who_pay_to_who(
            debtors=debtors, creditors=creditors, balance=balanced)
        
        return data



class Transaction(models.Model):
    owner = models.ForeignKey(
        CustomUser,
        null=False,
        blank=False,
        on_delete=models.PROTECT)
    group = models.ForeignKey(
        DongishGroup,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
    amount = models.IntegerField(
        default=0,
        blank=False,
        null=False)
    date = models.DateField(
        auto_now=True,)
    about = models.TextField(
        max_length=300,
        null=True,
        blank=True)

    def __str__(self):
        return self.about