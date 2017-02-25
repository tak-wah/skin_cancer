import os

from api.SkinCancerApi import SkinCancerApi as api

#entry point to fire up the app
def main():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    port = 8000

    app = api(__name__, specification_dir=root_dir + '/swagger/',
                        port=port,
                        api_file='skin-cancer-api.yaml')
    app.run()


if __name__ == '__main__':
    main()
