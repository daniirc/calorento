import logging
from dataclasses import dataclass

import httpx

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class WeatherInfo:
    city: str
    state: str

    temperature: float
    thermal: float
    humidity: float
    wind: str
    pressure: str

    description: str


async def get_weather(city_id: str) -> WeatherInfo:
    pass
