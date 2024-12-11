"""
Sphinx Read the Docs theme.

From https://github.com/ryan-roemer/sphinx-bootstrap-theme.
"""

from os import path
from sys import version_info as python_version

from sphinx import version_info as sphinx_version
from sphinx.locale import _
from sphinx.util.logging import getLogger


__version__ = '1.3.0'
__version_full__ = __version__

logger = getLogger(__name__)


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir


def config_initiated(app, config):
    theme_options = config.html_theme_options or {}
    if theme_options.get('canonical_url'):
        logger.warning(
            _('The canonical_url option is deprecated, use the html_baseurl option from Sphinx instead.')
        )


def extend_html_context(app, pagename, templatename, context, doctree):
     # Add ``sphinx_version_info`` tuple for use in Jinja templates
     context['sphinx_version_info'] = sphinx_version


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    if python_version[0] < 3:
        logger.warning("Python 2 is deprecated with sphinx_rtd_theme, update to Python 3")
    app.require_sphinx('1.6')
    if sphinx_version <= (2, 0, 0):
        logger.warning("Sphinx 1.x is deprecated with sphinx_rtd_theme, update to Sphinx 2.x or greater")
        if not app.config.html_experimental_html5_writer:
            logger.warning("'html4_writer' is deprecated with sphinx_rtd_theme")
    else:
        if app.config.html4_writer:
            logger.warning("'html4_writer' is deprecated with sphinx_rtd_theme")

    # Since Sphinx 6, jquery isn't bundled anymore and we need to ensure that
    # the sphinxcontrib-jquery extension is enabled.
    # See: https://dev.readthedocs.io/en/latest/design/sphinx-jquery.html
    if sphinx_version >= (6, 0, 0):
        # Documentation of Sphinx guarantees that an extension is added and
        # enabled at most once.
        # See: https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.setup_extension
        app.setup_extension("sphinxcontrib.jquery")
        # However, we need to call the extension's callback since setup_extension doesn't do it
        # See: https://github.com/sphinx-contrib/jquery/issues/23
        from sphinxcontrib.jquery import add_js_files as jquery_add_js_files
        jquery_add_js_files(app, app.config)

    # Register the theme that can be referenced without adding a theme path
    app.add_html_theme('sphinx_rtd_theme', path.abspath(path.dirname(__file__)))

    if sphinx_version >= (1, 8, 0):
        # Add Sphinx message catalog for newer versions of Sphinx
        # See http://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_message_catalog
        rtd_locale_path = path.join(path.abspath(path.dirname(__file__)), 'locale')
        app.add_message_catalog('sphinx', rtd_locale_path)
        app.connect('config-inited', config_initiated)

    # sphinx emits the permalink icon for headers, so choose one more in keeping with our theme
    if sphinx_version >= (3, 5, 0):
        app.config.html_permalinks_icon = "\uf0c1"
    else:
        app.config.html_add_permalinks = "\uf0c1"
version_info = (4, 1)

_ROOT_DIR = path.abspath(path.dirname(__file__))
_FILES = (
    (
        'jquery.js',
        'sha384-vtXRMe3mGCbOeY7l30aIg8H9p3GdeSe4IFlP6G8JMa7o7lXvnz3GFKzPxzJdPfGK',
    ),
    (
        '_sphinx_javascript_frameworks_compat.js',
        'sha384-lSZeSIVKp9myfKbDQ3GkN/KHjUc+mzg17VKDN4Y2kUeBSJioB9QSM639vM9fuY//',
    ),
)


def add_js_files(app, config):
    jquery_installed = getattr(app, "_sphinxcontrib_jquery_installed", False)

    if sphinx.version_info[:2] >= (6, 0) and not jquery_installed:
        makedirs(path.join(app.outdir, '_static'), exist_ok=True)
        for (filename, integrity) in _FILES:
            # The default is not to enable subresource integrity checks, as it
            # does not trigger the hash check but instead blocks the request
            # when viewing documentation locally through the ``file://`` URIs.
            if config.jquery_use_sri:
                app.add_js_file(filename, priority=100, integrity=integrity)
            else:
                app.add_js_file(filename, priority=100)
            shutil.copyfile(
                path.join(_ROOT_DIR, filename),
                path.join(app.outdir, '_static', filename)
            )
        app._sphinxcontrib_jquery_installed = True


def setup(app):
    # Configuration value for enabling `subresource integrity`__ (SRI) checks
    # __ https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity
    app.add_config_value("jquery_use_sri", default=True, rebuild="html", types=(bool,))

    app.connect('config-inited', add_js_files)

    # Extend the default context when rendering the templates.
    app.connect("html-page-context", extend_html_context)

    return {'parallel_read_safe': True, 'parallel_write_safe': True}
