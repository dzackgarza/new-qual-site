---
schema: qual/card@1
id: P-QNQTT
kind: problem
title: Galois group over $\QQ$ of an irreducible quintic with all but two roots real
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Polynomials
relations: []
review: draft
---

::: problem
Let $f(x) \in \QQ[x]$ be an irreducible polynomial of degree 5. Assume that $f$ has all but two roots in $\RR$.
Compute the Galois group of $f(x)$ over $\QQ$ and justify your answer.
:::

::: solution
Let $K$ be the splitting field of $f$ over $\QQ$, and let
$G=\operatorname{Gal}(K/\QQ)$. The group $G$ acts faithfully on the five roots
of $f$, so we regard $G$ as a subgroup of $S_5$.

Because $f$ is irreducible, this action is transitive. Hence, by
orbit-stabilizer, $5$ divides $|G|$. Cauchy's theorem therefore gives an
element of order $5$ in $G$, and any element of order $5$ in $S_5$ is a
$5$-cycle.

By hypothesis exactly three roots of $f$ are real and the remaining two are a
nonreal conjugate pair. Complex conjugation preserves the splitting field,
fixes the three real roots, and interchanges the two nonreal roots. Thus $G$
contains a transposition.

It remains to show that a subgroup of $S_5$ containing a $5$-cycle and a
transposition is all of $S_5$. Let
\[
\sigma=(0\ 1\ 2\ 3\ 4)
\]
be a $5$-cycle in $G$, after relabeling the roots, and let
$\tau=(i\ j)$ be a transposition in $G$. The conjugates
\[
\sigma^k\tau\sigma^{-k}
\qquad (k=0,1,2,3,4)
\]
are transpositions joining the pairs
\[
\{i+k,j+k\}\pmod5.
\]
These five edges form a connected graph on the five vertices, since
$j-i\not\equiv0\pmod5$. Transpositions corresponding to the edges of a
connected graph generate the full symmetric group on its vertices. Hence
$S_5\le G$. Since already $G\le S_5$, we obtain
\[
\boxed{\operatorname{Gal}(f/\QQ)\cong S_5}.
\]
:::
