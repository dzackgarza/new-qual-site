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
<1>1. The prime factorization is
\[
600=2^3\cdot3\cdot5^2.
\]

::: {.proof}
Indeed,
\[
600=8\cdot3\cdot25.
\]
:::

<1>2. The fundamental theorem of finite abelian groups implies that the
$2$-primary part is one of
\[
\mathbb Z_8,\qquad
\mathbb Z_4\times\mathbb Z_2,\qquad
\mathbb Z_2^3,
\]
the $3$-primary part is $\mathbb Z_3$, and the $5$-primary part is one of
\[
\mathbb Z_{25},\qquad
\mathbb Z_5^2.
\]

::: {.proof}
For a finite abelian $p$-group of order $p^r$, isomorphism types correspond
to partitions of $r$. The partitions of $3$ are
\[
3,\qquad2+1,\qquad1+1+1,
\]
the only partition of $1$ is $1$, and the partitions of $2$ are
\[
2,\qquad1+1.
\]
The displayed primary components are exactly the groups attached to those
partitions.
:::

<1>3. Hence there are exactly
\[
3\cdot1\cdot2=6
\]
isomorphism classes.

::: {.proof}
The primary decomposition is unique, and the choices for distinct primes are
independent. Thus every choice of one $2$-primary type and one $5$-primary
type, together with the unique $3$-primary type, gives one isomorphism class,
and no two such choices are isomorphic.
:::

<1>4. In invariant-factor form, the six groups are
\[
\boxed{
\begin{aligned}
&\mathbb Z_2\times\mathbb Z_{10}\times\mathbb Z_{30},\\
&\mathbb Z_{10}\times\mathbb Z_{60},\\
&\mathbb Z_5\times\mathbb Z_{120},\\
&\mathbb Z_2\times\mathbb Z_2\times\mathbb Z_{150},\\
&\mathbb Z_2\times\mathbb Z_{300},\\
&\mathbb Z_{600}.
\end{aligned}}
\]

::: {.proof}
Combining cyclic factors of pairwise coprime orders gives the equivalent
elementary-divisor descriptions
\[
\begin{aligned}
\mathbb Z_2^3\times\mathbb Z_3\times\mathbb Z_5^2
&\cong
\mathbb Z_2\times\mathbb Z_{10}\times\mathbb Z_{30},\\
(\mathbb Z_4\times\mathbb Z_2)\times\mathbb Z_3\times\mathbb Z_5^2
&\cong
\mathbb Z_{10}\times\mathbb Z_{60},\\
\mathbb Z_8\times\mathbb Z_3\times\mathbb Z_5^2
&\cong
\mathbb Z_5\times\mathbb Z_{120},\\
\mathbb Z_2^3\times\mathbb Z_3\times\mathbb Z_{25}
&\cong
\mathbb Z_2\times\mathbb Z_2\times\mathbb Z_{150},\\
(\mathbb Z_4\times\mathbb Z_2)\times\mathbb Z_3\times\mathbb Z_{25}
&\cong
\mathbb Z_2\times\mathbb Z_{300},\\
\mathbb Z_8\times\mathbb Z_3\times\mathbb Z_{25}
&\cong
\mathbb Z_{600}.
\end{aligned}
\]
These are the six cases counted in step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the complete classification up to isomorphism.
:::
:::
