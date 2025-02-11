from gupb.controller.aleph_aleph_zero.guarding_strategy import GuardingStrategy
from gupb.controller.aleph_aleph_zero.scanning_strategy import ScanningStrategy
from gupb.controller.aleph_aleph_zero.scouting_strategy import ScoutingStrategy
from gupb.controller.aleph_aleph_zero.shortest_path import build_graph, get_reachable
from gupb.controller.aleph_aleph_zero.strategy import Strategy
from gupb.controller.aleph_aleph_zero.travel_strategy import TravelStrategy
from gupb.controller.aleph_aleph_zero.utils import taxicab_distance
from gupb.model import characters


class MenhirRushStrategy(Strategy):
    def __init__(self, menhir_position):
        self.menhir_position = menhir_position

    def decide_and_proceed(self, knowledge, graph=None, **kwargs):
        if graph is None:
            graph = build_graph(knowledge)
        reachable = list(get_reachable(graph[(knowledge.position, knowledge.facing)]))

        reachable.sort(key=lambda x: taxicab_distance(x, self.menhir_position))
        best = reachable[0]

        if best==knowledge.position:
            if knowledge.position==self.menhir_position:
                return None, GuardingStrategy()
            else:
                return None, ScanningStrategy(self)

        return TravelStrategy(best, self).decide_and_proceed(knowledge, graph=graph)[0], self  # let Travel decide the path, but keep on being in charge


