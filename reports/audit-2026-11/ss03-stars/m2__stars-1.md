# Restored printed difficulty asterisks -- Chapter 1

Slice: chapter 1, Exercises and Problems.  Source: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`;
printed page = PDF page - 19.  Chapter 1 Exercises run printed pp. 24--31 (PDF 43--50); chapter 1 has no
Problems section (the table of contents goes straight from "4 Exercises 24" to Chapter 2).

Finding: **no printed item of chapter 1 carries an asterisk.**  All 26 printed items (Exercises 1--26, the
chapter has no Problems section) were located in the typeset glyph layer by their bold item number and
checked for a glyph sitting immediately to the right of it; none has one.  The only two asterisk glyphs on
PDF pp. 43--50 are the mathematical `t*` of Exercise 5(a) (PDF p. 44, CMSY6, inside the display
`t* = sup{t : z(s) in Omega_1 ...}` and in the sentence after it), not item markers.  The poppler text layer
(`pdftotext -layout`) agrees: no `∗` on pp. 43--50 except those two.  Nothing to patch, so this file has
no CARD blocks.

Convention: the asterisk is written `$^{*}$`, in LaTeX, because every card in this
collection writes its mathematics in LaTeX and no card in the corpus yet shows a
star glyph to copy (the only existing records of a star are prose: the remark on
`E-SS2.PR-5` and the audit notes on `E-SS3.PR-4`/`E-SS3.PR-5`).  The cards do not
print the item number inside the statement block, so the printed `2.∗` has no
number to follow on the card: for a starred whole item the star is inserted at the
head of the statement, in the position the printed number occupies, as `$^{*}$ `
(star, one space) before the first word of the statement.  For a starred sub-part
the star goes immediately after the sub-part label, e.g. `(b) $^{*}$ Fix ...`,
which is exactly where the print puts it (`(b) ∗ Fix ...`).


