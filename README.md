# HDF5 file format for the LUX experiment

This is a short demo of the HDF5 file format for the LUX experiment. LUX used an opaque and inflexible custom binary format, and adopting a flexible self-describing standard is a good improvement.

The file h5lux_PyMod.py implements functions for reading and writing HDF5 files in Python for both event-level and reduced-level (derived quantities) files.
