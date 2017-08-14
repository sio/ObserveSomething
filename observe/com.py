"""
Access COM object from Python
"""


import os.path
from comtypes.client import GetActiveObject, CreateObject


def make_COM(prog_id, allow_reuse=True):
    """
    Create or get Windows COM object.

    Try to reuse an existing instance before creating a new one.
    """
    com_object = None
    reuse_failed = False

    if allow_reuse:
        try:
            com_object = GetActiveObject(prog_id)
        except OSError:
            reuse_failed = True
    if not allow_reuse or reuse_failed:
        com_object = CreateObject(prog_id)
    return com_object


def make_MailItem(recipients,
                  subject="",
                  body="",
                  attachments=None):
    """
    Create Outlook MailItem object.
    Common MailItem methods are Display() and Send().

    Arguments:
    recipients
        String or sequence of strings with e-mail addresses
        of recipients.
    subject
        Message subject.
    body
        Message body in HTML.
    attachments
        Path or sequence of paths to files that will be attached
        to the message.
    """
    if isinstance(recipients, str): recipients = [recipients]
    if isinstance(attachments, str): attachments = [attachments]

    outlook = make_COM("Outlook.Application")
    message = outlook.CreateItem(0)  # olMaiiItem

    message.BodyFormat = 2  # olFormatHTML
    message.HTMLBody = body
    message.Subject = subject

    for address in recipients:
        message.Recipients.Add(address)
    if attachments:
        for path in attachments:
            message.Attachments.Add(os.path.abspath(path), 1)

    return message
