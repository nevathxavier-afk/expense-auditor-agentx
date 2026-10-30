"""Tool registry. To add a tool: subclass Tool in a new file, then add it to build_tools()."""


class Tool:
    name = "tool"
    description = ""
    args_doc = "{}"

    def execute(self, **kwargs):
        raise NotImplementedError


def build_tools():
    from tools.calculator import Calculator
    from tools.data_query import ListFiles, ReadFile, SqlQuery
    from tools.web_search import WebSearch
    from tools.auditor_tool import AuditTransactions
    from tools.blockchain_tool import MineAuditBlock, VerifyBlockchain
    from tools.budget_tool import RebalanceBudget

    tools = [
        ListFiles(),
        ReadFile(),
        SqlQuery(),
        Calculator(),
        WebSearch(),
        AuditTransactions(),
        MineAuditBlock(),
        VerifyBlockchain(),
        RebalanceBudget()
    ]
    return {t.name: t for t in tools}
