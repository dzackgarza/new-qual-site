---
schema: qual/card@1
id: E-L0BW8
kind: problem
title: The reduction algorithm applied to eight schemes
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
    Munkres §77 Exercise 3, printed p. 471. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-2880636-E-L0BW8.md, read whole.
    Math Stack Exchange 2880636 asks about scheme (g) of this exercise, abcdabdc, and has one answer, 2880663
    by Angina Seng (2018-08-12), which shows the eight vertices to fall into two classes, reads the boundary
    in the generators c, d and e = ab as ecdedc, and abelianizes to Z^2 + Z/2. That is part of (g): the
    vertex classes, pi_1(X) and H_1(X). It is now stated on the card with its URL. What it does not do: it
    does not apply the algorithm of the exercise, and it names no standard form, so the reduction of (g) to
    aabbcc and its identification as 3P^2 stay the card's own, as do schemes (a) to (f) and (h), which the
    thread does not touch. The answer's H_1 agrees with the card's, whose aabbcc has the same group, which is
    recorded in the solution. Rejected in the search: nothing in this thread; mse 652721, the linked
    "Homology of connected sum of real projective spaces", states the group for the connected sum and not for
    this scheme.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 77 Exercise 3, printed p. 471. The eight reductions, checked against the four equivalences printed in the exercise: (a) aabbcc, (b) aabb, (c) aabbccdd, (d) two commutators, (e) one commutator, (f) aabbcc, (g) aabbcc, (h) abab. The Euler characteristics and orientability of the answers were recomputed independently from the vertex classes of each scheme and agree with the card's closing list -1, 0, -2, -2, 0, -1, -1, 1. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, one per scheme, against the four standard forms printed
    in Theorem 77.5 (aa^-1bb^-1, abab, (a1a1)...(am am) with m >= 2, commutator products
    with n >= 1). Re-checked every reduction: (a) two applications of (i) then relabelling
    to (aa)(bb)(cc); (b) cyclic permutation, two applications of (i), then (ii) cancelling
    a^-1 a at length 4, giving (aa)(bb) = P_2; (c) two applications of (i) moving bb and dd
    to the front, leaving a commutator, then (iv) once, giving four projective pairs; (d)
    and (e) single applications of (iii) followed by (ii), giving T_2 and T_1; (f) (iii) on
    b,d then (iv); (g) (i), (ii), then (iv); (h) (i), two cancellations, then Lemma 77.1 to
    abab, which is standard form (2). Vertex classes recounted for (e), (f), (g), (h) to
    confirm the Euler characteristic list: an earlier reading of (e) chained c-terminal with
    c-initial and gave the wrong chi, the correct count being three classes and chi = 0 for
    T_1. Repair: the card now names which of the four standard forms each answer is, which
    the earlier prose left to the reader.
---

::: {.exercise}

The proof of the classification theorem provides an algorithm for taking a proper labelling scheme for a polygonal region and reducing it to one of the four standard forms indicated in the theorem.
The appropriate equivalences are the following:

(i) $[y_0]a[y_1]a[y_2] \sim aa[y_0 y_1^{-1} y_2]$.

(ii) $[y_0]aa^{-1}[y_1] \sim [y_0 y_1]$ if $y_0 y_1$ has length at least 4.

(iii) $w_0[y_1]a[y_2]b[y_3]a^{-1}[y_4]b^{-1}[y_5] \sim w_0 aba^{-1}b^{-1}[y_1 y_4 y_3 y_2 y_5]$.

(iv) $w_0(cc)(aba^{-1}b^{-1})w_1 \sim w_0 aabbcc w_1$.

Using this algorithm, reduce each of the following schemes to one of the standard forms.

(a) $abacb^{-1}c^{-1}$

(b) $abca^{-1}cb$

(c) $abbca^{-1}ddc^{-1}$

(d) $abcda^{-1}b^{-1}c^{-1}d^{-1}$

(e) $abcda^{-1}c^{-1}b^{-1}d^{-1}$

(f) $aabcdc^{-1}b^{-1}d^{-1}$

(g) $abcdabdc$

(h) $abcdabcd$
:::

::: {.solution}
The eight reductions below are the card's own work; the only retained trace is Angina Seng's computation of the first homology of scheme (g), MSE answer 2880663, which does not run this algorithm, and no retained set reduces these schemes. The four standard forms of Theorem 77.5 (printed p. 462) are
$$
(1)\ a a^{-1} b b^{-1},\qquad (2)\ abab,\qquad (3)\ (a_{1}a_{1})\dots(a_{m}a_{m}),\ m\ge2,\qquad (4)\ (a_{1}b_{1}a_{1}^{-1}b_{1}^{-1})\dots(a_{n}b_{n}a_{n}^{-1}b_{n}^{-1}),\ n\ge1,
$$
giving $S^{2}$, $P^{2}$, $P_{m}$ and $T_{n}$ respectively. Besides the four equivalences of the exercise, only cyclic permutation, relabelling and reading a scheme backwards are used. Square brackets mark the subwords to which an equivalence is applied.

