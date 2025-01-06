from playwright.async_api import async_playwright
import pytest_asyncio


@pytest_asyncio.fixture(scope="function")
async def api_request_context():
    '''Фикстура для создания контекста запроса'''
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        yield request_context
        await request_context.dispose()
