#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""initialize blueprint for api"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
<<<<<<< HEAD
=======
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
>>>>>>> 3e1910784406a73baa2ef096d8da0e16c6dbec33
# from api.v1.views.users import *
# from api.v1.views.places import *
# from api.v1.views.places_reviews import *
# from api.v1.views.places_amenities import *
<<<<<<< HEAD
# from api.v1.views.states import *
# from api.v1.views.cities import *
# from api.v1.views.amenities import *
=======
>>>>>>> 3e1910784406a73baa2ef096d8da0e16c6dbec33
