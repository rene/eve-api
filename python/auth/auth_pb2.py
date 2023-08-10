# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evecommon import evecommon_pb2 as evecommon_dot_evecommon__pb2
from evecommon import acipherinfo_pb2 as evecommon_dot_acipherinfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61uth/auth.proto\x12\x13org.lfedge.eve.auth\x1a\x19\x65vecommon/evecommon.proto\x1a\x1b\x65vecommon/acipherinfo.proto\"\x1b\n\x08\x41uthBody\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\"\xb4\x02\n\rAuthContainer\x12\x37\n\x10protectedPayload\x18\x01 \x01(\x0b\x32\x1d.org.lfedge.eve.auth.AuthBody\x12\x32\n\x04\x61lgo\x18\x02 \x01(\x0e\x32$.org.lfedge.eve.common.HashAlgorithm\x12\x16\n\x0esenderCertHash\x18\x03 \x01(\x0c\x12\x15\n\rsignatureHash\x18\x04 \x01(\x0c\x12\x12\n\nsenderCert\x18\x05 \x01(\x0c\x12;\n\rcipherContext\x18\x06 \x01(\x0b\x32$.org.lfedge.eve.common.CipherContext\x12\x36\n\ncipherData\x18\x07 \x01(\x0b\x32\".org.lfedge.eve.common.CipherBlockB9\n\x13org.lfedge.eve.authZ\"github.com/lf-edge/eve-api/go/authb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth.auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023org.lfedge.eve.authZ\"github.com/lf-edge/eve-api/go/auth'
  _globals['_AUTHBODY']._serialized_start=96
  _globals['_AUTHBODY']._serialized_end=123
  _globals['_AUTHCONTAINER']._serialized_start=126
  _globals['_AUTHCONTAINER']._serialized_end=434
# @@protoc_insertion_point(module_scope)
