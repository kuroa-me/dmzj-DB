# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dmzj.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dmzj.proto',
  package='dmzjpb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ndmzj.proto\x12\x06\x64mzjpb\"\'\n\x03Tag\x12\x0e\n\x06tag_id\x18\x01 \x01(\x05\x12\x10\n\x08tag_name\x18\x02 \x01(\t\"q\n\x07\x43hapter\x12\x12\n\nchapter_id\x18\x01 \x01(\r\x12\x15\n\rchapter_title\x18\x02 \x01(\t\x12\x12\n\nupdatetime\x18\x03 \x01(\x03\x12\x10\n\x08\x66ilesize\x18\x04 \x01(\r\x12\x15\n\rchapter_order\x18\x05 \x01(\x05\"8\n\x08\x43hapters\x12\r\n\x05title\x18\x01 \x01(\t\x12\x1d\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x0f.dmzjpb.Chapter\"q\n\x07\x43omment\x12\x12\n\ncomment_id\x18\x01 \x01(\r\x12\x0b\n\x03uid\x18\x02 \x01(\r\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x12\n\ncreatetime\x18\x04 \x01(\x03\x12\x10\n\x08nickname\x18\x05 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x06 \x01(\t\"J\n\x08\x43omments\x12\x15\n\rcomment_count\x18\x01 \x01(\r\x12\'\n\x0elatest_comment\x18\x02 \x03(\x0b\x32\x0f.dmzjpb.Comment\"\x95\x04\n\x05Manga\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06islong\x18\x02 \x01(\x05\x12\x11\n\tdirection\x18\x03 \x01(\x05\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0f\n\x07is_dmzj\x18\x05 \x01(\x05\x12\r\n\x05\x63over\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x17\n\x0flast_updatetime\x18\x08 \x01(\x03\x12 \n\x18last_update_chapter_name\x18\t \x01(\t\x12\x11\n\tcopyright\x18\n \x01(\x05\x12\x14\n\x0c\x66irst_letter\x18\x0b \x01(\t\x12\x10\n\x08\x63omic_py\x18\x0c \x01(\t\x12\x0e\n\x06hidden\x18\r \x01(\x05\x12\x0f\n\x07hot_num\x18\x0e \x01(\x05\x12\x0f\n\x07hit_num\x18\x0f \x01(\x05\x12\x0b\n\x03uid\x18\x10 \x01(\r\x12\x0f\n\x07is_lock\x18\x11 \x01(\x05\x12\x1e\n\x16last_update_chapter_id\x18\x12 \x01(\r\x12\x1a\n\x05types\x18\x13 \x03(\x0b\x32\x0b.dmzjpb.Tag\x12\x1c\n\x07\x61uthors\x18\x14 \x03(\x0b\x32\x0b.dmzjpb.Tag\x12\x1b\n\x06status\x18\x15 \x03(\x0b\x32\x0b.dmzjpb.Tag\x12\x15\n\rsubscribe_num\x18\x16 \x01(\x05\x12\"\n\x08\x63hapters\x18\x17 \x03(\x0b\x32\x10.dmzjpb.Chapters\x12!\n\x07\x63omment\x18\x18 \x01(\x0b\x32\x10.dmzjpb.Comments\"%\n\x04\x44mzj\x12\x1d\n\x06mangas\x18\x01 \x03(\x0b\x32\r.dmzjpb.Mangab\x06proto3')
)




_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='dmzjpb.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag_id', full_name='dmzjpb.Tag.tag_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_name', full_name='dmzjpb.Tag.tag_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=22,
  serialized_end=61,
)


_CHAPTER = _descriptor.Descriptor(
  name='Chapter',
  full_name='dmzjpb.Chapter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chapter_id', full_name='dmzjpb.Chapter.chapter_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chapter_title', full_name='dmzjpb.Chapter.chapter_title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updatetime', full_name='dmzjpb.Chapter.updatetime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filesize', full_name='dmzjpb.Chapter.filesize', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chapter_order', full_name='dmzjpb.Chapter.chapter_order', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=63,
  serialized_end=176,
)


_CHAPTERS = _descriptor.Descriptor(
  name='Chapters',
  full_name='dmzjpb.Chapters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='dmzjpb.Chapters.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dmzjpb.Chapters.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=178,
  serialized_end=234,
)


_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='dmzjpb.Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comment_id', full_name='dmzjpb.Comment.comment_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='dmzjpb.Comment.uid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='dmzjpb.Comment.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createtime', full_name='dmzjpb.Comment.createtime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='dmzjpb.Comment.nickname', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='dmzjpb.Comment.avatar', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=236,
  serialized_end=349,
)


_COMMENTS = _descriptor.Descriptor(
  name='Comments',
  full_name='dmzjpb.Comments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comment_count', full_name='dmzjpb.Comments.comment_count', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latest_comment', full_name='dmzjpb.Comments.latest_comment', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=351,
  serialized_end=425,
)


