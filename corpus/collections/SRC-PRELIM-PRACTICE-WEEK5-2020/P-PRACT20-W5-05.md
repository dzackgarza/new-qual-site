---
schema: qual/card@1
id: P-PRACT20-W5-05
kind: problem
title: Abelian groups of order $600$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Classify all abelian groups of order 600 (up to isomorphism).
:::

::: {.solution}

::: pf

::: pf-step

The prime factorization is
$$
600=2^3\cdot3\cdot5^2.
$$


::: pf-proof

Indeed,
$$
600=8\cdot3\cdot25.
$$

:::

:::

::: pf-step

The fundamental theorem of finite abelian groups implies that the
$2$-primary part is one of
$$
\ZZ_8,\qquad
\ZZ_4\times\ZZ_2,\qquad
\ZZ_2^3,
$$
the $3$-primary part is $\ZZ_3$, and the $5$-primary part is one of
$$
\ZZ_{25},\qquad
\ZZ_5^2.
$$


::: pf-proof

For a finite abelian $p$-group of order $p^r$, isomorphism types correspond
to partitions of $r$. The partitions of $3$ are
$$
3,\qquad2+1,\qquad1+1+1,
$$
the only partition of $1$ is $1$, and the partitions of $2$ are
$$
2,\qquad1+1.
$$
The displayed primary components are exactly the groups attached to those
partitions.

:::

:::

::: {.pf-step #s1-3}

Hence there are exactly
$$
3\cdot1\cdot2=6
$$
isomorphism classes.


::: pf-proof

The primary decomposition is unique, and the choices for distinct primes are
independent. Thus every choice of one $2$-primary type and one $5$-primary
type, together with the unique $3$-primary type, gives one isomorphism class,
and no two such choices are isomorphic.

:::

:::

::: {.pf-step #s1-4}

In invariant-factor form, the six groups are
$$
\boxed{
\begin{aligned}
&\ZZ_2\times\ZZ_{10}\times\ZZ_{30},\\
&\ZZ_{10}\times\ZZ_{60},\\
&\ZZ_5\times\ZZ_{120},\\
&\ZZ_2\times\ZZ_2\times\ZZ_{150},\\
&\ZZ_2\times\ZZ_{300},\\
&\ZZ_{600}.
\end{aligned}}
$$


::: pf-proof

Combining cyclic factors of pairwise coprime orders gives the equivalent
elementary-divisor descriptions
$$
\begin{aligned}
\ZZ_2^3\times\ZZ_3\times\ZZ_5^2
&\cong
\ZZ_2\times\ZZ_{10}\times\ZZ_{30},\\
(\ZZ_4\times\ZZ_2)\times\ZZ_3\times\ZZ_5^2
&\cong
\ZZ_{10}\times\ZZ_{60},\\
\ZZ_8\times\ZZ_3\times\ZZ_5^2
&\cong
\ZZ_5\times\ZZ_{120},\\
\ZZ_2^3\times\ZZ_3\times\ZZ_{25}
&\cong
\ZZ_2\times\ZZ_2\times\ZZ_{150},\\
(\ZZ_4\times\ZZ_2)\times\ZZ_3\times\ZZ_{25}
&\cong
\ZZ_2\times\ZZ_{300},\\
\ZZ_8\times\ZZ_3\times\ZZ_{25}
&\cong
\ZZ_{600}.
\end{aligned}
$$
These are the six cases counted in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the complete classification up to isomorphism.

:::

:::

:::
