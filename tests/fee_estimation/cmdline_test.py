from __future__ import annotations

import subprocess
import sysconfig
from pathlib import Path
from typing import Tuple, Union

from click.testing import CliRunner

from tad.cmds.tad import cli
from tad.full_node.full_node_api import FullNodeAPI
from tad.server.server import TadServer
from tad.simulator.block_tools import BlockTools
from tad.simulator.full_node_simulator import FullNodeSimulator


def test_print_fee_info_cmd(
    one_node_one_block: Tuple[Union[FullNodeAPI, FullNodeSimulator], TadServer, BlockTools]
) -> None:
    _, _, _ = one_node_one_block
    scripts_path = Path(sysconfig.get_path("scripts"))
    subprocess.run([scripts_path.joinpath("tad"), "show", "-f"], check=True)


def test_show_fee_info(
    one_node_one_block: Tuple[Union[FullNodeAPI, FullNodeSimulator], TadServer, BlockTools]
) -> None:
    _, _, _ = one_node_one_block
    runner = CliRunner()
    result = runner.invoke(cli, ["show", "-f"])
    assert result.exit_code == 0
