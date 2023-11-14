

import signal

from django.dispatch import Signal


meal_added = Signal("request")

meal_removed = Signal("request")