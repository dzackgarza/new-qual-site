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
::: pf

::: {.pf-step #char-is-prime}
The characteristic of $F$ is a prime number $p$.

::: pf-proof
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

:::

::: {.pf-step #prime-subfield}
The prime subfield of $F$ is isomorphic to $\FF_p$.

::: pf-proof
The ring homomorphism
$$
\ZZ\to F,
\qquad
n\longmapsto n\cdot1_F,
$$
has kernel $p\ZZ$ by step [](#char-is-prime){.pf-ref}. Hence its image is a subfield of $F$
isomorphic to
$$
\ZZ/p\ZZ=\FF_p.
$$
We identify this image with $\FF_p$.
:::

:::

::: {.pf-step #finite-dimensional}
The field $F$ is a finite-dimensional vector space over $\FF_p$.

::: pf-proof
Since $\FF_p\subset F$, the field $F$ is an $\FF_p$-vector space. Any
linearly independent subset of $F$ is, in particular, a subset of the
finite set $F$, so it is finite. Thus a basis of $F$ over $\FF_p$ is
finite. Write
$$
\dim_{\FF_p}F=r.
$$
Because $1_F\neq0$, this vector space is nonzero, so $r\geq1$.
:::

:::

::: {.pf-step #cardinality-boxed}
The field $F$ has exactly $p^r$ elements.

::: pf-proof
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

:::

::: pf-qed
Step [](#char-is-prime){.pf-ref} gives a prime $p$, step [](#finite-dimensional){.pf-ref} gives an integer $r\geq1$, and
step [](#cardinality-boxed){.pf-ref} gives the required cardinality.
:::

:::
:::
