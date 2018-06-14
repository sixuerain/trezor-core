# Automatically generated by pb2py
import protobuf as p


class StellarAccountMergeOp(p.MessageType):
    MESSAGE_WIRE_TYPE = 218
    FIELDS = {
        1: ('source_account', p.UnicodeType, 0),
        2: ('destination_account', p.UnicodeType, 0),
    }

    def __init__(
        self,
        source_account: str = None,
        destination_account: str = None
    ) -> None:
        self.source_account = source_account
        self.destination_account = destination_account
