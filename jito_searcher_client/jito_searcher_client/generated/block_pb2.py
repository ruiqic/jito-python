# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x62lock.proto\x12\x05\x62lock\x1a\x0cshared.proto\"\xb6\x01\n\x0e\x43ondensedBlock\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.shared.Header\x12\x1a\n\x12previous_blockhash\x18\x02 \x01(\t\x12\x11\n\tblockhash\x18\x03 \x01(\t\x12\x13\n\x0bparent_slot\x18\x04 \x01(\x04\x12\x1e\n\x16versioned_transactions\x18\x05 \x03(\x0c\x12\x0c\n\x04slot\x18\x06 \x01(\x04\x12\x12\n\ncommitment\x18\x07 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'block_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONDENSEDBLOCK._serialized_start=37
  _CONDENSEDBLOCK._serialized_end=219
# @@protoc_insertion_point(module_scope)