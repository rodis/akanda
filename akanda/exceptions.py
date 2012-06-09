class Error(Exception):
    """
    A base class for exceptions.
    """
    def __init__(self, msg=None):
        if msg == None:
            msg = self.__doc__.strip()
        super(Error, self).__init__(msg)


class PermissionDenied(Error):
    """
    You must be root to make changes to pf.
    """


class UnsupportedIOCTL(Error):
    """
    Is the pf device correct?
    """

class OperationNotSupported(Error):
    pass
