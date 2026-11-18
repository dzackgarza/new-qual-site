---
schema: qual/card@1
id: E-ECKDI
kind: problem
title: Normal forms for pasting schemes
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
    Munkres §77 Exercise 1, printed p. 470. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved, because none was found. The queries were the Stack
    Exchange advanced search "Munkres T_n # K Klein bottle exactly one list" (no hits) and the
    similar-question search from "Classification of surfaces list S^2, T_n, P^2, K_m, P^2 # K_m" (15 items).
    The thread that is this exercise, 1333637, was read: its two answers, 1333690 and 1333687, list the
    classification theorem and the invariants and both decline to solve the exercise, so the thread is a
    source searched and not a proof. The GitHub code searches "munkres "Section 77"" and "munkres
    "Classification Theorem"" returned no solutions file, and no course page found treats the section. The
    card keeps its own proof.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 77 Exercise 1, printed p. 470. Both lists are rewritings of Theorem 77.5's standard list using T_g#P^2 = P_{2g+1} and T_g#K = P_{2g+2}, which is Lemma 77.4, and the members are distinguished by orientability and Euler characteristic. Checked against Lemma 77.4 and Theorem 77.5. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Let $X$ be a space obtained by pasting the edges of a polygonal region together in pairs.

(a) Show that $X$ is homeomorphic to exactly one of the spaces in the following list: $S^2$, $P^2$, $K$, $T_n$, $T_n \# P^2$, $T_n \# K$, where $K$ is the Klein bottle and $n \geq 1$.

(b) Show that $X$ is homeomorphic to exactly one of the spaces in the following list: $S^2$, $T_n$, $P^2$, $K_m$, $P^2 \# K_m$, where $K_m$ is the $m$-fold connected sum of $K$ with itself and $m \geq 1$.
:::

::: {.solution}

The argument is the card's own, from Theorem 77.5 and Lemma 77.4; no published solution of Munkres §77 Exercise 2 was located, and the sets searched are recorded in the audit trail.

Let $X$ be obtained by pasting the edges of a polygonal region in pairs, let $T_{g}$ be the orientable surface of genus $g$ and $P_{r}$ the connected sum of $r$ copies of $P^{2}$, and let $K=P_{2}$ be the Klein bottle.

::: pf

::: {.pf-step #standard}
$X$ is homeomorphic to exactly one of $S^{2}$, $T_{g}$ for $g\ge1$ and $P_{r}$ for $r\ge1$.

::: pf-proof
Every quotient of a polygonal region by a pairwise pasting is a compact surface, and the classification of compact surfaces (Theorem 77.5) says that such a surface is homeomorphic to exactly one member of that list. Uniqueness is decided by two invariants: orientability, and the Euler characteristic, which for the standard forms is $\chi(T_{g})=2-2g$ and $\chi(P_{r})=2-r$ (§77, printed p. 466). The pairs (orientable or not, $\chi$) are distinct on that list, with $S^{2}$ the unique orientable member of characteristic $2$, the $T_{g}$ the orientable members of characteristic $2-2g<2$, and the $P_{r}$ the non-orientable ones of characteristic $2-r\le1$.
:::

:::

::: {.pf-step #rewrite}
$P_{2g+1}\cong T_{g}\#P^{2}$ and $P_{2g+2}\cong T_{g}\#K$ for every $g\ge1$.

::: pf-proof
Lemma 77.4 (printed p. 463) converts one torus summand together with one crosscap pair into two additional crosscaps, that is $T_{1}\#P_{r}\cong P_{r+2}$ for $r\ge1$; applying it $g$ times to $T_{g}\#P_{r}$ gives $T_{g}\#P_{r}\cong P_{r+2g}$. Taking $r=1$ gives $T_{g}\#P^{2}\cong P_{2g+1}$ and taking $r=2$, with $P_{2}=K$, gives $T_{g}\#K\cong P_{2g+2}$.
:::

:::

::: {.pf-step #a}
(a) $X$ is homeomorphic to exactly one of $S^{2}$, $P^{2}$, $K$, $T_{n}$, $T_{n}\#P^{2}$, $T_{n}\#K$, for $n\ge1$.

::: pf-proof
By step [](#rewrite){.pf-ref} the standard list of step [](#standard){.pf-ref} is, member by member, the list of this part: $P_{1}=P^{2}$, $P_{2}=K$, $P_{2g+1}=T_{g}\#P^{2}$ and $P_{2g+2}=T_{g}\#K$ for $g\ge1$, together with $S^{2}$ and the $T_{g}$. So the two lists contain the same spaces, and by step [](#standard){.pf-ref} exactly one member of the second represents $X$. Distinctness inside the second list is again read from orientability and Euler characteristic: $S^{2}$ has $(+,\ 2)$, $T_{n}$ has $(+,\ 2-2n)$, $P^{2}$ has $(-,\ 1)$, $K$ has $(-,\ 0)$, $T_{n}\#P^{2}$ has $(-,\ 1-2n)$ and $T_{n}\#K$ has $(-,\ -2n)$, all distinct.
:::

:::

::: {.pf-step #b}
(b) $X$ is homeomorphic to exactly one of $S^{2}$, $T_{n}$, $P^{2}$, $K_{m}$, $P^{2}\#K_{m}$, for $n,m\ge1$.

::: pf-proof
Put $K_{m}=K\#\cdots\#K$ with $m$ factors. Since $K=P_{2}$, the connected sum is associative and $P_{2}\#P_{2}=P_{4}$, one gets $K_{m}=P_{2m}$ and $P^{2}\#K_{m}=P_{2m+1}$. So the standard list is again, member by member, the list of this part: $P_{1}=P^{2}$ with $K_{0}$-free notation, $P_{2m}=K_{m}$ and $P_{2m+1}=P^{2}\#K_{m}$ for $m\ge1$, together with $S^{2}$ and the $T_{n}$. By step [](#standard){.pf-ref} exactly one member represents $X$, and the members are pairwise distinguished by orientability and Euler characteristic: $P^{2}$ has $(-,\ 1)$, $K_{m}=P_{2m}$ has $(-,\ 2-2m)$, and $P^{2}\#K_{m}=P_{2m+1}$ has $(-,\ 1-2m)$, which are distinct among themselves and from the orientable members.
:::

:::

:::
:::
