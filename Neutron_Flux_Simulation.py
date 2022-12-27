import numpy as np

# Define constants for the neutron mass and energy
NEUTRON_MASS = 1.00866491588  # in atomic mass units
NEUTRON_ENERGY = 0.0253  # in MeV

# Define the core materials and their masses
core_materials = ['Uranium-235', 'Plutonium-239', 'Beryllium', 'Graphite']
core_masses = [200, 100, 50, 100]  # in kg

# Define the initial neutron flux
initial_neutron_flux = 1e10  # in neutrons/cm^2/s

# Define a function to compute the neutron flux
def compute_neutron_flux(core_materials, core_masses, initial_neutron_flux):
    """Compute the neutron flux in a nuclear reactor.

    Args:
        core_materials (list): A list of the core materials in the reactor.
        core_masses (list): A list of the masses of the core materials in kg.
        initial_neutron_flux (float): The initial neutron flux in neutrons/cm^2/s.

    Returns:
        float: The neutron flux in neutrons/cm^2/s.
    """
    # Compute the total mass of the core materials
    total_mass = sum(core_masses)

    # Compute the neutron flux based on the masses and energies of the core materials
    neutron_flux = initial_neutron_flux * np.sqrt(total_mass * NEUTRON_ENERGY / NEUTRON_MASS)

    return neutron_flux

# Compute the neutron flux in the reactor
neutron_flux = compute_neutron_flux(core_materials, core_masses, initial_neutron_flux)
print(f'The neutron flux in the reactor is {neutron_flux:.2e} neutrons/cm^2/s')
