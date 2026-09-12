---
schema: qual/card@1
id: P-APASP07H
kind: problem
title: "Young diagrams with nonzero character on an (n-1)-cycle in S_n"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $\sigma$ be an $(n-1)$-cycle in $S_n$.
Determine all Young diagrams $\lambda$ with $n$ boxes for which $\chi^\lambda(\sigma) \neq 0$.
Partial credit if you calculate all characters of an $(n-1)$-cycle for $n = 3, 4$.
:::

::: solution
The cycle type of $\sigma$ is $(n-1,1)$. Apply the Murnaghan--Nakayama rule by removing the $(n-1)$-cycle first. After removing a rim hook of length $n-1$, one box remains. The only Young diagram with one box is $(1)$, so
\[
\chi^\lambda(\sigma)
=
\sum_R (-1)^{\operatorname{ht}(R)},
\]
where the sum is over rim hooks
\[
R=\lambda/(1)
\]
of size $n-1$.

Thus we must determine exactly when the skew diagram obtained from $\lambda$ by deleting its upper-left box is a border strip, i.e. connected and containing no $2\times2$ square.

There are three possibilities.

First, if $\lambda=(n)$, then $\lambda/(1)$ is a single row of length $n-1$, hence a border strip.

Second, if $\lambda=(1^n)$, then $\lambda/(1)$ is a single column of length $n-1$, hence a border strip.

Now suppose $\lambda$ has at least two rows and at least two columns. Write
\[
\lambda=(\lambda_1,\lambda_2,\lambda_3,\ldots).
\]
Because the box $(1,1)$ has been removed, connectivity of $\lambda/(1)$ forces
\[
\lambda_2\ge2:
\]
otherwise the boxes in the first row are disconnected from those below the first row. On the other hand, if $\lambda_2\ge3$, then the boxes in rows $1,2$ and columns $2,3$ form a $2\times2$ square inside $\lambda/(1)$. Hence
\[
\lambda_2=2.
\]
Similarly, if $\lambda_3\ge2$, then rows $2,3$ and columns $1,2$ form a $2\times2$ square. Therefore
\[
\lambda_3\le1,
\]
and hence every later part is also at most $1$.

Thus every remaining possibility is of the form
\[
\lambda=(a,2,1^b),
\qquad a\ge2,\quad b\ge0,\quad a+b=n-2.
\]
Conversely, for every such partition, $\lambda/(1)$ is visibly connected and has no $2\times2$ square, so it is a border strip.

Therefore
\[
\boxed{
\chi^\lambda(\sigma)\ne0
\iff
\lambda=(n),\ (1^n),\ \text{or }\lambda=(a,2,1^b)
\text{ with }a+b=n-2.
}
\]

In fact the values are immediate from the heights of these border strips:
\[
\chi^{(n)}(\sigma)=1,
\qquad
\chi^{(1^n)}(\sigma)=(-1)^{n-2},
\]
and for $\lambda=(a,2,1^b)$,
\[
\chi^{(a,2,1^b)}(\sigma)=(-1)^{b+1}.
\]
In every case the value is $\pm1$.

For example, when $n=3$, the nonzero values occur only for $(3)$ and $(1,1,1)$; the character for $(2,1)$ vanishes on a transposition. When $n=4$, the nonzero values occur for $(4)$, $(2,2)$, and $(1,1,1,1)$, with values $1,-1,1$ on a $3$-cycle.
:::
