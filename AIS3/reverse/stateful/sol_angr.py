import angr
import claripy
import logging
logging.getLogger('angr.sim_manager').setLevel(logging.DEBUG)
proj = angr.Project('./stateful', auto_load_libs=False)
sym_argv = claripy.BVS('sym_argv', 8 * 43)
prefix = claripy.BVV(b'AIS3{')
suffix_length = 43 - len(b'AIS3{')
suffix = claripy.BVS('sym_argv_suffix', 8 * suffix_length)
combined_sym_argv = claripy.Concat(prefix, suffix)
constraint = sym_argv == combined_sym_argv
state = proj.factory.entry_state(args=[proj.filename, sym_argv])
state.add_constraints(constraint)
simgr = proj.factory.simulation_manager(state)
simgr.explore(find=lambda s: b'Correct!!!' in s.posix.dumps(1))
if len(simgr.found) > 0:
    print(simgr.found[0].solver.eval(sym_argv, cast_to=bytes) )
else:
    print("No!")