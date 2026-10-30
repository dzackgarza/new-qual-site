---
schema: qual/card@1
id: P-XFX66
kind: problem
title: Alternating and skew-symmetric multilinear forms
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Determinants
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hungerford VII.3.1 in an independent exercise reproduction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $B$ be an $R$-module.
Show that if $r+r\neq 0$ for all $r\neq 0 \in R$, then an $n$-linear form $B^n\to R$ is alternating $\iff$ it is skew-symmetric.
What if $\operatorname{char} R = 2$?
:::

::: {.solution}
Let $f:B^n\to R$ be $n$-linear. Here “skew-symmetric” means that
interchanging two arguments multiplies the value by $-1$, and “alternating”
means that $f$ vanishes whenever two arguments are equal.

::: pf

::: {.pf-step #s1}

Every alternating $n$-linear form is skew-symmetric.

::: pf-proof

Fix all arguments except positions $i<j$, and write $x,y\in B$ in those
positions. Alternation gives
$$
0=f(\ldots,x+y,\ldots,x+y,\ldots).
$$
Expanding by multilinearity, the two terms with equal arguments vanish, leaving
$$
f(\ldots,x,\ldots,y,\ldots)
+f(\ldots,y,\ldots,x,\ldots)=0.
$$
Thus interchanging the two arguments changes the sign.

:::

:::

::: {.pf-step #s2}

Under the hypothesis $r+r\ne0$ for every $0\ne r\in R$, every
skew-symmetric $n$-linear form is alternating.

::: pf-proof

Suppose two arguments, say positions $i<j$, are equal to $x$. Skew-symmetry
under their transposition gives
$$
f(\ldots,x,\ldots,x,\ldots)
=-f(\ldots,x,\ldots,x,\ldots).
$$
Hence, with $r=f(\ldots,x,\ldots,x,\ldots)$,
$$
r+r=0.
$$
By the stated hypothesis this forces $r=0$. Therefore $f$ vanishes whenever
two arguments coincide, so $f$ is alternating.

:::

:::

::: {.pf-step #s3}

If $\operatorname{char}R=2$, a skew-symmetric form need not be alternating.

::: pf-proof

Let $R=B=\FF_2$, $n=2$ and $f(x,y)=xy$. Since $-1=1$ in $R$,
skew-symmetry is symmetry, and $f(x,y)=f(y,x)$. But $f(1,1)=1\ne0$, so $f$ is
not alternating. Step [](#s1){.pf-ref} still holds, so in characteristic $2$
alternating forms are a proper subset of skew-symmetric forms in general.

:::

:::

::: pf-step

Therefore the two notions are equivalent under the stated hypothesis, and only
the implication of step [](#s1){.pf-ref} survives in characteristic $2$.

::: pf-proof

Combine steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
