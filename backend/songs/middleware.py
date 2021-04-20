class AudioMiddleware:
    """
    Middleware provided for setting headers for audio files in DEBUG mode
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if response.get("CONTENT-TYPE") == "audio/mpeg":
            response.setdefault("ACCEPT-RANGES", "bytes")

        return response
