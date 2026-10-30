---
schema: qual/card@1
id: P-YAODF
kind: problem
title: Division by integers prime to the characteristic stays in the base field
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved UGA problem-set reproduction of the Hungerford exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Hungerford V.6.1 prints nv in K, so the statement stays; a remark proves the purely inseparable
    v^n in K version.
---

::: {.problem}
Let $F/K$ be a field extension.
Let $\mathrm{char} K = p \neq 0$ and let $n\geq 1$ be an integer such that $(p, n) = 1$.
If $v\in F$ and $nv \in K$, then $v\in K$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The element $n\cdot1_K$ is nonzero in $K$.

::: pf-proof

Since $\operatorname{char}K=p$, one has
$$
n\cdot1_K=0
\quad\Longleftrightarrow\quad
p\mid n.
$$
The hypothesis $(p,n)=1$ excludes this, so $n\cdot1_K\ne0$.

:::

:::

::: {.pf-step #s2}

The element $n\cdot1_K$ is invertible in $K$.

::: pf-proof

Every nonzero element of a field is invertible. Apply this to step [](#s1){.pf-ref}.

:::

:::

::: pf-step

If $nv\in K$, then $v\in K$.

::: pf-proof

Interpreting multiplication by the integer $n$ as scalar multiplication by
$n\cdot1_K$, we have
$$
nv=(n\cdot1_K)v.
$$
By hypothesis the left side belongs to $K$, and by step [](#s2){.pf-ref} the inverse
$(n\cdot1_K)^{-1}$ belongs to $K$. Therefore
$$
v=(n\cdot1_K)^{-1}(nv)\in K.
$$

:::

:::

:::

:::

::: {.remark}
The same hypotheses give a multiplicative version that uses the exponent instead of the
multiple. If $v\in F$ is purely inseparable over $K$ and $v^n\in K$, then $v\in K$. Indeed,
$v^{p^e}\in K$ for some $e\ge0$. Since $(n,p^e)=1$, there are integers $a,b$ with $an+bp^e=1$,
and so $v=(v^n)^a\,(v^{p^e})^b\in K$. This needs $v\ne0$ when $a$ or $b$ is negative, and
$v=0$ is already in $K$.
:::
