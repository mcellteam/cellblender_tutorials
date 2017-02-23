.. _cellblender_install:

*******************************************************************************
CellBlender Installation (for Developers and Advanced Users)
*******************************************************************************

.. note::

    Most Windows and Linux users should use the CellBlender 1.1 bundle (linux_,
    windows_). OSX users will need to install CellBlender from scratch.
    Additionally, some advanced users may want to regardless of their platform.
    They will need to manually install the following pieces:

.. _linux: http://mcell.org/download/files/cellblender1.1_bundle_linux.zip
.. _osx: http://mcell.org/download/files/cellblender1.1_bundle_osx.zip
.. _windows: http://mcell.org/download/files/cellblender1.1_bundle_windows.zip

Download CellBlender
---------------------------------------------

.. we need to tag a 1.1 release.

Download `CellBlender 1.1`_.

.. _CellBlender 1.1: http://mcell.org/download/files/cellblender1.1.zip

Installing CellBlender
---------------------------------------------

* Start Blender
* Select **File->User Preferences**

.. image:: ./images/install/user_prefs.png

* In the **User Preferences** control panel choose the **Addons** tab

.. image:: ./images/install/addons_tab.png

* Click the **Install from File** button at the bottom of the window.

.. image:: ./images/install/install_from_file.png

* Navigate to the unextracted zip file that you downloaded
  (cellblender_v1.1.zip) and select it
* Click the **Install from File** button near the upper-right hand corner.

.. image:: ./images/install/install_from_file2.png

.. note::

    If you need to install a newer version of CellBlender, the installation
    process is the same. The new version of CellBlender should cleanly install
    over the existing version.

Activating CellBlender in Blender
---------------------------------------------

* Select the **Cell Modeling** category button on left side of window
* Check the box for **Cell Modeling: CellBlender** (may take a few seconds)

.. image:: ./images/install/enable_cellblender.png

* Click **Save User Settings** to enable the addon permanently in Blender.
* Close the **Blender User Preferences** window
* Click **CellBlender** tab on left edge of window

.. image:: ./images/clean_slate/cellblender_tab.png

* Click **Initialize CellBlender** button

.. image:: ./images/clean_slate/init_cb.png

Setting up CellBlender
---------------------------------------------

You can finish setting up CellBlender by checking out the :ref:`first_time`
tutorial.
