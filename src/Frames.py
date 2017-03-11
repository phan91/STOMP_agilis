NULL = '\x00'


class BaseFrame(object):
    # TODO: Handle optional headers
    headers={}
    required_headers=()

    def __init__(self,msg=None,**kwargs):
        self.msg = msg
        self.headers.update(kwargs)

    def has_required(self):
        if set(self.required_headers) <= self.headers.viewkeys():
            return True
        else:
            return False


class CONNECT(BaseFrame):
    """
    headers:
        REQUIRED: accept-version, host
        OPTIONAL: login, passcode, heart-beat
    """
    required_headers=("accept-version","host",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class STOMP(BaseFrame):
    """
    headers:
        REQUIRED: accept-version, host
        OPTIONAL: login, passcode, heart-beat
    """
    required_headers=("accept-version","host",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class CONNECTED(BaseFrame):
    """
    headers:
        REQUIRED: version
        OPTIONAL: session, server, heart-beat
    """
    required_headers=("version",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class SEND(BaseFrame):
    """
    headers:
        REQUIRED: destination
        OPTIONAL: transaction
    """
    required_headers=("destination",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class SUBSCRIBE(BaseFrame):
    """
    headers:
        REQUIRED: destination, id
        OPTIONAL: ack
    """
    required_headers=("destination", "id",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class UNSUBSCRIBE(BaseFrame):
    """
    headers:
        REQUIRED: id
        OPTIONAL: none
    """
    required_headers=("id",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class ACK(BaseFrame):
    """
    headers:
        REQUIRED: id
        OPTIONAL: transaction
    """
    required_headers=("id",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class NACK(BaseFrame):
    """
    headers:
        REQUIRED: id
        OPTIONAL: transaction
    """
    required_headers=("id",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class BEGIN(BaseFrame):
    """
    headers:
        REQUIRED: transaction
        OPTIONAL: none
    """
    required_headers=("transaction",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class COMMIT(BaseFrame):
    """
    headers:
        REQUIRED: transaction
        OPTIONAL: none
    """
    required_headers=("transaction",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class ABORT(BaseFrame):
    """
    headers:
        REQUIRED: transaction
        OPTIONAL: none
    """
    required_headers=("transaction",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class DISCONNECT(BaseFrame):
    """
    headers:
        REQUIRED: none
        OPTIONAL: receipt
    """

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class MESSAGE(BaseFrame):
    """
    headers:
        REQUIRED: destination, message-id, subscription
        OPTIONAL: ack
    """
    required_headers=("destination", "message-id", "subscription",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class RECEIPT(BaseFrame):
    """
    headers:
        REQUIRED: receipt-id
        OPTIONAL: none
    """
    required_headers=("receipt-id",)

    def __init__(self, **kwargs):
        BaseFrame.__init__(self, **kwargs)


class ERROR(BaseFrame):
    """
    headers:
        REQUIRED: none
        OPTIONAL: message
    """

    def __init__(self, **kwargs):
        BaseFrame.__init__(self)
        self.message = kwargs.get('message')
