# StudyClaudeCode

## Git Workflow
- **Main branch**: `master` (production-ready, no direct commits)
- **Development branch**: `dev-claude` (main working branch)
- **Process**: Commit to `dev-claude` → Create PR to `master` → Self-review → Merge

## PR Review Process
- Create PR from `dev-claude` to `master`
- Perform self-review of changes (code quality, tests, docs)
- Use `/review` skill for automated code review
- Ensure all Conventional Commits guidelines are met
- Then merge to `master`

## Git Commit Rules
- Use Conventional Commits format: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, etc.
- Write commit messages in English
- Keep subject line under 50 characters
- Example: `feat: add user authentication module`
