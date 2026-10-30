import csv
import json
import hashlib

transactions = []
with open('data/sample_transactions.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, r in enumerate(reader):
        if i >= 150:
            break
        tx_id = r['transaction id']
        cat = r['merchant_category']
        amt = float(r['amount (INR)'])
        s_bank = r['sender_bank'].lower()
        r_bank = r['receiver_bank'].lower()
        s_state = r['sender_state']
        s_age = r['sender_age_group']
        t_type = r['transaction type']
        fraud = int(r.get('fraud_flag', '0'))
        ts = r['timestamp']

        if cat in ['Grocery', 'Utilities', 'Healthcare']:
            theme = 'Essential Survival'
        elif cat in ['Shopping', 'Entertainment', 'Food & Dining']:
            theme = 'Lifestyle & Wants'
        elif cat in ['Education']:
            theme = 'Future Growth & Education'
        else:
            theme = 'Transit & Commute'

        cat_clean = cat.lower().replace('&', 'and').replace(' ', '_')
        s_vpa = f"user_{s_state[:3].lower()}_{s_age.split('-')[0]}@{s_bank}"
        r_vpa = f"merchant_{cat_clean}@{r_bank}"
        raw_str = f"{tx_id}:{ts}:{amt}:{cat}:{s_vpa}:{r_vpa}"
        tx_hash = '0x' + hashlib.sha256(raw_str.encode()).hexdigest()

        risk = 98 if fraud == 1 else (68 if amt > 10000 else (45 if t_type == 'P2P' and amt > 5000 else 12))

        transactions.append({
            'id': tx_id,
            'hash': tx_hash,
            'timestamp': ts,
            'amount': amt,
            'category': cat,
            'theme': theme,
            'type': t_type,
            'sender_bank': r['sender_bank'],
            'sender_state': s_state,
            'sender_vpa': s_vpa,
            'receiver_vpa': r_vpa,
            'fraud': fraud,
            'risk': risk
        })

with open('data/sample_150.json', 'w', encoding='utf-8') as out:
    json.dump(transactions, out, indent=2)

print(f"Generated {len(transactions)} transactions successfully in data/sample_150.json")
