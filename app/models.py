import datetime

from sqlalchemy import Column, BigInteger, String, Integer, ForeignKey, \
    Table, Text, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()

# Tabel Many-to-Many Contact dengan List
list_contact = Table('list_contact', Base.metadata,
                     Column('contact_id', Integer, ForeignKey('contact.id')),
                     Column('list_id', Integer, ForeignKey('list.id')))

# Tabel Many-to-Many Contact dengan Mail Campaign
mail_contact = Table('mail_contact', Base.metadata,
                     Column('mail_id', BigInteger, ForeignKey('mail_campaign.id')),
                     Column('contact_id', BigInteger, ForeignKey('contact.id')))


# Tabel untuk menyimpan aktivitas "Click" pada kampanye email
class Click(Base):
    __tablename__ = 'click'

    id = Column(BigInteger, primary_key=True)
    mail_campaign_id = Column(BigInteger, ForeignKey('mail_campaign.id'))
    contact_id = Column(BigInteger, ForeignKey('contact.id'))
    timestamp = Column(DateTime)
    link_clicked = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'mail_campaign_id': self.mail_campaign_id,
            'contact_id': self.contact_id,
            'timestamp': self.timestamp,
            'link_clicked': self.link_clicked
        }


# Tabel untuk menyimpan aktivitas "Open" pada kampanye email
class Open(Base):
    __tablename__ = 'open'

    id = Column(BigInteger, primary_key=True)
    mail_campaign_id = Column(BigInteger, ForeignKey('mail_campaign.id'))
    contact_id = Column(BigInteger, ForeignKey('contact.id'))
    timestamp = Column(DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'mail_campaign_id': self.mail_campaign_id,
            'contact_id': self.contact_id,
            'timestamp': self.timestamp
        }


# Tabel untuk menyimpan aktivitas "Bounce" pada kampanye email
class Bounce(Base):
    __tablename__ = 'bounce'

    id = Column(BigInteger, primary_key=True)
    mail_campaign_id = Column(BigInteger, ForeignKey('mail_campaign.id'))
    contact_id = Column(BigInteger, ForeignKey('contact.id'))
    timestamp = Column(DateTime)
    bounce_reason = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'mail_campaign_id': self.mail_campaign_id,
            'contact_id': self.contact_id,
            'timestamp': self.timestamp,
            'bounce_reason': self.bounce_reason
        }


class StatusMail(PyEnum):
    SENT = 'sent'
    DRAFT = 'draft'
    SCHEDULED = 'scheduled'
    SUSPENDED = 'suspended'
    RUNNING = 'running'
    ARCHIVED = 'archived'


class StatusTemplate(PyEnum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class StatusContact(PyEnum):
    SUBSCRIBER = 'subscriber'
    UNSUBSCRIBE = 'unsubscribe'


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(BigInteger, primary_key=True)
    email = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String)
    status = Column(Enum(StatusContact), default=StatusContact.SUBSCRIBER)
    lists = relationship("List", secondary=list_contact, back_populates="contacts")
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "status": self.status.value,
            "lists": [lst.id for lst in self.lists],
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


class List(Base):
    __tablename__ = 'list'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    contacts = relationship("Contact", secondary=list_contact, back_populates="lists")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "contacts": [contact.id for contact in self.contacts],
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


class Mail(Base):
    __tablename__ = 'mail_campaign'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    from_name = Column(String)
    from_mail = Column(String)
    subject = Column(String)
    preview_line = Column(String)
    design = Column(Text)
    status = Column(Enum(StatusMail))
    template_id = Column(BigInteger, ForeignKey('template.id'))
    scheduled = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    recipients = relationship("Contact", secondary=mail_contact, backref="mails")
    template = relationship("Template")
    clicks = relationship("Click")
    opens = relationship("Open")
    bounces = relationship("Bounce")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'from_name': self.from_name,
            'from_mail': self.from_mail,
            'subject': self.subject,
            'preview_line': self.preview_line,
            'design': self.design,
            'status': self.status,
            'template_id': self.template_id,
            "scheduled": self.scheduled.strftime("%Y-%m-%d %H:%M:%S"),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


class Template(Base):
    __tablename__ = 'template'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    from_name = Column(String)
    from_mail = Column(String)
    subject = Column(String)
    preview_line = Column(String)
    design = Column(Text)
    status = Column(Enum(StatusTemplate))
    scheduled = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'from_name': self.from_name,
            'from_mail': self.from_mail,
            'subject': self.subject,
            'preview_line': self.preview_line,
            'design': self.design,
            'status': self.status,
            "scheduled": self.scheduled.strftime("%Y-%m-%d %H:%M:%S"),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
