from abc import ABC, abstractmethod
from sqlalchemy.sql.selectable import Select

from ddpui.datainsights.query_builder import AggQueryBuilder
from ddpui.datainsights.warehouse.warehouse_interface import WarehouseType


class ColInsight(ABC):
    """
    Interface
    All column insight should implement this interface/abstract class
    Basically returns a sql query to be executed and once executed it parses the result for that query
    """

    def __init__(
        self,
        column_name: str,
        db_table: str,
        db_schema: str,
        filter: dict = None,
        wtype: str = None,
    ):
        self.column_name: str = column_name
        self.builder: AggQueryBuilder = AggQueryBuilder()
        self.db_table: str = db_table
        self.db_schema: str = db_schema
        self.filter = filter
        self.wtype = wtype

    @abstractmethod
    def generate_sql(self) -> Select:
        pass

    @abstractmethod
    def parse_results(self, result: list[dict]):
        pass

    def chart_type(self) -> str:
        return None


class DataTypeColInsights(ABC):
    """
    Class that maintains a list of ColInsight for a column of particular type
    """

    def __init__(
        self,
        column_name: str,
        db_table: str,
        db_schema: str,
        filter: dict = None,
        wtype: str = None,
    ):
        self.column_name: str = column_name
        self.db_table: str = db_table
        self.db_schema: str = db_schema
        self.insights: list[ColInsight] = []
        self.filter = filter
        self.wtype = WarehouseType.POSTGRES  # default

    @abstractmethod
    def generate_sqls(self) -> list[Select]:
        pass

    @abstractmethod
    def merge_output(self, results: list[dict]):
        pass

    @abstractmethod
    def get_col_type(self) -> str:
        """Returns the translated data type"""
        pass
