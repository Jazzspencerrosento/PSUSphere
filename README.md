Project Name: PSUSphere

Short description:
PSUSphere is a Django-based management platform designed to organize and track student participation in campus organizations. It provides a structured database to manage the relationships between students, their academic programs, their respective colleges, and the student organizations they join .

List of Features:
Academic Hierarchy Management: Allows for the creation and tracking of different Colleges and their specific Academic Programs.
Student Profiling: Records detailed student information, including student IDs, full names, and assigned academic programs .

Organization Tracking: Manages a registry of student organizations, including their names, descriptions, and the colleges they are affiliated with.

Membership Management: Tracks which students belong to which organizations, including the specific date they joined.

Enhanced Administrative Dashboard: A customized back-end interface that allows administrators to:

.Search and filter records by name, college, or date.
.View specific details like "Member Program" directly within the membership lists.

Automated Data Seeding: A custom management command (create_initial_data) that uses the Faker package to automatically generate bulk test data for organizations, students, and memberships .

Dependency Tracking: Utilizes a requirements.txt file to ensure consistent environment setups across different development machines.

Authors: 
Jazz Spencer G. Rosento
Charles Maverick Gabarda