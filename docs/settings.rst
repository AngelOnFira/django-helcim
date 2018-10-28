========
Settings
========

Below is a comprehensive list of all the settings for
django-oscar-helcim.

------------
API settings
------------

These are settings that control interactions with the
Helcim Commerce API.

``HELCIM_API_URL``
==================

**Required:** ``False``

**Default:** ``https://secure.myhelcim.com/api/``

**Format:** ``String``

The URL to access the Helcim Commerce API. At this time there is only
access to the API through the default URL, but this setting is
available to handle any future situations where custom endpoints
become available or to allow users to quickly update their application
should the URL change before this package is updated.

``HELCIM_ACCOUNT_ID``
=====================

**Required:** ``True``

**Default:** ``''``

**Format:** ``String``

The account ID for your Helcim account.

``HELCIM_API_TOKEN``
====================

**Required:** ``True``

**Default:** ``''``

**Format:** ``String``

The API token generated on your Helcim Commerce API dashboard to allow
django-oscar-helcim to make transactions via the Helcim Commerce API.

``HELCIM_TERMINAL_ID``
======================

**Required:** ``False``

**Default:** ``''``

**Format:** ``String``

The Helcim terminal ID you are using. If not provided the Helcim
Commerce API will use the default terminal for the provided Account ID.

``HELCIM_API_TEST``
===================

**Required:** ``False``

**Default:** ``False``

**Format:** ``Boolean``

A flag declaring whether transactions should be submitted in test mode
or not. When set to `True` all transactions will have ``test=true`` added
to the POST data. This prevents the Helcim Commerce API from attempting
to process the transaction.

-----------------------------
Private data storage settings
-----------------------------

These are settings that control what kind of private data is stored in
your database. Django-oscar-helcim does not record the Primary Account
Number (PAN), but does give you the option to save select data that
could be used to identify a specify customer and their account. **You
should only store the minimum amount of data you need to reduce the
risk and severity of a data breach.**

``HELCIM_REDACT_ALL``
=====================

**Required:** ``False``

**Default:** ``False``

**Format:** ``Boolean``

If set to ``True``, all references to the cardholder name, credit card
number, credit card expiry, credit card type, and Helcim Commerce
token will be redacted. **This setting overrides any of the individual
settings below.**

``HELCIM_REDACT_CC_NAME``
=========================

**Required:** ``False``

**Default:** ``False``

**Format:** ``Boolean``

If set to ``True``, redacts all reference to the credit card cardholder
name.

``HELCIM_REDACT_CC_NUMBER``
===========================

**Required:** ``False``

**Default:** ``False``

**Format:** ``Boolean``

If set to ``True``, redacts all reference to the credit card number.

``HELCIM_REDACT_CC_EXPIRY``
===========================

**Required:** ``False``

**Default:** ``False``

**Format:** ``Boolean``

If set to ``True``, redacts all reference to the credit card expiry date.

``HELCIM_REDACT_CC_TYPE``
=========================

**Required:** ``False``

**Default:** ``False``

**Format:** ``Boolean``

If set to ``True``, redacts all reference to the credit card type.

``HELCIM_REDACT_TOKEN``
=======================

**Required:** ``False``

**Default:** ``False``

**Format:** ``Boolean``

If set to ``True``, redacts all reference to the Helcim Commerce credit
card token.