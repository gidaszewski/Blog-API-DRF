from rest_framework.routers import DefaultRouter
from api.views import PostApiViewSet

# routes
router_posts = DefaultRouter()

router_posts.register(prefix="post", basename="post", viewset=PostApiViewSet)
