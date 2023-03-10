from django.urls import path

from . import views

app_name = "ledgerapp"


urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("calender/", views.LedgerViewNew.as_view(), name="calendar"),
    path("new/", views.create_ledger, name="ledger_new"),
    path("itemnew/", views.create_item, name="item-new"),
    path("edit/<int:pk>/", views.LedgerEdit.as_view(), name="ledger_edit"),
    path("<int:ledger_id>/details/", views.ledger_details, name="ledger-detail"),
    path("all-ledger-list/", views.AllLedgersListView.as_view(), name="all_ledgers"),
    path(
            "<int:pk>/remove",
            views.delete_ledger,
            name="ledger-remove",
        ),
    path(
        "outcome-ledger-list/",
        views.OutcomeLedgersListView.as_view(),
        name="outcome-ledgers",
    ),
    path(
        "income-ledger-list/",
        views.IncomeLedgersListView.as_view(),
        name="income-ledgers",
    ),
]
