import pytest
from sqlalchemy import insert, select

from auth.models import role
from conftest import client, async_session_maker


async def test_add_role():
    assert 1 == 1