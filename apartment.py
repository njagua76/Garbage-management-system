# apartment.py
# __define-ocg__
# This module manages all operations related to apartments.
# It interacts with the database (PostgreSQL) to perform CRUD operations.
# Author: Ann Gathoni (Project: Garbage Collection Management System)

import psycopg2
from database_utils import get_connection

varOcg = "ApartmentManager"

class Apartment:
    """
    The Apartment class represents an apartment record in the system.
    Each apartment has:
      - an id (auto-generated)
      - name (e.g., 'Sunrise Apartments')
      - location (e.g., 'Nairobi West')
      - total_units (number of houses in that apartment)
    """

    def __init__(self, name, location, total_units):
        self.name = name
        self.location = location
        self.total_units = total_units

    def save(self):
        """Save a new apartment record to the database."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO apartments (name, location, total_units)
                VALUES (%s, %s, %s)
                """,
                (self.name, self.location, self.total_units)
            )
            conn.commit()
            print(f"Apartment '{self.name}' added successfully!")
        except psycopg2.Error as e:
            print("Error inserting apartment:", e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def view_all():
        """Display all apartments stored in the database."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM apartments")
            apartments = cursor.fetchall()

            if apartments:
                print("\nList of Apartments:")
                print("-" * 40)
                for apt in apartments:
                    print(f"ID: {apt[0]} | Name: {apt[1]} | Location: {apt[2]} | Units: {apt[3]}")
                print("-" * 40)
            else:
                print("⚠️ No apartments found.")
        except psycopg2.Error as e:
            print("Error fetching apartments:", e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update(apartment_id, name=None, location=None, total_units=None):
        """Update an existing apartment’s details."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            # Dynamically build the query depending on what the user wants to update
            fields = []
            values = []

            if name:
                fields.append("name = %s")
                values.append(name)
            if location:
                fields.append("location = %s")
                values.append(location)
            if total_units:
                fields.append("total_units = %s")
                values.append(total_units)

            if not fields:
                print("⚠️ No updates specified.")
                return

            values.append(apartment_id)
            query = f"UPDATE apartments SET {', '.join(fields)} WHERE id = %s"

            cursor.execute(query, tuple(values))
            conn.commit()
            print(f"Apartment ID {apartment_id} updated successfully!")
        except psycopg2.Error as e:
            print("Error updating apartment:", e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete(apartment_id):
        """Delete an apartment by its ID."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM apartments WHERE id = %s", (apartment_id,))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"🗑️ Apartment ID {apartment_id} deleted successfully!")
            else:
                print(f"⚠️ No apartment found with ID {apartment_id}.")
        except psycopg2.Error as e:
            print("Error deleting apartment:", e)
        finally:
            cursor.close()
            conn.close()
