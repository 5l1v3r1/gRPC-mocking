# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: polynomial.proto

import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database


_b = sys.version_info[0] < 3 and (lambda x: x) or(lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)


_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='polynomial.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x10polynomial.proto\"\x1c\n\x0fPolynomialInput\x12\t\n\x01x\x18\x01 \x01(\x02\"0\n\x10PolynomialOutput\x12\r\n\x05res_x\x18\x01 \x01(\x02\x12\r\n\x05res_y\x18\x02 \x01(\x02\x32<\n\nPolynomial\x12.\n\x05Solve\x12\x10.PolynomialInput\x1a\x11.PolynomialOutput\"\x00\x62\x06proto3'
    ),
)


_POLYNOMIALINPUT = _descriptor.Descriptor(
    name='PolynomialInput',
    full_name='PolynomialInput',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='x',
            full_name='PolynomialInput.x',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=20,
    serialized_end=48,
)


_POLYNOMIALOUTPUT = _descriptor.Descriptor(
    name='PolynomialOutput',
    full_name='PolynomialOutput',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='res_x',
            full_name='PolynomialOutput.res_x',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR
        ),
        _descriptor.FieldDescriptor(
            name='res_y',
            full_name='PolynomialOutput.res_y',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=50,
    serialized_end=98,
)

DESCRIPTOR.message_types_by_name['PolynomialInput'] = _POLYNOMIALINPUT
DESCRIPTOR.message_types_by_name['PolynomialOutput'] = _POLYNOMIALOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolynomialInput = _reflection.GeneratedProtocolMessageType(
    'PolynomialInput',
    (_message.Message,),
    {
        'DESCRIPTOR': _POLYNOMIALINPUT,
        '__module__': 'polynomial_pb2'
        # @@protoc_insertion_point(class_scope:PolynomialInput)
    },
)
_sym_db.RegisterMessage(PolynomialInput)

PolynomialOutput = _reflection.GeneratedProtocolMessageType(
    'PolynomialOutput',
    (_message.Message,),
    {
        'DESCRIPTOR': _POLYNOMIALOUTPUT,
        '__module__': 'polynomial_pb2'
        # @@protoc_insertion_point(class_scope:PolynomialOutput)
    },
)
_sym_db.RegisterMessage(PolynomialOutput)


_POLYNOMIAL = _descriptor.ServiceDescriptor(
    name='Polynomial',
    full_name='Polynomial',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=100,
    serialized_end=160,
    methods=[
        _descriptor.MethodDescriptor(
            name='Solve',
            full_name='Polynomial.Solve',
            index=0,
            containing_service=None,
            input_type=_POLYNOMIALINPUT,
            output_type=_POLYNOMIALOUTPUT,
            serialized_options=None,
        ),
    ]
)
_sym_db.RegisterServiceDescriptor(_POLYNOMIAL)

DESCRIPTOR.services_by_name['Polynomial'] = _POLYNOMIAL

# @@protoc_insertion_point(module_scope)