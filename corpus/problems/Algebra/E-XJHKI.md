---
schema: qual/card@1
id: E-XJHKI
kind: problem
title: Primitive odd $n$th root of unity implies a primitive $2n$th root of unity
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Fields
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the order argument directly instead of a divisor case split.
---

::: {.exercise}
Suppose $K$ has characteristic different from $2$ and contains a primitive $n$th root of unity for odd $n$. Prove that $K$ contains a primitive $2n$th root of unity.
:::

::: {.solution}
Let $\zeta\in K$ have order $n$, with $n$ odd. We claim that $-\zeta$ has order $2n$.

Certainly
\[
(-\zeta)^{2n}=1.
\]
Suppose $(-\zeta)^m=1$. Then
\[
\zeta^m=(-1)^m.
\]
If $m$ is odd, this says that the odd-order group $\langle\zeta\rangle$ contains $-1$, an element of order $2$, impossible because $\operatorname{char}K\ne2$. Hence $m$ is even. Then $\zeta^m=1$, so $n\mid m$. Since $n$ is odd and $m$ is even, $2n\mid m$.

Thus the least positive exponent annihilating $-\zeta$ is $2n$, so $-\zeta$ is a primitive $2n$th root of unity in $K$.
:::
