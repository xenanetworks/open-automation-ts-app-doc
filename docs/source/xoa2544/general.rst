General Information
===================

Capabilities
---------------

The XOA2544 application features the following capabilities:

* Enables the user to create, edit and execute test configurations using Xena Networks test equipment in accordance with `RFC 2544 <https://www.ietf.org/rfc/rfc2544.txt.pdf>`_.
* Enables the user to run multiple tests simultaneously. 
* Full support for the four test types specified in `RFC 2544 <https://www.ietf.org/rfc/rfc2544.txt.pdf>`_.
* Ability to partially enable one or more of the test types.
* Support for multiple Valkyrie test chassis.
* Support for different network topologies and traffic directions.
* Support for Layer 2 and Layer 3 traffic.
* Support for IPv4 and IPv6.
* Ability to flexibly define the protocol layers supported by the test (Ethernet, Customer and Service VLANs, IP and UDP).
* Ability to specify different protocol headers for each port.
* Ability to set modifiers on virtually any protocol field in the protocol headers.
* Support for asymmetric port rates and DUT throughput rates. The Throughput test can be configured to either measure the least common throughput rate or measure a per-port rate.
* Test reports can be created in either PDF, XML or CSV format or any combination hereof.
* Extensive configuration options to fine-tune the tests.


Available Tests
---------------

This section describes the test available in :term:`XOA2544`. They closely follow the definition in the `RFC 2544 <https://www.ietf.org/rfc/rfc2544.txt.pdf>`_ specification.

Throughput Test
^^^^^^^^^^^^^^^

The Throughput Test is an iterative test that attempts to find the throughput for a Device Under Test (:term:`DUT`). `RFC 1242 <https://www.ietf.org/rfc/rfc1242.txt.pdf>`_ defines the throughput as *The maximum rate at which none of the offered frames are dropped by the device*.

The test uses a binary search algorithm to locate the throughput rate. One iteration of the test will produce a single test result.


Latency/Jitter Test
^^^^^^^^^^^^^^^^^^^

The Latency/Jitter Test is a rate sweep test that attempts to determine the latency and jitter for a DUT throughout a defined range of input data rates. `RFC 1242 <https://www.ietf.org/rfc/rfc1242.txt.pdf>`_ broadly defines latency as the time it takes for a frame to traverse the DUT, but the precise definition depends on the type of forwarding used in the DUT. Latency is also known as the “Frame Transfer Delay” (FTD). Jitter is not defined in this RFC but is defined as the variation in latency over time. It is also known as the “Frame Delay Variance” (FDV).
The test measures the average, maximum and minimum latency and jitter values at a series of input rates defined by an initial value a, maximum value and a step value. One iteration of the test will produce a test result for each rate in the series.


Frame Loss Test
^^^^^^^^^^^^^^^

The Frame Loss Test is a rate sweep test that attempts to determine the frame loss rate for a DUT throughout a defined range of input data rates. RFC 1242 defines the loss as the “percentage of frames that should have been forwarded by a network device under steady state (constant) load that were not forwarded due to lack of resources”.
The test measures the frame loss at a series of input rates defined by an initial value a, maximum value and a step value. One iteration of the test will produce a test result for each rate in the series.


Back-To-Back Frames Test
^^^^^^^^^^^^^^^^^^^^^^^^

The Back-to-Back Frames Test is a combination of an iterative test and a rate sweep test that characterizes the ability of a DUT to process back-to-back frames at various rates. RFC 1242 defines back-to-back frames as “fixed length frames presented at a rate such that there is the minimum legal separation for a given medium between frames over a short to medium period of time, starting from an idle state”. The test attempts to locate the maximum number of frames that can be sent back-to-back at a given rate without any frame loss. This is also known as the “burst size”.
The test uses a binary search algorithm to locate the burst size at a given rate. One iteration of the test will produce a single test result for each input rate used.



