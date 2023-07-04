from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='192.168.29.81', port=80)
