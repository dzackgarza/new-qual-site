# stars-ch10.md — printed difficulty asterisks, Chapter 10 (Applications of Theta Functions)

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


CARD: corpus/collections/SRC-TEXT-SS03/ch10-problems/E-SS10.PR-1.md
BOOK: Stein--Shakarchi, *Complex Analysis*, Chapter 10, Problem 1; printed p. 314 / PDF p. 333
OLD:
```
::: {.exercise}
Suppose $n=4^a(8k+7)$, where $a$ and $k$ are nonnegative integers. Show that $n$ cannot be written as a sum of three integer squares. The converse for positive integers is the three-square theorem of Legendre and Gauss.
```
NEW:
```
::: {.exercise}
$^{*}$Suppose $n=4^a(8k+7)$, where $a$ and $k$ are nonnegative integers. Show that $n$ cannot be written as a sum of three integer squares. The converse for positive integers is the three-square theorem of Legendre and Gauss.
```
WHY: item 1; the glyph after `1.` in CMBX9 is U+2217 in CMSY6, superscript size.

CARD: corpus/collections/SRC-TEXT-SS03/ch10-problems/E-SS10.PR-5.md
BOOK: Stein--Shakarchi, *Complex Analysis*, Chapter 10, Problem 5; printed p. 316 / PDF p. 335
OLD:
```
::: {.exercise}
The Weierstrass function satisfies
```
NEW:
```
::: {.exercise}
$^{*}$The Weierstrass function satisfies
```
WHY: item 5; the glyph after `5.` in CMBX9 is U+2217 in CMSY6, superscript size.

CARD: corpus/collections/SRC-TEXT-SS03/ch10-problems/E-SS10.PR-6.md
BOOK: Stein--Shakarchi, *Complex Analysis*, Chapter 10, Problem 6; printed p. 316 / PDF p. 335
OLD:
```
::: {.exercise}
Let $r_8(n)$ count representations of $n$ as a sum of eight squares. Prove $r_8(n)=16\sigma_3^*(n)$, where $\sigma_3^*(n)=\sum_{d\mid n}d^3$ for odd $n$, while for even $n$,
```
NEW:
```
::: {.exercise}
$^{*}$Let $r_8(n)$ count representations of $n$ as a sum of eight squares. Prove $r_8(n)=16\sigma_3^*(n)$, where $\sigma_3^*(n)=\sum_{d\mid n}d^3$ for odd $n$, while for even $n$,
```
WHY: item 6; the glyph after `6.` in CMBX9 is U+2217 in CMSY6, superscript size.  Parts (a)--(f) carry no asterisk.
