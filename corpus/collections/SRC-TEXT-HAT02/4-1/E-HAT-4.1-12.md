---
schema: qual/card@1
id: E-HAT-4.1-12
kind: problem
title: "$n$-connected $n$-dimensional CW complexes are contractible"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 12; the stored statement matches.
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
    Read against the book (AT.txt:17871 for the statement, 17254-17256 for n-connected, 18258-18262
    for the Hurewicz theorem). The argument is correct except at one hypothesis: it said without
    qualification that the Hurewicz map pi_m -> H_m is an isomorphism, and Hatcher's absolute form
    (Theorem 4.32) requires (m-1)-connected with m >= 2. At m = 1 it gives only the abelianised pi_1,
    so a nonzero perfect pi_1 would not be contradicted. The card now disposes of n = 0 first (a
    path-connected 0-dimensional CW complex is a point), which makes m >= n+1 >= 2 and restores the
    hypothesis. The remaining steps were checked and are unchanged: minimality of m makes X
    (m-1)-connected, X has no cells above dimension n so the cellular chain complex vanishes there so
    H_m = 0, and Whitehead applies since X and a point are CW complexes. Not checked: Hatcher's proof
    of Theorem 4.32 was not re-read, only its statement and hypothesis.

---

::: {.problem}
Show that an $n$-connected, $n$-dimensional CW complex is contractible.
:::

::: {.solution}
Let $X$ be an $n$-connected, $n$-dimensional CW complex. Thus
$$
\pi_i(X)=0\qquad(0\le i\le n).
$$
If $n=0$ then $X$ is a path-connected CW complex with no positive-dimensional cells, hence a single point, and is contractible; so assume $n\ge1$.
Suppose some higher homotopy group were nonzero, and let $m>n$ be the least integer with
$$
\pi_m(X)\ne0.
$$
Then $X$ is $(m-1)$-connected, and $m\ge n+1\ge2$, so the Hurewicz theorem applies in its absolute form, whose hypothesis is $(m-1)$-connected with $m\ge2$ (Hatcher, Theorem 4.32); at $m=1$ it would give only the abelianized $\pi_1$, which is why the case $n=0$ was disposed of first. Thus the Hurewicz map
$$
\pi_m(X)\longrightarrow H_m(X;\ZZ)
$$
is an isomorphism. Hence $H_m(X;\ZZ)\ne0$.

But $X$ has no cells in dimensions greater than $n$, so its cellular chain complex is zero above dimension $n$. Therefore
$$
H_m(X;\ZZ)=0\qquad(m>n),
$$
a contradiction. Thus every homotopy group of $X$ is trivial.

The map $X\to *$ is consequently an isomorphism on all homotopy groups. Since $X$ and a point are CW complexes, Whitehead's theorem implies that $X\to *$ is a homotopy equivalence. Hence
$$
\boxed{X\text{ is contractible}.}
$$
:::
