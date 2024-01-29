#!/usr/bin/env python3
"""
Module Docs
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for a given page and page_size.
    Pages and indexes are 1-indexed.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
