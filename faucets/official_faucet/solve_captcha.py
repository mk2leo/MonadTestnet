import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = 'YOUR_2CAPTCHA_API'

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6Le4e90qAAAAAFmgNU7C2dwxuRHj9lO7x54cKaJt',
        url='https://testnet.monad.xyz/'
    )
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)
else:
    print(json.dumps(result))