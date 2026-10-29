---
schema: qual/card@1
id: P-TCB4X
kind: problem
title: Quadratic extensions in characteristic not $2$ are Galois
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Show that any quadratic extension of a field $F$ with $\ch(F)\neq 2$ is Galois.
:::

::: {.solution}
Let $K/F$ be a quadratic extension with $\ch(F)\ne2$.

::: pf

::: {.pf-step #pure}
$K=F(\beta)$ for some $\beta\in K\setminus F$ with $d\coloneqq\beta^2\in F$, and the minimal polynomial of $\beta$ over $F$ is $x^2-d$.

::: pf-proof
Choose $\alpha\in K\setminus F$. Since $[K:F]=2$, $K=F(\alpha)$ and the minimal polynomial of $\alpha$ is some $x^2+bx+c\in F[x]$.
Since $2$ is invertible in $F$, put $\beta=\alpha+b/2$. Then $K=F(\beta)$, $\beta\notin F$, and
$$
\beta^2=\alpha^2+b\alpha+\frac{b^2}{4}=\frac{b^2-4c}{4}\in F.
$$
So $\beta$ is a root of $x^2-d$, which is its minimal polynomial because $\beta\notin F$.
:::

:::

::: {.pf-step #normal}
$K/F$ is normal.

::: pf-proof
The roots of $x^2-d$ are $\beta$ and $-\beta$, both in $K$, so by step [](#pure){.pf-ref} $K$ is the splitting field of $x^2-d$ over $F$.
:::

:::

::: {.pf-step #separable}
$K/F$ is separable.

::: pf-proof
Since $\ch(F)\ne2$ and $\beta\ne0$, the roots $\beta$ and $-\beta$ are distinct, so the minimal polynomial $x^2-d$ of the generator $\beta$ is separable.
:::

:::

::: pf-step
$K/F$ is Galois.

::: pf-proof
A finite extension that is normal and separable is Galois; apply step [](#normal){.pf-ref} and step [](#separable){.pf-ref}.
:::

:::

:::

:::
