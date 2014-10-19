info = {
  'name': 'cal/61A/fa14/proj3',
  'params': {
    'doctest': {
      'cache': r"""
      from ants import *
      import ants
      import imp
      """,
      'setup': r"""
      hive, layout = Hive(make_test_assault_plan()), test_layout
      colony = AntColony(None, hive, ant_types(), layout)
      """
    }
  },
  'src_files': [
    'ants.py'
  ],
  'version': '1.0'
}