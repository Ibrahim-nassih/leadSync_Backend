from django.urls import path
from .views import RegisterView,SpaceView,WorkflowView,WorkflowStepsAPIView,SpaceViewDetails
from .views import TransactionView,TeamView,MembershipView,TicketView,UsersView,TaskView,SprintView,TicketsSprintView
app_name = 'app1'
urlpatterns = [
    path('register',RegisterView.as_view()),
    path('space', SpaceView.as_view(), name='space'),
    path('workflow', WorkflowView.as_view(), name='space'),
    path('step', WorkflowStepsAPIView.as_view(), name='space'),
    path('steps/<int:id>', SpaceViewDetails.as_view(), name='steps_by_workflow'),
    path('transaction',TransactionView.as_view(),name='transactions'),
    path('team',TeamView.as_view(),name='team'),
    path('users',UsersView.as_view(),name='users'),
    path('member',MembershipView.as_view(),name='member'),
    path('ticket',TicketView.as_view(),name='ticket'),
    path('tasks',TaskView.as_view(),name='tasks'),
    path('sprint',SprintView.as_view(),name='sprint'),
    path('sprint/tickets',TicketsSprintView.as_view(),name='tickets_sprint')

]