---
schema: qual/card@1
id: E-HAT-2.2-36
kind: problem
title: Künneth formula $H_i(X \times S^n) \approx H_i(X) \oplus H_{i-n}(X)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Products
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 36; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/algebraic proof checked.
---

Show that $H_i(X \times S^n) \approx H_i(X) \oplus H_{i-n}(X)$ for all $i$ and $n$, where $H_i = 0$ for $i < 0$ by definition.
Namely, show $H_i(X \times S^n) \approx H_i(X) \oplus H_i(X \times S^n, X \times \{x_0\})$ and $H_i(X \times S^n, X \times \{x_0\}) \approx H_{i-1}(X \times S^{n-1}, X \times \{x_0\})$.
[For the latter isomorphism the relative Mayer–Vietoris sequence yields an easy proof.]

::: {.solution}
Fix $x_0\in S^n$ and write
\[
P_n=X\times S^n,
\qquad
A_n=X\times\{x_0\}.
\]

<1>1. The long exact sequence of $(P_n,A_n)$ splits and gives
\[
H_i(P_n)\cong H_i(X)\oplus H_i(P_n,A_n).
\]
::: {.proof}
The inclusion
\[
A_n\cong X\hookrightarrow X\times S^n
\]
has the projection $X\times S^n\to X$ as a retraction. Hence its induced map on homology is injective and split. The long exact sequence of the pair therefore breaks into split short exact sequences
\[
0\to H_i(X)\to H_i(P_n)\to H_i(P_n,A_n)\to0.
\]
:::

<1>2. For $n\ge1$ there are natural isomorphisms
\[
H_i(P_n,A_n)\cong H_{i-1}(P_{n-1},A_{n-1}).
\]
::: {.proof}
Decompose $S^n$ into upper and lower hemispheres $D_+^n$ and $D_-^n$, meeting in $S^{n-1}$, and choose $x_0$ on the equator. Apply relative Mayer--Vietoris to the pair
\[
(X\times S^n,\,X\times\{x_0\}).
\]
The two hemisphere pairs
\[
(X\times D_\pm^n,\,X\times\{x_0\})
\]
deformation retract to $(X,X)$ and hence have zero relative homology. Their intersection pair is
\[
(X\times S^{n-1},\,X\times\{x_0\}).
\]
Thus the connecting homomorphism in the relative Mayer--Vietoris sequence is an isomorphism shifting degree by one.
:::

<1>3. One has
\[
H_i(P_n,A_n)\cong H_{i-n}(X).
\]
::: {.proof}
Iterate <1>2 until $n=0$. Since $S^0$ consists of two points and $A_0$ is one copy of $X$,
\[
H_j(X\times S^0,\,X\times\{x_0\})\cong H_j(X).
\]
Therefore after $n$ shifts,
\[
H_i(P_n,A_n)\cong H_{i-n}(X),
\]
where the latter is zero for negative indices.
:::

Combining <1>1 and <1>3 gives
\[
\boxed{H_i(X\times S^n)\cong H_i(X)\oplus H_{i-n}(X).}
\]
:::
