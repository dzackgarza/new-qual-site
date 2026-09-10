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
Define $M$ as the group ring $R = \ZZ[\ZZ_2]$ with the action $(\cdot) \times -1$.
Construct a free resolution of $M$ and compute $\tor_R^*(M, M)$.
:::

::: {.solution}
Let $G=C_2=\{1,\sigma\}$, let
$$
R=\mathbb Z[G]=\mathbb Z[\sigma]/(\sigma^2-1),
$$
and let $M\cong\mathbb Z$ be the sign module, so $\sigma m=-m$.

<1>1. The $R$-linear surjection
$$
\epsilon_-:R\to M,
\qquad
\epsilon_-(a+b\sigma)=a-b,
$$
has kernel $(1+\sigma)R$.
::: {.proof}
The map is $R$-linear because multiplication by $\sigma$ interchanges $a$ and $b$, while $\sigma$ acts by $-1$ on $M$. Moreover,
$$
\epsilon_-(a+b\sigma)=0\iff a=b\iff a+b\sigma=a(1+\sigma).
$$
:::

<1>2. Multiplication by $1+\sigma$ has kernel $(1-\sigma)R$, and multiplication by $1-\sigma$ has kernel $(1+\sigma)R$.
::: {.proof}
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

<1>3. Therefore a free resolution of $M$ is
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
::: {.proof}
Exactness at $F_0$ follows from <1>1, and exactness at every higher term follows from the two alternating kernel computations in <1>2.
:::

<1>4. Tensoring this resolution with $M$ over $R$ gives the chain complex
$$
\cdots\xrightarrow{-2}\mathbb Z
\xrightarrow{0}\mathbb Z
\xrightarrow{-2}\mathbb Z
\xrightarrow{0}\mathbb Z\to0,
$$
where the rightmost copy is degree $0$.
::: {.proof}
Under $R\otimes_RM\cong M\cong\mathbb Z$, multiplication by $1+\sigma$ becomes multiplication by $1+(-1)=0$, while multiplication by $1-\sigma$ becomes multiplication by $1-(-1)=2$ (up to the harmless sign convention $-2$ if one writes $\sigma-1$ instead).
:::

<1>5. Hence
$$
\operatorname{Tor}_0^R(M,M)\cong\mathbb Z.
$$
::: {.proof}
At degree $0$ the outgoing differential is zero and the incoming differential $d_1\otimes M$ is also zero, so
$$
H_0(F_\bullet\otimes_RM)=\mathbb Z/0\cong\mathbb Z.
$$
Equivalently, $M\otimes_RM\cong R/(1+\sigma)\cong\mathbb Z$.
:::

<1>6. For $j\ge0$,
$$
\operatorname{Tor}_{2j+1}^R(M,M)\cong\mathbb Z/2.
$$
::: {.proof}
At odd degree the outgoing differential is $0$, so the kernel is all of $\mathbb Z$, while the incoming even differential is multiplication by $2$. Thus the homology is $\mathbb Z/2\mathbb Z$.
:::

<1>7. For $j\ge1$,
$$
\operatorname{Tor}_{2j}^R(M,M)=0.
$$
::: {.proof}
At positive even degree the outgoing differential is multiplication by $2$, whose kernel in $\mathbb Z$ is zero; hence the homology vanishes.
:::

<1>8. Therefore
$$
\boxed{
\operatorname{Tor}_n^R(M,M)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z/2,&n\text{ odd},\\
0,&n>0\text{ even}.
\end{cases}}
$$
::: {.proof}
Combine <1>5--<1>7.
:::
:::
