# Single entry point used by GUI/API

# call engine/normalize.py
# call parsing/* to produce a "plan" (or directly an eval-ready structure)
# calls a dispatcher that invokes engine/ops/*
# returns a standardized CalculationResult from `engine/models.py
