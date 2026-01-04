"""Scenario plugin system for Security Arena"""

from .base import ScenarioPlugin
from .registry import list_scenarios, load_scenario, register_scenario

# from .portfolioiq import PortfolioIQPlugin
# from .thingularity import ThingularityPlugin
# from .example_medical import MedicalRecordsPlugin

__all__ = ["ScenarioPlugin", "load_scenario", "list_scenarios", "register_scenario"]
