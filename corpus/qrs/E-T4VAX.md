---
schema: qual/card@1
id: E-T4VAX
kind: exercise
title: $z^5+3z+1$ has five zeros in $|z|\leq 2$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

::: {.exercise}
Show that $h(z) =z^5 + 3z + 1$ has 5 zeros in $\abs z \leq 2$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that $h(z) = z^5 + 3z + 1$ has exactly 5 zeros in $\abs{z} \le 2$.

<1>1. Setup: write $h = f + g$ with $f(z) = z^5$ and $g(z) = 3z + 1$.
Proof: $h(z) = z^5 + 3z + 1$.

<1>2. On $\abs{z} = 2$: $\abs{g(z)} < \abs{f(z)}$.
Proof: $\abs{g(z)} \le 3\abs{z} + 1 = 7$ on $\abs{z} = 2$, while $\abs{f(z)} = \abs{z}^5 = 32$.
Since $7 < 32$, the strict inequality holds everywhere on the circle.

<1>3. $h$ and $f$ have the same number of zeros inside $\abs{z} < 2$.
Proof: Rouch\'e's theorem with $f(z) = z^5$, $g(z) = 3z+1$, $\gamma = \abs{z}=2$, using <1>2.

<1>4. $f(z) = z^5$ has exactly 5 zeros in $\abs{z} < 2$ (counting multiplicity).
Proof: The only zero is $z = 0$ with multiplicity 5, and $0$ lies in the disk.

<1>5. Q.E.D. Proof: <1>3 and <1>4 give that $h$ has exactly $5$ zeros in $\abs{z} < 2$, hence in $\abs{z} \le 2$.
:::
