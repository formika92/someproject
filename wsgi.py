# from blog.app import app
#
# if __name__ == '__main__':
#     app.run(
#         host='0.0.0.0',
#         debug=True,
#     )
#
#
# def util():
#     pass
from blog.app import create_app

app = create_app()
