# NOAA_SatTrack

## Goals
The goal of this project will be to take a file describing a satellite's orbit (TLE/Emphemeris file), the current location of the software host, and a time profile and produce a skyplot and estimate of when the satellite will be in view for tracking and recording.

This is essentially a more generic version of Trimble's GNSS planning app that will create skyplots for any satellite and can also predict when satellites will be in view given a location.

This will allow a user to know when to start recording a satellite passing overhead.

A separate project will be created for active pointing of an az/el positioner. That project till take the output of SatTrack and create pointing vectors between a directional antenna on an az/el positioner and the satellite given a time profile.

