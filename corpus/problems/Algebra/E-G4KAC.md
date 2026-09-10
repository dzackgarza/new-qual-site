---
schema: qual/card@1
id: E-G4KAC
kind: problem
title: $x\in J(R)\iff 1-xR\subseteq R^\times$
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Rings
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the left/right ideal orientation and supplied the 1-ab versus 1-ba unit argument.
---

::: {.exercise}
Let $R$ be a ring with identity and let $J(R)$ be its Jacobson radical. Prove that
\[
x\in J(R)\iff 1-xr\in R^\times\quad\text{for every }r\in R.
\]
:::

::: {.solution}
We use the description
\[
J(R)=\bigcap_{M\text{ maximal left ideal}}M.
\]

<1>1. If $j\in J(R)$, then $1-j$ is a unit.
::: {.proof}
If the left ideal $R(1-j)$ were proper, it would lie in a maximal left ideal $M$. Since $j\in J(R)\subseteq M$, we would have
\[
1=(1-j)+j\in M,
\]
a contradiction. Hence $R(1-j)=R$, so some $u\in R$ satisfies
\[
u(1-j)=1.
\]
Then
\[
1-u=-uj\in J(R)
\]
because $J(R)$ is a two-sided ideal. Applying the same argument to $1-u\in J(R)$ shows that $u=1-(1-u)$ has a left inverse $v$, so $vu=1$. If $a=1-j$, then $ua=1$ and
\[
v=v(ua)=(vu)a=a.
\]
Thus $au=1$ as well, and $a=1-j$ is a unit.
:::

<1>2. If $x\in J(R)$, then $1-xr$ is a unit for every $r\in R$.
::: {.proof}
Since $J(R)$ is a two-sided ideal, $xr\in J(R)$. Apply <1>1 to $j=xr$.
:::

<1>3. Conversely, suppose $1-xr$ is a unit for every $r\in R$. Then $x\in J(R)$.
::: {.proof}
We first use the elementary identity: if $1-ab$ is a unit, then so is $1-ba$, with inverse
\[
(1-ba)^{-1}=1+b(1-ab)^{-1}a.
\]
Hence the hypothesis also gives that $1-rx$ is a unit for every $r\in R$.

Let $M$ be a maximal left ideal. If $x\notin M$, then maximality gives
\[
M+Rx=R.
\]
Thus $1=m+rx$ for some $m\in M$ and $r\in R$, so
\[
m=1-rx.
\]
But $1-rx$ is a unit, impossible for an element of the proper left ideal $M$. Therefore $x\in M$ for every maximal left ideal $M$, hence $x\in J(R)$.
:::

Thus
\[
x\in J(R)\iff 1-xR\subseteq R^\times.
\]
:::
