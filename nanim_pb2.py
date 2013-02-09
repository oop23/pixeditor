# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='nanim.proto',
  package='im.bci.nanim',
  serialized_pb='\n\x0bnanim.proto\x12\x0cim.bci.nanim\"g\n\x05\x46rame\x12\x11\n\timageName\x18\x01 \x02(\t\x12\x10\n\x08\x64uration\x18\x02 \x02(\x05\x12\n\n\x02u1\x18\x03 \x02(\x02\x12\n\n\x02v1\x18\x04 \x02(\x02\x12\n\n\x02u2\x18\x05 \x02(\x02\x12\n\n\x02v2\x18\x06 \x02(\x02*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"I\n\tAnimation\x12\x0c\n\x04name\x18\x01 \x02(\t\x12#\n\x06\x66rames\x18\x02 \x03(\x0b\x32\x13.im.bci.nanim.Frame*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"z\n\x05Image\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05width\x18\x02 \x02(\x05\x12\x0e\n\x06height\x18\x03 \x02(\x05\x12)\n\x06\x66ormat\x18\x04 \x02(\x0e\x32\x19.im.bci.nanim.PixelFormat\x12\x0e\n\x06pixels\x18\x05 \x02(\x0c*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"\x85\x01\n\x05Nanim\x12#\n\x06images\x18\x01 \x03(\x0b\x32\x13.im.bci.nanim.Image\x12+\n\nanimations\x18\x02 \x03(\x0b\x32\x17.im.bci.nanim.Animation\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0f\n\x07license\x18\x04 \x01(\t*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02*)\n\x0bPixelFormat\x12\x0b\n\x07RGB_888\x10\x01\x12\r\n\tRGBA_8888\x10\x02\x42\rB\x0bNanimParser')

_PIXELFORMAT = descriptor.EnumDescriptor(
  name='PixelFormat',
  full_name='im.bci.nanim.PixelFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='RGB_888', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RGBA_8888', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=469,
  serialized_end=510,
)


RGB_888 = 1
RGBA_8888 = 2



_FRAME = descriptor.Descriptor(
  name='Frame',
  full_name='im.bci.nanim.Frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='imageName', full_name='im.bci.nanim.Frame.imageName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='duration', full_name='im.bci.nanim.Frame.duration', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u1', full_name='im.bci.nanim.Frame.u1', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='v1', full_name='im.bci.nanim.Frame.v1', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u2', full_name='im.bci.nanim.Frame.u2', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='v2', full_name='im.bci.nanim.Frame.v2', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  is_extendable=True,
  extension_ranges=[(1000, 536870912), ],
  serialized_start=29,
  serialized_end=132,
)


_ANIMATION = descriptor.Descriptor(
  name='Animation',
  full_name='im.bci.nanim.Animation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='im.bci.nanim.Animation.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='frames', full_name='im.bci.nanim.Animation.frames', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  is_extendable=True,
  extension_ranges=[(1000, 536870912), ],
  serialized_start=134,
  serialized_end=207,
)


_IMAGE = descriptor.Descriptor(
  name='Image',
  full_name='im.bci.nanim.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='im.bci.nanim.Image.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='width', full_name='im.bci.nanim.Image.width', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='height', full_name='im.bci.nanim.Image.height', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='format', full_name='im.bci.nanim.Image.format', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pixels', full_name='im.bci.nanim.Image.pixels', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  is_extendable=True,
  extension_ranges=[(1000, 536870912), ],
  serialized_start=209,
  serialized_end=331,
)


_NANIM = descriptor.Descriptor(
  name='Nanim',
  full_name='im.bci.nanim.Nanim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='images', full_name='im.bci.nanim.Nanim.images', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='animations', full_name='im.bci.nanim.Nanim.animations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='author', full_name='im.bci.nanim.Nanim.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='license', full_name='im.bci.nanim.Nanim.license', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  is_extendable=True,
  extension_ranges=[(1000, 536870912), ],
  serialized_start=334,
  serialized_end=467,
)

_ANIMATION.fields_by_name['frames'].message_type = _FRAME
_IMAGE.fields_by_name['format'].enum_type = _PIXELFORMAT
_NANIM.fields_by_name['images'].message_type = _IMAGE
_NANIM.fields_by_name['animations'].message_type = _ANIMATION
DESCRIPTOR.message_types_by_name['Frame'] = _FRAME
DESCRIPTOR.message_types_by_name['Animation'] = _ANIMATION
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Nanim'] = _NANIM

class Frame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRAME
  
  # @@protoc_insertion_point(class_scope:im.bci.nanim.Frame)

class Animation(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ANIMATION
  
  # @@protoc_insertion_point(class_scope:im.bci.nanim.Animation)

class Image(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IMAGE
  
  # @@protoc_insertion_point(class_scope:im.bci.nanim.Image)

class Nanim(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NANIM
  
  # @@protoc_insertion_point(class_scope:im.bci.nanim.Nanim)

# @@protoc_insertion_point(module_scope)
