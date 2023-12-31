# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['synapse',
 'synapse._scripts',
 'synapse.api',
 'synapse.app',
 'synapse.appservice',
 'synapse.config',
 'synapse.crypto',
 'synapse.events',
 'synapse.federation',
 'synapse.federation.sender',
 'synapse.federation.transport',
 'synapse.federation.transport.server',
 'synapse.handlers',
 'synapse.handlers.ui_auth',
 'synapse.http',
 'synapse.http.federation',
 'synapse.logging',
 'synapse.media',
 'synapse.metrics',
 'synapse.module_api',
 'synapse.push',
 'synapse.replication',
 'synapse.replication.http',
 'synapse.replication.tcp',
 'synapse.replication.tcp.streams',
 'synapse.rest',
 'synapse.rest.admin',
 'synapse.rest.client',
 'synapse.rest.consent',
 'synapse.rest.key',
 'synapse.rest.key.v2',
 'synapse.rest.media',
 'synapse.rest.media.v1',
 'synapse.rest.synapse',
 'synapse.rest.synapse.client',
 'synapse.rest.synapse.client.oidc',
 'synapse.rest.synapse.client.saml2',
 'synapse.server_notices',
 'synapse.spam_checker_api',
 'synapse.state',
 'synapse.storage',
 'synapse.storage.controllers',
 'synapse.storage.databases',
 'synapse.storage.databases.main',
 'synapse.storage.databases.state',
 'synapse.storage.engines',
 'synapse.storage.schema',
 'synapse.storage.schema.main.delta.20',
 'synapse.storage.schema.main.delta.25',
 'synapse.storage.schema.main.delta.27',
 'synapse.storage.schema.main.delta.30',
 'synapse.storage.schema.main.delta.31',
 'synapse.storage.schema.main.delta.33',
 'synapse.storage.schema.main.delta.34',
 'synapse.storage.schema.main.delta.37',
 'synapse.storage.schema.main.delta.42',
 'synapse.storage.schema.main.delta.48',
 'synapse.storage.schema.main.delta.50',
 'synapse.storage.schema.main.delta.56',
 'synapse.storage.schema.main.delta.57',
 'synapse.storage.schema.main.delta.58',
 'synapse.storage.schema.main.delta.59',
 'synapse.storage.schema.main.delta.61',
 'synapse.storage.schema.main.delta.68',
 'synapse.storage.schema.main.delta.69',
 'synapse.storage.schema.main.delta.72',
 'synapse.storage.schema.main.delta.73',
 'synapse.storage.schema.state.delta.47',
 'synapse.storage.util',
 'synapse.streams',
 'synapse.types',
 'synapse.util',
 'synapse.util.caches']

package_data = \
{'': ['*'],
 'synapse': ['res/*',
             'res/templates/*',
             'static/*',
             'static/client/login/*',
             'static/client/login/js/*',
             'static/client/register/*',
             'static/client/register/js/*'],
 'synapse.storage.schema': ['common/*',
                            'common/delta/25/*',
                            'common/delta/35/*',
                            'common/delta/58/*',
                            'common/full_schemas/54/*',
                            'common/full_schemas/72/*',
                            'main/delta/12/*',
                            'main/delta/13/*',
                            'main/delta/14/*',
                            'main/delta/15/*',
                            'main/delta/16/*',
                            'main/delta/17/*',
                            'main/delta/18/*',
                            'main/delta/19/*',
                            'main/delta/21/*',
                            'main/delta/22/*',
                            'main/delta/24/*',
                            'main/delta/26/*',
                            'main/delta/28/*',
                            'main/delta/29/*',
                            'main/delta/32/*',
                            'main/delta/35/*',
                            'main/delta/36/*',
                            'main/delta/38/*',
                            'main/delta/39/*',
                            'main/delta/40/*',
                            'main/delta/41/*',
                            'main/delta/43/*',
                            'main/delta/44/*',
                            'main/delta/45/*',
                            'main/delta/46/*',
                            'main/delta/47/*',
                            'main/delta/49/*',
                            'main/delta/51/*',
                            'main/delta/52/*',
                            'main/delta/53/*',
                            'main/delta/54/*',
                            'main/delta/55/*',
                            'main/delta/60/*',
                            'main/delta/62/*',
                            'main/delta/63/*',
                            'main/delta/64/*',
                            'main/delta/65/*',
                            'main/delta/67/*',
                            'main/delta/70/*',
                            'main/delta/71/*',
                            'main/full_schemas/16/*',
                            'main/full_schemas/54/*',
                            'main/full_schemas/72/*',
                            'state/delta/23/*',
                            'state/delta/32/*',
                            'state/delta/35/*',
                            'state/delta/56/*',
                            'state/delta/61/*',
                            'state/delta/70/*',
                            'state/full_schemas/54/*',
                            'state/full_schemas/72/*']}

