Step-By-Step Guide
============================



Add Tester
--------------

Go to :menuselection:`Test Resources` . Click :guilabel:`Add Tester`.

.. figure:: ../_static/xoa2544/add_tester_1.png
    :width: 100%
    :alt: Add tester

Enter the IP of the management port under ``Address``. Use ``xena`` as default password.

.. figure:: ../_static/xoa2544/add_tester_2.png
    :width: 100%
    :alt: Enter IP


Make Test Configuration
---------------------------

Create New
^^^^^^^^^^^

Click :menuselection:`Configuration --> XOA 2544 --> Test Configuration`.

.. figure:: ../_static/xoa2544/make_test_configuration_01.png
    :width: 100%
    :alt: Enter 2544 test configuration

Click :guilabel:`New` and select :guilabel:`Create New` to create a new 2544 test configuration.

.. figure:: ../_static/xoa2544/make_test_configuration_02.png
    :width: 100%
    :alt: Create new test configuration


Topology Configuration
^^^^^^^^^^^^^^^^^^^^^^^

For :guilabel:`Pairs` topology, use the stepper to add/remove slot pairs or loop slots.

.. figure:: ../_static/xoa2544/make_test_configuration_03.png
    :width: 100%
    :alt: PAIR topology configuration


For :guilabel:`Blocks` topology, use the stepper to add/remove west slots and east slots.

.. figure:: ../_static/xoa2544/make_test_configuration_04.png
    :width: 100%
    :alt: BLOCKS topology configuration


For :guilabel:`Mesh` topology, use the stepper to add/remove slots.

.. figure:: ../_static/xoa2544/make_test_configuration_05.png
    :width: 100%
    :alt: MESH topology configuration


Frame Size Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

Choose the frame sizes, and the payload content.

.. figure:: ../_static/xoa2544/make_test_configuration_06.png
    :width: 100%
    :alt: Frame sizes configuration


Multi-Stream Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The total number of streams is shown on the right side.

.. figure:: ../_static/xoa2544/make_test_configuration_07.png
    :width: 100%
    :alt: Multi-stream configuration


Test Execution Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/xoa2544/make_test_configuration_08.png
    :width: 100%
    :alt: Test execution configuration


Test Case Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

Click :guilabel:`Throughput` to configure the throughput test.

.. figure:: ../_static/xoa2544/make_test_configuration_09.png
    :width: 100%
    :alt: Throughput test configuration


Click :guilabel:`Latency & Jitter` to configure the throughput test.

.. figure:: ../_static/xoa2544/make_test_configuration_10.png
    :width: 100%
    :alt: Latency & Jitter test configuration


Click :guilabel:`Frame Loss Rate` to configure the throughput test.

.. figure:: ../_static/xoa2544/make_test_configuration_11.png
    :width: 100%
    :alt: Frame Loss Rate test configuration


Click :guilabel:`Back-to-Back` to configure the throughput test.

.. figure:: ../_static/xoa2544/make_test_configuration_12.png
    :width: 100%
    :alt: Back-to-Back test configuration


Save and Complete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click :guilabel:`Save and Complete` to finish the test configuration.

.. figure:: ../_static/xoa2544/make_test_configuration_13.png
    :width: 100%
    :alt: Click Save and Complete button


Enter a name for the test configuration.

.. figure:: ../_static/xoa2544/make_test_configuration_14.png
    :width: 100%
    :alt: Name the test configuration

.. figure:: ../_static/xoa2544/make_test_configuration_15.png
    :width: 100%
    :alt: Saving successful


You will see the test configuration with the ``Locked`` label.

.. figure:: ../_static/xoa2544/make_test_configuration_16.png
    :width: 100%
    :alt: Saving successful


Save as Draft
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click :guilabel:`Save as Draft` to save the test configuration as a draft if you want to resume editing later.

.. figure:: ../_static/xoa2544/make_test_configuration_17.png
    :width: 100%
    :alt: Click Save and Complete button

You will see the test configuration with the ``Draft`` label.

.. figure:: ../_static/xoa2544/make_test_configuration_18.png
    :width: 100%
    :alt: Saving successful


Preview Test Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the test configuration to preview.

.. figure:: ../_static/xoa2544/make_test_configuration_19.png
    :width: 100%
    :alt: Preview test configuration


Create From
^^^^^^^^^^^^

Locked test configuration cannot be edited, but you can create a new one based on it, which is called Create From.

.. figure:: ../_static/xoa2544/make_test_configuration_20.png
    :width: 100%
    :alt: Create from a locked one


Run Test
---------------------------

Select Test Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to :menuselection:`Runners`. Only the test configuration that is ``locked`` is shown and ready to run. Click on the test configuration to preview.

.. figure:: ../_static/xoa2544/run_test_00.png
    :width: 100%
    :alt: Preview test configuration

Click the button :guilabel:`Prepare this test configuration for running`.

