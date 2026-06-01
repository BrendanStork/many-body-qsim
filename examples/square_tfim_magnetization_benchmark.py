import matplotlib.pyplot as plt
from src.circuit import Quantum_Circuit
from src.hamiltonian import general_hamiltonian, transverse_ising_hamiltonian
from src.lattices import squarelattice
from src.observables import observable_vs_time, magnetization
from src.plotting import (
    	plot_observable
)

# This version of the trotterization function uses a fixed number
# of trotter steps, rather than a fixed delta t (dt). This is
# to compare what times the trotterized method begins
# to diverge from the exact solution and by what degree for different
# numbers of repititions of trotter step operations.

# This means that for each time t_i, trotterization with that fixed
# number of steps N is implemented, with dt = t_i/N. dt increases
# as time increases, which is the source of error, with the function
# approching the exact solution as N -> inf.


  
def main():
	
	bonds = squarelattice(Nx = 3, Ny = 2)
	H = transverse_ising_hamiltonian(bonds, J = 1, h = 0.5)

	qc = Quantum_Circuit(6)
	qc.x(0) # Initial excitation


	obs_magX = magnetization(axis = 'X')
	obs_magY = magnetization(axis = 'Y')
	obs_magZ = magnetization(axis = 'Z')
	
	t, magXexact = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'exact', observable = obs_magX)
	t, magXtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 20, observable = obs_magX)
    t, magXtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 30, observable = obs_magX)
    t, magXtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 40, observable = obs_magX)
	
	t, magYexact = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'exact', observable = obs_magY)
	t, magYtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 20, observable = obs_magY)
    t, magYtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 30, observable = obs_magY)
    t, magYtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 40, observable = obs_magY)
	
	t, magZexact = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'exact', observable = obs_magZ)
	t, magZtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 20, observable = obs_magZ)
    t, magZtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 30, observable = obs_magZ)
    t, magZtrot = observable_vs_time(qc, H, time = 20, timesteps = 100, method = 'trotter_fixed_steps', trotter_steps = 40, observable = obs_magZ)
	
	
	fig, axs = plt.subplots(1, 3, figsize = (15, 5))
	ylim = (-0.3, 0.75)

	plot_observable(t, magXexact, title = 'X-axis', label = 'Exact', ax = axs[0], ylim = ylim)
	plot_observable(t, magXtrot, linestyle = '-.',  color ='r', label = 'Trotter', ax = axs[0])

	plot_observable(t, magYexact, title = 'Y-axis', label = 'Exact', ax = axs[1], ylim = ylim)
	plot_observable(t, magYtrot, linestyle = '-.',  color ='r', label = 'Trotter', ax = axs[1])

	plot_observable(t, magZexact, title = 'Z-axis',  label = 'Exact', ax = axs[2], ylim = ylim)
	plot_observable(t, magZtrot, linestyle = '-.',  color ='r', label = 'Trotter', ax = axs[2])

	
	plt.suptitle('Magnetization vs Time\n (Square Lattice Transverse Field Ising Model N=6)', fontsize = 18)
	fig.supxlabel('Time', fontsize = 18)
	fig.supylabel('Magnetization', fontsize = 18)
	plt.tight_layout()
	plt.savefig('square_tfim_magnetization_exact_vs_trotter.png')
	plt.show()

if __name__ == '__main__':
    main()


