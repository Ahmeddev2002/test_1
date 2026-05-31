from __future__ import annotations

import datetime as dt

from django.conf import settings


def tax_year_bounds(year: int) -> tuple[dt.date, dt.date]:
    """Return the (start, end) dates for Pakistani tax year `year`.

    Tax year 2025 = 1 July 2024 to 30 June 2025.
    """
    start = dt.date(year - 1, settings.TAX_YEAR_START_MONTH, settings.TAX_YEAR_START_DAY)
    # End is the day before the next year's start.
    next_start = dt.date(year, settings.TAX_YEAR_START_MONTH, settings.TAX_YEAR_START_DAY)
    end = next_start - dt.timedelta(days=1)
    return start, end
