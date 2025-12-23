from datetime import date, timedelta

def compute_status(expiry):
    today = date.today()
    start = expiry - timedelta(days=120)
    end = expiry - timedelta(days=60)

    if today > expiry:
        return "Expiré"
    if end < today <= expiry:
        return "En fin de validité"
    if start <= today <= end:
        return "À renouveler"
    return "Régulier"
