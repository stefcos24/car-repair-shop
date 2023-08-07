from typing import Set, List


class FixtureBuilder:
    def __init__(self) -> None:
        self._needed: Set[str] = set()
        self._ordered: List[str] = ["test_person_user", "test_customer"]

    def person_user(self):
        self._needed.update({"test_person_user"})
        return self

    def customer(self):
        self._needed.update(({"test_customer"}))
        return self

    def build(self) -> List[str]:
        fixtures: List[str] = []

        self._verify_fixture_names()

        for possible_feature in self._ordered:
            if possible_feature in self._needed:
                fixtures.append(possible_feature)

        return fixtures

    def _verify_fixture_names(self):
        for fixture in self._needed:
            if fixture not in self._ordered:
                raise ValueError(f"Wrong fixture name '{fixture}'.")
