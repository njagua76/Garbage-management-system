"""
this file handles the connection to the postgreSQL database and sets 
up all the required tables for my system.
"""
import psycopg2
def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="garbage_db",
            user="njagua",
            password="mypassword",   
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)

def create_tables():
    """This function creates tables if they don't exist."""
    conn = get_connection()
    cur = conn.cursor()

    # SQL commands to create tables
    cur.execute("""
        CREATE TABLE IF NOT EXISTS apartments (
            apartment_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            location VARCHAR(100)
        );
        CREATE TABLE IF NOT EXISTS tenants (
            tenant_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            house_number VARCHAR(20),
            phone_number VARCHAR(20),
            apartment_id INTEGER REFERENCES apartments(apartment_id) ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS garbage_bags (
            bag_id SERIAL PRIMARY KEY,
            tenant_id INTEGER REFERENCES tenants(tenant_id) ON DELETE CASCADE,
            month VARCHAR(20),
            number_of_bags INTEGER DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS payments (
            payment_id SERIAL PRIMARY KEY,
            tenant_id INTEGER REFERENCES tenants(tenant_id) ON DELETE CASCADE,
            amount DECIMAL(10, 2),
            payment_date DATE DEFAULT CURRENT_DATE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Tables verified or created successfully!")

