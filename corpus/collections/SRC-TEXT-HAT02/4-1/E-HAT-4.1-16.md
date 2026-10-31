---
schema: qual/card@1
id: E-HAT-4.1-16
kind: problem
title: "Factoring maps through $n$-connective covers"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 16 and the cell-attachment construction preceding Proposition 4.13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Show that a map $f: X \to Y$ between connected CW complexes factors as a composition $X \to Z_n \to Y$ where the first map induces isomorphisms on $\pi_i$ for $i \leq n$ and the second map induces isomorphisms on $\pi_i$ for $i \geq n+1$.
:::

::: {.solution}
Use the cell-attachment construction from the proof preceding Proposition 4.13. Starting with
$$
f:X\longrightarrow Y,
$$
attach cells to the source only in dimensions at least $n+1$, extending the map over every attached cell. The cells of dimension $n+1$ will have constant attaching maps, so they do not change $\pi_n$.

Inductively, suppose a map
$$
f_k:Z_k\to Y
$$
has already been made an isomorphism on $\pi_i$ for
$$
n+1\le i<k.
$$
For each class of $\pi_k(Y)$ not yet in the image, wedge a $k$-sphere onto $Z_k$ at the basepoint and extend $f_k$ over it by a representative of that class. This makes the map surjective on $\pi_k$ without changing lower homotopy groups. Then attach $(k+1)$-cells along representatives of the kernel of
$$
\pi_k(Z_k)\to\pi_k(Y)
$$
and extend them over $Y$ by chosen nullhomotopies. The resulting map is an isomorphism on $\pi_k$, while the already established lower homotopy groups are unchanged.

Begin this process at $k=n+1$ and continue for all $k$. Let $Z_n$ be the union. At the first stage the $(n+1)$-cells are attached by constant maps, so this stage is a wedge with $(n+1)$-spheres and induces isomorphisms on $\pi_i$ for $i\le n$. All later cells have dimension at least $n+2$ and preserve these groups by cellular approximation. Hence
$$
\pi_i(X)\xrightarrow{\cong}\pi_i(Z_n)
\qquad(i\le n).
$$
By the inductive construction, the extension
$$
g:Z_n\to Y
$$
induces isomorphisms
$$
\pi_i(Z_n)\xrightarrow{\cong}\pi_i(Y)
\qquad(i\ge n+1).
$$
The original map is the composite
$$
X\longrightarrow Z_n\xrightarrow{g}Y.
$$
Thus
$$
\boxed{f\text{ has the required factorization}.}
$$
:::
