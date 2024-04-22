from dataclasses import dataclass
from typing import Optional, List
from sd_data_adapter.models.util.Parcel import ProductCategory


@dataclass
class AgriProductType:
    """
    Class: AgriProductType

    Description:
    This class represents an agricultural product type. It stores information about the product's ID, type, name, root status, and other related attributes.

    Attributes:
        id (str): The unique identifier for the agricultural product type.
        type (str): The type of the agricultural product.
        name (str): The name of the agricultural product type.
        root (bool): Indicates whether the product is a root product or not.

    Optional Attributes:
        agroVocConcept (Optional[str]): Reference to the Agrovoc term associated with this product.
        alternateName (Optional[str]): Alternate name for the product type.
        category (Optional[List[ProductCategory]]): The category/categories to which the product type belongs.
        dataProvider (Optional[str]): The data provider who created this product type.
        dataCreated (Optional[str]): The date when the product type data was created.
        dateModified (Optional[str]): The date when the product type data was last modified.
        description (Optional[str]): The description of the product type.
        hasAgriProductTypeChildren (Optional[List['AgriProductType']]): List of child product types.
        hasAgriProductTypeParent (Optional[List['AgriProductType']]): List of parent product types.
        owner (Optional[List[str]]): List of product owners.
        relatedSource (Optional[List[str]]): List of related sources.
        seeAlso (Optional[List[str]]): List of references to other sources related to the product type.
        source (Optional[List[str]]): List of primary sources of the product type.
    """

    id: str
    type: str
    name: str
    root: bool

    agroVocConcept = Optional[str]
    alternateName: Optional[str] = None
    category: Optional[List[ProductCategory]] = None
    dataProvider: Optional[str] = None
    dataCreated: Optional[str] = None
    dateModified: Optional[str] = None
    description: Optional[str] = None
    hasAgriProductTypeChildren: Optional[List['AgriProductType']] = None
    hasAgriProductTypeParent: Optional[List['AgriProductType']] = None
    owner: Optional[List[str]] = None
    relatedSource: Optional[List[str]] = None
    seeAlso: Optional[List[str]] = None
    source: Optional[List[str]] = None