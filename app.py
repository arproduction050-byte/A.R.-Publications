from flask import Flask, render_template

app = Flask(__name__)

# ==========================================
#   MAIN WEBSITE ROUTES
# ==========================================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('./books')
def books():
    return render_template('index.html')

@app.route('./about')
def about():
    return render_template('about.html')

# ==========================================
#   PRODUCT ROUTES (Inside 'products/' folder)
# ==========================================

@app.route('./sanatan-the-eternal-way')
def book_eternal_way():
    return render_template('products/book_eternal_way.html')

@app.route('./sanatan-birth-till-death')
def book_birth_death():
    return render_template('products/book_birth_death.html')

@app.route('./sanatan-hindi-edition')
def book_hindi_edition():
    return render_template('products/book_hindi_edition.html')

@app.route('./the-vankari-debt')
def book_vankari():
    return render_template('products/book_vankari.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)