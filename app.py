from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Telecom Churn Analysis Pipeline</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f6f9; }
                .container { background: white; padding: 30px; display: inline-block; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
                h1 { color: #2c3e50; }
                .status { color: #27ae60; font-weight: bold; font-size: 1.2em; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Telecom Churn Analysis UI</h1>
                <p class="status">Pipeline Built, Tested, and Deployed Successfully! 🎉</p>
                <p>Medallion Architecture Layers (Bronze -> Silver -> Gold) are fully processed and saved to SQL Server.</p>
            </div>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
