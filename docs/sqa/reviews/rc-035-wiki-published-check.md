# Review of WIKI

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-035 |
| CrossReference | [WIKI], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [WIKI]
- Checklist used: [QC-WIKI-001]
- Scope: delta re-review of criterion 14; reason: published wiki checked after the merge; earlier record [RC-033]
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | Unchanged since RC-033. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Unchanged since RC-033. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Unchanged since RC-033. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | Unchanged since RC-033. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Unchanged since RC-033. |
| 6 | The sidebar does not repeat the page list per language | Pass | Unchanged since RC-033. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | Unchanged since RC-033. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Unchanged since RC-033. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | Unchanged since RC-033. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Unchanged since RC-033. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Unchanged since RC-033. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Unchanged since RC-033. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Unchanged since RC-033. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | Checked on the published wiki: 22 pages answer 200 (7 pages in 3 languages plus the sidebar), the sidebar and every language line link to existing pages, and the four screenshots load from the raw URLs. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; no layout rule changes. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | Unchanged: flat folder. |

## Overall Verdict

Go — Criterion 14 is now confirmed on the published wiki; every mandatory criterion passes.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[WIKI]: ../../wiki/Home.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
