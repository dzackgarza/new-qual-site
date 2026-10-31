---
schema: qual/card@1
id: P-FHW1-09
kind: problem
title: Minimal polynomials of coprime degrees stay irreducible
classification:
  areas: [algebra]
  topics: [Field Extensions, Irreducibility Criteria]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $\alpha,\beta\in F$ be algebraic over $K$, let $f(x)$ and $g(x)$ be their minimal polynomials, and suppose that $\deg f$ and $\deg g$ are coprime. Prove that $f(x)$ is irreducible in $K(\beta)[x]$.
:::

::: {.solution}
Let $m=\deg f$ and $n=\deg g$, let $L=K(\beta)$, and let $h\in L[x]$ be the minimal polynomial of $\alpha$ over $L$; put $r=\deg h$ and $s=[K(\alpha,\beta):K(\alpha)]$.

::: pf

::: {.pf-step #tower-one}
$[K(\alpha,\beta):K]=rn$ and $[K(\alpha,\beta):K]=sm$.

::: pf-proof
Since $[L(\alpha):L]=r$ and $[L:K]=n$, the tower law applied to $K\subseteq L\subseteq L(\alpha)=K(\alpha,\beta)$ gives the first equality.
Since $[K(\alpha):K]=m$ and $[K(\alpha,\beta):K(\alpha)]=s$, the same law applied to $K\subseteq K(\alpha)\subseteq K(\alpha,\beta)$ gives the second.
:::

:::

::: {.pf-step #divisibility}
$r$ divides $m$, and $s$ divides $n$.

::: pf-proof
The polynomial $f$ lies in $K[x]\subseteq L[x]$ and has $\alpha$ as a root, so $h$ divides $f$ in $L[x]$; both are monic, hence $m=r\deg(f/h)$ and $r$ divides $m$.
The polynomial $g$ lies in $K[x]\subseteq K(\alpha)[x]$ and has $\beta$ as a root, so the minimal polynomial of $\beta$ over $K(\alpha)$ divides $g$; its degree is $s$, so $s$ divides $n$.
:::

:::

::: {.pf-step #f-irreducible-over-l}
$f$ is irreducible over $L$, that is $r=m$.

::: pf-proof
By steps [](#tower-one){.pf-ref} and [](#divisibility){.pf-ref} we have $rn=sm$, so writing $m=rk$ for the integer $k=m/r$ gives $rn=srk$ and hence $n=sk$ after cancelling $r\ne0$.
Thus $k$ divides both $m$ and $n$.
Since $m$ and $n$ are coprime, $k=1$, so $r=m$ and $h$ and $f$ are monic polynomials of the same degree with $h$ dividing $f$; hence $h=f$ and $f$ is irreducible over $L$.
:::

:::

:::

:::
