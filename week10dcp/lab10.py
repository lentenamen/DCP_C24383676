import tkinter as tk
from tkinter import ttk
import sqlite3

class SQLTableViewer(tk.Tk):
    """A Tkinter application to display and filter an SQL table."""

    def __init__(self, db_name=':memory:', table_name='products'):
        super().__init__()
        self.title("SQL Database Table Viewer (Tkinter)")
        self.db_name = db_name
        self.table_name = table_name

        # 1. Initialize Database and Table
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._setup_database()

        # 2. Setup the UI Layout
        self._create_widgets()
        
        # Load initial data
        self.load_data()

    def _setup_database(self):
        """Creates a sample table and populates it with data."""
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY,
                name TEXT,
                category TEXT,
                price REAL
            )
        """)
        
        # Clear existing data and insert sample data
        self.cursor.execute(f"DELETE FROM {self.table_name}")
        sample_data = [
            ('Laptop', 'Electronics', 1200.00),
            ('Desk Chair', 'Furniture', 150.99),
            ('Monitor', 'Electronics', 350.50),
            ('Keyboard', 'Accessories', 75.00),
            ('Mousepad', 'Accessories', 15.00),
            ('Dining Table', 'Furniture', 499.99),
        ]
        self.cursor.executemany(f"INSERT INTO {self.table_name} (name, category, price) VALUES (?, ?, ?)", sample_data)
        self.conn.commit()
        
    def _create_widgets(self):
        """Creates and packs all UI elements."""
        
        # --- Search Frame ---
        search_frame = ttk.Frame(self, padding="10")
        search_frame.pack(fill='x')

        ttk.Label(search_frame, text="Search Query:").pack(side='left', padx=(0, 5))
        
        # Text field for search
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        # Button to filter the table
        self.filter_button = ttk.Button(search_frame, text="Filter", command=self.filter_data)
        self.filter_button.pack(side='left')
        
        # Button to clear the filter
        self.clear_button = ttk.Button(search_frame, text="Clear Filter", command=self.clear_filter)
        self.clear_button.pack(side='left', padx=(10, 0))

        # --- Table Frame (Treeview) ---
        table_frame = ttk.Frame(self, padding="10")
        table_frame.pack(fill='both', expand=True)

        # Columns for the Treeview
        columns = ('ID', 'Name', 'Category', 'Price')
        
        # Create the Treeview
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings')
        self.tree.pack(side='left', fill='both', expand=True)

        # Setup column headings
        for col in columns:
            self.tree.heading(col, text=col, anchor='center')
            self.tree.column(col, width=100, anchor='center')
            
        # Add a Scrollbar
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side='right', fill='y')

    def clear_table(self):
        """Removes all items from the Treeview."""
        for item in self.tree.get_children():
            self.tree.delete(item)

    def load_data(self, query=""):
        """
        Fetches and loads data into the Treeview.
        If a query is provided, it filters the SQL results.
        """
        self.clear_table()
        
        # Base SQL command
        sql_command = f"SELECT id, name, category, price FROM {self.table_name}"
        params = []
        
        if query:
            # Add WHERE clause to search across Name and Category fields (case-insensitive)
            search_term = f'%{query}%'
            sql_command += " WHERE name LIKE ? OR category LIKE ?"
            params = [search_term, search_term]
        
        # Execute the query
        self.cursor.execute(sql_command, params)
        rows = self.cursor.fetchall()

        # Insert the data into the Treeview
        for row in rows:
            # Format the price column to two decimal places
            formatted_row = (row[0], row[1], row[2], f"${row[3]:.2f}")
            self.tree.insert('', 'end', values=formatted_row)

    def filter_data(self):
        """Reads the search entry and reloads data with the filter applied."""
        search_query = self.search_entry.get().strip()
        self.load_data(search_query)

    def clear_filter(self):
        """Clears the search entry and reloads all data."""
        self.search_entry.delete(0, tk.END)
        self.load_data()

    def on_closing(self):
        """Closes the database connection when the window is closed."""
        self.conn.close()
        self.destroy()

if __name__ == "__main__":
    app = SQLTableViewer()
    # Ensure the database connection is closed when the app exits
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()