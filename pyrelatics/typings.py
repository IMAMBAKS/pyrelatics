from typing import List, Dict, TypeVar, Tuple

# Typings
dict_or_list_dict = TypeVar('ROWS', dict, List[dict])
tuple_or_list_tuple = TypeVar('PARAMETER', Tuple[str, str], List[Tuple[str, str]], str)
