---
schema: qual/card@1
id: E-TUPHD
kind: problem
title: Pasting schemes for two polygonal regions
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §76 Exercise 1, printed p. 462. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved for this card. The queries were the Stack Exchange
    advanced searches "acbc^{-1} cdba^{-1}d" and "Munkres pasting edges labelled 7-sided", both with no hits,
    and the similar-question search from "Pasting two polygonal regions along an edge labelling scheme
    Munkres" (15 items), whose threads describe the pasting operation in general and solve no exercise; the
    GitHub code searches "munkres labelling scheme", "munkres "polygonal region"", "munkres "elementary
    operations"" and "munkres "Section 76"" returned no file of solutions for this section, and the fourteen
    solution repositories found by repository search stop before Chapter 12. The card keeps its own proof,
    re-read here against the printed list of operations on p. 458: the two a-edges are the only a-edges and
    the two b-edges the only b-edges of the total scheme, which is what makes those two pastings
    elementary, and c occurs three times, which is what forbids the third. The three answers were re-derived
    from the schemes and agree with the words on the card.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 76 Exercise 1, printed p. 462. The three pastings, checked against operations (i) to (v) of the printed list on p. 458: along a (each a appears exactly twice) the scheme cbc^{-1}dcdb, along b after a flip c^{-1}acd^{-1}c^{-1}d^{-1}a, and along c impossible because c occurs three times in the total scheme. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the pasting rule as a step and the three parts as
    the remaining top-level steps with (c) as the QED step. Re-derived all three answers: cyclic
    permutations of $w_1=acbc^{-1}$ and $w_2=cdba^{-1}d$ followed by a paste along $a$ give
    $cbc^{-1}dcdb$ with $4+5-2=7$ letters; the flip of $w_2$ gives $d^{-1}ab^{-1}d^{-1}c^{-1}$,
    after which cyclic permutations and a paste along $b$ give $c^{-1}acd^{-1}c^{-1}d^{-1}a$, also
    $7$ letters; and $c$ occurs three times in the pair of words, which is what forbids the third
    pasting. Added: the letter count as a check on each word, and the explicit statement of what a
    flip does to a word, which the earlier prose used without saying. No defect found in the
    statement, §76 Exercise 1 on printed p. 462. The collection retains no solution set for §76, so
    the argument is the card's own, as the card says.
---

::: {.exercise}

Consider the quotient space $X$ obtained from two polygonal regions by means of the labelling schemes $w_1 = acbc^{-1}$ and $w_2 = cdba^{-1}d$.

(a) If one pastes these regions together along the edges labelled "a," one can represent $X$ as the quotient space of a single 7-sided region $P$.
What is a labelling scheme for $P$?
What sequence of elementary operations is involved in obtaining this scheme?

(b) Repeat (a), pasting along the edges labelled "b".

(c) Explain why one cannot paste along the edges labelled "c" to obtain the scheme $acbdba^{-1}d$ as a way of representing $X$.
:::

::: {.solution}
No retained solution set covers this exercise — dbFin's index ends at §67 and the other sets searched stop earlier — so the argument is the card's own, checked against operations (i)--(v) of the printed list on p. 458. Write
$$
w_1=acbc^{-1},\qquad w_2=cdba^{-1}d,
$$
for the two labelled polygonal regions. Recall that pasting is the inverse of cutting: after a cyclic permutation of a word and, if necessary, a flip of one polygon, schemes $y_0e$ and $e^{-1}y_1$ may be replaced by the single scheme $y_0y_1$, provided the two $e$-edges are the only edges pasted to one another.

::: pf

::: {.pf-step #rule}
If a word is $y_0e$ and another is $e^{-1}y_1$ with the $e$-edges pasted together, the resulting scheme is $y_0y_1$; flipping a polygon replaces its word $e_1\cdots e_r$ by $e_r^{-1}\cdots e_1^{-1}$, and a cyclic permutation of a word does not change the quotient.

::: pf-proof
Pasting the $e$-edge of the first region to the $e^{-1}$-edge of the second deletes that pair of edges and joins the remaining boundary into one cycle, which reads $y_0$ followed by $y_1$. Flipping a polygon reverses the cyclic order of its boundary and inverts each label, since the oriented boundary is traversed the other way. A cyclic permutation moves the starting point of a closed boundary word, which names the same quotient.
:::

:::

::: {.pf-step #part-a}
(a) Pasting along the $a$-edges gives the scheme $cbc^{-1}dcdb$.

::: pf-proof
Cyclic permutations give $acbc^{-1}\sim cbc^{-1}a$ and $cdba^{-1}d\sim a^{-1}dcdb$. With $y_0=cbc^{-1}$ and $e=a$ in the first word, and $e^{-1}=a^{-1}$, $y_1=dcdb$ in the second, step [](#rule){.pf-ref} replaces the pair by $y_0y_1=cbc^{-1}dcdb$, a word in $7$ letters. The letter $a$ occurs once in each word before pasting and in neither after, which is the expected count $4+5-2=7$.
:::

:::

::: {.pf-step #part-b}
(b) Pasting along the $b$-edges gives the scheme $c^{-1}acd^{-1}c^{-1}d^{-1}a$.

:::: pf-proof

::: {.pf-step #flip}
The second word becomes $d^{-1}ab^{-1}d^{-1}c^{-1}$ after a flip.

::: pf-proof
The labels of $cdba^{-1}d$ in order are $c,d,b,a^{-1},d$; reversing the cyclic order and inverting each label gives $d^{-1},a,b^{-1},d^{-1},c^{-1}$, the word $d^{-1}ab^{-1}d^{-1}c^{-1}$.
:::

:::

::: {.pf-step}
(b) The pasting produces $c^{-1}acd^{-1}c^{-1}d^{-1}a$.

::: pf-proof
The two $b$-edges now carry opposite exponents, which is the condition of step [](#rule){.pf-ref}: the flipped word is a flip, not a cyclic permutation, and it is the flip that makes the exponents opposite, the original words both writing $b$ with exponent $+1$. Cyclic permutations give $acbc^{-1}\sim c^{-1}acb$ and $d^{-1}ab^{-1}d^{-1}c^{-1}\sim b^{-1}d^{-1}c^{-1}d^{-1}a$, and pasting along $b$ with $y_0=c^{-1}ac$, $e=b$, $y_1=d^{-1}c^{-1}d^{-1}a$ gives $c^{-1}acd^{-1}c^{-1}d^{-1}a$, again $7$ letters. Any cyclic permutation, global relabelling or reversal of the scheme describes the same quotient.
:::

:::

:::

:::

::: {.pf-step}
(c) The two regions cannot be pasted along the $c$-edges to obtain $acbdba^{-1}d$.

::: pf-proof
The label $c$ occurs three times in the pair of schemes, as $c$ and $c^{-1}$ in $w_1$ and as $c$ in $w_2$. The quotient relation identifies all three $c$-edges with one another, so if one $c$-edge is glued from each region the chosen pair is still identified with the third $c$-edge by the original relation; once the pasted pair becomes an interior seam, that further identification is no longer recorded by a boundary word. This violates the hypothesis of step [](#rule){.pf-ref}, that the pasted $e$-edges be the only ones pasted together, so $acbdba^{-1}d$ does not arise from the stated quotient by a valid pasting along $c$. Parts (a) and (b) are steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref}.
:::

:::

:::
:::
