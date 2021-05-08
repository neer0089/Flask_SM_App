# Run a test server.
from app.smapp import app, config_container

if __name__ == '__main__':
    app.run(host=config_container.config.sm.host(),
        port=config_container.config.sm.port(),
        debug=True
        )