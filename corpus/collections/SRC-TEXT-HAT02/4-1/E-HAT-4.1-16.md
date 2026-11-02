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

- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Read against the book (AT.txt:17887-17889 for the statement, 17590-17602 and 17605-17609 for the
    cell-attachment constructions it follows). The construction is correct: cells of dimension at least
    n+1 preserve pi_i for i <= n, and at each k the map is made surjective by wedging k-spheres and then
    injective by attaching (k+1)-cells along representatives of the kernel. One step was asserted and is
    now given: passing from an isomorphism at the stage k = i to an isomorphism on the union Z_n needs
    pi_i(Z_n) = colim_k pi_i(Z_k), which holds because a map S^i -> Z_n has compact image, hence lies in
    a finite subcomplex and so in a single stage (Hatcher, Proposition A.1, AT.txt:25888-25889). The
    pi_0 hypothesis is met because X, Y and Z_n are connected. Not checked: no verification of the
    book's own construction beyond the two cited spans.

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
Passing from a single stage to the union uses compactness: $Z_n$ is the increasing union of the stages of the construction, and a map $S^i\to Z_n$ has compact image, hence by Hatcher's Proposition A.1 lies in a finite subcomplex and therefore in some single stage $Z_k$, so $\pi_i(Z_n)=\varinjlim_k\pi_i(Z_k)$. The isomorphism at stage $k=i$, for every $i\ge n+1$, therefore assembles to the displayed isomorphism of the union.
The original map is the composite
$$
X\longrightarrow Z_n\xrightarrow{g}Y.
$$
Thus
$$
\boxed{f\text{ has the required factorization}.}
$$
:::
