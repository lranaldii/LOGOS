import pkg_resources
from typing import Dict, Type
from prompt_framework.core import LogosModule

def discover_modules() -> Dict[str, Type[LogosModule]]:
    """
    Discover external modules registered under the
    'logos_framework.modules' entry-point group.
    Returns a dict mapping class name -> class.
    """
    registry: Dict[str, Type[LogosModule]] = {}
    for ep in pkg_resources.iter_entry_points("logos_framework.modules"):
        ModuleClass = ep.load()
        registry[ModuleClass.__name__] = ModuleClass
    return registry
