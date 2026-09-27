from pathlib import Path
s=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_surface():
 for n in ['open_bench','transmit_check','get_bench','get_signals_page','get_benches_page','get_summary']:assert f'def {n}' in s
def test_guards():
 for n in ['actor in helpers','int(b.cursor)>=len(stages)','int(b.fuses)>=3','run_nondet_unsafe']:assert n in s
