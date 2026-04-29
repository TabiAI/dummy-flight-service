import sqlite3

# LEGACY CODE: DO NOT DEPLOY TO PRODUCTION
# This script handles basic flight searches but desperately needs refactoring.

# Fixed Data
PRICING = {
    "domestic": {"base_price": 150.00, "tax_rate": 0.08, "airport_fee": 25.00},
    "international": {"base_price": 450.00, "tax_rate": 0.15, "airport_fee": 50.00},
}

# Helper Functions
def calculate_price(base_price, tax_rate, airport_fee):
    tax = base_price * tax_rate
    return base_price + tax + airport_fee

def execute_query(query, params):
    with sqlite3.connect('travelbase_legacy.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()


# Main Functions
def search_flights(origin, destination, date, flight_type):
    pricing = PRICING[flight_type]
    total_price = calculate_price(pricing["base_price"], pricing["tax_rate"], pricing["airport_fee"])
    print(f"Searching {flight_type} flights from {origin} to {destination} on {date}")
    print(f"Estimated ticket price: ${total_price:.2f}")
    query = "SELECT * FROM flights WHERE origin=? AND dest=? AND date=? AND type=?"
    return execute_query(query, (origin, destination, date, flight_type))


def get_flight_by_id(flight_id):
    query = "SELECT * FROM flights WHERE id=?"
    return execute_query(query, (flight_id,))