import numpy as np

# Define constants for the neutron mass and energy
NEUTRON_MASS = 1.00866491588  # in atomic mass units
NEUTRON_ENERGY = 0.0253  # in MeV

# Define the initial energy and mass of the two colliding neutrons
neutron1_energy = 1.0  # in MeV
neutron1_mass = NEUTRON_MASS  # in atomic mass units
neutron2_energy = 1.5  # in MeV
neutron2_mass = NEUTRON_MASS  # in atomic mass units

# Define a function to compute the collision products
def compute_collision_products(neutron1_energy, neutron1_mass, neutron2_energy, neutron2_mass):
    """Compute the collision products of a neutron-neutron collision.

    Args:
        neutron1_energy (float): The energy of the first neutron in MeV.
        neutron1_mass (float): The mass of the first neutron in atomic mass units.
        neutron2_energy (float): The energy of the second neutron in MeV.
        neutron2_mass (float): The mass of the second neutron in atomic mass units.

    Returns:
        tuple: A tuple containing the following elements:
            - product1_energy (float): The energy of the first collision product in MeV.
            - product1_mass (float): The mass of the first collision product in atomic mass units.
            - product2_energy (float): The energy of the second collision product in MeV.
            - product2_mass (float): The mass of the second collision product in atomic mass units.
    """
    # Compute the total energy and mass of the colliding neutrons
    total_energy = neutron1_energy + neutron2_energy
    total_mass = neutron1_mass + neutron2_mass

    # Compute the collision products based on the conservation of energy and mass
    product1_energy = total_energy / 2
    product1_mass = total_mass / 2
    product2_energy = total_energy / 2
    product2_mass = total_mass / 2

    return product1_energy, product1_mass, product2_energy, product2_mass

# Compute the collision products
product1_energy, product1_mass, product2_energy, product2_mass = compute_collision_products(
    neutron1_energy, neutron1_mass, neutron2_energy, neutron2_mass
)
print(f'The collision products have energies of {product1_energy:.2f} MeV and {product2_energy:.2f} MeV')
print(f'The collision products have masses of {product1_mass:.2f} atomic mass units and {product2_mass:.2f} atomic mass units')

#Output would look like:
#The collision products have energies of 0.75 MeV and 0.75 MeV
#The collision products have masses of 0.50 atomic mass units and 0.50 atomic mass units
