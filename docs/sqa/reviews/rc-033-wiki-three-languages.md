# Review of WIKI

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-033 |
| CrossReference | [WIKI], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5dc94c1] |

---

## Artifact Under Review

- Instance reviewed: [WIKI]
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `_Sidebar.md` exists in `docs/wiki/`. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Starts with the bold title, then one English list with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Seven links, one per English page; a script found no dead link. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wikis, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last with English, Dansk and Bahasa Malaysia, each linking to its Home page. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | The sidebar is hand written, not generated, so no generator comment applies. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | PO language is English; Danish and Bahasa Malaysia (ms) are added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Seven pages in each of the three languages. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with `**English** · [Dansk](..) · [Bahasa Malaysia](..)` with the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Files are `<Page>-da.md` and `<Page>-ms.md`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, file names, class names and IDs are English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The wiki is published only when the pull request is merged; links are checked on the host after the merge (delta review). |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; no layout rule changes. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All pages and `_Sidebar.md` are directly in `docs/wiki/`. |

## Overall Verdict

Go-with-conditions — All mandatory criteria pass except criterion 14, which can only be checked on the published wiki after the merge; the delta review follows the merge.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the sidebar and every page on the published wiki and record a delta review | S01 | after the merge |

---

[WIKI]: ../../wiki/Home.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[5dc94c1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/commit/5dc94c137814bec4a092751030acb1316d4b7e77
