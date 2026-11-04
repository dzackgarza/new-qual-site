# stars-appendix-a.md — printed difficulty asterisks, Appendix A (Asymptotics)

Restores the asterisk that Stein--Shakarchi print immediately after a starred item
number.  Statements only; nothing else in the card is touched.

Rendering convention used throughout (the same one in every file of this run):
the asterisk is written as `$^{*}$` in LaTeX -- a superscript asterisk with an
empty base, which is what the print sets (TeX `^{*}`, glyph U+2217 in CMSY6 at
superscript size).  It is placed immediately after the printed item marker.  The
cards do not reproduce the item number in the statement body, so for an item the
marker is the start of the statement block: `$^{*}$` becomes the first thing
after the `::: {.exercise}` opener, exactly where the number stands in the book.
For a starred sub-part the marker is the sub-part label, so the star would go
directly after e.g. `(b)` on that line; **no sub-part in this chapter is starred**,
so no such patch appears below.

Evidence: `pdftotext -bbox-layout` and `mutool draw -F stext` on
`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`.  For every item claimed
below, the glyph layer shows a single U+2217 in CMSY6 (5.98 pt, superscript) whose
box sits immediately to the right of the item number, which is set in CMBX9.  The
two extractors agree on every asterisk on these pages, so nothing is left unsettled.


CARD: corpus/collections/SRC-TEXT-SS03/appendix-a-problems/E-SSA.PR-5.md
BOOK: Stein--Shakarchi, *Complex Analysis*, Appendix A, Problem 5; printed p. 343 / PDF p. 362
OLD:
```
::: {.exercise}
The one shortcoming in our derivation of the asymptotic formula for $p(n)$ arose from the fact that while $f_1(z)=\frac{z}{i}e^{\frac{\pi i}{12z}}e^{\frac{\pi iz}{12}}$ is a good approximation to the generating function $f(z)$ near $z=0$, this fails near other points on the real axis, since $f_1$ is regular there, but $f$ is not.
```
NEW:
```
::: {.exercise}
$^{*}$The one shortcoming in our derivation of the asymptotic formula for $p(n)$ arose from the fact that while $f_1(z)=\frac{z}{i}e^{\frac{\pi i}{12z}}e^{\frac{\pi iz}{12}}$ is a good approximation to the generating function $f(z)$ near $z=0$, this fails near other points on the real axis, since $f_1$ is regular there, but $f$ is not.
```
WHY: item 5; the glyph after `5.` in CMBX9 is U+2217 in CMSY6, superscript size.
