---
schema: qual/card@1
id: E-SS1.EX-22
kind: problem
title: "SS 1.22: The integers are not a finite union of arithmetic progressions with distinct steps"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
22. Let $\mathbb { N } = \{ 1 , 2 , 3 , . . . \}$ denote the set of positive integers.
    A subset $S \subset \mathbb { N }$ is said to be in arithmetic progression if

$$
S = \{a, a + d, a + 2 d, a + 3 d, \dots \}
$$

where $a , d \in \mathbb { N } .$ . Here d is called the step of S.

Show that N cannot be partitioned into a finite number of subsets that are in arithmetic progression with distinct steps (except for the trivial case $a = d = 1 )$ . [Hint: Write $\sum { _ { n \in \mathbb { N } } z ^ { n } }$ as a sum of terms of the type ${ \frac { z ^ { a } } { 1 - z ^ { d } } } . ]$
:::

::: {.solution}
Suppose
\[
\mathbb N=S_1\sqcup\cdots\sqcup S_r,
\qquad
S_j=\{a_j+k d_j:k\ge0\},
\]
where the positive steps $d_1,\ldots,d_r$ are distinct. For $|z|<1$, disjointness of the partition gives
\[
\frac{z}{1-z}
=\sum_{n\ge1}z^n
=\sum_{j=1}^r\sum_{k\ge0}z^{a_j+kd_j}
=\sum_{j=1}^r\frac{z^{a_j}}{1-z^{d_j}}.
\tag{1}
\]
Both sides are rational functions, so (1), initially valid on the unit disc, is an identity of rational functions.

Let $D=\max_j d_j$. If $D>1$, choose a primitive $D$th root of unity $\zeta$. The left side of (1) is regular at $\zeta$, because $\zeta\ne1$.

On the right, a denominator $1-z^{d_j}$ vanishes at $\zeta$ exactly when $D\mid d_j$. Since $1\le d_j\le D$, this happens exactly for the unique index $j$ with $d_j=D$. For that term, $z^{a_j}$ is nonzero at $\zeta$, while $1-z^D$ has a simple zero there because
\[
\frac{d}{dz}(1-z^D)\bigg|_{z=\zeta}=-D\zeta^{D-1}\ne0.
\]
Hence the right side has a genuine pole at $\zeta$, contradicting regularity of the left side.

Therefore $D=1$. Since the steps are distinct positive integers, there is only one progression, and its step is $1$. A progression $\{a,a+1,a+2,\ldots\}$ equals all of $\mathbb N$ only when $a=1$. Thus the only such partition is the trivial one $a=d=1$.
:::
