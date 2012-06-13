from twisted.web import resource


class RESTAPIBase(object):
    """
    Base class for the controllers used by the REST service.

    This (and any subclasses) is what constitutes the API.

    The general guidelines that should be used for defining API methods,
    establishing the URLs with which they are associated, and the HTTP
    method(s) that will access them are outlined with the following:

    * For Collections (e.g., /
    """


class RenderableRESTAPIBase(resource.Resource):
    """
    The base class for REST API classes.

    This class isn't currently used, but if we want to do object dispatch
    instead of routes, this would be the way to go.
    """
    def render_GET(self, request):
        """
        """

    def render_PUT(self, request):
        """
        """

    def render_POST(self, request):
        """
        """
        return self.render_GET(request)

    def render_DELETE(self, request):
        """
        """

    def render_PATCH(self, request):
        """
        This one's for you, Mark.
        """
