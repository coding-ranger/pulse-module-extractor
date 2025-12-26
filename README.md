Overview

This project is an AI-powered system that automatically extracts modules and submodules from documentation-based help websites and generates accurate, structured descriptions purely from the source content.

It is designed to work with large documentation portals such as:

WordPress

Zendesk-based help centers

B2B SaaS documentation platforms



🎯 Key Features

Recursive documentation crawling

Intelligent content extraction (no headers/footers)

Hierarchical structure inference (modules & submodules)

LLM-assisted summarization using extracted content only

Streamlit-based UI + CLI support

JSON output suitable for downstream systems



Architecture

Input URLs
   ↓
Crawler (Domain-restricted BFS)
   ↓
HTML Cleaning & Structure Parsing
   ↓
Module/Submodule Inference
   ↓
Description Generation (LLM)
   ↓
Structured JSON Output