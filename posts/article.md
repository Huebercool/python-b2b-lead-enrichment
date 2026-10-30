---
title: Automated B2B Lead Enrichment Pipeline in Python (Under 30 Lines)
published: true
tags: python, webdev, devops, productivity
canonical_url: https://github.com/huebercool/python-b2b-lead-enrichment
---

Building sales intelligence and lead enrichment pipelines often requires piecing together bulky enterprise SDKs. You can automate domain profiling, tech stack detection, and email deliverability checks using a streamlined Python script.

## Quick Setup

Clone the open-source repository and install dependencies:

```bash
git clone https://github.com/huebercool/python-b2b-lead-enrichment.git
cd python-b2b-lead-enrichment
pip install -r requirements.txt
export RAPIDAPI_KEY="your_api_key_here"
python lead_enrichment.py
