import sqlite3

# LEGACY CODE: DO NOT DEPLOY TO PRODUCTION
# This script handles basic flight searches but desperately needs refactoring.

FLIGHT_PRICING = {
    "domestic":      {"base": 125.00, "tax_rate": 0.08, "fee": 25.00},
    "international": {"base": 450.00, "tax_rate": 0.15, "fee": 50.00},
}
def calculate_price(base_price,tax_rate,airport_fee):
    total_price = base_price + (base_price*tax_rate) + airport_fee
    return total_price

def execute_query(query, params=()):
    with sqlite3.connect('travelbase_legacy.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

def search_flights(origin, destination, date, flighttype):
    pricing = FLIGHT_PRICING.get(flighttype)
    
    if pricing is None:
        raise ValueError(f"Unknown flight type: '{flighttype}'")
    
    total_price = calculate_price(pricing["base"], pricing["tax_rate"], pricing["fee"])
    
    print(f"Searching {flighttype} flights from {origin} to {destination} on {date}")
    print(f"Estimated ticket price: ${total_price:.2f}")
    
    query = "SELECT * FROM flights WHERE origin=? AND dest=? AND date=? AND type=?"
    return execute_query(query, (origin, destination, date, flighttype))

def get_flight_by_id(flight_id):
    query = "SELECT * FROM flights WHERE id=?"
    results = execute_query(query, (flight_id,))
    return results[0] if results else None