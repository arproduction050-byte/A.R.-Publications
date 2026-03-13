import os
import csv
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Secret key for flash messages
app.secret_key = 'ar-publications-secure-key-2026'

# --- DATA FILE SETUP FOR CONTACT FORM ---
DATA_DIR = os.path.join(app.root_path, 'data')
os.makedirs(DATA_DIR, exist_ok=True)
CONTACT_FILE = os.path.join(DATA_DIR, 'contacts.csv')

# Create the CSV file with headers if it doesn't exist
if not os.path.exists(CONTACT_FILE):
    with open(CONTACT_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Name', 'Email', 'Subject', 'Message'])

# ==========================================
#   MAIN WEBSITE ROUTES (Root Templates)
# ==========================================

@app.route('/')
def home():
    """Renders the main A.R. Publications Storefront (your superb cinematic design)."""
    return render_template('index.html')

@app.route('/books')
def books():
    """Keeps the url_for('books') links working by redirecting them to the main page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the Author & Contact page."""
    return render_template('about.html')

# ==========================================
#   PRODUCT ROUTES (Inside 'products/' folder)
# ==========================================

@app.route('/sanatan-the-eternal-way')
def book_eternal_way():
    # Added 'products/' before the filename
    return render_template('products/book_eternal_way.html')

@app.route('/sanatan-birth-till-death')
def book_birth_death():
    # Added 'products/' before the filename
    return render_template('products/book_birth_death.html')

@app.route('/sanatan-hindi-edition')
def book_hindi_edition():
    # Added 'products/' before the filename
    return render_template('products/book_hindi_edition.html')

@app.route('/the-vankari-debt')
def book_vankari():
    # Added 'products/' before the filename
    return render_template('products/book_vankari.html')

# ==========================================
#   CONTACT FORM HANDLING
# ==========================================

@app.route('/contact', methods=['POST'])
def contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject', 'A.R. Publications Inquiry') 
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Please fill in all required fields.', 'error')
            return redirect(request.referrer or url_for('home'))

        with open(CONTACT_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, email, subject, message])

        flash('Your message has been sent successfully! We will get back to you soon.', 'success')
        return redirect(request.referrer or url_for('home'))

    except Exception as e:
        print(f"Error saving contact: {e}")
        flash('Something went wrong. Please try again later.', 'error')
        return redirect(request.referrer or url_for('home'))

# --- MAIN BLOCK ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)