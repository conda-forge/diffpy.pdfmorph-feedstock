#!/usr/bin/env python

import pytest

if __name__ == "__main__":
    exit_code = pytest.main(["-v"])
    assert exit_code == 0
