# Pic Poet: AI-Powered Image-To-Poem Generator

Stuart Rimel, Fall 2023

[Link to deployed website](https://pic-poet-syj2dyiavq-uw.a.run.app)

## Overview

Pic Poet is a Flask application develop as part of a class project at PSU.
This web app allows users to upload images, leveraging generative AI to
generate unique poems inspired by the visual content. This project was
deployed on Google's Cloud Platform using Cloud Run.

## Key Features

- **Google Cloud Vision AI Integration:** Pic Poet harnesses the power of Google Cloud
  Vision AI to analyze and annotate the uploaded images, extracting objects and labels.
- **OpenAI GPT Model Integration:** Pic Poet transforms the Google Cloud Vision annoations
  into eloquent poems via integration with OpenAI's GPT-3.5 turbo model.
- **Download as PDF:** Users can download their generated poems as a PDF to save and share
  with friends.

## Dependencies

- For PDF conversion
  - Must install wkhtmltopdf
    - `sudo apt-get install wkhtmltopdf`
  - If program is having trouble finding the bin on PATH, then you may optionally provide
    the path explicitly with an environment variable:
    - `WKHTMLTOPDF_PATH=<path>`
