# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Run Commands
- Install dependencies: `uv sync`
- Run a Python file: `uv run <filename.py>`
- Run basic test: `uv run basic_example.py`
- Run other examples: `uv run examples/<example_name>.py`

## Environment Setup
- Required Python version: >=3.13
- Create .env file with at least one LLM API key (see .env.example)
- Optional: Configure logging with logfire

## Code Style Guidelines
- Follow PEP 8 conventions for Python code
- Use type hints and Pydantic models for validation
- Imports: standard library first, then third-party, then local (alphabetical order)
- Naming: snake_case for functions/variables, PascalCase for classes
- Error handling: Use assertions for preconditions, proper exception handling
- Include docstrings for classes and functions, especially for tools
- Follow the pattern of existing agent/workflow examples when creating new ones

## Project Structure
- examples/ - Example implementations for reference
- exercises/ - Exercise files for workshop
- docs/ - Documentation files