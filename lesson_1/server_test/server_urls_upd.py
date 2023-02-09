from dataclasses import dataclass
from server_views import View

@dataclass
class Url:
    path: str
    view: View
