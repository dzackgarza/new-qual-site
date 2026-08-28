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
---

::: problem
23. Suppose that a field $K$ with characteristic not equal to 2 contains an primitive $n$ th root of unity for some odd integer $n$.
    Prove that $K$ must also contain a primitive $2 n$ th root of unity.
:::

::: {.solution}
**Goal.** If $K$ (char $\neq 2$) contains a primitive $n$-th root of unity for odd $n$, show it contains a primitive $2n$-th root of unity.

<1>1. Let $\zeta$ be a primitive $n$-th root of unity in $K$.
Proof: by hypothesis.

<1>2. $-\zeta$ is a primitive $2n$-th root of unity.
<2>1. $(-\zeta)^{2n} = \zeta^{2n} = (\zeta^n)^2 = 1$.
Proof: $(-1)^{2n} = 1$ and $\zeta^{2n} = 1$.
<2>2. $(-\zeta)^n = (-1)^n \zeta^n = -\zeta^n = -1 \neq 1$ (since $n$ is odd and char $\neq 2$).
Proof: $(-1)^n = -1$ for odd $n$, and $-1 \neq 1$ in char $\neq 2$.
<2>3. For any proper divisor $d$ of $2n$, $(-\zeta)^d \neq 1$.
Proof: if $d \mid n$, then $(-\zeta)^d = (-1)^d \zeta^d$; since $\zeta$ is primitive $n$-th root, $\zeta^d \neq 1$ for $d < n$; and if $d$ is even with $d \mid 2n$ but $d \nmid n$, then $d = 2e$ with $e \mid n$, and $(-\zeta)^d = \zeta^{2e} = (\zeta^e)^2$, which is $1$ only if $\zeta^e = \pm 1$, i.e. only if $e = n$ (so $d = 2n$). Hence $(-\zeta)^d \neq 1$ for all proper divisors $d$.
<2>4. Hence $-\zeta$ has order exactly $2n$, so it is a primitive $2n$-th root of unity.
Proof: the order of $-\zeta$ is $2n$.

<1>3. Q.E.D.
Proof: <1>2.4 shows $K$ contains a primitive $2n$-th root of unity.
:::
