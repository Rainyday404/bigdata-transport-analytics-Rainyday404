def generate_alert(df):
    alerts = []
    
    # Mengecek apakah volume data (traffic) melebihi ambang batas
    if len(df) > 100:
        alerts.append("🚨 High traffic volume")
    
    # Mengecek apakah ada tarif (fare) yang sangat tinggi
    if df["fare"].max() > 90000:
        alerts.append("💰 High fare detected")
        
    return alerts