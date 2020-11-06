![](https://img.shields.io/badge/api-v2.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/groupdocs-signature-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/groupdocs-signature-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/groupdocs-signature-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/groupdocs-signature-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-signature-cloud/groupdocs-signature-cloud-java)](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-java/blob/master/LICENSE) 

# Python SDK to Document Signature REST API

[GroupDocs.Signature Cloud SDK for Python](https://products.groupdocs.cloud/signature/python) wraps GroupDocs.Signature RESTful API so you may integrate Document Signing features in your own apps with zero initial cost.

GroupDocs.Signature Cloud API allows the developers to create, remove, verify and search different types of signature objects in a number of different formats including Word documents, Excel speradsheets, PowerPoint presentations, PDF, OpenDocument formats & images.

## Manage Digital Signatures in the Cloud

- [Support for 55+ document & image formats](https://docs.groupdocs.cloud/signature/supported-document-formats/).
- Add stamp, text, barcode, QR-code, image and digital signatures.
- Search & verify signatures.
- Update & delete signatures by ID.
- Extract document properties like size, creation & update dates, page count and so on.
- Get a list of supported document formats.
- Get a list of supported barcode & QR-Code encode types.

Check out the [Developer's Guide](https://docs.groupdocs.cloud/signature/developer-guide/) to know more about GroupDocs.Signature REST API.

## Supported Signature Types

- **Text Signature** 
- **Image Signature** 
- **Barcode Signature** 
- **QR-Code Signature**
- **Digital Signature** 
- **Stamp Signature**

## Microsoft Office Formats

**Microsoft Word:** DOC, DOCM, DOCX, DOT, DOTM, DOTX\
**Microsoft Excel:** XLS, XLSB, XLSM, XLSX\
**Microsoft PowerPoint:** POTM, POTX, PPS, PPSM, PPSX, PPT, PPTM, PPTX

## Other Document Formats

**Portable:** PDF\
**OpenDocument:** ODT, OTT, ODP, OTP\
**Images:** BMP, PNG, JPG, JPEG, TIFF, GIF, CDR, CGM, CMX, DCM, DJVU, DNG, EMF, WMF, EPS, ICO, JP2, ODG, PCL, PS, PSD, SVG, WEBP\
**Others:** TXT, RTF, CSV, TSV

## Get Started with GroupDocs.Signature Cloud SDK for Python

First create an account at [GroupDocs for Cloud](https://dashboard.groupdocs.cloud/) and get your application information. Next, follow the installation steps as given below.

### Installation

Install `groupdocs-signature-cloud` with [PIP](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/project/groupdocs-signature-cloud/).

```sh
pip install groupdocs-signature-cloud
```

Or clone repository and install it via [Setuptools](http://pypi.python.org/pypi/setuptools): 

```sh
python setup.py install
```

## Get Supported File Formats for e-Signature

```python
# Import module
import groupdocs_signature_cloud

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
app_sid = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
app_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Create instance of the API
api = groupdocs_signature_cloud.InfoApi.from_keys(app_sid, app_key)

try:
    # Retrieve supported file-formats
    response = api.get_supported_file_formats()

    # Print out supported file-formats
    print("Supported file-formats:")
    for format in response.formats:
        print('{0} ({1})'.format(format.file_format, format.extension)) 
except groupdocs_signature_cloud.ApiException as e:
    print("Exception when calling get_supported_file_formats: {0}".format(e.message))
```

## GroupDocs.Signature Cloud SDKs in Popular Languages

| .NET | Java | PHP | Python | Ruby | Node.js |
|---|---|---|---|---|---|
| [GitHub](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-dotnet) | [GitHub](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-java) | [GitHub](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-php) | [GitHub](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-python) | [GitHub](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-ruby)  | [GitHub](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-node) |
| [NuGet](https://www.nuget.org/packages/GroupDocs.Signature-Cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-signature-cloud) | [Composer](https://packagist.org/packages/groupdocscloud/groupdocs-signature-cloud) | [PIP](https://pypi.org/project/groupdocs-signature-cloud/) | [GEM](https://rubygems.org/gems/groupdocs_signature_cloud)  | [NPM](https://www.npmjs.com/package/groupdocs-signature-cloud) | 

[Home](https://www.groupdocs.cloud/) | [Product Page](https://products.groupdocs.cloud/signature/python) | [Documentation](https://docs.groupdocs.cloud/signature/) | [Live Demo](https://products.groupdocs.app/signature/total) | [API Reference](https://apireference.groupdocs.cloud/signature/) | [Code Samples](https://github.com/groupdocs-signature-cloud/groupdocs-signature-cloud-dotnet-samples) | [Blog](https://blog.groupdocs.cloud/category/signature/) | [Free Support](https://forum.groupdocs.cloud/c/signature) | [Free Trial](https://dashboard.groupdocs.cloud)
