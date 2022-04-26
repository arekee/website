from django.contrib import admin

from .models import Basket
from .models import Comment
from .models import Hotel
from .models import Posts
from .models import Signup

admin.site.register(Signup)
admin.site.register(Posts)
admin.site.register(Hotel)
admin.site.register(Comment)
admin.site.register(Basket)
