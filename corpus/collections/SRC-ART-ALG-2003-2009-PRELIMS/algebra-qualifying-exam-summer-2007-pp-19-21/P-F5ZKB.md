---
schema: qual/card@1
id: P-F5ZKB
kind: problem
title: A finite field has $p^n$ elements; subfields of a field of size $3^{12}$; an
  infinite field of characteristic $3$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---
::: {.problem}
(a) Show that a finite field must have exactly $p^n$ elements for some prime $p$ and some positive integer $n$.

(b) List all the subfields of the field of size $3^{12}$.

(c) Give an example of an infinite field of characteristic $3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every finite field has cardinality $p^n$ for some prime $p$ and integer $n\ge1$.

::: pf-proof

Let $F$ be finite. Its characteristic cannot be $0$, because then its prime subfield would be isomorphic to the infinite field $\QQ$. Hence
$$
\operatorname{char}(F)=p
$$
for some prime $p$, and the prime subfield is $\FF_p$.

Thus $F$ is a vector space over $\FF_p$. Since $F$ is finite, this vector space has finite dimension, say
$$
n=[F:\FF_p]\ge1.
$$
An $n$-dimensional vector space over the $p$-element field has exactly $p^n$ elements. Therefore
$$
\boxed{\cardinality{F}=p^n}.
$$

:::

:::

::: {.pf-step #s2}

Every subfield of $\FF_{3^{12}}$ has order $3^d$ for some divisor $d\mid12$.

::: pf-proof

Every subfield contains the prime field $\FF_3$. If
$$
K\subseteq\FF_{3^{12}}
$$
and
$$
d=[K:\FF_3],
$$
then the tower law gives
$$
12=[\FF_{3^{12}}:K]\,d.
$$
Hence $d\mid12$, and step [](#s1){.pf-ref} gives
$$
\cardinality{K}=3^d.
$$
The positive divisors of $12$ are
$$
1,2,3,4,6,12.
$$

:::

:::

::: {.pf-step #s3}

For each divisor $d\mid12$, there is exactly one subfield of order $3^d$.

::: pf-proof

Inside $F=\FF_{3^{12}}$, define
$$
F_d=\{a\in F:a^{3^d}=a\}.
$$
Because $d\mid12$, the polynomial
$$
X^{3^d}-X
$$
divides
$$
X^{3^{12}}-X.
$$
The latter has every element of $F$ as a root, and has derivative $-1$, so it splits into distinct linear factors over $F$. Hence $X^{3^d}-X$ also splits into $3^d$ distinct linear factors in $F[X]$. Thus $\cardinality{F_d}=3^d$.

The Frobenius power map
$$
a\longmapsto a^{3^d}
$$
is a field endomorphism in characteristic $3$, so its fixed set $F_d$ is closed under addition, multiplication, additive inverses, and inverses of nonzero elements. Therefore $F_d$ is a subfield.

If $K\subseteq F$ is any subfield of order $3^d$, then every nonzero $a\in K$ satisfies
$$
a^{3^d-1}=1
$$
by Lagrange's theorem, so every $a\in K$ satisfies $a^{3^d}=a$. Hence
$$
K\subseteq F_d.
$$
Both fields have $3^d$ elements, so $K=F_d$. This proves uniqueness.

:::

:::

::: {.pf-step #s4}

Therefore the subfields of $\FF_{3^{12}}$ are exactly
$$
\boxed{\FF_3,\ \FF_9,\ \FF_{27},\ \FF_{81},\ \FF_{729},\ \FF_{3^{12}}}.
$$

::: pf-proof

Combine step [](#s2){.pf-ref} with the existence and uniqueness from step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The field
$$
\boxed{\FF_3(t)}
$$
is an infinite field of characteristic $3$.

::: pf-proof

The polynomial ring $\FF_3[t]$ is an integral domain, so its field of fractions $\FF_3(t)$ is a field. Its prime subfield is $\FF_3$, hence its characteristic is $3$. The elements
$$
1,t,t^2,t^3,\ldots
$$
are pairwise distinct, so the field is infinite.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), step [](#s4){.pf-ref} answers part (b), and step [](#s5){.pf-ref} answers part (c).

:::

:::

:::
