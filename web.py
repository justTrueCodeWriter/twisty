from twisty import app

if __name__ == "__main__":
    app.run(host=app.config["SERVER_DOMAIN"],
            port=app.config["SERVER_PORT"],
            debug=app.config["DEBUG"])
