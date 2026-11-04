# stars-ch4.md — printed difficulty asterisks, Stein--Shakarchi chapter 4

Rendering convention: `$^{*}$` immediately before the first word of the statement
block, followed by one space (so the card reads like the print's "3.∗ In this
problem, ..."). No card in the corpus renders a star inline: the only star on
record is `E-SS2.PR-5`, and it states the fact in a `::: {.remark}` ("The book
marks this problem with an asterisk.") rather than in the statement. The
statements themselves carry no item number — the number lives in the card id and
in the collection index `comment: Ch. N, Problem m` — so the head of the
statement is exactly where the printed number sits, and the star goes there.
Starred sub-parts would be patched on the sub-part line as `(b) $^{*}$`, the
shape `m2` fixed for slice 1; this slice has none.

Each block below is one repair: `OLD` is the card's statement opener with
its first statement line, `NEW` is the same two lines with the star
restored. Nothing else in the card changes.

CARD: corpus/collections/SRC-TEXT-SS03/ch4-problems/E-SS4.PR-3.md
BOOK: Stein--Shakarchi, *Complex Analysis*, ch. 4, Problem 3, printed p. 133 (PDF p. 152)
OLD:
```
::: {.exercise}
In this problem, we investigate the behavior of certain bounded holomorphic functions in an infinite strip. The particular result described here is sometimes called the three-lines lemma.
```
NEW:
```
::: {.exercise}
$^{*}$ In this problem, we investigate the behavior of certain bounded holomorphic functions in an infinite strip. The particular result described here is sometimes called the three-lines lemma.
```
WHY: the print sets a raised asterisk immediately after the item number (PDF p. 152: glyph U+2217 in CMSY6, 5.98 pt against an 8.97 pt body, baseline raised 3.9 pt, i.e. a superscript star, not a math exponent). Both text extractors and the rendered page agree.

CARD: corpus/collections/SRC-TEXT-SS03/ch4-problems/E-SS4.PR-4.md
BOOK: Stein--Shakarchi, *Complex Analysis*, ch. 4, Problem 4, printed p. 133 (PDF p. 152)
OLD:
```
::: {.exercise}
There is a relation between the Paley–Wiener theorem and an earlier representation due to E. Borel.
```
NEW:
```
::: {.exercise}
$^{*}$ There is a relation between the Paley–Wiener theorem and an earlier representation due to E. Borel.
```
WHY: the print sets a raised asterisk immediately after the item number (PDF p. 152: glyph U+2217 in CMSY6, 5.98 pt against an 8.97 pt body, baseline raised 3.9 pt, i.e. a superscript star, not a math exponent). Both text extractors and the rendered page agree.
