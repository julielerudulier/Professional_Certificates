import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    check = db.execute("SELECT * FROM balance WHERE username_id = ?", user_id)
    if len(check) != 0:
        stocks = db.execute(
            "SELECT SUM(shares) AS shares, symbol FROM transactions WHERE username_id = ? GROUP BY symbol",
            user_id,
        )
        balance = db.execute(
            "SELECT * FROM balance WHERE username_id = ? ORDER BY transaction_id DESC",
            user_id,
        )
        balance = balance[0]["balance"]
        stock_value = 0
        for stock in stocks:
            quote = lookup(stock["symbol"])
            stock["price"] = quote["price"]
            stock_value = (stock["price"] * stock["shares"]) + stock_value
        return render_template(
            "index.html", stocks=stocks, balance=balance, stock_value=stock_value
        )
    elif len(check) == 0:
        balance = 10000
        stock_value = 0
        return render_template("index.html", balance=balance, stock_value=stock_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        symbol = symbol.upper()
        shares = request.form.get("shares")
        if not symbol or not shares:
            return apology("All fields must be filled in")
        for i in shares:
            if not i.isdigit():
                return apology("Please enter a number superior to 0")
        if int(shares) < 1:
            return apology("Please enter a number superior to 0")
        quote = lookup(symbol)
        if quote == None:
            return apology("Oops... Are you sure this symbol exists?")
        price = float(quote["price"])
        user_id = session["user_id"]
        total = price * int(shares)
        check = db.execute("SELECT * FROM balance WHERE username_id = ?", user_id)
        if len(check) != 0:
            check_balance = db.execute(
                "SELECT * FROM balance WHERE username_id = ? ORDER BY transaction_id DESC",
                user_id,
            )
            credit = check_balance[0]["balance"]
            if credit >= total:
                balance = credit - total
                action = "Bought"
                db.execute(
                    "INSERT INTO transactions (symbol, shares, quote, total, username_id, action) VALUES(?, ?, ?, ?, ?, ?)",
                    symbol,
                    shares,
                    price,
                    total,
                    user_id,
                    action,
                )
                rows = db.execute(
                    "SELECT * FROM transactions WHERE username_id = ? ORDER BY transaction_id DESC",
                    user_id,
                )
                transaction_id = rows[0]["transaction_id"]
                db.execute(
                    "INSERT INTO balance (username_id, transaction_id, orders, balance) VALUES(?, ?, ?, ?)",
                    user_id,
                    transaction_id,
                    total,
                    balance,
                )
                return redirect("/")
            elif credit < total:
                return apology(
                    "You do not have enough credit to buy such quantity of stock"
                )
        elif len(check) == 0:
            if 10000 >= total:
                balance = 10000 - total
                action = "Bought"
                db.execute(
                    "INSERT INTO transactions (symbol, shares, quote, total, username_id, action) VALUES(?, ?, ?, ?, ?, ?)",
                    symbol,
                    shares,
                    price,
                    total,
                    user_id,
                    action,
                )
                rows = db.execute(
                    "SELECT * FROM transactions WHERE username_id = ? ORDER BY transaction_id DESC",
                    user_id,
                )
                transaction_id = rows[0]["transaction_id"]
                db.execute(
                    "INSERT INTO balance (username_id, transaction_id, orders, balance) VALUES(?, ?, ?, ?)",
                    user_id,
                    transaction_id,
                    total,
                    balance,
                )
                return redirect("/")
            elif check["balance"] < total:
                return apology(
                    "You do not have enough credit to buy such quantity of stock"
                )
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    rows = db.execute("SELECT * FROM transactions WHERE username_id = ?", user_id)
    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Please provide a username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Please provide a password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("Invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please enter stock symbol")
        quote = lookup(symbol)
        if quote == None:
            return apology("Oops... Are you sure this symbol exists?")
        return render_template(
            "quoted.html", price=quote["price"], symbol=quote["symbol"]
        )

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username or not password or not confirmation:
            return apology("All fields must be filled in.")
        if password != confirmation:
            return apology("Passwords do not match.")
        check = db.execute("SELECT username FROM users WHERE username = ?", username)
        if len(check) != 0:
            return apology(
                "This username is already taken. Please choose another username."
            )
        l, u, p, d = 0, 0, 0, 0
        specials = [
            "@",
            "#",
            "&",
            "§",
            "!",
            "?",
            "%",
            "$",
            "/",
            "+",
            "=",
            "-",
            "_",
            "*",
            "¥",
            "€",
            "£",
        ]
        if len(password) >= 8:
            for i in password:
                if i.islower():
                    l += 1
                if i.isupper():
                    u += 1
                if i.isdigit():
                    d += 1
                if i in specials:
                    p += 1
        if l == 0 or u == 0 or p == 0 or d == 0 or l + p + u + d != len(password):
            return apology(
                "The password must be at least 8 characters long and must contain at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 symbol."
            )
        hash = generate_password_hash(password)
        rows = db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)", username, hash
        )
        session["user_id"] = rows
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        stocks = db.execute(
            "SELECT SUM(shares) AS shares, symbol FROM transactions WHERE username_id = ? GROUP BY symbol",
            user_id,
        )
        return render_template("sell.html", stocks=stocks, user_id=user_id)

    elif request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Please select a stock symbol")
        if not shares:
            return apology("Please enter a number of shares superior to 0")
        for i in shares:
            if not i.isdigit():
                return apology("Please enter a number superior to 0")
            elif i.isdigit() and int(shares) <= 0:
                return apology("Please enter a number superior to 0")
        shares = int(shares)
        if shares > 0:
            user_id = session["user_id"]
            stocks = db.execute(
                "SELECT SUM(shares) AS shares, symbol FROM transactions WHERE username_id = ? GROUP BY symbol",
                user_id,
            )
            stock_list = []
            for stock in stocks:
                stock_list.append(stock["symbol"])
            if symbol in stock_list:
                getinfo = db.execute(
                    "SELECT SUM(shares) AS shares FROM transactions WHERE username_id = ? AND symbol = ? GROUP BY symbol",
                    user_id,
                    symbol,
                )
                if getinfo[0]["shares"] < shares:
                    return apology(
                        "Hmm... It seems you do not own that many shares of that stock"
                    )
                elif getinfo[0]["shares"] >= shares:
                    shares = shares * -1
                    quote = lookup(symbol)
                    price = float(quote["price"])
                    total = price * shares
                    action = "Sold"
                    db.execute(
                        "INSERT INTO transactions (symbol, shares, quote, total, username_id, action) VALUES(?, ?, ?, ?, ?, ?)",
                        symbol,
                        shares,
                        price,
                        total,
                        user_id,
                        action,
                    )
                    rows = db.execute(
                        "SELECT * FROM transactions WHERE username_id = ? ORDER BY transaction_id DESC",
                        user_id,
                    )
                    transaction_id = rows[0]["transaction_id"]
                    check_balance = db.execute(
                        "SELECT * FROM balance WHERE username_id = ? ORDER BY transaction_id DESC",
                        user_id,
                    )
                    balance = check_balance[0]["balance"]
                    balance = balance - total
                    db.execute(
                        "INSERT INTO balance (username_id, transaction_id, sellings, balance) VALUES(?, ?, ?, ?)",
                        user_id,
                        transaction_id,
                        total,
                        balance,
                    )
                    return redirect("/")
            else:
                return apology(
                    "Hmm... It seems you do not own any shares of that stock!"
                )
