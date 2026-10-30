---
schema: qual/card@1
id: P-AMD-7NJ4YRS5
kind: problem
title: $\operatorname{Tor}$ of the sign module over $\ZZ[\ZZ_2]$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Modules
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $R = \ZZ[\ZZ_2]$ be the group ring, and let $M$ be $\ZZ$ with the generator of $\ZZ_2$ acting by $-1$.
Construct a free resolution of $M$ and compute $\Tor_R^*(M, M)$.
:::

::: {.solution}
Let $G=C_2=\{1,\sigma\}$, let
$$
R=\ZZ[G]=\ZZ[\sigma]/(\sigma^2-1),
$$
and let $M\cong\ZZ$ be the sign module, so $\sigma m=-m$.

::: pf

::: {.pf-step #s1}

The $R$-linear surjection
$$
\epsilon_-:R\to M,
\qquad
\epsilon_-(a+b\sigma)=a-b,
$$
has kernel $(1+\sigma)R$.

::: pf-proof

The map is $R$-linear because multiplication by $\sigma$ interchanges $a$ and $b$, while $\sigma$ acts by $-1$ on $M$. Moreover,
$$
\epsilon_-(a+b\sigma)=0\iff a=b\iff a+b\sigma=a(1+\sigma).
$$

:::

:::

::: {.pf-step #s2}

Multiplication by $1+\sigma$ has kernel $(1-\sigma)R$, and multiplication by $1-\sigma$ has kernel $(1+\sigma)R$.

::: pf-proof

For $r=a+b\sigma$,
$$
r(1+\sigma)=(a+b)(1+\sigma),
$$
so this vanishes exactly when $b=-a$, i.e. $r=a(1-\sigma)$. Likewise
$$
r(1-\sigma)=(a-b)(1-\sigma),
$$
which vanishes exactly when $a=b$, i.e. $r=a(1+\sigma)$.

:::

:::

::: pf-step

Therefore a free resolution of $M$ is
$$
\cdots\xrightarrow{\,1+\sigma\,}R
\xrightarrow{\,1-\sigma\,}R
\xrightarrow{\,1+\sigma\,}R
\xrightarrow{\epsilon_-}M\to0,
$$
so, with $F_0=R$, the differentials are
$$
d_{2j+1}=1+\sigma,
\qquad
d_{2j}=1-\sigma\quad(j\ge1).
$$

::: pf-proof

Exactness at $F_0$ follows from step [](#s1){.pf-ref}, and exactness at every higher term follows from the two alternating kernel computations in step [](#s2){.pf-ref}.

:::

:::

::: pf-step

Tensoring this resolution with $M$ over $R$ gives the chain complex
$$
\cdots\xrightarrow{-2}\ZZ
\xrightarrow{0}\ZZ
\xrightarrow{-2}\ZZ
\xrightarrow{0}\ZZ\to0,
$$
where the rightmost copy is degree $0$.

::: pf-proof

Under $R\otimes_RM\cong M\cong\ZZ$, multiplication by $1+\sigma$ becomes multiplication by $1+(-1)=0$, while multiplication by $1-\sigma$ becomes multiplication by $1-(-1)=2$ (up to the harmless sign convention $-2$ if one writes $\sigma-1$ instead).

:::

:::

::: {.pf-step #s5}

Hence
$$
\operatorname{Tor}_0^R(M,M)\cong\ZZ.
$$

::: pf-proof

At degree $0$ the outgoing differential is zero and the incoming differential $d_1\otimes M$ is also zero, so
$$
H_0(F_\bullet\otimes_RM)=\ZZ/0\cong\ZZ.
$$
Equivalently, $M\otimes_RM\cong R/(1+\sigma)\cong\ZZ$.

:::

:::

::: {.pf-step #s6}

For $j\ge0$,
$$
\operatorname{Tor}_{2j+1}^R(M,M)\cong\ZZ/2.
$$

::: pf-proof

At odd degree the outgoing differential is $0$, so the kernel is all of $\ZZ$, while the incoming even differential is multiplication by $2$. Thus the homology is $\ZZ/2\ZZ$.

:::

:::

::: {.pf-step #s7}

For $j\ge1$,
$$
\operatorname{Tor}_{2j}^R(M,M)=0.
$$

::: pf-proof

At positive even degree the outgoing differential is multiplication by $2$, whose kernel in $\ZZ$ is zero; hence the homology vanishes.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\operatorname{Tor}_n^R(M,M)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ/2,&n\text{ odd},\\
0,&n>0\text{ even}.
\end{cases}}
$$

::: pf-proof

Combine steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref}.

:::

:::

:::

:::
