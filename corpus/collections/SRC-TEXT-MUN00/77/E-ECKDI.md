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
By Theorem 77.5, every such quotient is homeomorphic to exactly one of
$$
S^2,\qquad T_g\ (g\ge1),\qquad P_r\ (r\ge1),
$$
where $T_g$ is the orientable surface of genus $g$ and $P_r$ is the connected sum of $r$ projective planes. Uniqueness of these standard surfaces follows from orientability and Euler characteristic:
$$
\chi(T_g)=2-2g,\qquad \chi(P_r)=2-r,
$$
and $S^2$ is the unique orientable case with Euler characteristic $2$.

(a) We have
$$
P_1=P^2,\qquad P_2\cong K.
$$
Lemma 77.4 converts one torus summand together with one crosscap pair into two additional crosscaps; equivalently
$$
T_1\# P_r\cong P_{r+2}.
$$
Inductively,
$$
P_{2g+1}\cong T_g\# P^2,
\qquad
P_{2g+2}\cong T_g\# K.
$$
Thus the standard list $S^2,T_g,P_r$ can be rewritten exactly as
$$
S^2,\quad P^2,\quad K,\quad T_g,\quad T_g\#P^2,\quad T_g\#K
\qquad(g\ge1).
$$
Since the original standard forms are unique, exactly one member of this list represents $X$.

(b) Put $K_m=K\#\cdots\#K$ with $m$ factors. Since $K\cong P_2$,
$$
K_m\cong P_{2m},
\qquad
P^2\#K_m\cong P_{2m+1}.
$$
Therefore the same classification can be rewritten as
$$
S^2,\quad T_g,\quad P^2,\quad K_m,\quad P^2\#K_m
\qquad(g,m\ge1).
$$
Again these are pairwise distinguished by orientability and Euler characteristic, so exactly one occurs.
:::
