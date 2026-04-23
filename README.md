mallaymagic-qa

Playwright automation suite for MallayMagic.com, a professional magician's website. This suite was written TDD-style: tests first, and the site will be built to conform to the tests. 

The tests serve as acceptance criteria, defining what the site needs to do as well as testing if they do it.
The automation suite is designed as a regression harness. It's not meant to replace manual testing, as a site like this lives or dies on trust, tone, and buyer psychology(none of which a selector can measure).

Structure
tests/
  smoke/       — Is the page working
  acceptance/  — Does each feature function as intended
Smoke tests check page titles and basic availability. Acceptance tests cover navigation behaviour, structural elements, CTAs, form interaction, and a gated email signup flow.

Test approach

Different elements call for different locator strategies:
get_by_test_id() for structural elements like summaries and media sections

get_by_role() for navigation, buttons, and forms

get_by_label() for form fields — checking for labels rather than using field names doubles as an accessibility check

get_by_text() for user-facing confirmation messages

to_have_url() for navigation behaviour


The form tests cover both happy path and empty-submission validation. The email gate tests verify both directions — content hidden before submission, visible after.

Baseline runtime: ~3 minutes against the live site, sequential, headless Chromium. Parallelization via pytest-xdist would be a straightforward next step for CI use.

Status:
The site is currently under development. All acceptance tests are intentionally failing — that's the point. They'll pass as pages are built to spec.

