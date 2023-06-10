Port Selection Panel
=======================

.. _port_selection:

.. figure:: ../../../_static/xoa2544/reference/runners/port_selection.png
    :width: 100%
    :alt: Port Selection

    XOA Test Runner - Port Selection

This page displays all available test ports on the currently connected Xena testers. It is possible to connect to multiple Xena testers at the same time.

It also allows you to perform the following actions:

* View the current sync (link) and traffic state of the ports.
* View the current ownership of the ports.
* Determine which ports are used in the test configuration.

Name
-----
The leftmost column shows the name of the tester, module, and port in a tree view.

Status
------
The column right to column :guilabel:`Name` contain two state bullet icons.

The first bullet indicate the port sync (link) state:

* A green bullet means that the port is in sync
* A red bullet means that the port has lost sync.

The second bullet indicate the traffic state:

* A yellow bullet means that traffic is being sent from the port.
* A gray bullet means that no traffic is active.

Selected
----------
The number in the bracket indicates how many ports you should select to run a test with the chosen test configuration.

Port Ownership
--------------
The rightmost column display the username of the current port owner.


..note::
    
    There is no need to explicitly reserve the ports. When you run the test, XOA2544 will automatically reserve the ownership of the selected ports.