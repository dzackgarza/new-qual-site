---
schema: qual/card@1
id: E-AMD-X26OEAAA
kind: problem
title: $[\QQ(\sqrt{2}+\sqrt{3}):\QQ]=4$ and $\QQ(\sqrt{2}+\sqrt{3})=\QQ(\sqrt{2}-\sqrt{3})=\QQ(\sqrt{2},\sqrt{3})$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Recovered both square roots from the primitive element and computed the degree by the tower law.
---

::: {.exercise}
(a) Prove that
$$
\QQ(\sqrt2+\sqrt3)=\QQ(\sqrt2-\sqrt3)=\QQ(\sqrt2,\sqrt3).
$$

(b) Prove that this extension has degree $4$ over $\QQ$.
:::

::: {.solution}
Set $\alpha=\sqrt2+\sqrt3$.

::: pf

::: {.pf-step #fields-equal}
(a) $\QQ(\alpha)=\QQ(\sqrt2-\sqrt3)=\QQ(\sqrt2,\sqrt3)$.

::: pf-proof
Since $(\sqrt3+\sqrt2)(\sqrt3-\sqrt2)=1$, we have $\alpha^{-1}=\sqrt3-\sqrt2$, so $\sqrt2-\sqrt3=-\alpha^{-1}$ and $\QQ(\sqrt2-\sqrt3)=\QQ(\alpha^{-1})=\QQ(\alpha)$.
Moreover
$$
\sqrt2=\frac{\alpha-\alpha^{-1}}2,
\qquad
\sqrt3=\frac{\alpha+\alpha^{-1}}2
$$
lie in $\QQ(\alpha)$, so $\QQ(\sqrt2,\sqrt3)\subseteq\QQ(\alpha)$. The reverse inclusion holds because $\alpha\in\QQ(\sqrt2,\sqrt3)$.
:::

:::

::: {.pf-step #sqrt3-not-in}
$\sqrt3\notin\QQ(\sqrt2)$.

::: pf-proof
Suppose $\sqrt3=a+b\sqrt2$ with $a,b\in\QQ$. Squaring gives
$$
3=a^2+2b^2+2ab\sqrt2.
$$
If $ab\ne0$, then $\sqrt2$ is rational, which is false. If $a=0$, then $b^2=3/2$, and if $b=0$, then $a^2=3$; neither has a rational solution.
:::

:::

::: pf-step
(b) $[\QQ(\alpha):\QQ]=4$, and the minimal polynomial of $\alpha$ is $x^4-10x^2+1$.

::: pf-proof
The polynomial $x^2-2$ has no rational root, so $[\QQ(\sqrt2):\QQ]=2$. By step [](#sqrt3-not-in){.pf-ref}, $x^2-3$ has no root in $\QQ(\sqrt2)$, so $[\QQ(\sqrt2,\sqrt3):\QQ(\sqrt2)]=2$. The tower law and step [](#fields-equal){.pf-ref} give $[\QQ(\alpha):\QQ]=4$.
From $\alpha^2=5+2\sqrt6$ we get $(\alpha^2-5)^2=24$, so $\alpha$ is a root of the monic polynomial $x^4-10x^2+1$ of degree $4=[\QQ(\alpha):\QQ]$, which is therefore its minimal polynomial.
:::

:::

:::

:::
