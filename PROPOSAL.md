# AI Code Reviewer - Project Proposal

This document outlines 5 unique AI-powered features designed to make this AI Code Reviewer stand out as a final-year diploma project.

## 1. Semantic Impact & Side-Effect Analysis (Implemented)
Instead of just reviewing the diff, the AI analyzes the "ripple effect" of changes. It identifies which parts of the system might be affected by the logic changes and uses an LLM to explain the *logical* risk (e.g., "Changing the tax calculation here may affect the final invoice generation in the accounting module").

## 2. Automated Security "Proof-of-Concept" (PoC) Generator
When the AI detects a vulnerability (like a SQL injection or unsafe regex), it generates a temporary, failing test case that demonstrates the exploit. This makes the risk undeniable and serves as an educational tool for the developer.

## 3. Architectural Consistency Guard
The AI learns the project's specific architectural patterns (e.g., "We always use the Repository pattern for database access") and flags code that violates these patterns, even if the code is syntactically correct and bug-free.

## 4. Interactive "Rubber Duck" Refactoring
A conversational interface where the developer can discuss refactoring options with the AI reviewer. For example, asking for a performance-optimized version of a complex loop while maintaining readability.

## 5. Historical "Bug-Magnet" Warning
By analyzing git history and previous bug reports, the AI identifies "fragile" files or modules. It then applies stricter review criteria to changes in these high-risk areas.
