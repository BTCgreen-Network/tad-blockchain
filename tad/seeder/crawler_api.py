from typing import Optional

import tad.server.ws_connection as ws
from tad.protocols import full_node_protocol, wallet_protocol
from tad.seeder.crawler import Crawler
from tad.server.outbound_message import Message
from tad.server.server import TadServer
from tad.util.api_decorators import api_request, peer_required


class CrawlerAPI:
    crawler: Crawler

    def __init__(self, crawler):
        self.crawler = crawler

    def __getattr__(self, attr_name: str):
        async def invoke(*args, **kwargs):
            pass

        return invoke

    @property
    def server(self) -> TadServer:
        assert self.crawler.server is not None
        return self.crawler.server

    @property
    def log(self):
        return self.crawler.log

    @peer_required
    @api_request
    async def request_peers(self, _request: full_node_protocol.RequestPeers, peer: ws.WSTadConnection):
        pass

    @peer_required
    @api_request
    async def respond_peers(
        self, request: full_node_protocol.RespondPeers, peer: ws.WSTadConnection
    ) -> Optional[Message]:
        pass

    @peer_required
    @api_request
    async def new_peak(self, request: full_node_protocol.NewPeak, peer: ws.WSTadConnection) -> Optional[Message]:
        await self.crawler.new_peak(request, peer)
        return None

    @api_request
    async def new_transaction(self, transaction: full_node_protocol.NewTransaction) -> Optional[Message]:
        pass

    @api_request
    @peer_required
    async def new_signage_point_or_end_of_sub_slot(
        self, new_sp: full_node_protocol.NewSignagePointOrEndOfSubSlot, peer: ws.WSTadConnection
    ) -> Optional[Message]:
        pass

    @api_request
    async def new_unfinished_block(
        self, new_unfinished_block: full_node_protocol.NewUnfinishedBlock
    ) -> Optional[Message]:
        pass

    @peer_required
    @api_request
    async def new_compact_vdf(self, request: full_node_protocol.NewCompactVDF, peer: ws.WSTadConnection):
        pass

    @api_request
    async def request_transaction(self, request: full_node_protocol.RequestTransaction) -> Optional[Message]:
        pass

    @api_request
    async def request_proof_of_weight(self, request: full_node_protocol.RequestProofOfWeight) -> Optional[Message]:
        pass

    @api_request
    async def request_block(self, request: full_node_protocol.RequestBlock) -> Optional[Message]:
        pass

    @api_request
    async def request_blocks(self, request: full_node_protocol.RequestBlocks) -> Optional[Message]:
        pass

    @api_request
    async def request_unfinished_block(
        self, request_unfinished_block: full_node_protocol.RequestUnfinishedBlock
    ) -> Optional[Message]:
        pass

    @api_request
    async def request_signage_point_or_end_of_sub_slot(
        self, request: full_node_protocol.RequestSignagePointOrEndOfSubSlot
    ) -> Optional[Message]:
        pass

    @peer_required
    @api_request
    async def request_mempool_transactions(
        self,
        request: full_node_protocol.RequestMempoolTransactions,
        peer: ws.WSTadConnection,
    ) -> Optional[Message]:
        pass

    @api_request
    async def request_block_header(self, request: wallet_protocol.RequestBlockHeader) -> Optional[Message]:
        pass

    @api_request
    async def request_additions(self, request: wallet_protocol.RequestAdditions) -> Optional[Message]:
        pass

    @api_request
    async def request_removals(self, request: wallet_protocol.RequestRemovals) -> Optional[Message]:
        pass

    @api_request
    async def request_puzzle_solution(self, request: wallet_protocol.RequestPuzzleSolution) -> Optional[Message]:
        pass

    @api_request
    async def request_header_blocks(self, request: wallet_protocol.RequestHeaderBlocks) -> Optional[Message]:
        pass