install_requires = \
['Jinja2>=3.0',
 'Pillow>=5.4.0',
 'PyYAML>=3.13',
 'Twisted[tls]>=18.9.0',
 'attrs>=19.2.0,!=21.1.0',
 'bcrypt>=3.1.7',
 'bleach>=1.4.3',
 'canonicaljson>=1.5.0,<2.0.0',
 'cryptography>=3.4.7',
 'frozendict>=1,!=2.1.2,<2.3.5',
 'ijson>=3.1.4',
 'jsonschema>=3.0.0',
 'matrix-common>=1.3.0,<2.0.0',
 'msgpack>=0.5.2',
 'netaddr>=0.7.18',
 'packaging>=16.1',
 'phonenumbers>=8.2.0',
 'prometheus-client>=0.4.0',
 'pyOpenSSL>=16.0.0',
 'pyasn1-modules>=0.0.7',
 'pyasn1>=0.1.9',
 'pydantic>=1.7.4',
 'pymacaroons>=0.13.0',
 'service-identity>=18.1.0',
 'setuptools_rust>=1.3',
 'signedjson>=1.1.0,<2.0.0',
 'sortedcontainers>=1.5.2',
 'treq>=15.1',
 'typing-extensions>=3.10.0.1',
 'unpaddedbase64>=2.1.0']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.4'],
 'all': ['matrix-synapse-ldap3>=0.1',
         'pysaml2>=4.5.0',
         'authlib>=0.15.1',
         'lxml>=4.2.0',
         'sentry-sdk>=0.7.2',
         'opentracing>=2.2.0',
         'jaeger-client>=4.0.0',
         'txredisapi>=1.4.7',
         'hiredis',
         'Pympler',
         'pyicu>=2.10.2'],
 'all:platform_python_implementation != "PyPy"': ['psycopg2>=2.8'],
 'all:platform_python_implementation == "PyPy"': ['psycopg2cffi>=2.8',
                                                  'psycopg2cffi-compat==1.1'],
 'cache-memory': ['Pympler'],
 'jwt': ['authlib>=0.15.1'],
 'matrix-synapse-ldap3': ['matrix-synapse-ldap3>=0.1'],
 'oidc': ['authlib>=0.15.1'],
 'opentracing': ['opentracing>=2.2.0', 'jaeger-client>=4.0.0'],
 'postgres:platform_python_implementation != "PyPy"': ['psycopg2>=2.8'],
 'postgres:platform_python_implementation == "PyPy"': ['psycopg2cffi>=2.8',
                                                       'psycopg2cffi-compat==1.1'],
 'redis': ['txredisapi>=1.4.7', 'hiredis'],
 'saml2': ['pysaml2>=4.5.0'],
 'sentry': ['sentry-sdk>=0.7.2'],
 'systemd': ['systemd-python>=231'],
 'test': ['parameterized>=0.7.4', 'idna>=2.5'],
 'url-preview': ['lxml>=4.2.0'],
 'user-search': ['pyicu>=2.10.2']}