_MANGA = _descriptor.Descriptor(
  name='Manga',
  full_name='dmzjpb.Manga',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dmzjpb.Manga.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='islong', full_name='dmzjpb.Manga.islong', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='dmzjpb.Manga.direction', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='dmzjpb.Manga.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_dmzj', full_name='dmzjpb.Manga.is_dmzj', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cover', full_name='dmzjpb.Manga.cover', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='dmzjpb.Manga.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_updatetime', full_name='dmzjpb.Manga.last_updatetime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_update_chapter_name', full_name='dmzjpb.Manga.last_update_chapter_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='copyright', full_name='dmzjpb.Manga.copyright', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_letter', full_name='dmzjpb.Manga.first_letter', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comic_py', full_name='dmzjpb.Manga.comic_py', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='dmzjpb.Manga.hidden', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hot_num', full_name='dmzjpb.Manga.hot_num', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hit_num', full_name='dmzjpb.Manga.hit_num', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='dmzjpb.Manga.uid', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_lock', full_name='dmzjpb.Manga.is_lock', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_update_chapter_id', full_name='dmzjpb.Manga.last_update_chapter_id', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='dmzjpb.Manga.types', index=18,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authors', full_name='dmzjpb.Manga.authors', index=19,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dmzjpb.Manga.status', index=20,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribe_num', full_name='dmzjpb.Manga.subscribe_num', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chapters', full_name='dmzjpb.Manga.chapters', index=22,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='dmzjpb.Manga.comment', index=23,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=428,
  serialized_end=961,
)


_DMZJ = _descriptor.Descriptor(
  name='Dmzj',
  full_name='dmzjpb.Dmzj',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mangas', full_name='dmzjpb.Dmzj.mangas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=963,
  serialized_end=1000,
)

_CHAPTERS.fields_by_name['data'].message_type = _CHAPTER
_COMMENTS.fields_by_name['latest_comment'].message_type = _COMMENT
_MANGA.fields_by_name['types'].message_type = _TAG
_MANGA.fields_by_name['authors'].message_type = _TAG
_MANGA.fields_by_name['status'].message_type = _TAG
_MANGA.fields_by_name['chapters'].message_type = _CHAPTERS
_MANGA.fields_by_name['comment'].message_type = _COMMENTS
_DMZJ.fields_by_name['mangas'].message_type = _MANGA
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['Chapter'] = _CHAPTER
DESCRIPTOR.message_types_by_name['Chapters'] = _CHAPTERS
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
DESCRIPTOR.message_types_by_name['Comments'] = _COMMENTS
DESCRIPTOR.message_types_by_name['Manga'] = _MANGA
DESCRIPTOR.message_types_by_name['Dmzj'] = _DMZJ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'dmzj_pb2'
  # @@protoc_insertion_point(class_scope:dmzjpb.Tag)
  })
_sym_db.RegisterMessage(Tag)

Chapter = _reflection.GeneratedProtocolMessageType('Chapter', (_message.Message,), {
  'DESCRIPTOR' : _CHAPTER,
  '__module__' : 'dmzj_pb2'
  # @@protoc_insertion_point(class_scope:dmzjpb.Chapter)
  })
_sym_db.RegisterMessage(Chapter)

Chapters = _reflection.GeneratedProtocolMessageType('Chapters', (_message.Message,), {
  'DESCRIPTOR' : _CHAPTERS,
  '__module__' : 'dmzj_pb2'
  # @@protoc_insertion_point(class_scope:dmzjpb.Chapters)
  })
_sym_db.RegisterMessage(Chapters)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), {
  'DESCRIPTOR' : _COMMENT,
  '__module__' : 'dmzj_pb2'
  # @@protoc_insertion_point(class_scope:dmzjpb.Comment)
  })
_sym_db.RegisterMessage(Comment)

Comments = _reflection.GeneratedProtocolMessageType('Comments', (_message.Message,), {
  'DESCRIPTOR' : _COMMENTS,
  '__module__' : 'dmzj_pb2'
  # @@protoc_insertion_point(class_scope:dmzjpb.Comments)
  })
_sym_db.RegisterMessage(Comments)

Manga = _reflection.GeneratedProtocolMessageType('Manga', (_message.Message,), {
  'DESCRIPTOR' : _MANGA,
  '__module__' : 'dmzj_pb2'
  # @@protoc_insertion_point(class_scope:dmzjpb.Manga)
  })
_sym_db.RegisterMessage(Manga)

Dmzj = _reflection.GeneratedProtocolMessageType('Dmzj', (_message.Message,), {
  'DESCRIPTOR' : _DMZJ,
  '__module__' : 'dmzj_pb2'
  # @@protoc_insertion_point(class_scope:dmzjpb.Dmzj)
  })
_sym_db.RegisterMessage(Dmzj)


# @@protoc_insertion_point(module_scope)