from flask import Flask, render_template, request, jsonify
import csv
from io import StringIO
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_data', methods=['POST'])
def save_data():
    if request.method == 'POST':
        data = request.json  # 클라이언트에서 받은 데이터

        file_path = 'data.csv'
        is_empty = os.stat(file_path).st_size == 0 


        # 데이터를 CSV 형식으로 작성
        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)
        
        if is_empty:
            csv_writer.writerow(['Name', 'Time'])  # CSV 파일 헤더

        # 받은 데이터를 CSV 파일에 추가
        csv_writer.writerow([data['Name'], data['Time']])

        # CSV 파일 저장
        with open('data.csv', 'a', newline='') as file:
            file.write(csv_data.getvalue())

        return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
