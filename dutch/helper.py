#receive all spends in a Dongish group and return the average spend.
def average_spend(allpersons_spend, average_spend):
    total_spend = 0
    for item in allpersons_spend:
        total_spend += item[1]
    average_spend = total_spend / len(allpersons_spend)
    return average_spend

#dividing all group members to tree lists Debtors, Creditors and Balance and return them back.
def who_debt_owe_balance(average_spend, allpersons_spend):
    debtors = []
    creditors= []
    balance = []
    for item in allpersons_spend:
        if item[1] < average_spend:
            item = list(item)
            item[1] = average_spend - item[1]
            debtors.append(item)
        elif item[1] > average_spend:
            item = list(item)
            item[1] = item[1] - average_spend
            creditors.append(item)
        else:
            balance.append(item)

    return debtors, creditors, balance

#finding out the best method of dutch payment by the most less possible transactions and return them as list of lists.
def who_pay_to_who(debtors, creditors, balance):
    debtors = sorted(debtors, key=lambda x:- x[1])
    creditors = sorted(creditors, key=lambda x:- x[1])
    balanced_ower = 0
    balanced_debtor = 0
    answer = []
    for debtor in debtors:
        if debtor[1] == 0:
            balanced_debtor += 1
            continue
        for ower in creditors:
            if ower[1] == 0:
                balanced_ower += 1
                continue
            if debtor[1] == ower[1] and debtor[1] != 0 and ower[1] != 0:
                answer.append([debtor[0], debtor[1], ower[0]])
                debtor[1], ower[1] = 0, 0
            elif debtor[1] > ower[1] and debtor[1] != 0 and ower[1] != 0:
                answer.append([debtor[0], ower[1], ower[0]])
                debtor[1] = debtor[1] - ower[1]
                ower[1] = 0
            elif ower[1] != 0 and debtor[1] != 0:
                answer.append([debtor[0], debtor[1], ower[0]])
                ower[1] = ower[1] - debtor[1]
                debtor[1] = 0
    return answer