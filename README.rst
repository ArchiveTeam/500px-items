500px-items
===========

Processes discovery data and creates items for 500px-grab.

.. note:: Make sure you keep the repository updated, for example with discovered data or item lists that have been created or added to the tracker.

How to run
----------

Unpack new response data into directory ``original``, see the directory itself for examples. Run the following to get a list of photo identifiers from the responses::

    cd original
    python get_ids.py <responses>

where ``<responses>`` is for example ``AttributionLicense3-API-Sever-Responses``.

An ``*_ids.txt`` file is then created. In the main directory run::

    python generate.py <_ids.txt file> <num>

where ``<_ids.txt file>`` is for example the previously created ``original/AttributionLicense3-API-Sever-Responses_ids.txt`` and ``<num>`` is a number not yet used for item lists (also see the item lists that have been added to the tracker in ``ADDED``).

A file containing an item list is now created. Add the file to the tracker. Move the file to the ``ADDED`` directory.

