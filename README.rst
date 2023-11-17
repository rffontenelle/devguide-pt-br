devguide-pt-br
==============

|ReadTheDocs|

.. |ReadTheDocs| image:: https://readthedocs.org/projects/devguide-pt-br/badge/
    :alt: ReadTheDocs Build Status
    :scale: 100%
    :target: https://devguide-pt-br.readthedocs.io

Brazilian Portuguese translation for `the Python developer's guide <https://devguide.python.org>`_.
See `devguide at GitHub <https://github.com/python/devguide>`_ for more info.


How to set up the environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clone this repository:

.. code-block:: sh

    git clone github.com/rffontenelle/devguide-pt-br

2. Set up a virtual environment, and activate it:

.. code-block:: sh

    python3 -mvenv venv
    source venv/bin/activate

3. Prepare the devguide repository, which is a submodule of this one:

.. code-block:: sh

    git submodule init
    git submodule update

4. (optional) Update pip:

.. code-block:: sh

    pip install -U pip

5. Install dependencies:

.. code-block:: sh

    pip install -U -r requirements.txt -r devguide/requirements.txt


Updating translations
~~~~~~~~~~~~~~~~~~~~~

With the environment ready, run:

.. code-block:: sh

    python update.py --devguide_repo=devguide

Once the script is done, running ``git status`` should show the po files
that were updated, and ``git diff`` should show the changes.


Build translations locally
~~~~~~~~~~~~~~~~~~~~~~~~~~

The docs are already `available online <https://devguide-pt-br.readthedocs.io>`_, so are its `build logs <https://readthedocs.org/projects/devguide-pt-br/builds/>`_.

With the environment ready, first copy po files into devguide locales directory:

.. code-block:: sh

    find . -maxdepth 2 -name '*.po' -type f -exec install -Dm644 {} devguide/locales/pt_BR/LC_MESSAGES/{} \;

Then build the documentation:

.. code-block:: sh

    sphinx-build -c devguide/ -Dlanguage=pt_BR -Dgettext_compact=0 devguide/ _build

See the directory *_built/* for the HTML documentation.


Maintenance
~~~~~~~~~~~

Pages could have been deleted in the upstream, so translation files might be useless in this repo.

After updating translations, one can list the obsolete files using the following command from the repository root directory:

.. code-block:: sh

    for file in $(ls *.po **/*.po); do [ ! -f "devguide/locales/pt_BR/LC_MESSAGES/$file" ] && echo "$file"; done

If no file is obsolete, no output is emitted.
