import webbrowser

url = "http://127.0.0.1:8000/index.html"

try:
    opened = webbrowser.open(url)
    if opened:
        print("Opened game in browser:", url)
    else:
        print("Could not open browser automatically. Please open this URL manually:", url)
except Exception as exc:
    print("Could not open browser automatically:", exc)
    print("Please open this URL manually:", url)
