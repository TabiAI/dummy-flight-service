import sqlite3

# LEGACY CODE: DO NOT DEPLOY TO PRODUCTION
# This script handles basic flight searches but desperately needs refactoring.

def search_domestic_flights(origin, destination, date):
    # Establish database connection
    conn = sqlite3.connect('travelbase_legacy.db')
    cursor = conn.cursor()
    
    # Calculate pricing
    base_price = 150.00
    tax = base_price * 0.08
    airport_fee = 25.00
    total_price = base_price + tax + airport_fee
    
    print(f"Searching domestic flights from {origin} to {destination} on {date}")
    print(f"Estimated ticket price: ${total_price:.2f}")
    
    # Fetch from database
    query = f"SELECT * FROM flights WHERE origin='{origin}' AND dest='{destination}' AND date='{date}' AND type='domestic'"
    cursor.execute(query)
    flights = cursor.fetchall()
    
    conn.close()
    return flights

def search_international_flights(origin, destination, date):
    # Establish database connection
    conn = sqlite3.connect('travelbase_legacy.db')
    cursor = conn.cursor()
    
    # Calculate pricing
    base_price = 450.00
    tax = base_price * 0.15
    airport_fee = 50.00
    total_price = base_price + tax + airport_fee
    
    print(f"Searching international flights from {origin} to {destination} on {date}")
    print(f"Estimated ticket price: ${total_price:.2f}")
    
    # Fetch from database
    query = f"SELECT * FROM flights WHERE origin='{origin}' AND dest='{destination}' AND date='{date}' AND type='international'"
    cursor.execute(query)
    flights = cursor.fetchall()
    
    conn.close()
    return flights

def get_flight_by_id(flight_id):
    # Establish database connection
    conn = sqlite3.connect('travelbase_legacy.db')
    cursor = conn.cursor()
    
    # Fetch from database
    query = f"SELECT * FROM flights WHERE id='{flight_id}'"
    cursor.execute(query)
    flight = cursor.fetchone()
    
    conn.close()
    return flight