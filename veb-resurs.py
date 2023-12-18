from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run_process', methods=['POST'])
def run_process():
    process_name = request.form['process_name']
    try:
        subprocess.Popen(process_name)
        return 'Process {} started'.format(process_name)
    except Exception as e:
        return 'Error starting process {}: {}'.format(process_name, str(e))

if __name__ == '__main__':
    app.run()



