# Pic Poet

Stuart Rimel, Fall 2023

## Overview

Pic Poet is a flask app that allows a user to upload a photo and then AI will be utilized
to generate a poem about the photo that was uploaded.

This web app uses Google Cloud Vision AI to analyze and annotate the image and then using
integration with OpenAI GPT models will generate a poem about the image.

## Setup

Dependencies:

- For PDF conversion
  - Must install wkhtmltopdf
    - `sudo apt-get install wkhtmltopdf`
  - If program is having trouble finding the bin on PATH, then you may optionally provide
    the path explicitly with env var:
    - `WKHTMLTOPDF_PATH=<path>`
