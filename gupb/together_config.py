from gupb.controller import aleph_aleph_zero
from gupb.controller import barabasz
from gupb.controller import dart
from gupb.controller import dzikie_borsuki
from gupb.controller import elvis
from gupb.controller import intercontinental_bajers
from gupb.controller import killer
from gupb.controller import lord_icon
from gupb.controller import shrek
from gupb.controller import sniezny_kockodan
from gupb.controller import spejson
from gupb.controller import tuptus

CONFIGURATION = {
    'arenas': [
        'lone_sanctum',
    ],
    'controllers': [
        aleph_aleph_zero.AlephAlephZeroBot("AA0"),
        barabasz.BarabaszController("BenadrylowyBarabasz"),
        dart.DartController("Dart", dart.strategy.AxeAndCenterStrategy()),
        dzikie_borsuki.DzikieBorsuki("DzikieBorsuki"),
        elvis.DodgeController("Elvis"),
        intercontinental_bajers.IntercontinentalBajers("IntercontinentalBajers"),
        killer.KillerController("Killer"),
        lord_icon.LordIcon("Marko"),
        shrek.ShrekController("Fiona"),
        sniezny_kockodan.SnieznyKockodanController("SnieznyKockodan"),
        spejson.Spejson("Spejson"),
        tuptus.TuptusController("CiCik"),
    ],
    'start_balancing': False,
    'visualise': False,
    'show_sight': None,
    'runs_no': 100,
}
