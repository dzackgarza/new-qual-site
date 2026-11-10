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
Let $\{f_n:X\to\RR\}_{n\ge1}$ be a countable family of continuous functions that separates points from closed sets, and define
$$
F:X\longrightarrow\RR^\omega,
\qquad
F(x)=(f_1(x),f_2(x),\ldots),
$$
where $\RR^\omega$ has the product topology. We verify that $F$ is an embedding.

First, $F$ is continuous. A subbasic open set in the product has the form
$$
\pi_n^{-1}(U),
$$
with $U\subset\RR$ open, and
$$
F^{-1}(\pi_n^{-1}(U))=f_n^{-1}(U),
$$
which is open in $X$.

Second, $F$ is injective. If $x\ne y$, the singleton $\{y\}$ is closed under the hypotheses of the theorem (the space is regular, hence $T_1$). Since the family separates points from closed sets, some $f_n$ satisfies
$$
f_n(x)\notin \overline{f_n(\{y\})}=\{f_n(y)\}.
$$
Thus $F(x)\ne F(y)$.

It remains to prove that $F^{-1}:F(X)\to X$ is continuous. It is enough to show that for every open $U\subset X$ and every $x\in U$, there is a product-open set $W\subset\RR^\omega$ such that
$$
F(x)\in W
\quad\text{and}\quad
F^{-1}(W)\subset U.
$$
Let $C=X-U$, a closed set not containing $x$. By separation, choose $f_n$ such that
$$
f_n(x)\notin\overline{f_n(C)}.
$$
There is therefore an open interval $V\subset\RR$ containing $f_n(x)$ and disjoint from $f_n(C)$. Set
$$
W=\pi_n^{-1}(V).
$$
Then $W$ is product-open, contains $F(x)$, and if $z\in F^{-1}(W)$, then $f_n(z)\in V$, so $z\notin C$, hence $z\in U$. Thus
$$
F(U)=F(X)\cap \bigcup_{x\in U}W_x
$$
is open in $F(X)$. Therefore $F$ is a homeomorphism from $X$ onto the subspace $F(X)\subset\RR^\omega$, as required.
:::
