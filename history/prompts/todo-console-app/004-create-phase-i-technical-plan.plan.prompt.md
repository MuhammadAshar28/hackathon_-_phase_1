---
id: 4
title: Create Phase I Technical Plan
stage: plan
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-console-app
branch: 1-todo-console-app
user: NLN
command: sp.plan
labels: [planning,architecture,todo-app,phase1]
links:
  spec: specs/1-todo-console-app/spec.md
  plan: specs/1-todo-console-app/plan.md
  adr: null
  pr: null
files:
 - specs/1-todo-console-app/plan.md
 - specs/1-todo-console-app/research.md
 - specs/1-todo-console-app/data-model.md
 - specs/1-todo-console-app/quickstart.md
 - specs/1-todo-console-app/contracts/cli-interface.md
tests:
---

## Prompt

```text
Phase I Technical Plan

Evolution of Todo — In-Memory Python Console Application

1. Scope Confirmation (Phase I Only)

This technical plan implements only the Phase I requirements defined by the Global Constitution:

Single-user

Single Python program

In-memory task management

Console-based interface

Basic task lifecycle (create, view, update, complete, delete)

Simple, reliable, and understandable behavior

🚫 Explicitly excluded:

Persistence (files, databases)

Authentication or users

Tags, projects, collaboration

AI, automation, analytics

Web, APIs, frameworks

2. High-Level Application Structure
Single Python Program Structure

The application will be implemented as one Python file, logically divided using functions and in-memory state.

todo_app.py

Logical Sections (Not Separate Files)

Data Layer

Task storage

ID generation

Task lookup and mutation logic

Business Logic

Create task

Update task

Complete task

Delete task

Retrieve task(s)

CLI Layer

Menu display

User input handling

Output formatting

Error messaging

This separation is conceptual, not modularized into files, to preserve simplicity per Phase I.

3. In-Memory Data Structures
Task Representation

Each task is represented as a dictionary with a fixed schema:

{
  "id": int,
  "title": str,
  "completed": bool
}

Task Storage

Tasks are stored in a list:

tasks = []


Rationale:

Ordered display

Simple iteration

Sufficient for Phase I scale

No premature optimization

4. Task Identification Strategy (ID Generation)
ID Type

Integer (int)

Strategy

Maintain a global counter:

next_task_id = 1

Behavior

When a task is created:

Assign current next_task_id

Increment next_task_id by 1

IDs are never reused, even if tasks are deleted

Guarantees

Unique within runtime

Predictable

Simple

No dependency on storage or time

5. CLI Control Flow
Main Loop

The application runs inside a continuous loop:

while True:
  show menu
  get user input
  execute selected action

Menu Options (Phase I Only)

Example options:

Add task

View all tasks

Update task title

Mark task as completed

Delete task

Exit

Input Handling

All user input is read using input()

Numeric choices are converted using int()

Invalid conversions are caught and handled

Exit Condition

User explicitly selects the exit option

Program terminates cleanly using break

6. Separation of Responsibilities
Data & Logic Functions

Functions that do not interact with user input/output:

create_task(title)

get_all_tasks()

find_task_by_id(task_id)

update_task(task_id, new_title)

complete_task(task_id)

delete_task(task_id)

These functions:

Operate only on in-memory data

Return success/failure indicators or data

Do not print anything

CLI Functions

Functions responsible for:

Displaying menus

Prompting user input

Printing tasks and messages

Handling errors gracefully

Examples:

show_menu()

handle_add_task()

handle_update_task()

7. Error Handling Strategy
Invalid Menu Input

Handled using:

try/except ValueError

Re-prompt user without crashing

Example:

Non-numeric menu choice

Out-of-range option

Missing Task (Invalid ID)

When a task ID does not exist:

find_task_by_id() returns None

CLI layer displays a clear message:

“Task not found.”

No exceptions propagate to the user.

Empty State Handling

If no tasks exist:

Viewing tasks displays:

“No tasks available.”

Update/delete/complete operations warn user appropriately

8. Output & UX Rules (Phase I)

Clear, minimal text output

No colors or formatting dependencies

Immediate feedback after each action

No silent failures

UX goal: Zero confusion, zero learning curve

9. Non-Negotiable Phase I Constraints (Enforced)

✅ No persistence

✅ No external libraries

✅ No background processes

✅ No hidden state

✅ No future-phase abstractions

This plan intentionally avoids extensibility hooks to remain constitutionally compliant.

10. Completion Criteria

Phase I is considered complete when:

All task operations work reliably in a single run

Application never crashes on invalid input

Logic and CLI responsibilities are clearly separated

Code remains readable and minimal
## Response snapshot

Created comprehensive technical plan for Phase I Todo Console Application with all required components:

1. Implementation Plan (plan.md): Detailed architecture and structure decision
2. Research Document (research.md): Technical decisions with rationale and alternatives
3. Data Model (data-model.md): Complete entity definitions and validation rules
4. Quickstart Guide (quickstart.md): User instructions and application usage
5. Interface Contract (contracts/cli-interface.md): CLI interaction patterns and error handling

All artifacts comply with the global constitution and Phase I specification requirements. The plan implements a single-file Python console application with clean separation between data management (Task/TaskManager classes) and user interface (CLI functions). The application uses in-memory storage with sequential ID generation and comprehensive error handling.

## Outcome

- ✅ Impact: Complete technical plan created for Phase I implementation
- 🧪 Tests: N/A (Planning artifacts)
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, contracts/
- 🔁 Next prompts: Ready for task breakdown with /sp.tasks
- 🧠 Reflection: Plan aligns with constitution and specification requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A