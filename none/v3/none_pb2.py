# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: none/v3/none.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='none/v3/none.proto',
  package='none.v3',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12none/v3/none.proto\x12\x07none.v3\"&\n\x07Message\x12\x1b\n\x04none\x18\x01 \x01(\x0e\x32\r.none.v3.None*\x16\n\x04None\x12\x0e\n\nENUM_VALUE\x10\x00\x62\x06proto3'
)

_NONE = _descriptor.EnumDescriptor(
  name='None',
  full_name='none.v3.None',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENUM_VALUE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=71,
  serialized_end=93,
)
_sym_db.RegisterEnumDescriptor(_NONE)

globals()['None'] = enum_type_wrapper.EnumTypeWrapper(_NONE)
ENUM_VALUE = 0



_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='none.v3.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='none', full_name='none.v3.Message.none', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=69,
)

_MESSAGE.fields_by_name['none'].enum_type = _NONE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['None'] = _NONE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'none.v3.none_pb2'
  # @@protoc_insertion_point(class_scope:none.v3.Message)
  })
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
