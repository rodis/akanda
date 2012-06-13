from twisted.application.service import ServiceMaker


AkandaRESTAService = ServiceMaker(
    "Akanda REST Server",
    "akanda.service",
    "DreamHost REST API Server for Akanda/Layer 3 Support",
    "akanda")
