# MallayMagic QA

Playwright automation suite for MallayMagic.com, a professional magician's website.

This suite was written TDD-style: tests first, with the site being built to conform to the tests. The tests serve as acceptance criteria, defining what the site needs to do while also providing a regression harness as the site develops.

This project is not meant to replace manual testing. A site like this depends heavily on trust, tone, and buyer psychology, none of which a selector can fully measure.

## Status

The site is currently under development.

All acceptance tests are intentionally failing at this stage. That is expected. The tests define the intended behaviour, and the site will be built to satisfy them.

## Test Structure

```text
tests/
├── smoke/
│   └── Basic availability and page title checks
└── acceptance/
    └── Feature behaviour and user-facing requirements
```

## What the Tests Cover

Smoke tests check basic page availability and titles.

Acceptance tests cover:

* Navigation behaviour
* Structural page elements
* Calls to action
* Form interaction
* A gated email signup flow

## Locator Strategy

Different elements use different locator strategies depending on what is being tested:

* `get_by_test_id()` for structural elements such as summaries and media sections
* `get_by_role()` for navigation, buttons, and forms
* `get_by_label()` for form fields
* `get_by_text()` for user-facing confirmation messages
* `to_have_url()` for navigation behaviour

Using `get_by_label()` for form fields also checks that the field is accessible by its label, rather than only testing the field name or selector.

## Example Coverage

The homepage acceptance tests verify that:

* Navigation links route to the expected pages
* The homepage summary is visible
* The primary call to action is visible
* The homepage media section is present

The free trick acceptance tests verify that:

* The page summary is visible
* The call to action is visible
* The free trick content is hidden before email submission
* The email gate is visible before submission
* Submitting a valid email reveals the gated content
* Submitting without an email shows a validation message

## Runtime

Baseline runtime is approximately 3 minutes against the live site, running sequentially in headless Chromium.
