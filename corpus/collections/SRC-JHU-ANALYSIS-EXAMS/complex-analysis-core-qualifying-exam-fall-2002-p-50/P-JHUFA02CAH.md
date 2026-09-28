---
schema: qual/card@1
id: P-JHUFA02CAH
kind: problem
title: "Entire functions bounded by the square of the modulus"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Determine all entire functions $f: \mathbb{C} \to \mathbb{C}$ for which $|f(z)| \le |z|^2$ for all $z \in \mathbb{C}$.
:::

::: {.solution}
Write $f(z)=\sum_{n\ge0}a_nz^n$, the Taylor series of $f$ at $0$, which converges on $\CC$.

<1>1. $a_n=0$ for $n\ge3$.

::: {.proof}
Cauchy's estimate on $\abs z=R$ gives $\abs{a_n}\le R^{-n}\max_{\abs z=R}\abs f\le R^{2-n}$, which tends to $0$ as $R\to\infty$ when $n\ge3$.
:::

<1>2. $a_0=a_1=0$.

::: {.proof}
$\abs{a_0}=\abs{f(0)}\le0$. Then $\abs{a_1+a_2z}=\abs{f(z)}/\abs z\le\abs z$ for $z\ne0$, and letting $z\to0$ gives $a_1=0$.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, $f(z)=a_2z^2$, and the bound at $z=1$ gives $\abs{a_2}\le1$. Conversely, $cz^2$ with $\abs c\le1$ satisfies the bound. So the functions are $\boxed{f(z)=cz^2,\ \abs c\le1}$.
:::
:::
