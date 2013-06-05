# Copyright 2013 mdtraj developers
#
# This file is part of mdtraj
#
# mdtraj is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# mdtraj is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# mdtraj. If not, see http://www.gnu.org/licenses/.
"""OpenMM Reporter for saving the positions of a molecular dynamics simulation
in the HDF5 format.
"""

##############################################################################
# Imports
##############################################################################
from mdtraj.hdf5 import HDF5TrajectoryFile
from mdtraj.reporters.basereporter import _BaseReporter

##############################################################################
# Classes
##############################################################################


class HDF5Reporter(_BaseReporter):
    """HDF5Reporter stores a molecular dynamics trajectory in the HDF5 format.
    The atomic positions, periodic box vectors, and time index are saved.

    Example
    -------
    >>> simulation = Simulation(topology, system, integrator) # doctest: +SKIP
    >>> h5_reporter = HDF5Reporter('traj.h5', 100)            # doctest: +SKIP
    >>> simulation.reporters.append(h5_reporter)              # doctest: +SKIP
    >>> simulation.step(10000)                                # doctest: +SKIP

    >>> traj = mdtraj.trajectory.load('traj.lh5')             # doctest: +SKIP
    """
    backend = HDF5TrajectoryFile

    def __init__(self, file, reportInterval, coordinates=True, time=True,
                 cell=True, potentialEnergy=True, kineticEnergy=True,
                 temperature=True, velocities=False, atomSubset=None):
        """Create a HDF5Reporter.

        Parameters
        ----------
        file : str, or HDF5Trajectory
            Either an open HDF5Trajecory object to write to, or a string
            specifying the filename of a new HDF5 file
        reportInterval : int
            The interval (in time steps) at which to write frames.
        coordinates : bool
            Whether to write the coordinates to the file.
        time : bool
            Whether to write the current time to the file.
        cell : bool
            Whether to write the current unitcell dimensions to the file.
        potentialEnergy : bool
            Whether to write the potential energy to the file.
        kineticEnergy : bool
            Whether to write the kinetic energy to the file.
        temperature : bool
            Whether to write the instantaneous temperature to the file.
        """
        super(HDF5Reporter, self).__init__(file, reportInterval,
            coordinates, time, cell, potentialEnergy, kineticEnergy,
            temperature, velocities, atomSubset)
