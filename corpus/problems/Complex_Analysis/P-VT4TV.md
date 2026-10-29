---
schema: qual/card@1
id: P-VT4TV
kind: problem
title: Invert $\sin(z)$, one coefficient at a time
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
  - Trigonometry
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Find $1/\sin(z)$ using this method.", referring to the coefficient recursion stated earlier in the source; the statement now states that recursion and asks for the Laurent expansion at 0.'
---

::: {.exercise}
If $A(z) = \sum_{k \geq 0} a_k z^k$ is a power series with $a_0 \neq 0$, then $1/A(z) = \sum_{k \geq 0} b_k z^k$, where $b_0 = 1/a_0$ and $b_n = -\frac{1}{a_0}\sum_{k=1}^{n} a_k b_{n-k}$ for $n \geq 1$.
Find $1/\sin(z)$ using this method: give its Laurent expansion at $0$ through the $z^3$ term.
:::

::: {.solution}
The series of $\sin z$ has zero constant term, so factor out $z$: $\sin z = z f(z)$ with $f(z) = \sum_{k \geq 0} c_k z^k$, where $c_0 = 1$, $c_2 = -\frac{1}{3!}$, $c_4 = \frac{1}{5!}$, and $c_k = 0$ for odd $k$. Write $1/f(z) = \sum_{k \geq 0} b_k z^k$.

::: pf

::: {.pf-step #coeffs}

$b_0 = 1$, $b_1 = b_3 = 0$, $b_2 = -c_2 = \frac16$, and $b_4 = c_2^2 - c_4 = \frac{7}{360}$.

::: pf-proof

By the recursion with $c_0 = 1$: $b_0 = 1$; $b_1 = -c_1 b_0 = 0$; $b_2 = -(c_1 b_1 + c_2 b_0) = -c_2$; $b_3 = -(c_1 b_2 + c_2 b_1 + c_3 b_0) = 0$; $b_4 = -(c_1 b_3 + c_2 b_2 + c_3 b_1 + c_4 b_0) = c_2^2 - c_4 = \frac{1}{36} - \frac{1}{120} = \frac{7}{360}$.

:::

:::

::: pf-step

$\dfrac{1}{\sin z} = \boxed{\dfrac{1}{z} + \dfrac{1}{6}z + \dfrac{7}{360}z^3 + \bigo(z^5)}$.

::: pf-proof

$\frac{1}{\sin z} = \frac{1}{z}\cdot\frac{1}{f(z)}$, and step [](#coeffs){.pf-ref} gives $\frac{1}{f(z)} = 1 + \frac16 z^2 + \frac{7}{360}z^4 + \bigo(z^5)$.

:::

:::

:::

:::