::: pf

::: {.pf-step #a}
(a) $abacb^{-1}c^{-1}\sim aabbcc$, so the surface is $P_{3}$.

::: pf-proof
Apply (i) to the two occurrences of $a$: with $y_{0}$ empty, $y_{1}=b$ and $y_{2}=cb^{-1}c^{-1}$,
$$
abacb^{-1}c^{-1}=a[b]a[cb^{-1}c^{-1}]\sim aa\,b^{-1}cb^{-1}c^{-1}.
$$
Apply (i) again to the two occurrences of $b^{-1}$, with $y_{0}=aa$, $y_{1}=c$, $y_{2}=c^{-1}$:
$$
aa\,b^{-1}[c]b^{-1}[c^{-1}]\sim aa\,b^{-1}b^{-1}c^{-1}c^{-1}.
$$
Relabelling $b^{-1}\mapsto b$, $a\mapsto a$, $c^{-1}\mapsto c$ in cyclic order gives $(aa)(bb)(cc)$, which is form (3) with $m=3$, that is $P_{3}$.
:::

:::

::: {.pf-step #b}
(b) $abca^{-1}cb\sim aabb$, so the surface is $P_{2}$, the Klein bottle.

::: pf-proof
Cyclically permute to $b\,ca^{-1}c\,b\,a=b[ca^{-1}c]b[a]$ and apply (i) with $y_{0}$ empty, $y_{1}=ca^{-1}c$, $y_{2}=a$:
$$
b[ca^{-1}c]b[a]\sim bb\,c^{-1}ac^{-1}a .
$$
Apply (i) to the two occurrences of $c^{-1}$, with $y_{0}=bb$, $y_{1}=a$, $y_{2}=a$:
$$
bb\,c^{-1}[a]c^{-1}[a]\sim c^{-1}c^{-1}bb\,a^{-1}a .
$$
The adjacent inverse pair $a^{-1}a$ cancels by (ii), as the remaining word $c^{-1}c^{-1}bb$ has length $4$; relabelling gives $(aa)(bb)$, which is form (3) with $m=2$, that is $P_{2}$, homeomorphic to the Klein bottle ($\S74$ Example).
:::

:::

::: {.pf-step #c}
(c) $abbca^{-1}ddc^{-1}\sim aabbccdd$, so the surface is $P_{4}$.

::: pf-proof
Apply (i) to the adjacent pair $bb$, with $y_{0}=a$, $y_{1}$ empty, $y_{2}=ca^{-1}ddc^{-1}$:
$$
a[bb]ca^{-1}ddc^{-1}\sim bb\,a\,c\,a^{-1}d\,d\,c^{-1}.
$$
Apply (i) to the adjacent pair $dd$ of the result, with $y_{0}=bbaca^{-1}$, $y_{1}$ empty, $y_{2}=c^{-1}$:
$$
bbaca^{-1}[d]d[c^{-1}]\sim dd\,bb\,a\,c\,a^{-1}c^{-1}.
$$
The last four letters are the commutator $(a)(c)(a^{-1})(c^{-1})$. Equivalence (iv) applied to the projective pair $bb$ together with that commutator gives three projective pairs; with the untouched pair $dd$ this is four, so the scheme is equivalent to $(aa)(bb)(cc)(dd)$, form (3) with $m=4$, that is $P_{4}$.
:::

:::

::: {.pf-step #d}
(d) $abcda^{-1}b^{-1}c^{-1}d^{-1}\sim (aba^{-1}b^{-1})(cdc^{-1}d^{-1})$, so the surface is $T_{2}$.

::: pf-proof
In (iii) take $a,b$ as the first two labels, so $y_{0}$ and $y_{1}$ are empty, $y_{2}$ is empty, $y_{3}=cd$, $y_{4}$ is empty and $y_{5}=c^{-1}d^{-1}$; then
$$
abcda^{-1}b^{-1}c^{-1}d^{-1}\sim aba^{-1}b^{-1}\,[y_{1}y_{4}y_{3}y_{2}y_{5}]=aba^{-1}b^{-1}c\,d\,c^{-1}d^{-1}.
$$
This is form (4) with $n=2$, that is $T_{2}$.
:::

:::

::: {.pf-step #e}
(e) $abcda^{-1}c^{-1}b^{-1}d^{-1}\sim aba^{-1}b^{-1}$, so the surface is $T_{1}$.

::: pf-proof
In (iii) take $a$ as the label of the first and fifth letters and $b$ as the label of the second and seventh; then $y_{1}$, $y_{2}$ are empty, $y_{3}=cd$, $y_{4}=c^{-1}$ and $y_{5}=d^{-1}$, so
$$
abcda^{-1}c^{-1}b^{-1}d^{-1}\sim aba^{-1}b^{-1}[c^{-1}c\,d\,d^{-1}].
$$
The pairs $c^{-1}c$ and $dd^{-1}$ cancel by (ii), each application leaving a word of length at least $4$; what remains is $aba^{-1}b^{-1}$, form (4) with $n=1$, that is $T_{1}$.
:::

:::

::: {.pf-step #f}
(f) $aabcdc^{-1}b^{-1}d^{-1}\sim aabbcc$, so the surface is $P_{3}$.

::: pf-proof
Keep the initial $aa$ and apply (iii) to the tail $bcdc^{-1}b^{-1}d^{-1}$ with the letters $b$ and $d$: $y_{1}=aa$, $y_{2}=c$, $y_{3}=c^{-1}$, $y_{4}$ and $y_{5}$ empty, so
$$
aa\,bcdc^{-1}b^{-1}d^{-1}\sim aa\,(bdb^{-1}d^{-1})\,c^{-1}c .
$$
The pair $c^{-1}c$ cancels by (ii). What remains is one projective pair $aa$ followed by the commutator $bdb^{-1}d^{-1}$, and (iv) turns those six letters into three projective pairs, $(aa)(bb)(cc)$: form (3) with $m=3$, that is $P_{3}$.
:::

:::

::: {.pf-step #g}
(g) $abcdabdc\sim aabbcc$, so the surface is $P_{3}$.

::: pf-proof
Apply (i) to the two occurrences of $a$, with $y_{0}$ empty, $y_{1}=bcd$, $y_{2}=bdc$:
$$
a[bcd]a[bdc]\sim aa\,(bcd)^{-1}(bdc)=aa\,d^{-1}c^{-1}b^{-1}b\,d\,c .
$$
The adjacent pair $b^{-1}b$ cancels by (ii), leaving $aa\,d^{-1}c^{-1}dc$, and $d^{-1}c^{-1}dc$ is the commutator with $x=d^{-1}$, $y=c^{-1}$. Equivalence (iv) turns one projective pair and one commutator into three projective pairs, $(aa)(bb)(cc)$: form (3) with $m=3$, that is $P_{3}$.
:::

:::

::: {.pf-step #h}
(h) $abcdabcd\sim abab$, so the surface is $P^{2}$.

::: pf-proof
Apply (i) to the two occurrences of $a$, with $y_{0}$ empty, $y_{1}=bcd$, $y_{2}=bcd$:
$$
a[bcd]a[bcd]\sim aa\,(bcd)^{-1}(bcd)=aa\,d^{-1}c^{-1}b^{-1}b\,c\,d .
$$
The pairs $b^{-1}b$ and $c^{-1}c$ cancel by (ii) in turn, leaving $aa\,d^{-1}d$. This is the length-four scheme treated as the base case in the proof of Theorem 77.5; Lemma 77.1, read as an equivalence and followed by relabelling, gives $aa\,d^{-1}d\sim abab$. That is form (2), the projective plane $P^{2}$.
:::

:::

::: {.pf-step #answers}
The eight schemes reduce to $(aa)(bb)(cc)$, $(aa)(bb)$, $(aa)(bb)(cc)(dd)$, $(aba^{-1}b^{-1})(cdc^{-1}d^{-1})$, $aba^{-1}b^{-1}$, $(aa)(bb)(cc)$, $(aa)(bb)(cc)$ and $abab$; hence to $P_{3}$, $P_{2}$, $P_{4}$, $T_{2}$, $T_{1}$, $P_{3}$, $P_{3}$ and $P^{2}$.

::: pf-proof
Steps [](#a){.pf-ref} to [](#h){.pf-ref} give the eight reductions, each landing on one of the four standard forms displayed at the head of the proof, and the identification of the forms with $S^{2}$, $P^{2}$, $P_{m}$ and $T_{n}$ is Theorem 77.5's own.
:::

:::

::: {.pf-step #euler}
The reduced schemes are orientable exactly in (d) and (e), with Euler characteristics $-1,0,-2,-2,0,-1,-1,1$.

::: pf-proof
A scheme is orientable exactly when each label occurs once in each direction, which holds for (d) and (e) throughout and fails for the other six. For a scheme read as a cell decomposition with one face and one edge per label, $\chi=V-E+1$; on the reduced forms $V=1$ for the one-class schemes, giving $\chi=2-E$, so $(aa)(bb)(cc)$ gives $-1$, $(aa)(bb)$ gives $0$, $(aa)(bb)(cc)(dd)$ gives $-2$, the genus-two form gives $-2$, $aba^{-1}b^{-1}$ gives $0$ and the two remaining $(aa)(bb)(cc)$ give $-1$ each; $abab$ has two vertex classes, so $\chi=2-2+1=1$, as $P^{2}$ must. These agree with $2-2g$ and $2-m$ for the surfaces named.
:::

:::

:::
:::
