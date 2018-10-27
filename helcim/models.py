"""Models for the django-oscar-helcim application."""
from uuid import uuid4

from django.db import models


class HelcimTransaction(models.Model):
    """Details of a single Helcim transaction."""
    # TODO: Figure out good length for response and notice messages
    uuid = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID',
    )
    raw_request = models.CharField(
        blank=True,
        help_text='The raw request used for this transaction',
        max_length=1024,
        null=True,
    )
    raw_response = models.CharField(
        blank=True,
        help_text='The raw response returned for this transaction',
        max_length=1024,
        null=True,
    )
    transaction_status = models.BooleanField(
        help_text='Whether the transaction was approved or not',
    )
    notice_message = models.CharField(
        blank=True,
        help_text='Any error or warning messages from Helcim',
        max_length=128,
        null=True,
    )
    date_response = models.DateTimeField(
        help_text='The date and time of the API response',
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time this transaction was recorded in database',
    )
    transaction_types = (
        ('s', 'purchase (sale)'),
        ('p', 'pre-authorization'),
        ('c', 'capture'),
        ('r', 'refund'),
    )
    transaction_type = models.CharField(
        choices=transaction_types,
        help_text='The type of transaction',
        max_length=1
    )
    amount = models.DecimalField(
        blank=True,
        decimal_places=2,
        help_text='The transaction amount',
        max_digits=12,
        null=True,
    )
    currency = models.CharField(
        blank=True,
        help_text='The transaction currency',
        max_length=8,
        null=True,
    )
    card_name = models.CharField(
        blank=True,
        help_text='The cardholder name',
        max_length=256,
        null=True,
    )
    card_number = models.CharField(
        blank=True,
        help_text='The first four and last 4 digits of the credit card number',
        max_length=16,
        null=True,
    )
    card_expiry = models.DateField(
        blank=True,
        help_text='The credit card expiry date',
        null=True,
    )
    card_type = models.CharField(
        blank=True,
        help_text='The credit card type',
        max_length=32,
        null=True,
    )
    card_token = models.CharField(
        blank=True,
        help_text='The Helcim generated and stored credit card token',
        max_length=23,
        null=True,
    )
    avs_response = models.CharField(
        blank=True,
        help_text='The address verification response',
        max_length=1,
        null=True,
    )
    cvv_response = models.CharField(
        blank=True,
        help_text='The CVV verification response',
        max_length=1,
        null=True,
    )
    approval_code = models.CharField(
        blank=True,
        help_text='The transaction approval code',
        max_length=16,
        null=True,
    )
    order_number = models.CharField(
        blank=True,
        help_text='The Helcim order number',
        max_length=16,
        null=True,
    )
    customer_code = models.CharField(
        blank=True,
        help_text='The Helcim customer code',
        max_length=16,
        null=True,
    )