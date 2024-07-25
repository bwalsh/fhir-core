# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Extension
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class Extension(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Optional Extensions Element.
    Optional Extension Element - found in all resources.
    """

    __resource_type__ = "Extension"

    url: fhirtypes.UriType = Field(
        None,
        alias="url",
        title="identifies the meaning of the extension",
        description=(
            "Source of the definition for the extension code - a logical name or a "
            "URL."
        ),
        # if property is element of this resource.
        json_schema_extra={"element_property": True, "element_required": True},
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        # if property is element of this resource.
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueAge: fhirtypes.AgeType = Field(
    #     None,
    #     alias="valueAge",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueAnnotation: fhirtypes.AnnotationType = Field(
    #     None,
    #     alias="valueAnnotation",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueAttachment: fhirtypes.AttachmentType = Field(
    #     None,
    #     alias="valueAttachment",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueAvailability: fhirtypes.AvailabilityType = Field(
    #     None,
    #     alias="valueAvailability",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    valueBase64Binary: fhirtypes.Base64BinaryType = Field(
        None,
        alias="valueBase64Binary",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBoolean: fhirtypes.BooleanType = Field(
        None,
        alias="valueBoolean",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCanonical: fhirtypes.CanonicalType = Field(
        None,
        alias="valueCanonical",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCode: fhirtypes.CodeType = Field(
        None,
        alias="valueCode",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
    #     None,
    #     alias="valueCodeableConcept",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueCodeableReference: fhirtypes.CodeableReferenceType = Field(
    #     None,
    #     alias="valueCodeableReference",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueContactDetail: fhirtypes.ContactDetailType = Field(
    #     None,
    #     alias="valueContactDetail",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueContactPoint: fhirtypes.ContactPointType = Field(
    #     None,
    #     alias="valueContactPoint",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueCount: fhirtypes.CountType = Field(
    #     None,
    #     alias="valueCount",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueDataRequirement: fhirtypes.DataRequirementType = Field(
    #     None,
    #     alias="valueDataRequirement",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    valueDate: fhirtypes.DateType = Field(
        None,
        alias="valueDate",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDateTime: fhirtypes.DateTimeType = Field(
        None,
        alias="valueDateTime",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDecimal: fhirtypes.DecimalType = Field(
        None,
        alias="valueDecimal",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueDistance: fhirtypes.DistanceType = Field(
    #     None,
    #     alias="valueDistance",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueDosage: fhirtypes.DosageType = Field(
    #     None,
    #     alias="valueDosage",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueDuration: fhirtypes.DurationType = Field(
    #     None,
    #     alias="valueDuration",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueExpression: fhirtypes.ExpressionType = Field(
    #     None,
    #     alias="valueExpression",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueExtendedContactDetail: fhirtypes.ExtendedContactDetailType = Field(
    #     None,
    #     alias="valueExtendedContactDetail",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueHumanName: fhirtypes.HumanNameType = Field(
    #     None,
    #     alias="valueHumanName",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    valueId: fhirtypes.IdType = Field(
        None,
        alias="valueId",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueIdentifier: fhirtypes.IdentifierType = Field(
    #     None,
    #     alias="valueIdentifier",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     json_schema_extra={
    #         "element_property": True,
    #         "one_of_many": "value",
    #         "one_of_many_required": False,
    #     },
    # )

    valueInstant: fhirtypes.InstantType = Field(
        None,
        alias="valueInstant",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueInteger: fhirtypes.IntegerType = Field(
        None,
        alias="valueInteger",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueInteger64: fhirtypes.Integer64Type = Field(
        None,
        alias="valueInteger64",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueMarkdown: fhirtypes.MarkdownType = Field(
        None,
        alias="valueMarkdown",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueMeta: fhirtypes.MetaType = Field(
    #     None,
    #     alias="valueMeta",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueMoney: fhirtypes.MoneyType = Field(
    #     None,
    #     alias="valueMoney",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    valueOid: fhirtypes.OidType = Field(
        None,
        alias="valueOid",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
    #     None,
    #     alias="valueParameterDefinition",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valuePeriod: fhirtypes.PeriodType = Field(
    #     None,
    #     alias="valuePeriod",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    valuePositiveInt: fhirtypes.PositiveIntType = Field(
        None,
        alias="valuePositiveInt",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueQuantity: fhirtypes.QuantityType = Field(
    #     None,
    #     alias="valueQuantity",
    #     title="Value of extension",
    #     description=(
    #         "Value of extension - must be one of a constrained set of the data "
    #         "types (see [Extensibility](extensibility.html) for a list)."
    #     ),
    #     # if property is element of this resource.
    #     element_property=True,
    #     # Choice of Data Types. i.e value[x]
    #     one_of_many="value",
    #     one_of_many_required=False,
    # )

    # valueRange: fhirtypes.RangeType = Field(
    #    None,
    #    alias="valueRange",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    # valueRatio: fhirtypes.RatioType = Field(
    #    None,
    #    alias="valueRatio",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    # valueRatioRange: fhirtypes.RatioRangeType = Field(
    #    None,
    #    alias="valueRatioRange",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    # valueReference: fhirtypes.ReferenceType = Field(
    #    None,
    #    alias="valueReference",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    # valueRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
    #    None,
    #    alias="valueRelatedArtifact",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    # valueSampledData: fhirtypes.SampledDataType = Field(
    #    None,
    #    alias="valueSampledData",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    # valueSignature: fhirtypes.SignatureType = Field(
    #    None,
    #    alias="valueSignature",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    valueString: fhirtypes.StringType = Field(
        None,
        alias="valueString",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueTime: fhirtypes.TimeType = Field(
        None,
        alias="valueTime",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueTiming: fhirtypes.TimingType = Field(
    #    None,
    #    alias="valueTiming",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    # valueTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
    #    None,
    #    alias="valueTriggerDefinition",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    valueUnsignedInt: fhirtypes.UnsignedIntType = Field(
        None,
        alias="valueUnsignedInt",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueUri: fhirtypes.UriType = Field(
        None,
        alias="valueUri",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueUrl: fhirtypes.UrlType = Field(
        None,
        alias="valueUrl",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    # valueUsageContext: fhirtypes.UsageContextType = Field(
    #    None,
    #    alias="valueUsageContext",
    #    title="Value of extension",
    #    description=(
    #        "Value of extension - must be one of a constrained set of the data "
    #        "types (see [Extensibility](extensibility.html) for a list)."
    #    ),
    # if property is element of this resource.
    #    element_property=True,
    # Choice of Data Types. i.e value[x]
    #    one_of_many="value",
    #    one_of_many_required=False,
    # )

    valueUuid: fhirtypes.UuidType = Field(
        None,
        alias="valueUuid",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        json_schema_extra={
            "element_property": True,
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Extension`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "url",
            "valueBase64Binary",
            "valueBoolean",
            "valueCanonical",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInstant",
            "valueInteger",
            "valueInteger64",
            "valueMarkdown",
            "valueOid",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueUrl",
            "valueUuid",
            "valueAddress",
            "valueAge",
            "valueAnnotation",
            "valueAttachment",
            "valueCodeableConcept",
            "valueCodeableReference",
            "valueCoding",
            "valueContactPoint",
            "valueCount",
            "valueDistance",
            "valueDuration",
            "valueHumanName",
            "valueIdentifier",
            "valueMoney",
            "valuePeriod",
            "valueQuantity",
            "valueRange",
            "valueRatio",
            "valueRatioRange",
            "valueReference",
            "valueSampledData",
            "valueSignature",
            "valueTiming",
            "valueContactDetail",
            "valueDataRequirement",
            "valueExpression",
            "valueParameterDefinition",
            "valueRelatedArtifact",
            "valueTriggerDefinition",
            "valueUsageContext",
            "valueAvailability",
            "valueExtendedContactDetail",
            "valueDosage",
            "valueMeta",
        ]

    def get_one_of_many_fields(self):
        """ """
        return {
            "value": [
                "valueAddress",
                "valueAge",
                "valueAnnotation",
                "valueAttachment",
                "valueAvailability",
                "valueBase64Binary",
                "valueBoolean",
                "valueCanonical",
                "valueCode",
                "valueCodeableConcept",
                "valueCodeableReference",
                "valueCoding",
                "valueContactDetail",
                "valueContactPoint",
                "valueCount",
                "valueDataRequirement",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueDistance",
                "valueDosage",
                "valueDuration",
                "valueExpression",
                "valueExtendedContactDetail",
                "valueHumanName",
                "valueId",
                "valueIdentifier",
                "valueInstant",
                "valueInteger",
                "valueInteger64",
                "valueMarkdown",
                "valueMeta",
                "valueMoney",
                "valueOid",
                "valueParameterDefinition",
                "valuePeriod",
                "valuePositiveInt",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueRatioRange",
                "valueReference",
                "valueRelatedArtifact",
                "valueSampledData",
                "valueSignature",
                "valueString",
                "valueTime",
                "valueTiming",
                "valueTriggerDefinition",
                "valueUnsignedInt",
                "valueUri",
                "valueUrl",
                "valueUsageContext",
                "valueUuid",
            ]
        }