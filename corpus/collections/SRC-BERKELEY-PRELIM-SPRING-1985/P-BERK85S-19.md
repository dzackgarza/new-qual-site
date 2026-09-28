---
schema: qual/card@1
id: P-BERK85S-19
kind: problem
title: Every finite field has prime-power cardinality
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Proved directly that a finite field has prime characteristic p, contains
    F_p as its prime subfield, and is a finite-dimensional F_p-vector space,
    whose coefficient tuples give cardinality p^r.
---

::: {.problem}
Let $F$ be a finite field. Give a complete proof that
\[
|F|=p^r
\]
for some prime $p$ and integer $r\ge1$.
:::

::: {.solution}
<1>1. The characteristic of $F$ is a prime number $p$.

::: {.proof}
Because $F$ is finite, the elements
$$
0,\ 1,\ 1+1,\ 1+1+1,\ \ldots
$$
cannot all be distinct. Hence there is a least positive integer $m$ such
that
$$
m\cdot1_F=0.
$$
Thus $\operatorname{char}F=m>0$.

If $m=uv$ with $1<u<m$ and $1<v<m$, then
$$
(u\cdot1_F)(v\cdot1_F)
=
m\cdot1_F
=0.
$$
By minimality of $m$, neither factor is zero. This contradicts the fact
that a field has no zero divisors. Therefore $m$ is prime; write
$m=p$.
:::

<1>2. The prime subfield of $F$ is isomorphic to $\FF_p$.

::: {.proof}
The ring homomorphism
$$
\ZZ\to F,
\qquad
n\longmapsto n\cdot1_F,
$$
has kernel $p\ZZ$ by step <1>1. Hence its image is a subfield of $F$
isomorphic to
$$
\ZZ/p\ZZ=\FF_p.
$$
We identify this image with $\FF_p$.
:::

<1>3. The field $F$ is a finite-dimensional vector space over $\FF_p$.

::: {.proof}
Since $\FF_p\subset F$, the field $F$ is an $\FF_p$-vector space. Any
linearly independent subset of $F$ is, in particular, a subset of the
finite set $F$, so it is finite. Thus a basis of $F$ over $\FF_p$ is
finite. Write
$$
\dim_{\FF_p}F=r.
$$
Because $1_F\neq0$, this vector space is nonzero, so $r\geq1$.
:::

<1>4. The field $F$ has exactly $p^r$ elements.

::: {.proof}
Choose a basis $e_1,\ldots,e_r$ of $F$ over $\FF_p$. Every element of
$F$ has a unique expression
$$
c_1e_1+\cdots+c_re_r,
\qquad
c_j\in\FF_p.
$$
There are $p$ independent choices for each of the $r$ coefficients, so
there are exactly $p^r$ such coefficient tuples. Hence
$$
\boxed{\abs{F}=p^r}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 gives a prime $p$, step <1>3 gives an integer $r\geq1$, and
step <1>4 gives the required cardinality.
:::
:::
