# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config/patch_envelope.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from evecommon import acipherinfo_pb2 as evecommon_dot_acipherinfo__pb2
from config import storage_pb2 as config_dot_storage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63onfig/patch_envelope.proto\x12\x15org.lfedge.eve.config\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1b\x65vecommon/acipherinfo.proto\x1a\x14\x63onfig/storage.proto\"\x94\x02\n\x13\x45veOpaqueBase64Data\x12\x11\n\tencrypted\x18\x01 \x01(\x08\x12\x1d\n\x13\x62\x61se64ClearTextData\x18\x02 \x01(\tH\x00\x12\x42\n\x14\x62\x61se64CipherTextData\x18\x03 \x01(\x0b\x32\".org.lfedge.eve.common.CipherBlockH\x00\x12!\n\x17\x62\x61se64ClearTextMetaData\x18\x04 \x01(\tH\x01\x12\x46\n\x18\x62\x61se64CipherTextMetaData\x18\x05 \x01(\x0b\x32\".org.lfedge.eve.common.CipherBlockH\x01\x42\n\n\x08textDataB\x10\n\x0e\x62\x61se64MetaData\"J\n\x13\x45veOpaqueBinaryBlob\x12\x33\n\x0copaqueVolume\x18\x01 \x01(\x0b\x32\x1d.org.lfedge.eve.config.Volume\"\x9d\x02\n\x11\x45veBinaryArtifact\x12>\n\x06\x66ormat\x18\x01 \x01(\x0e\x32..org.lfedge.eve.config.EveOpaqueObjectCategory\x12\x44\n\x0e\x62\x61se64Artifact\x18\x02 \x01(\x0b\x32*.org.lfedge.eve.config.EveOpaqueBase64DataH\x00\x12\x44\n\x0e\x62inaryArtifact\x18\x03 \x01(\x0b\x32*.org.lfedge.eve.config.EveOpaqueBinaryBlobH\x00\x12\x1d\n\x10\x61rtifactMetaData\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06scriptB\x13\n\x11_artifactMetaData\"\x9e\x02\n\x10\x45vePatchEnvelope\x12\x13\n\x0b\x64isplayName\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x14\n\x07version\x18\x03 \x01(\tH\x00\x88\x01\x01\x12=\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32-.org.lfedge.eve.config.EvePatchEnvelopeAction\x12;\n\tartifacts\x18\x05 \x03(\x0b\x32(.org.lfedge.eve.config.EveBinaryArtifact\x12\x19\n\x11\x61ppInstIdsAllowed\x18\x06 \x03(\t\x12.\n\ncreateTime\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\n\x08_version*\xb9\x01\n\x17\x45veOpaqueObjectCategory\x12%\n!EVE_OPAQUE_OBJECT_CATEGORY_UNKOWN\x10\x00\x12%\n!EVE_OPAQUE_OBJECT_CATEGORY_BASE64\x10\x01\x12)\n%EVE_OPAQUE_OBJECT_CATEGORY_BINARYBLOB\x10\x02\x12%\n!EVE_OPAQUE_OBJECT_CATEGORY_SECRET\x10\x03*e\n\x16\x45vePatchEnvelopeAction\x12#\n\x1f\x45VE_PATCH_ENVELOPE_ACTION_STORE\x10\x00\x12&\n\"EVE_PATCH_ENVELOPE_ACTION_ACTIVATE\x10\x01\x42=\n\x15org.lfedge.eve.configZ$github.com/lf-edge/eve-api/go/configb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config.patch_envelope_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025org.lfedge.eve.configZ$github.com/lf-edge/eve-api/go/config'
  _globals['_EVEOPAQUEOBJECTCATEGORY']._serialized_start=1071
  _globals['_EVEOPAQUEOBJECTCATEGORY']._serialized_end=1256
  _globals['_EVEPATCHENVELOPEACTION']._serialized_start=1258
  _globals['_EVEPATCHENVELOPEACTION']._serialized_end=1359
  _globals['_EVEOPAQUEBASE64DATA']._serialized_start=139
  _globals['_EVEOPAQUEBASE64DATA']._serialized_end=415
  _globals['_EVEOPAQUEBINARYBLOB']._serialized_start=417
  _globals['_EVEOPAQUEBINARYBLOB']._serialized_end=491
  _globals['_EVEBINARYARTIFACT']._serialized_start=494
  _globals['_EVEBINARYARTIFACT']._serialized_end=779
  _globals['_EVEPATCHENVELOPE']._serialized_start=782
  _globals['_EVEPATCHENVELOPE']._serialized_end=1068
# @@protoc_insertion_point(module_scope)
