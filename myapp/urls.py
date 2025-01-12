"""evidanceprotection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [


    path('login/',views.login),
    path('login_post/',views.login_post),
    path('adminHome/',views.adminHome),
    path('ChangePassword/',views.ChangePassword),
    path('ChangePassword_post/',views.ChangePassword_post),
    path('Add_Investigator/',views.Add_Investigator),
    path('Add_Investigator_post/',views.Add_Investigator_post),
    path('View_Investigator/',views.View_Investigator),
    path('View_Investigator_post/',views.View_Investigator_post),
    path('Edit_Investigator/<id>',views.Edit_Investigator),
    path('Edit_Investigator_post/',views.Edit_Investigator_post),
    path('delete_Investigator/<id>',views.delete_Investigator),
    path('View_Case/',views.View_Case),
    path('View_Case_post/',views.View_Case_post),
    path('View_Evidane/',views.View_Evidane),
    path('View_Evidance_post/',views.View_Evidance_post),
    path('View_Users/',views.View_Users),
    # path('View_Users_post/',views.View_Users),
    path('View_complaints/',views.View_complaints),
    path('View_complaints_post/',views.View_complaints_post),
    path('send_reply_get/<id>',views.send_reply_get),
    path('SendReply_post/',views.SendReply_post),
    path('View_Feedback/',views.View_Feedback),
    path('View_Feedback_post/',views.View_Feedback_post),
    path('Logout/',views.Logout),

# ------------------ investigator ---------------- #

    path('InvestigatorHome/',views.InvestigatorHome),
    path('inves_View_Users/',views.inves_View_Users),
    path('Investigator_Profile/',views.Investigator_Profile),
    path('ADD_Case_get/',views.ADD_Case_get),
    path('ADD_Case_Post/',views.ADD_Case_Post),
    path('Add_Victim_or_sus_post/',views.Add_Victim_or_sus_post),
    path('View_Victim/<id>',views.View_Victim),
    path('View_Suspect/<id>',views.View_Suspect),
    path('Investigator_View_Case/',views.Investigator_View_Case),
    path('Investigator_View_Case_post/',views.Investigator_View_Case_post),
    path('Edit_Case_get/<id>',views.Edit_Case_get),
    path('Edit_Case_post/',views.Edit_Case_post),
    path('Delete_Case/<id>',views.Delete_Case),
    path('Investigator_Add_Evidance/',views.Investigator_Add_Evidance),
    path('Investigator_Add_Evidance_post/',views.Investigator_Add_Evidance_post),
    path('View_Complaint_Users/',views.View_Complaint_Users),
    path('View_complaints_Users_post/',views.View_complaints_Users_post),
    path('reject_complaint/<id>',views.reject_complaint),
    path('accept_complaint/<id>',views.accept_complaint),
    path('View_Approved_Complaint_Users/',views.View_Approved_Complaint_Users),
    path('View_Approved_Complaint_Users_post/',views.View_Approved_Complaint_Users_post),
    path('View_Rejected_Complaint_Users/',views.View_Rejected_Complaint_Users),
    path('View_Rejected_Complaint_Users_post/',views.View_Rejected_Complaint_Users_post),
    path('Take_Action_get/<id>',views.Take_Action_get),
    path('Take_Action_Post/',views.Take_Action_Post),
    path('View_Action/<id>',views.View_Action),
    path('Edit_Action_get/<id>',views.Edit_Action_get),
    path('Edit_Action_post/',views.Edit_Action_post),
    path('delete_action/<id>',views.delete_action),
    path('chat1/',views.chat1),
    path('chat_view/',views.chat_view),
    path('chat_send/',views.chat_send),
    path('Investigator_ChangePassword/',views.Investigator_ChangePassword),
    path('Investigator_ChangePassword_post/',views.Investigator_ChangePassword_post),
    # path('Investigator_View_Complaints/<id>',views.Investigator_View_Complaints),


# ================== user ==================


    path('user_signup/', views.user_signup),
    path('user_edit_profile/', views.user_edit_profile),
    path('user_login/', views.user_login),
    path('user_view_profile/', views.user_view_profile),
    path('user_view_investigator/', views.user_view_investigator),
    path('view_case/', views.view_case),
    path('view_evidance/', views.view_evidance),
    path('send_own_complaint/', views.send_own_complaint),
    path('view_action/', views.view_action),
    path('send_feedback/', views.send_feedback),
    path('change_password/', views.change_password),
    path('chat_send_by_user/', views.chat_send_by_user),
    path('chat_view_and/', views.chat_view_and),
    path('view_complaint/', views.view_complaint),
    # path('send_case_complaint/', views.send_case_complaint),

]
