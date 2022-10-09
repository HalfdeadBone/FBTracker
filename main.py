from bot import *

if __name__ == "__main__":
    try:
        f = Mobile_fbBot()
        f.RecoverData()
        f.LoadCookie()
        while True:
            response = requests.get('https://www.facebook.com')
            if response.status_code == 200:
                print(InfoMsg("Connected To Facebook"))
                f.LoadSite()
                while True:
                    f.NewDataHolding()
                    f.TempFiles()
                    time.sleep(60)

            else:
                print(ErrorMsg("Couldnt connect to Facebook. New try in 60 seconds"))
                time.sleep(60)
    except KeyboardInterrupt:
        print('\n')
        print(InfoMsg("Clossing Bot, Saving Progress"))
        f.ClosingSequence()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)