from dataclasses import dataclass
from typing import Optional

@dataclass
class QueryResult:
    success: bool
    rows_affected: int = 0
    # the value can either be str or None
    error_type: Optional[str] = None
    error_message : Optional[str] = None


class QueryExecutionFailedException(Exception):
    def __init__(self, raw_error: Exception):
        err_name  = raw_error.__class__.__name__
        msg = str(raw_error)
        self.result = QueryResult(
            success=False,
            rows_affected=0,
            error_type=err_name,
            error_message=msg
        )
        super().__init__(f"Databse query failed [{err_name}:{msg}]")
