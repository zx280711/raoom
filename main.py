from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>رعوم</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #0f172a;
                    color: white;
                    text-align: center;
                    padding: 60px;
                }
                h1 {
                    font-size: 48px;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 20px;
                    color: #94a3b8;
                }
                .box {
                    margin-top: 40px;
                    padding: 30px;
                    background: #1e293b;
                    border-radius: 12px;
                }
                .btn {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 12px 25px;
                    background: #22c55e;
                    color: black;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>رعوم</h1>
            <p>منصة ذكية لاكتشاف الاحتيال قبل حدوثه</p>
            <div class="box">
                <h2>نظام كشف الاحتيال اللحظي</h2>
                <p>نوفر على شركات التأمين ملايين الريالات سنويًا عبر تحليل الأنماط المشبوهة قبل الموافقة على المطالبات.</p>
                <a href="#" class="btn">اطلب عرض تجريبي</a>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