.. figure:: ../_static/xoa2544/run_test_01.png
    :width: 100%
    :alt: Prepare locked test configuration


Port Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select the required number of ports for the test configuration.

.. figure:: ../_static/xoa2544/run_test_02.png
    :width: 100%
    :alt: Select ports


Association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Associate the physical ports to the logical slots in the test configuration.

.. figure:: ../_static/xoa2544/run_test_03.png
    :width: 100%
    :alt: Associate physical ports to logical slots


Run Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click :guilabel:`Run Test` to start running a test with the test configuration and the physical ports.

.. figure:: ../_static/xoa2544/run_test_04.png
    :width: 100%
    :alt: Run test


The spinner indicates which sub test is currently running. Each table row contains the state and the test result of a test iteration. Enable :guilabel:`Auto-scroll` to automatically scroll to the last test iteration of the sub test.

.. figure:: ../_static/xoa2544/run_test_05.png
    :width: 100%
    :alt: Test result table

The test runs automatically until all test iterations are done. If you want to stop/pause the test before that, click :guilabel:`Stop Test` or :guilabel:`Pause Test`.

.. figure:: ../_static/xoa2544/run_test_06.png
    :width: 100%
    :alt: Stop/pause test

The test keeps running even if you exit the page. Click :guilabel:`Go to test` to go back to the test result page of the running test.

.. figure:: ../_static/xoa2544/run_test_07.png
    :width: 100%
    :alt: Go to running test


The test automatically stops when all test iterations are finished.

.. figure:: ../_static/xoa2544/run_test_08.png
    :width: 100%
    :alt: Go to running test


Download Test Report
---------------------------

Download Single Report
^^^^^^^^^^^^^^^^^^^^^^^

Go to :menuselection:`Reports`, expand the test configuration. Every time you run a test using the test configuration, a test result is attached to it. Find the test result you want to use and select a test report template configuration to generate the report. Click :guilabel:`Download this report`.

.. figure:: ../_static/xoa2544/download_test_report_01.png
    :width: 100%
    :alt: Select report configuration and download

Download Multiple Reports
^^^^^^^^^^^^^^^^^^^^^^^^^^

To download multiple reports at the same time, select the ones you want to download and click :guilabel:`Download`.

.. figure:: ../_static/xoa2544/download_test_report_02.png
    :width: 100%
    :alt: Batch download

Report Downloaded as Zip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test reports (CSV, XML, PDF) are zipped and downloaded.

.. figure:: ../_static/xoa2544/download_test_report_03.png
    :width: 100%
    :alt: Download in zip



Make Protocol Segment Profile
------------------------------

Create New
^^^^^^^^^^

Go to :menuselection:`Configuration --> XOA 2544 --> Protocol Segment Profiles`.

.. figure:: ../_static/xoa2544/make_psp_01.png
    :width: 100%
    :alt: Create new psp


Add Protocol Segments
^^^^^^^^^^^^^^^^^^^^^^

Click :guilabel:`Add protocol segments` to add new segments to the profile.

.. figure:: ../_static/xoa2544/make_psp_02.png
    :width: 100%
    :alt: Add new segments

Select the segments and click :guilabel:`Add Selected`.
.. figure:: ../_static/xoa2544/make_psp_03.png
    :width: 100%
    :alt: Add selected segments

Add a new modifier on a field, and click :guilabel:`Save`.
.. figure:: ../_static/xoa2544/make_psp_04.png
    :width: 100%
    :alt: Add new modifier to a field

Add a new value range on a field, and click :guilabel:`Save`.
.. figure:: ../_static/xoa2544/make_psp_05.png
    :width: 100%
    :alt: Add new value range to a field


Preview Protocol Segment Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the protocol segment profile to preview.

.. figure:: ../_static/xoa2544/make_psp_06.png
    :width: 100%
    :alt: Preview psp

.. figure:: ../_static/xoa2544/make_psp_07.png
    :width: 100%
    :alt: Preview psp


Make Report Configuration
------------------------------

Create New
^^^^^^^^^^

Click :menuselection:`Configuration --> XOA 2544 --> Report Configurations`.

.. figure:: ../_static/xoa2544/make_report_config_01.png
    :width: 100%
    :alt: Create new report configuration

Enable Report Type 
^^^^^^^^^^^^^^^^^^^^

Enable the types of report you want to generate and configure their settings.

.. figure:: ../_static/xoa2544/make_report_config_02.png
    :width: 100%
    :alt: Configure report configuration


Save Report Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Click :guilabel:`Save` to save the report configuration. Enter a name for the report configuration and click :guilabel:`Save`.

.. figure:: ../_static/xoa2544/make_report_config_03.png
    :width: 100%
    :alt: Save report configuration

.. figure:: ../_static/xoa2544/make_report_config_04.png
    :width: 100%
    :alt: Save report configuration


