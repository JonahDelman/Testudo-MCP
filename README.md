# Testudo MCP

An MCP (Model Context Protocol) server that provides access to University of Maryland (UMD) course data through the UMD.io API. This server enables AI assistants to retrieve comprehensive information about UMD courses, departments, professors, and majors.

## Features

### Course Information
- **Get courses by department**: Retrieve all courses for a specific UMD department
- **Get courses by gen-ed**: Find courses that fulfill specific general education requirements
- **Get specific courses**: Look up detailed information for specific course codes
- **Get course sections**: Access section details including meeting times, instructors, and availability

### Department and Major Information  
- **List all departments**: Get a complete list of UMD departments
- **List all majors**: Retrieve information about all available majors including college affiliation

### Professor Information
- **Find professors by course**: Discover which professors teach a specific course
- **Find courses by professor**: See what courses a professor has taught

## Installation

### Prerequisites
- Python 3.13 or higher
- uv (recommended) or pip for package management

### Using uv (recommended)
```bash
git clone https://github.com/yourusername/testudo-mcp.git
cd testudo-mcp
uv sync
```

### Using pip
```bash
git clone https://github.com/yourusername/testudo-mcp.git
cd testudo-mcp
pip install -e .
```

## Usage

### Running the MCP Server
```bash
python testudo.py
```

The server runs using the Model Context Protocol with stdio transport, making it compatible with AI assistants that support MCP.

### Available Tools

#### `get_courses(dept: str = "", gen_ed: str = "") -> str`
Retrieves courses for a department and/or general education requirement.
- `dept`: Department code (e.g., "CMSC", "MATH")
- `gen_ed`: General education code (e.g., "FSAW", "DSHS")

#### `get_course_by_course_code(courses: list) -> str`
Gets detailed information for specific course codes.
- `courses`: List of course codes (e.g., ["CMSC131", "MATH140"])

#### `get_course_sections(course: str) -> str`
Retrieves section information for a specific course.
- `course`: Course code (e.g., "CMSC131")

#### `get_departments() -> str`
Lists all UMD departments.

#### `get_majors() -> str`
Lists all UMD majors with college information.

#### `get_professors_for_course(course: str) -> str`
Finds professors who teach a specific course.
- `course`: Course code (e.g., "CMSC131")

#### `get_courses_by_professor(professor: str) -> str`
Retrieves courses taught by a specific professor.
- `professor`: Professor's name

## Data Sources

This MCP server uses the [UMD.io API](https://api.umd.io) to retrieve up-to-date information about:
- Course catalogs and descriptions
- Prerequisites and corequisites
- Course sections and schedules
- Professor assignments
- Department and major listings

## Configuration

The server connects to the UMD API at `https://api.umd.io/v1`. No API key is required as the UMD.io API is publicly accessible.

## Response Format

All tools return formatted strings with detailed information:

### Course Information Includes:
- Course name and department
- Credits and description
- Prerequisites and corequisites
- General education categories
- Grading methods
- Section details

### Section Information Includes:
- Meeting times and locations
- Instructor assignments
- Seat availability
- Waitlist information

### Professor Information Includes:
- Professor names
- Course teaching history
- Semester information

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.

## Acknowledgments

- Built using the [FastMCP](https://github.com/pydantic/fastmcp) framework
- Data provided by the [UMD.io API](https://api.umd.io)
- Serves the University of Maryland community

## Support

For issues or questions:
1. Check existing GitHub issues
2. Create a new issue with detailed information
3. Include error messages and reproduction steps
