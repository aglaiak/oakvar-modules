# VRS ID
### A module for annotating single nucleotide variants with their corresponding VRS ID
The Global Alliance for Genomics and Health (GA4GH) recently introduced the Variant Representation Specification (VRS); a computational framework designed to facilitate and improve sharing of genetic information. VRS defines precise terminology for describing genetic variants and provides a means for storing and sharing variants unambiguously. The specification also provides a way to define a specific variant using a unique computed identifier, or VRS id. This module enables annotation of single nucleotide variants with their corresponding VRS computed identifier. 

For more information about VRS see: https://vrs.ga4gh.org/en/stable/
For more information about computed identifiers see: https://vrs.ga4gh.org/en/stable/impl-guide/computed\_identifiers.html#:~:text=VRS%20provides%20an%20algorithmic%20solution,identifiers%20when%20they%20are%20not.

![Screenshot](https://storage.oakvar.com/oakvar-public/screenshots/vrs_id/computed_identifiers.jpg)

For installation issues relating to the 'psycopg2' library, try the following in your terminal:  
`pip uninstall psycopg2 psycopg2-binary`  
`pip install psycopg2-binary`

If installation issues with 'psycopg2' still persist, try the following:  
MacOS:      `brew install postgresql` followed by `brew link postgresql`  
Ubuntu:     `sudo apt install libpq-dev`  
Fedora:     `sudo yum install postgresql-devel`
