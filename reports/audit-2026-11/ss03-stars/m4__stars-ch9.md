# stars-ch9.md — printed difficulty asterisks, Chapter 9 (An Introduction to Elliptic Functions)

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


CARD: corpus/collections/SRC-TEXT-SS03/ch9-problems/E-SS9.PR-3.md
BOOK: Stein--Shakarchi, *Complex Analysis*, Chapter 9, Problem 3; printed p. 281 / PDF p. 300
OLD:
```
::: {.exercise}
Let $\Omega$ be a simply connected domain excluding the three roots of $4z^3-g_2z-g_3$. Fix $\omega_0\in\Omega$ and define
```
NEW:
```
::: {.exercise}
$^{*}$Let $\Omega$ be a simply connected domain excluding the three roots of $4z^3-g_2z-g_3$. Fix $\omega_0\in\Omega$ and define
```
WHY: item 3; the glyph after `3.` in CMBX9 is U+2217 in CMSY6, superscript size.

CARD: corpus/collections/SRC-TEXT-SS03/ch9-problems/E-SS9.PR-4.md
BOOK: Stein--Shakarchi, *Complex Analysis*, Chapter 9, Problem 4; printed p. 282 / PDF p. 301
OLD:
```
::: {.exercise}
Suppose $\tau$ is purely imaginary, say $\tau=it$ with $t>0$. Consider the division of the complex plane into congruent rectangles obtained by considering the lines $x=n/2$, $y=tm/2$ as $n$ and $m$ range over the integers. (An example is the rectangle whose vertices are $0$, $1/2$, $1/2+\tau/2$, and $\tau/2$.)
```
NEW:
```
::: {.exercise}
$^{*}$Suppose $\tau$ is purely imaginary, say $\tau=it$ with $t>0$. Consider the division of the complex plane into congruent rectangles obtained by considering the lines $x=n/2$, $y=tm/2$ as $n$ and $m$ range over the integers. (An example is the rectangle whose vertices are $0$, $1/2$, $1/2+\tau/2$, and $\tau/2$.)
```
WHY: item 4; the glyph after `4.` in CMBX9 is U+2217 in CMSY6, superscript size.  Parts (a) and (b) carry no asterisk.
