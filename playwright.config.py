from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.config import PlaywrightTestConfig

config = PlaywrightTestConfig(
    use={
        "viewport": {"width": 1920, "height": 1080}, 
    }
)