# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detect.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detect.proto',
  package='objectdetect',
  syntax='proto3',
  serialized_pb=_b('\n\x13object_detect.proto\x12\x0cobjectdetect\"D\n\x08Location\x12\x0c\n\x04left\x18\x01 \x01(\x02\x12\r\n\x05right\x18\x02 \x01(\x02\x12\x0b\n\x03top\x18\x03 \x01(\x02\x12\x0e\n\x06\x62ottom\x18\x04 \x01(\x02\"\"\n\rDetectRequest\x12\x11\n\tfile_data\x18\x01 \x01(\x0c\"p\n\x0b\x44\x65tectReply\x12(\n\x08location\x18\x01 \x01(\x0b\x32\x16.objectdetect.Location\x12\x12\n\nclass_name\x18\x02 \x01(\t\x12\x12\n\nclass_code\x18\x03 \x01(\t\x12\x0f\n\x07\x66\x65\x61ture\x18\x04 \x01(\x0c\x32R\n\x06\x44\x65tect\x12H\n\nGetObjects\x12\x1b.objectdetect.DetectRequest\x1a\x19.objectdetect.DetectReply\"\x00\x30\x01\x42\x31\n\x13io.stylelens.detectB\x11ObjectDetectProtoP\x01\xa2\x02\x04STYLb\x06proto3')
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='objectdetect.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='objectdetect.Location.left', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right', full_name='objectdetect.Location.right', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top', full_name='objectdetect.Location.top', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='objectdetect.Location.bottom', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=105,
)


_DETECTREQUEST = _descriptor.Descriptor(
  name='DetectRequest',
  full_name='objectdetect.DetectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_data', full_name='objectdetect.DetectRequest.file_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=141,
)


_DETECTREPLY = _descriptor.Descriptor(
  name='DetectReply',
  full_name='objectdetect.DetectReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='objectdetect.DetectReply.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='objectdetect.DetectReply.class_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_code', full_name='objectdetect.DetectReply.class_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature', full_name='objectdetect.DetectReply.feature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=255,
)

_DETECTREPLY.fields_by_name['location'].message_type = _LOCATION
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['DetectRequest'] = _DETECTREQUEST
DESCRIPTOR.message_types_by_name['DetectReply'] = _DETECTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'object_detect_pb2'
  # @@protoc_insertion_point(class_scope:objectdetect.Location)
  ))
_sym_db.RegisterMessage(Location)

DetectRequest = _reflection.GeneratedProtocolMessageType('DetectRequest', (_message.Message,), dict(
  DESCRIPTOR = _DETECTREQUEST,
  __module__ = 'object_detect_pb2'
  # @@protoc_insertion_point(class_scope:objectdetect.DetectRequest)
  ))
_sym_db.RegisterMessage(DetectRequest)

DetectReply = _reflection.GeneratedProtocolMessageType('DetectReply', (_message.Message,), dict(
  DESCRIPTOR = _DETECTREPLY,
  __module__ = 'object_detect_pb2'
  # @@protoc_insertion_point(class_scope:objectdetect.DetectReply)
  ))
_sym_db.RegisterMessage(DetectReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023io.stylelens.detectB\021ObjectDetectProtoP\001\242\002\004STYL'))

_DETECT = _descriptor.ServiceDescriptor(
  name='Detect',
  full_name='objectdetect.Detect',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=257,
  serialized_end=339,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetObjects',
    full_name='objectdetect.Detect.GetObjects',
    index=0,
    containing_service=None,
    input_type=_DETECTREQUEST,
    output_type=_DETECTREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DETECT)

DESCRIPTOR.services_by_name['Detect'] = _DETECT

# @@protoc_insertion_point(module_scope)
