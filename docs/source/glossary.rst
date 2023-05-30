.. _glossary-label:

Glossary of Terms
====================

.. glossary::
    :sorted:

    Test Resource
        Test chassis, test module, and test port, both hardware and virtual are referred to as test resources. A user must have the ownership of a test resource before be able to perform testing.

    API 
        Application Programming Interface.

    TGA
        Traffic Generation and Analysis.

    XOA
        Xena OpenAutomation

    XOA2544
        Xena OpenAutomation RFC 2544 Test Methodology Application

    XOA2889
        Xena OpenAutomation RFC 2889 Test Methodology Application

    XOA3918
        Xena OpenAutomation RFC 3918 Test Methodology Application

    XOA1564
        Xena OpenAutomation ITU-T Y.2561 Test Methodology Application

    DUT
        Device Under Test

    RFC 2544
        Benchmarking Methodology for Network Interconnect Devices (:rfc:`2544`)

    RFC 1242
        Benchmarking Terminology for Network Interconnection Devices (:rfc:`1242`)

    Iteration
        A test iteration (or simply iteration) denotes the part of the test configuration that is associated with a single test-type and a single packet size. This concept is used for the purpose of progress reporting. A test configuration that specifies the use of e.g. 5 packet sizes and has enabled 3 of the possible 4 test-types will thus consist of 5*3 = 15 iterations.

    Repetition
        Each test-type can be configured to repeat the test iterations associated with the test-type a number of times. Each of these additional runs is called an repetition.

    Trial
        A trial denotes a single execution of an repetition.

    Direction
        Denotes the direction of the traffic flows in relation to the group definitions. The direction can be either unidirectional or bidirectional. Unidirectional flows can be either EAST-to-WEST or WEST-to-EAST.

    Pair Topology
        A topology where each port is associated with exactly one other peer port. The ports must be associated with opposing EAST/WEST groups. A test configuration can contain several port pairs.
        The transmit and receive roles of the two ports are determined by the Direction setting.

    Blocks Topology
        A topology where each port is associated with either the EAST or the WEST group. Each port in the EAST group will then communicate with all ports in the WEST group, and vice versa. There are thus no direct relation between ports like there are for the Pairs topology.
        The transmit and receive roles of the ports are determined by the Direction setting.

    Mesh Topology
        A topology where all ports communicate with each other. The direction will always be bidirectional and the EAST/WEST group attribute is not used.

    XOA Cluster
        A ``Cluster`` is a group of cooperative nodes that form a XOA deployment. A Cluster consists of at least one XOA Node.

        * It is highly recommended to set up only one XOA Cluster for an organization because of the centralized persistent data storage. 
        * Clusters are designed to adapt to inter-network communication between Workers and the Manager.

    XOA Fleet
        A ``Fleet`` is the management domain of a XOA Worker that manages a group of Xena physical and virtual testers. A Fleet consists of only one XOA Worker and at least one Xena tester (hardware or virtual).

        * Fleets are designed to be run in a local network with low-latency links between the Worker and Xena testers.
        * Large testbed, such as inter-network, may require multiple Fleets to cover Xena testers at different remote locations (available in a future release).

    XOA Node
        A XOA Node is a docker container hosting the entire service stack. A XOA Node can be configured into three different working modes, Manager, Worker, and Duo.

    XOA Node - Manager
        ``Manager`` nodes are XOA Nodes configured into Manager mode. A Manager node is the central point of a XOA Cluster for operations, administration, and management. An organization should only have one active Manager due to its centralized persistent data storage.
    
    XOA Node - Worker
        ``Worker`` nodes are XOA Nodes configured into Worker mode. A Worker node is the central point of a Fleet.

    XOA Node - Duo
        ``Duo`` nodes are XOA Nodes configured into Duo mode, which provides functionalities of a Manager and a Worker.