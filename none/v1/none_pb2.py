# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: none/v1/none.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='none/v1/none.proto',
  package='none.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12none/v1/none.proto\x12\x07none.v1\"\x15\n\x04None\x12\r\n\x05\x66ield\x18\x01 \x01(\t\"&\n\x07Message\x12\x1b\n\x04none\x18\x01 \x01(\x0b\x32\r.none.v1.None\"\x1c\n\x0cOtherMessage\x12\x0c\n\x04None\x18\x01 \x01(\tb\x06proto3'
)




_NONE = _descriptor.Descriptor(
  name='None',
  full_name='none.v1.None',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='none.v1.None.field', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_end=52,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='none.v1.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='none', full_name='none.v1.Message.none', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=54,
  serialized_end=92,
)


_OTHERMESSAGE = _descriptor.Descriptor(
  name='OtherMessage',
  full_name='none.v1.OtherMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='None', full_name='none.v1.OtherMessage.None', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=94,
  serialized_end=122,
)

_MESSAGE.fields_by_name['none'].message_type = _NONE
DESCRIPTOR.message_types_by_name['None'] = _NONE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['OtherMessage'] = _OTHERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

globals()['None'] = _reflection.GeneratedProtocolMessageType('None', (_message.Message,), {
  'DESCRIPTOR' : _NONE,
  '__module__' : 'none.v1.none_pb2'
  # @@protoc_insertion_point(class_scope:none.v1.None)
  })
_sym_db.RegisterMessage(globals()['None'])

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'none.v1.none_pb2'
  # @@protoc_insertion_point(class_scope:none.v1.Message)
  })
_sym_db.RegisterMessage(Message)

OtherMessage = _reflection.GeneratedProtocolMessageType('OtherMessage', (_message.Message,), {
  'DESCRIPTOR' : _OTHERMESSAGE,
  '__module__' : 'none.v1.none_pb2'
  # @@protoc_insertion_point(class_scope:none.v1.OtherMessage)
  })
_sym_db.RegisterMessage(OtherMessage)


# @@protoc_insertion_point(module_scope)
