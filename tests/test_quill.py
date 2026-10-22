"""DevProject's tests: the manifest, against the real record store and gate.

DevProject has no code: its projects, board and secrets are kit screens.
What a list of projects does on a machine (`cm devproject init`, `update`,
`clone`, `secrets`) is Cloudmorrow's, and tested there.
"""

import pytest

from cloudmorrow.quill.testing import Harness


@pytest.fixture()
def q():
    with Harness(".") as harness:
        yield harness


def test_a_project_has_its_repository_and_vault(q):
    q.seed("project", {"name": "myapp", "devproject.repo": "git@github.com:me/myapp.git", "devproject.vault": "myapp"})
    (project,) = q.list("project", **{"devproject.vault": "myapp"})
    assert project["devproject.repo"] == "git@github.com:me/myapp.git"


def test_each_project_has_a_board_of_its_own(q):
    mine = q.seed("project", name="myapp")
    other = q.seed("project", name="other")
    q.seed("devproject.card", project=mine.id, title="Ship the login", lane="doing")
    q.seed("devproject.card", project=other.id, title="Not this one")
    cards = q.list("devproject.card", project=mine.id)
    assert [(c["title"], c["lane"]) for c in cards] == [("Ship the login", "doing")]


def test_cards_go_with_their_project(q):
    mine = q.seed("project", name="myapp")
    q.seed("devproject.card", project=mine.id, title="Ship the login")
    q.delete("project", mine.id)
    assert q.list("devproject.card") == []
