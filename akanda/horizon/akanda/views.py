from horizon import tabs

from tabs import NetworkingTabs


class IndexView(tabs.TabbedTableView):
    template_name = 'akanda/index.html'
    tab_group_class = NetworkingTabs

    def get_data(self, request, context, *args, **kwargs):
        return context
