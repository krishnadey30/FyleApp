import falcon,json
import jwt
import os
from task import bankDetails, branchDetails
from generate_tokens import genearte

secret = os.environ['SECRET']
#sh1 hash for fyle
def token_is_valid(token, account_id):
		token = bytes(token,"utf-8")
		try:
			detail = jwt.decode(token, secret, algorithms=['HS256'])
			if detail['name'] == account_id:
				return True  # Suuuuuure it's valid...
			else:
				return False
		except:
			return False	

def checkAuthToken(token, account_id):
    if token is None:
        description = ('Please provide an auth token '
                        'as part of the request.')

        raise falcon.HTTPUnauthorized('Auth token required',
                                        description)

    if not token_is_valid(token, account_id):
        description = ('The provided auth token is not valid. '
                        'Please request a new token and try again.')

        raise falcon.HTTPUnauthorized('Authentication required',
                                        description)


class SearchBank(object):
    def on_get(self, req, resp):
        doc = {}
        token = req.get_header('Authorization')
        account_id = req.get_header('username')
        #authenticating the id
        checkAuthToken(token, account_id)
        
        ifsc=req.get_param('ifsc',required = True)
        bankDetail = bankDetails(ifsc)
        doc['bank_detail']=bankDetail
        resp.body = json.dumps(doc, ensure_ascii = False)
        resp.status = falcon.HTTP_200

    
class SearchBranch(object):
    def on_get(self, req, resp):
        doc = {}
        token = req.get_header('Authorization')
        account_id = req.get_header('username')
        #authenticating the id
        checkAuthToken(token, account_id)
        
        bank_name = req.get_param('bank_name',required = True)
        city = req.get_param('city',required = True)
        offset = req.get_param('offset')
        limit = req.get_param('limit')
        if offset is None:
            offset = 0
        if limit is None:
            limit = 10

        branches = branchDetails(bank_name, city, limit, offset)
        doc['branches']=branches
        resp.body = json.dumps(doc, ensure_ascii = False)
        resp.status = falcon.HTTP_200

class Generate(object):
    def on_get(self, req, resp):
        doc = {}
        name = req.get_param('name', required = True)
        doc['token'] = genearte(name)
        resp.body = json.dumps(doc, ensure_ascii = False)
        resp.status = falcon.HTTP_200