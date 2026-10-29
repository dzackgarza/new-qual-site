---
schema: qual/card@1
id: P-MXATB
kind: problem
title: A $p$-cycle and a transposition generate $S_p$ for $p$ prime
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Group Presentations
  - Conjugacy
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
Let $p$ be prime, let $\sigma\in S_p$ be a $p$-cycle, and let $\tau\in S_p$ be any transposition. Show that
$$
\langle\sigma,\tau\rangle=S_p.
$$
:::

::: {.solution}
Label the $p$ points by $\ZZ/p\ZZ$ so that $\sigma(x)=x+1$, write $\tau=(a\ b)$ with $d=b-a\ne0$ in $\ZZ/p\ZZ$, and let $H=\langle\sigma,\tau\rangle$.

::: pf

::: {.pf-step #conj}
$H$ contains $(x\ x+d)$ for every $x\in\ZZ/p\ZZ$.

::: pf-proof
$\sigma^k\tau\sigma^{-k}=(a+k\ b+k)$ for every $k$.
:::

:::

::: {.pf-step #path}
$H$ contains $(0\ jd)$ for every $j$ with $1\le j\le p-1$.

::: pf-proof
For $j=1$ this is step [](#conj){.pf-ref}.
If $(0\ jd)\in H$ and $j+1\le p-1$, then conjugating $(0\ jd)$ by $(jd\ (j+1)d)\in H$ gives $(0\ (j+1)d)$, because $(j+1)d\ne0$.
:::

:::

::: pf-step
$H=S_p$.

::: pf-proof
Since $p$ is prime and $d\ne0$, the multiples $d,2d,\ldots,(p-1)d$ are the nonzero elements of $\ZZ/p\ZZ$.
By step [](#path){.pf-ref}, $H$ contains every transposition $(0\ y)$, and $(x\ y)=(0\ x)(0\ y)(0\ x)$, so $H$ contains every transposition and therefore equals $S_p$.
:::

:::

:::

:::
