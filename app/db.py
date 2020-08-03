from flask_sqlalchemy import SQLAlchemy


class Database:
    orm = SQLAlchemy()

    def init_app(self, app):
        """
        Init database on app context
        :param app:
        :return:
        """
        from app.commands import init_db_command

        app.cli.add_command(init_db_command)
        self.orm.init_app(app)




