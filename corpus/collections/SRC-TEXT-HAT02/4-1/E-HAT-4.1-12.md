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

The argument is the card's own: Hurewicz in the least degree above $n$ where homotopy survives, against the vanishing of cellular homology above the dimension, then Whitehead.

Let $X$ be an $n$-connected, $n$-dimensional CW complex, so that $\pi_{i}(X)=0$ for $0\le i\le n$.

::: pf

::: {.pf-step #zero}
If $n=0$ then $X$ is a point, hence contractible.

::: pf-proof
A $0$-dimensional CW complex is a discrete space, and $0$-connected means path connected, so $X$ is a single point; a point is contractible. This case is separated because the Hurewicz theorem below needs $m\ge2$, and at $m=1$ it would only identify the abelianised $\pi_{1}$.
:::

:::

::: {.pf-step #hurewicz}
If $n\ge1$ and some homotopy group $\pi_{m}(X)$ with $m>n$ is nonzero, then $H_{m}(X;\ZZ)\ne0$ for the least such $m$.

::: pf-proof
Let $m>n$ be the least integer with $\pi_{m}(X)\ne0$, which exists by hypothesis. Then $\pi_{i}(X)=0$ for all $i<m$, that is $X$ is $(m-1)$-connected, and $m\ge n+1\ge2$. The absolute Hurewicz theorem (Hatcher, Theorem 4.32) then says the Hurewicz map $\pi_{m}(X)\to H_{m}(X;\ZZ)$ is an isomorphism, so $H_{m}(X;\ZZ)\cong\pi_{m}(X)\ne0$.
:::

:::

::: {.pf-step #homology}
$H_{m}(X;\ZZ)=0$ for every $m>n$.

::: pf-proof
The cellular chain group $C_{m}(X)$ is free on the $m$-cells, of which there are none when $m>n$, so the cellular chain complex vanishes in degrees above $n$ and its homology does too; cellular homology agrees with singular homology.
:::

:::

::: {.pf-step #contractible}
$X$ is contractible.

::: pf-proof
Steps [](#hurewicz){.pf-ref} and [](#homology){.pf-ref} contradict each other unless no such $m$ exists, so $\pi_{i}(X)=0$ for every $i\ge0$; with step [](#zero){.pf-ref} this covers $n=0$ as well. Hence the map $X\to\ast$ induces isomorphisms on all homotopy groups, and both $X$ and the point are CW complexes, so Whitehead's theorem gives that $X\to\ast$ is a homotopy equivalence. Therefore
$$
\boxed{X\text{ is contractible}.}
$$
:::

:::

:::
:::
