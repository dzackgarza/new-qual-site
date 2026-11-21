---
schema: qual/card@1
id: E-TFUF2
kind: problem
title: Details of the imbedding theorem proof
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: dbFin, "Section 34: Problem 6 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-34-the-urysohn-metrization-theorem/problem-6-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-34-the-urysohn-metrization-theorem/problem-6-solution.txt), checked
    against Munkres, Topology (2000), Section 34 Exercise 6, printed p. 218, and Theorem 34.2 with
    its proof on the preceding pages. The three details are the card's: F is continuous because the
    preimage of a subbasic set is f_n^{-1}(U); F is injective because the family separates points
    from closed sets and one-point sets are closed; and F carries open sets to open sets of the
    image because a function f_n with f_n(x) outside the closure of f_n(X - U) gives a product-open
    set about F(x) whose preimage lies in U. The card writes the last step for an arbitrary closed
    C = X - U and an interval V about f_n(x) disjoint from f_n(C). No correction to the mathematics
    was needed; the source's own version writes the special case f_alpha(x) different from
    0 = f_alpha(X - U).
---

::: {.exercise}

Check the details of the proof of Theorem 34.2 (the imbedding theorem for a space admitting a countable family of continuous functions that separates points from closed sets).
:::

::: {.solution}

The check is the card's own; the assertion is the proof of Theorem 34.2 (printed p. 215), whose four points are verified here as the exercise asks.

Let $X$ be regular, let $\{f_{n}:X\to\RR\}_{n\ge1}$ be a countable family of continuous functions separating points from closed sets — for each $x$ and each closed $C$ with $x\notin C$ some $f_{n}$ has $f_{n}(x)\notin\overline{f_{n}(C)}$ — and let $F:X\to\RR^{\omega}$, $F(x)=\big(f_{1}(x),f_{2}(x),\ldots\big)$, with $\RR^{\omega}$ in the product topology.

::: pf

::: {.pf-step #continuous}
$F$ is continuous.

::: pf-proof
For $n$ and $U\subset\RR$ open, the preimage $F^{-1}\big(\pi_{n}^{-1}(U)\big)=f_{n}^{-1}(U)$ is open in $X$ because $f_{n}$ is continuous, and the sets $\pi_{n}^{-1}(U)$ form a subbasis of the product topology (§19, printed p. 114); a map whose preimages of subbasic open sets are open is continuous (Theorem 18.1, printed p. 104).
:::

:::

::: {.pf-step #injective}
$F$ is injective.

::: pf-proof
Let $x\ne y$. The space $X$ is regular, hence $T_{1}$, so $\{y\}$ is closed (§17, printed p. 99). By separation there is $n$ with $f_{n}(x)\notin\overline{f_{n}(\{y\})}=\{f_{n}(y)\}$, since $f_{n}(\{y\})$ is a point and points are closed in $\RR$; so $f_{n}(x)\ne f_{n}(y)$ and $F(x)\ne F(y)$.
:::

:::

::: {.pf-step #open}
$F$ carries open sets of $X$ to open sets of the subspace $F(X)$.

::: pf-proof
Let $U\subset X$ be open and $x\in U$. The set $C=X\setminus U$ is closed and does not contain $x$, so there is $n$ with $f_{n}(x)\notin\overline{f_{n}(C)}$. Hence there is an open interval $V\ni f_{n}(x)$ disjoint from $f_{n}(C)$: take $V$ an interval about $f_{n}(x)$ inside the open set $\RR\setminus\overline{f_{n}(C)}$. Put $W=\pi_{n}^{-1}(V)$, which is open in $\RR^{\omega}$; then $F(x)\in W$, and $z\in F^{-1}(W)$ means $f_{n}(z)\in V$, so $z\notin C$, that is $z\in U$. Therefore
$$
F(U)=F(X)\cap\bigcup_{x\in U}W_{x}
$$
is open in $F(X)$, because the two sets have the same elements: if $F(z)\in W_{x}$ for some $x\in U$ then $z\in U$ by the choice of $W_{x}$, and if $z\in U$ then $F(z)\in W_{z}$.
:::

:::

::: {.pf-step #imbedding}
$F$ is an imbedding of $X$ in $\RR^{\omega}$.

::: pf-proof
$F$ is continuous by step [](#continuous){.pf-ref} and injective by step [](#injective){.pf-ref}, so it is a bijection of $X$ onto the subspace $F(X)$; step [](#open){.pf-ref} says that this bijection carries open sets to open sets of $F(X)$, so its inverse is continuous and $F$ is a homeomorphism of $X$ with $F(X)$ — that is, an imbedding. In particular $F$ is an imbedding of $X$ in $\RR^{\omega}$ in the product topology.
:::

:::

:::
:::
