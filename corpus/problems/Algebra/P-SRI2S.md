---
schema: qual/card@1
id: P-SRI2S
kind: problem
title: Galois group of $x^2+1$ and the Gaussian integers
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Integral Extensions
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What's the Galois group of $x^2 + 1$ over $\QQ$? What's the integral closure of $\ZZ$ in $\QQ(i)$?
:::

::: {.solution}

::: pf

::: pf-step

$\Gal(\QQ(i)/\QQ)=\{1,\text{complex conjugation}\}\cong\boxed{C_2}$.

::: pf-proof

$x^2+1$ has no rational root, so it is irreducible over $\QQ$; its roots are $\pm i$, so its splitting field is $\QQ(i)$, of degree $2$. A $\QQ$-automorphism sends $i$ to $\pm i$, and both choices occur.

:::

:::

::: {.pf-step #integral}

If $\alpha=a+bi$ with $a,b\in\QQ$ is integral over $\ZZ$, then $a,b\in\ZZ$.

::: pf-proof

The conjugate $\overline\alpha$ is also integral, so the rational numbers $\alpha+\overline\alpha=2a$ and $\alpha\overline\alpha=a^2+b^2$ are integral over $\ZZ$, hence lie in $\ZZ$. Put $m=2a$. Then $(2b)^2=4(a^2+b^2)-m^2\in\ZZ$, and a rational number whose square is an integer is an integer, so $2b\in\ZZ$. Since $m^2+(2b)^2=4(a^2+b^2)\equiv0\pmod 4$ and squares are $0$ or $1$ modulo $4$, both $m$ and $2b$ are even. Hence $a,b\in\ZZ$.

:::

:::

::: pf-qed

Conversely, $i$ satisfies $x^2+1=0$, so $\ZZ[i]$ is integral over $\ZZ$. With step [](#integral){.pf-ref}, the integral closure of $\ZZ$ in $\QQ(i)$ is $\boxed{\ZZ[i]}$.

:::

:::

:::
