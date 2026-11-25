# Proof status: the three words a problem page states

Solution status says whether a solution is written. Proof status says what
backs it, and every rendered problem page states one of three:

- **certified** — `proofs/README.md` lists a certificate row for the card, in
  section 1 (a Lean declaration on lean-categories main) or section 2 (an exact
  finite computation in this repository: Sage, GAP), and that row says it
  covers the card's **whole statement**. A certificate that proves one claim of
  a card whose statement has several says `part` and does not certify it.
- **reviewed** — no certificate covering the whole statement, and the card's
  `review:` field is `reviewed`.
- **draft** — neither.

The status is derived at build time and stored nowhere. The two authored
sources are the card's `review:` field and the certificate tables of
`proofs/README.md`, so adding a certificate means adding its row to one of
those tables and nothing on the card. A second `certificate:` field on the card
would drift from the file; `qualc check` reads the tables instead, and fails on
a row naming a card no card carries, a file that is not there, or a row whose
`Covers` cell neither says `the statement` nor says `part`. The certificate file
is published beside the pages and linked from the status line, which names the
tool that checks it; a card that is not certified but has rows says on its page
that the certificates cover part of its statement only.

Nothing in the tables outside sections 1 and 2 certifies a card: section 6's
repairs table names certificate files while saying no certificate exists for
what it lists. A card's audit events (`audit:`) render on its page with their
dates, at the foot, under `Audit trail`. An event dated before the commit that
carries it is a record, not a draft: the local gate refuses a commit that
changes or deletes one, so a correction is a new event dated the commit's date
(`QUAL-11`, issue #147). Events dated the commit's own day are still in flight.
A correction of a card's *mathematics* is recorded with the event kind
`solution-corrected`, which is what makes issue #111's "every correction arrives with its
certificate" checkable: the commit gate refuses that event on a card no row of
`proofs/README.md` covers for the whole statement.
The rule also runs the other way: an event a later commit rewrote in place is
restored to the text it carried on its day, and the gate accepts that
restoration when the replacement text stands in an earlier revision of the same
path — the text is the evidence, so a session cannot write new words into a
dated event. `STYLE-02`, `STYLE-03` and `STYLE-04` are not applied to the
`audit:` block for the same reason: a record keeps the symbols of its day.
`COMPLAINTS.md`'s dated records are held to the same rule, and a record a session
writes states its own day first: a section heading begins with it
(`## 2026-11-16: …`), and the bold or italic lead that opens a paragraph or
numbered item carries it, a numbered item being one record with its continuation
line and the blocks indented under it. Deleting a card or that file deletes the
records it holds, and the gate reads the deletion from Git's own diff because the
shared hook's payload lists only the paths that survive a change. The three headings
named by `RESTORED_SECTIONS` in `tools/qualc/authoring.py` are the exception to the
date-first format: the day each restored heading carries mid-title dates its record and
keeps it append-only. A push replays each published commit against its own parent and
its own committer day, and replays
the pushed tip even when the payload names no path, so a sanctioned `--no-verify`
content commit is still judged by the day it was written. A merge commit (`git pull
--no-rebase` of the published `main`) is judged only on the paths it authored — those
whose merged blob differs from every parent and from Git's automatic merge of the two —
against each parent in turn; every other change it carries belongs to the commit that
made it, which was judged when it was published or earlier in the same replay.