entry_points = \
{'console_scripts': ['export_signing_key = '
                     'synapse._scripts.export_signing_key:main',
                     'generate_config = synapse._scripts.generate_config:main',
                     'generate_log_config = '
                     'synapse._scripts.generate_log_config:main',
                     'generate_signing_key = '
                     'synapse._scripts.generate_signing_key:main',
                     'hash_password = synapse._scripts.hash_password:main',
                     'register_new_matrix_user = '
                     'synapse._scripts.register_new_matrix_user:main',
                     'synapse_homeserver = synapse.app.homeserver:main',
                     'synapse_port_db = synapse._scripts.synapse_port_db:main',
                     'synapse_review_recent_signups = '
                     'synapse._scripts.review_recent_signups:main',
                     'synapse_worker = synapse.app.generic_worker:main',
                     'synctl = synapse._scripts.synctl:main',
                     'update_synapse_database = '
                     'synapse._scripts.update_synapse_database:main']}

setup_kwargs = {
    'name': 'matrix-synapse',
    'version': '1.79.0',
    'description': 'Homeserver for the Matrix decentralised comms protocol',
    'long_description': '=========================================================================\nSynapse |support| |development| |documentation| |license| |pypi| |python|\n=========================================================================\n\nSynapse is an open-source `Matrix <https://matrix.org/>`_ homeserver written and\nmaintained by the Matrix.org Foundation. We began rapid development in 2014,\nreaching v1.0.0 in 2019. Development on Synapse and the Matrix protocol itself continues\nin earnest today.\n\nBriefly, Matrix is an open standard for communications on the internet, supporting\nfederation, encryption and VoIP. Matrix.org has more to say about the `goals of the\nMatrix project <https://matrix.org/docs/guides/introduction>`_, and the `formal specification\n<https://spec.matrix.org/>`_ describes the technical details.\n\n.. contents::\n\nInstalling and configuration\n============================\n\nThe Synapse documentation describes `how to install Synapse <https://matrix-org.github.io/synapse/latest/setup/installation.html>`_. We recommend using\n`Docker images <https://matrix-org.github.io/synapse/latest/setup/installation.html#docker-images-and-ansible-playbooks>`_ or `Debian packages from Matrix.org\n<https://matrix-org.github.io/synapse/latest/setup/installation.html#matrixorg-packages>`_.\n\n.. _federation:\n\nSynapse has a variety of `config options\n<https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html>`_\nwhich can be used to customise its behaviour after installation.\nThere are additional details on how to `configure Synapse for federation here\n<https://matrix-org.github.io/synapse/latest/federate.html>`_.\n\n.. _reverse-proxy:\n\nUsing a reverse proxy with Synapse\n----------------------------------\n\nIt is recommended to put a reverse proxy such as\n`nginx <https://nginx.org/en/docs/http/ngx_http_proxy_module.html>`_,\n`Apache <https://httpd.apache.org/docs/current/mod/mod_proxy_http.html>`_,\n`Caddy <https://caddyserver.com/docs/quick-starts/reverse-proxy>`_,\n`HAProxy <https://www.haproxy.org/>`_ or\n`relayd <https://man.openbsd.org/relayd.8>`_ in front of Synapse. One advantage of\ndoing so is that it means that you can expose the default https port (443) to\nMatrix clients without needing to run Synapse with root privileges.\nFor information on configuring one, see `the reverse proxy docs\n<https://matrix-org.github.io/synapse/latest/reverse_proxy.html>`_.\n\nUpgrading an existing Synapse\n-----------------------------\n\nThe instructions for upgrading Synapse are in `the upgrade notes`_.\nPlease check these instructions as upgrading may require extra steps for some\nversions of Synapse.\n\n.. _the upgrade notes: https://matrix-org.github.io/synapse/develop/upgrade.html\n\n\nPlatform dependencies\n---------------------\n\nSynapse uses a number of platform dependencies such as Python and PostgreSQL,\nand aims to follow supported upstream versions. See the\n`deprecation policy <https://matrix-org.github.io/synapse/latest/deprecation_policy.html>`_\nfor more details.\n\n\nSecurity note\n-------------\n\nMatrix serves raw, user-supplied data in some APIs -- specifically the `content\nrepository endpoints`_.\n\n.. _content repository endpoints: https://matrix.org/docs/spec/client_server/latest.html#get-matrix-media-r0-download-servername-mediaid\n\nWhilst we make a reasonable effort to mitigate against XSS attacks (for\ninstance, by using `CSP`_), a Matrix homeserver should not be hosted on a\ndomain hosting other web applications. This especially applies to sharing\nthe domain with Matrix web clients and other sensitive applications like\nwebmail. See\nhttps://developer.github.com/changes/2014-04-25-user-content-security for more\ninformation.\n\n.. _CSP: https://github.com/matrix-org/synapse/pull/1021\n\nIdeally, the homeserver should not simply be on a different subdomain, but on\na completely different `registered domain`_ (also known as top-level site or\neTLD+1). This is because `some attacks`_ are still possible as long as the two\napplications share the same registered domain.\n\n.. _registered domain: https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-03#section-2.3\n\n.. _some attacks: https://en.wikipedia.org/wiki/Session_fixation#Attacks_using_cross-subdomain_cookie\n\nTo illustrate this with an example, if your Element Web or other sensitive web\napplication is hosted on ``A.example1.com``, you should ideally host Synapse on\n``example2.com``. Some amount of protection is offered by hosting on\n``B.example1.com`` instead, so this is also acceptable in some scenarios.\nHowever, you should *not* host your Synapse on ``A.example1.com``.\n\nNote that all of the above refers exclusively to the domain used in Synapse\'s\n``public_baseurl`` setting. In particular, it has no bearing on the domain\nmentioned in MXIDs hosted on that server.\n\nFollowing this advice ensures that even if an XSS is found in Synapse, the\nimpact to other applications will be minimal.\n\n\nTesting a new installation\n==========================\n\nThe easiest way to try out your new Synapse installation is by connecting to it\nfrom a web client.\n\nUnless you are running a test instance of Synapse on your local machine, in\ngeneral, you will need to enable TLS support before you can successfully\nconnect from a client: see\n`TLS certificates <https://matrix-org.github.io/synapse/latest/setup/installation.html#tls-certificates>`_.\n\nAn easy way to get started is to login or register via Element at\nhttps://app.element.io/#/login or https://app.element.io/#/register respectively.\nYou will need to change the server you are logging into from ``matrix.org``\nand instead specify a Homeserver URL of ``https://<server_name>:8448``\n(or just ``https://<server_name>`` if you are using a reverse proxy).\nIf you prefer to use another client, refer to our\n`client breakdown <https://matrix.org/docs/projects/clients-matrix>`_.\n\nIf all goes well you should at least be able to log in, create a room, and\nstart sending messages.\n\n.. _`client-user-reg`:\n\nRegistering a new user from a client\n------------------------------------\n\nBy default, registration of new users via Matrix clients is disabled. To enable\nit:\n\n1. In the\n   `registration config section <https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html#registration>`_\n   set ``enable_registration: true`` in ``homeserver.yaml``.\n2. Then **either**:\n\n   a. set up a `CAPTCHA <https://matrix-org.github.io/synapse/latest/CAPTCHA_SETUP.html>`_, or\n   b. set ``enable_registration_without_verification: true`` in ``homeserver.yaml``.\n\nWe **strongly** recommend using a CAPTCHA, particularly if your homeserver is exposed to\nthe public internet. Without it, anyone can freely register accounts on your homeserver.\nThis can be exploited by attackers to create spambots targetting the rest of the Matrix\nfederation.\n\nYour new user name will be formed partly from the ``server_name``, and partly\nfrom a localpart you specify when you create the account. Your name will take\nthe form of::\n\n    @localpart:my.domain.name\n\n(pronounced "at localpart on my dot domain dot name").\n\nAs when logging in, you will need to specify a "Custom server".  Specify your\ndesired ``localpart`` in the \'User name\' box.\n\nTroubleshooting and support\n===========================\n\nThe `Admin FAQ <https://matrix-org.github.io/synapse/latest/usage/administration/admin_faq.html>`_\nincludes tips on dealing with some common problems. For more details, see\n`Synapse\'s wider documentation <https://matrix-org.github.io/synapse/latest/>`_.\n\nFor additional support installing or managing Synapse, please ask in the community\nsupport room |room|_ (from a matrix.org account if necessary). We do not use GitHub\nissues for support requests, only for bug reports and feature requests.\n\n.. |room| replace:: ``#synapse:matrix.org``\n.. _room: https://matrix.to/#/#synapse:matrix.org\n\n.. |docs| replace:: ``docs``\n.. _docs: docs\n\nIdentity Servers\n================\n\nIdentity servers have the job of mapping email addresses and other 3rd Party\nIDs (3PIDs) to Matrix user IDs, as well as verifying the ownership of 3PIDs\nbefore creating that mapping.\n\n**They are not where accounts or credentials are stored - these live on home\nservers. Identity Servers are just for mapping 3rd party IDs to matrix IDs.**\n\nThis process is very security-sensitive, as there is obvious risk of spam if it\nis too easy to sign up for Matrix accounts or harvest 3PID data. In the longer\nterm, we hope to create a decentralised system to manage it (`matrix-doc #712\n<https://github.com/matrix-org/matrix-doc/issues/712>`_), but in the meantime,\nthe role of managing trusted identity in the Matrix ecosystem is farmed out to\na cluster of known trusted ecosystem partners, who run \'Matrix Identity\nServers\' such as `Sydent <https://github.com/matrix-org/sydent>`_, whose role\nis purely to authenticate and track 3PID logins and publish end-user public\nkeys.\n\nYou can host your own copy of Sydent, but this will prevent you reaching other\nusers in the Matrix ecosystem via their email address, and prevent them finding\nyou. We therefore recommend that you use one of the centralised identity servers\nat ``https://matrix.org`` or ``https://vector.im`` for now.\n\nTo reiterate: the Identity server will only be used if you choose to associate\nan email address with your account, or send an invite to another user via their\nemail address.\n\n\nDevelopment\n===========\n\nWe welcome contributions to Synapse from the community!\nThe best place to get started is our\n`guide for contributors <https://matrix-org.github.io/synapse/latest/development/contributing_guide.html>`_.\nThis is part of our larger `documentation <https://matrix-org.github.io/synapse/latest>`_, which includes\n\ninformation for Synapse developers as well as Synapse administrators.\nDevelopers might be particularly interested in:\n\n* `Synapse\'s database schema <https://matrix-org.github.io/synapse/latest/development/database_schema.html>`_,\n* `notes on Synapse\'s implementation details <https://matrix-org.github.io/synapse/latest/development/internal_documentation/index.html>`_, and\n* `how we use git <https://matrix-org.github.io/synapse/latest/development/git.html>`_.\n\nAlongside all that, join our developer community on Matrix:\n`#synapse-dev:matrix.org <https://matrix.to/#/#synapse-dev:matrix.org>`_, featuring real humans!\n\n\n.. |support| image:: https://img.shields.io/matrix/synapse:matrix.org?label=support&logo=matrix\n  :alt: (get support on #synapse:matrix.org)\n  :target: https://matrix.to/#/#synapse:matrix.org\n\n.. |development| image:: https://img.shields.io/matrix/synapse-dev:matrix.org?label=development&logo=matrix\n  :alt: (discuss development on #synapse-dev:matrix.org)\n  :target: https://matrix.to/#/#synapse-dev:matrix.org\n\n.. |documentation| image:: https://img.shields.io/badge/documentation-%E2%9C%93-success\n  :alt: (Rendered documentation on GitHub Pages)\n  :target: https://matrix-org.github.io/synapse/latest/\n\n.. |license| image:: https://img.shields.io/github/license/matrix-org/synapse\n  :alt: (check license in LICENSE file)\n  :target: LICENSE\n\n.. |pypi| image:: https://img.shields.io/pypi/v/matrix-synapse\n  :alt: (latest version released on PyPi)\n  :target: https://pypi.org/project/matrix-synapse\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/matrix-synapse\n  :alt: (supported python versions)\n  :target: https://pypi.org/project/matrix-synapse\n',
    'author': 'Matrix.org Team and Contributors',
    'author_email': 'packages@matrix.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/matrix-org/synapse',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}
from build_rust import *
build(setup_kwargs)

setup(**setup_kwargs)
