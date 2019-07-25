import falcon

api = application = falcon.API()
from bank import SearchBank,SearchBranch, Generate

bank = SearchBank()
branch = SearchBranch()
key = Generate()
# Add a route to serve the resource
api.add_route('/bank',bank)
api.add_route('/branch',branch)
api.add_route('/generate',key)