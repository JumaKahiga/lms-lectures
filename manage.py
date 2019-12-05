from dotenv import load_dotenv
from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app
from app.models.person_model import User, Admin


app = create_app('config')


@app.cli.command('migrate')
def migrate():
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()

    return True


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, host='0.0.0.0')
