from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

UMD_API_BASE = "https://api.umd.io/v1"

async def make_request(url: str) -> dict[str, Any] | None:
    headers = {
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
def format_course(course: dict) -> str:
    gradingMethod = ""
    for method in course.get('grading_method', 'Unknown'):
        gradingMethod += f"{method}, "
    gradingMethod = gradingMethod.rstrip(", ")
    relationships = course.get('relationships', 'Unknown')
    if relationships != 'Unknown':
        allRelationships = f"""
        Coreqs: {relationships.get('coreqs', 'Unknown')}
        Prereqs: {course.get('prereqs', 'Unknown')}
        Formerly: {course.get('formerly', 'Unknown')}
        Restrictions: {course.get('restrictions', 'N/A')}
        Additional Info: {course.get('additional_info', 'None')}
        Also Offered As: {course.get('also_offered_as', 'Unknown')}
        Credit Granted for: {course.get('credit_granted_for', 'Unknown')}"""
    
    return f"""
    Semester: {course.get('semester', 'Unknown')}
    Name: {course.get('name', 'No name provided')}
    Department: {course.get('dept_id', 'No department')}
    Credits: {course.get('credits', 'N/A')}
    Description: {course.get('description', 'No description')}
    Grading Method: {course.get('grading_method', 'Unknown')}
    Gen Eds: {course.get('gen_ed', 'Unknown')}
    Relationships: {allRelationships}
    Sections: {course.get('sections', 'Unknown')}
    """
def format_course_section(section : dict) -> str:
    meetingData = ""
    if section.get('meetings', 'Unknown') != 'Unknown':
        for meeting in section.get('meetings', 'Unknown'):
            meetingData += f"""
            Days: {meeting.get('days', 'Unknown')}
            Room: {meeting.get('room', 'Unknown')}
            Building: {meeting.get('building', 'Unknown')}
            Class Type: {meeting.get('classtype', 'Unknown')}
            Start Time: {meeting.get('start_time', 'Unknown')}
            End Time: {meeting.get('end_time', 'Unknown')}
        """
    meetingData = meetingData.rstrip(", ")
    instructors = ""
    if section.get('instructors', 'Unknown') != 'Unknown':
        for instructor in section.get('instructors', 'Unknown'):
            instructors += f"{instructor},"
    instructors = instructors.rstrip(", ")
    return f"""
    Semester: {section.get('semester', 'Unknown')}
    Section ID: {section.get('section_id', 'No department')}
    Section Number: {section.get('number', 'N/A')}
    Number of Seats: {section.get('seats', 'No description')}
    Course Meeting Information: {meetingData}
    Open Seats: {section.get('open_seats', 'Unknown')}
    Number of Students on Waitlist: {section.get('waitlist', 'Unknown')}
    Instructors: {instructors}
    """
@mcp.tool()
async def get_courses(courses: list) -> str:
    """Gets UMD courses. Takes a list of course codes as an arg"""
    courseList = ""
    for course in courses:
        courseList += f"{course},"
    courseList = courseList.rstrip(", ")
    url = f"{UMD_API_BASE}/courses/{courseList}"
    data = await make_request(url)

    if not data:
        return "Unable to fetch course or no course found."

    allData = [format_course(c) for c in data]
    return "\n---\n".join(allData)
@mcp.tool()
async def get_course_sections(courses: list) -> str:
    """Gets sections for UMD courses. Takes a list of course codes as an arg"""
    courseList = ""
    for course in courses:
        courseList += f"{course},"
    courseList = courseList.rstrip(", ")
    url = f"{UMD_API_BASE}/courses/{courseList}/sections"
    data = await make_request(url)

    if not data:
        return "Unable to fetch course or no course found."

    allData = [format_course_section(c) for c in data]
    return "\n---\n".join(allData)


if __name__ == "__main__":
    mcp.run(transport='stdio')
