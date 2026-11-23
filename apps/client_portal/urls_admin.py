from django.urls import path

from . import views_admin

app_name = "client_portal_admin"

urlpatterns = [
    path("", views_admin.client_list, name="client_list"),
    path("invite/", views_admin.invite_client, name="invite_client"),
    path("direct-link/", views_admin.direct_link, name="direct_link"),
    path("<uuid:membership_id>/direct-link/", views_admin.direct_link_for_member, name="direct_link_for_member"),
    path("<uuid:membership_id>/send-link/", views_admin.send_magic_link, name="send_magic_link"),
    path("<uuid:membership_id>/remove/", views_admin.remove_client, name="remove_client"),
]
