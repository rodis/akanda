# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2011 Nicira Networks, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
# @author: Somik Behera, Nicira Networks, Inc.
# @author: Brad Hall, Nicira Networks, Inc.
# @author: Dan Wendlandt, Nicira Networks, Inc.
# @author: Salvatore Orlando, Citrix Systems

import uuid
import sqlalchemy as sa
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relation


from quantum.api import api_common as common
from quantum.db import model_base
from quantum.db import models_v2 as models
from quantum.openstack.common import timeutils


BASE = model_base.BASE


class Port(model_base.BASE):
    """Represents a port on a quantum network"""
    __tablename__ = 'ports'

    uuid = Column(String(255), primary_key=True)
    network_id = Column(String(255), ForeignKey("networks.uuid"),
                        nullable=False)
    interface_id = Column(String(255), nullable=True)
    # Port state - Hardcoding string value at the moment
    state = Column(String(8))
    op_status = Column(String(16))

    def __init__(self, network_id, op_status=common.OperationalStatus.UNKNOWN):
        self.uuid = str(uuid.uuid4())
        self.network_id = network_id
        self.interface_id = None
        self.state = "DOWN"
        self.op_status = op_status

    def __repr__(self):
        return "<Port(%s,%s,%s,%s,%s)>" % (self.uuid, self.network_id,
                                           self.state, self.op_status,
                                           self.interface_id)


class Network(model_base.BASE):
    """Represents a quantum network"""
    __tablename__ = 'networks'

    uuid = Column(String(255), primary_key=True)
    tenant_id = Column(String(255), nullable=False)
    name = Column(String(255))
    ports = relation(Port, order_by=Port.uuid, backref="network")
    op_status = Column(String(16))

    def __init__(self, tenant_id, name,
                 op_status=common.OperationalStatus.UNKNOWN):
        self.uuid = str(uuid.uuid4())
        self.tenant_id = tenant_id
        self.name = name
        self.op_status = op_status

    def __repr__(self):
        return "<Network(%s,%s,%s,%s)>" % (self.uuid, self.name,
                                           self.op_status, self.tenant_id)



#DreamHost PortFoward, Firewall(FilterRule), AddressBook models for
#Quantum extensions
class PortForward(model_base.BASEV2, models.HasId, models.HasTenant):
    name = sa.Column(sa.String(255))
    public_port = sa.Column(sa.Integer, nullable=False)
    instance_id = sa.Column(sa.String(36), nullable=False)
    private_port = sa.Column(sa.Integer, nullable=True)
    # Quantum port address are stored in ipallocation which are internally
    # referred to as fixed_id, thus the name below.
    # XXX can we add a docsting to this model that explains how fixed_id is
    # used?
    fixed_id = sa.Column(
        sa.String(36), sa.ForeignKey('ipallocation.id', ondelete="CASCADE"),
        nullable=True)


class AddressBookEntry(model_base.BASEV2, models.HasId, models.HasTenant):
    group_id = sa.Column(sa.String(36), sa.ForeignKey('addressbookgroup.id'),
        nullable=False)
    cidr = sa.Column(sa.String(64), nullable=False)


class AddressBookGroup(model_base.BASEV2, models.HasId, models.HasTenant):
    name = sa.Column(sa.String(255), nullable=False, primary_key=True)
    table_id = sa.Column(sa.String(36), sa.ForeignKey('addressbook.id'),
        nullable=False)
    entries = orm.relationship(AddressBookEntry, backref='groups')


class AddressBook(model_base.BASEV2, models.HasId, models.HasTenant):
    name = sa.Column(sa.String(255), nullable=False, primary_key=True)
    groups = orm.relationship(AddressBookGroup, backref='book')


class Firewall(model_base.BASEV2, models.HasId, models.HasTenant):
    action = sa.Column(sa.String(6), nullable=False, primary_key=True)
    ip_version = sa.Column(sa.Integer, nullable=True)
    protocol = sa.Column(sa.String(4), nullable=False)
    source_alias = sa.Column(sa.String(36),
        sa.ForeignKey('addressbookentry.id'),
        nullable=False)
    source_port = sa.Column(sa.Integer, nullable=True)
    destination_alias = sa.Column(sa.String(36),
        sa.ForeignKey('addressbookentry.id'),
        nullable=False)
    destination_port = sa.Column(sa.Integer, nullable=True)
    created_at = sa.Column(sa.DateTime, default=timeutils.utcnow,
        nullable=False)
