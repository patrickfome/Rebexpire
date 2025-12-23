from datetime import date, timedelta

STATUS_REGULIER = "Régulier"
STATUS_A_RENOUVELER = "À renouveler"
STATUS_FIN_VALIDITE = "En fin de validité"
STATUS_EXPIRE = "Expiré"

STATUS_COLORS = {
    STATUS_REGULIER: "green",
    STATUS_A_RENOUVELER: "yellow",
    STATUS_FIN_VALIDITE: "orange",
    STATUS_EXPIRE: "red",
}

def compute_status(expiry_date: date):
    today = date.today()

    start_renewal = expiry_date - timedelta(days=120)
    end_renewal = expiry_date - timedelta(days=60)

    if today > expiry_date:
        status = STATUS_EXPIRE
    elif today >= end_renewal:
        status = STATUS_FIN_VALIDITE
    elif today >= start_renewal:
        status = STATUS_A_RENOUVELER
    else:
        status = STATUS_REGULIER

    return {
        "status": status,
        "color": STATUS_COLORS[status],
        "start_renewal": start_renewal,
        "end_renewal": end_renewal,
    }
