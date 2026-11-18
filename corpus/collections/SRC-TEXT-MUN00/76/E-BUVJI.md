---
schema: qual/card@1
id: E-BUVJI
kind: problem
title: Two reduction sequences for the same scheme disagree
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
    Munkres §76 Exercise 2, printed p. 462. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved for this card. The queries were the Stack Exchange
    advanced search "four-fold dunce cap abcc" (no hits) and the similar-question search from "Two sequences
    of elementary operations give the dunce cap and the projective plane, which is correct" (15 items), no
    thread of which treats this exercise; the GitHub code searches for "munkres "dunce cap"" and
    "munkres "elementary operations"" returned nothing of this section. The card keeps its own proof, re-read
    here: the first sequence's pasting along b is elementary because b occurs exactly twice in the total
    scheme abcc, c^{-1}c^{-1}ab before it, and its cancellation is operation (vi) with the letter a occurring
    twice and two letters on each side, while the second sequence pastes along a c-edge when c occurs four
    times in the total scheme, so its first step is not the inverse of a cutting operation. The verdict --
    the first argument correct, the space the four-fold dunce cap -- is unchanged.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 76 Exercise 2, printed p. 462. The first sequence is valid: paste along b after permuting and flipping, then cancel aa^{-1} with y_0 = y_1 = cc of length two and a appearing nowhere else, as operation (vi) on p. 458 requires. The second is invalid at its first step, because c occurs four times in the total scheme. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Consider the space $X$ obtained from two polygonal regions by means of the labelling schemes $w_1 = abcc$ and $w_2 = c^{-1}c^{-1}ab$.
The sequence of elementary operations

$$
\begin{array}{rl}
abcc \text{ and } c^{-1}c^{-1}ab & \to ccab \text{ and } b^{-1}a^{-1}cc \text{ by permuting and flipping} \\
& \to ccaa^{-1}cc \text{ by pasting} \\
& \to cccc \text{ by cancelling}
\end{array}
$$

indicates that $X$ is homeomorphic to the four-fold dunce cap.
The sequence of operations

$$
\begin{array}{rl}
abcc \text{ and } c^{-1}c^{-1}ab & \to abcc^{-1}ab \text{ by pasting} \\
& \to abab \text{ by cancelling}
\end{array}
$$

indicates that $X$ is homeomorphic to $P^2$.
But these two spaces are not homeomorphic.
Which (if either) argument is correct?
:::

::: {.solution}

The argument is the card's own; no published solution of Munkres §76 Exercise 2 was located, and the sets searched are recorded in the audit trail. The elementary operations are those of §76 (printed p. 460): permuting the edge labels cyclically, flipping a scheme, pasting two polygons along a pair of edges whose label occurs exactly twice in the total scheme, and cancelling an adjacent pair $aa^{-1}$ whose label occurs nowhere else.

Let $X$ be obtained from two polygonal regions with schemes $w_{1}=abcc$ and $w_{2}=c^{-1}c^{-1}ab$.

::: pf

::: {.pf-step #first-valid}
The first sequence is a valid sequence of elementary operations, and it presents $X$ by the scheme $cccc$.

::: pf-proof

::: {.pf-step #permute}
Permuting and flipping carries the pair $(abcc,\ c^{-1}c^{-1}ab)$ to $(ccab,\ b^{-1}a^{-1}cc)$.

::: pf-proof
A cyclic permutation of $abcc$ gives $ccab$, and a cyclic permutation of $c^{-1}c^{-1}ab$ gives $ab\,c^{-1}c^{-1}$, whose flip is $cc\,b^{-1}a^{-1}$ up to cyclic permutation. Both operations are elementary: they replace a scheme by another scheme for the same quotient space (§76).
:::

:::

::: {.pf-step #paste}
Pasting along the two $b$-edges gives $cc\,aa^{-1}cc$.

::: pf-proof
In the total scheme $(ccab,\ b^{-1}a^{-1}cc)$ the label $b$ occurs exactly twice, once as $b$ in the first word and once as $b^{-1}$ in the second, so the two $b$-edges are exactly the pair being identified and the pasting operation applies: the two polygons are replaced by one whose boundary word is obtained by deleting the two $b$-edges, which gives $cc\,aa^{-1}cc$.
:::

:::

::: {.pf-step #cancel}
Cancelling the pair $aa^{-1}$ gives $cccc$.

::: pf-proof
In $cc\,aa^{-1}cc$ the label $a$ occurs exactly in the adjacent pair $aa^{-1}$, with opposite exponents, and the words on either side of that pair are $cc$ and $cc$, each of length at least two; these are the hypotheses of the cancelling operation (§76), which deletes the pair and gives $cccc$.
:::

:::

::: {.pf-qed}
Steps [](#permute){.pf-ref}, [](#paste){.pf-ref} and [](#cancel){.pf-ref} are the three arrow steps of the first sequence, each elementary, and they carry the original pair of schemes to $cccc$, the scheme of the four-fold dunce cap (§75).
:::

:::

:::

::: {.pf-step #second-invalid}
The second sequence is not a valid sequence of elementary operations.

::: pf-proof
Its first arrow pastes the two polygons along a pair of $c$-edges. But the label $c$ occurs four times in the total scheme $abcc,\ c^{-1}c^{-1}ab$: twice in the first word and twice in the second. The elementary pasting operation requires the label of the selected edges to occur exactly twice in the total scheme, since otherwise the remaining edges with that label are also to be identified and the seam is not the only identification between the two polygons; the inverse-cutting theorem does not license replacing the pair by a single polygon whose boundary word drops the other occurrences. So
$$
abcc,\ c^{-1}c^{-1}ab\ \not\longmapsto\ abcc^{-1}ab
$$
by an elementary pasting, and the later cancellation from $abcc^{-1}ab$ to $abab$ proceeds from a scheme not known to present $X$, so it establishes nothing about $X$.
:::

:::

::: {.pf-step #conclusion}
Only the first argument is correct: $X$ is homeomorphic to the four-fold dunce cap, not to $P^{2}$.

::: pf-proof
The first sequence is valid by step [](#first-valid){.pf-ref} and presents $X$ by the scheme $cccc$; the second is not by step [](#second-invalid){.pf-ref}, so no scheme $abab$ is obtained for $X$. The schemes $cccc$ and $abab$ present the four-fold dunce cap and $P^{2}$ respectively (§75), and these spaces are not homeomorphic: the scheme $cccc$ has one vertex class, so by Theorem 74.2 its fundamental group is $\langle c\mid c^{4}=1\rangle\cong\ZZ/4$, while $P^{2}$ has fundamental group $\ZZ/2$; groups of different orders are not isomorphic, and a homeomorphism would induce an isomorphism of fundamental groups (Corollary 52.5). So the two conclusions cannot both be right, and the valid computation gives the four-fold dunce cap.
:::

:::

:::
:::
