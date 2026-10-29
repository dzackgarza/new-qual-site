---
schema: qual/card@1
id: P-MVETM
kind: problem
title: If every irreducible in $F[x]$ is separable then every element of $F$ is a $p$-th power
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $F$ be a field of characteristic $p>0$. Suppose every irreducible polynomial in $F[x]$ is separable. Show that every $a\in F$ is a $p$-th power in $F$.
:::

::: {.solution}
Let $a\in F$. If $a=0$, then $a=0^p$, so assume $a\ne0$. Let $f(x)=x^p-a$, and let $\beta$ be a root of $f$ in an algebraic closure $\bar F$, so that $\beta^p=a$, $\beta\ne0$, and $f(x)=(x-\beta)^p$.

::: pf

::: {.pf-step #factor}
$f$ has a monic irreducible factor $g\in F[x]$ of degree $\ell$ with $1\le\ell<p$, and $g=(x-\beta)^\ell$.

::: pf-proof
If $f$ were irreducible, it would be separable by hypothesis, but $f=(x-\beta)^p$ has a repeated root.
So a monic irreducible factor $g$ of $f$ has degree $\ell<p$.
Every root of $g$ in $\bar F$ is a root of $f$, hence equal to $\beta$, so $g=(x-\beta)^\ell$.
:::

:::

::: {.pf-step #power}
$\beta^\ell\in F$.

::: pf-proof
By step [](#factor){.pf-ref}, the constant coefficient of $g\in F[x]$ is $(-\beta)^\ell$.
:::

:::

::: pf-step
$\beta\in F$, so $a=\beta^p$ is a $p$-th power in $F$.

::: pf-proof
Since $p$ is prime and $1\le\ell<p$, there are integers $u,v$ with $u\ell+vp=1$.
Then $\beta=(\beta^\ell)^u(\beta^p)^v=(\beta^\ell)^u a^v$, which lies in $F$ by step [](#power){.pf-ref}, because $\beta\ne0$ and $a\ne0$.
:::

:::

:::

:::
