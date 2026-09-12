---
schema: qual/card@1
id: P-HFGO1
kind: problem
title: A polynomial not solvable by radicals
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give an example of a polynomial that is not solvable by radicals.
:::

::: solution
Take
\[
f(x)=x^5-x-1\in\mathbb Q[x].
\]
Its Galois group over $\mathbb Q$ is $S_5$, so $f$ is not solvable by radicals.

<1>1. The polynomial $f$ is irreducible over $\mathbb Q$.
::: proof
Modulo $3$,
\[
\bar f(x)=x^5-x-1.
\]
It has no root in $\mathbb F_3$. The monic irreducible quadratics over
$\mathbb F_3$ are
\[
x^2+1,\qquad x^2+x+2,\qquad x^2+2x+2,
\]
and division of $\bar f$ by these gives remainders respectively
\[
-1,\qquad x-1,\qquad x-1.
\]
Thus $\bar f$ has no factor of degree $1$ or $2$. A reducible polynomial of
degree $5$ over a field must have a factor of degree at most $2$, so $\bar f$ is
irreducible. Hence $f$ is irreducible over $\mathbb Q$ by Gauss's lemma.
:::

<1>2. The Galois group $G$ contains a transposition.
::: proof
Modulo $2$,
\[
\bar f(x)=x^5+x+1
=(x^2+x+1)(x^3+x^2+1).
\]
The discriminant of $f$ is
\[
\operatorname{disc}(f)=2869,
\]
which is odd, so $2$ is unramified in the splitting field. Dedekind's
factorization theorem therefore gives an element of $G\le S_5$ with cycle type
$(2)(3)$. The cube of such an element is a transposition.
:::

<1>3. A transitive subgroup of $S_5$ containing a transposition is $S_5$.
::: proof
By <1>1, $G$ acts transitively on the five roots. Since the degree $5$ is prime,
this action is primitive.

Let $\tau\in G$ be a transposition. Form a graph whose vertices are the five
roots and whose edges are the transpositions $g\tau g^{-1}$ for $g\in G$.
The connected components are permuted by $G$, hence form a block system. By
primitivity the graph is connected. Transpositions along the edges of a
connected graph generate the full symmetric group on its vertices. Therefore
the normal closure of $\tau$ in $G$ is $S_5$, so $G=S_5$.
:::

<1>4. The polynomial $f$ is not solvable by radicals.
::: proof
A polynomial over a field of characteristic $0$ is solvable by radicals only if
its Galois group is solvable. The group $S_5$ is not solvable because it contains
the nonabelian simple subgroup $A_5$. Hence $f$ is not solvable by radicals.
:::
:::
