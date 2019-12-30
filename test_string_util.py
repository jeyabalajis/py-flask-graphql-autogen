from utils.string_util import to_camel_case


class TestToCamelCase():
    def test_to_camel_case(self):
        assert to_camel_case("contract_header", True) == "ContractHeader"
        assert to_camel_case("movement_order", True) == "MovementOrder"
