---
schema: qual/card@1
id: E-HAT-4.1-20
kind: problem
title: "Finiteness of $[X, Y]$ for finite CW complexes"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 20; the stored statement matches.
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
    Read against the book (AT.txt:17898-17899 for the statement). The obstruction induction is written at
    sketch level but is sound: replacing Y by its d-th Postnikov stage is legitimate because Y -> Y^d is an
    isomorphism on pi_i for i <= d and X is d-dimensional; a map is then built cell by cell, with
    obstructions in pi_{k-1}(Y) and the set of extensions up to homotopy rel boundary a torsor under
    pi_k(Y); both finite for k <= d, and only finitely many cells occur. The free-homotopy bookkeeping is
    covered by the card's use of the hypothesis at i = 0: a map lands in one component of Y and pi_0(Y) is
    finite, which the statement's "for i <= dim X" supplies, and without it the claim fails (a point and a
    space with infinitely many components). Not checked: no re-derivation of the Postnikov-stage reduction
    beyond the argument given.

---

::: {.problem}
Show that $[X, Y]$ is finite if $X$ is a finite connected CW complex and $\pi_i(Y)$ is finite for $i \leq \dim X$.
:::

::: {.solution}
Let $d=\dim X$. Replace $Y$ by its $d$-th Postnikov stage $Y^d$. The map
$$
Y\to Y^d
$$
induces isomorphisms on $\pi_i$ for $i\le d$, so obstruction theory (or cellular induction) gives a bijection
$$
[X,Y]\cong[X,Y^d]
$$
for the $d$-dimensional CW complex $X$.

We now construct maps $X\to Y^d$ cell by cell. Since $X$ is connected, each map lands in one path component of $Y$. There are finitely many such choices by the hypothesis on $\pi_0(Y)$; fix one component at a time. Suppose a map has been constructed on $X^{k-1}$. For each $k$-cell, extension across the cell is obstructed by an element of
$$
\pi_{k-1}(Y),
$$
and, when extensions exist, the set of choices up to homotopy rel boundary is a torsor under
$$
\pi_k(Y).
$$
Both groups are finite for $k\le d$ by hypothesis.

Since $X$ has only finitely many cells, at each stage there are only finitely many possible obstruction values and finitely many choices of extensions. Inducting over the finitely many skeleta, only finitely many homotopy classes of maps can occur. Thus
$$
\boxed{[X,Y]\text{ is finite}.}
$$
:::
