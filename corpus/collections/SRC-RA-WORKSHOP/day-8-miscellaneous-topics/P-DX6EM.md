---
schema: qual/card@1
id: P-DX6EM
kind: problem
title: A function of bounded variation is the difference of two increasing functions
classification:
  areas:
  - real-analysis
  topics:
  - Variation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $f \colon [a,b] \to \mathbb{R}$.
Suppose $f \in \text{BV}[a,b]$.
Prove $f$ is the difference of two increasing functions.
:::
::: {.solution}

::: pf

::: pf-step

Define the total variation $V(x) = \sup \sum_{i=1}^n |f(x_i) - f(x_{i-1})|$ over all partitions $a = x_0 < \cdots < x_n = x$ of $[a, x]$, for $a \le x \le b$.

::: pf-proof

For $x>a$, take the supremum over finite partitions of $[a,x]$; define $V(a)=0$ using the trivial partition. Every such partition extends to one of $[a,b]$ when $x<b$, so $0\le V(x)\le V(b)<\infty$ by bounded variation.

:::

:::

::: pf-step

$V$ is increasing on $[a,b]$: for $a \le x < y \le b$, $V(y) \ge V(x)$.

::: pf-proof

For any partition of $[a,x]$, append $y$. The resulting variation sum is the original sum plus $|f(y)-f(x)|\ge0$. Taking the supremum over partitions of $[a,x]$ proves $V(y)\ge V(x)$.

:::

:::

::: {.pf-step #s3}

$V + f$ and $V - f$ are increasing on $[a,b]$.

::: pf-proof

::: {.pf-step #s3-1}

For $a \le x < y \le b$: $V(y) - V(x) \ge |f(y) - f(x)|$.

::: pf-proof

Fix $\varepsilon>0$ and choose a partition of $[a,x]$ whose variation sum exceeds $V(x)-\varepsilon$. Appending $y$ produces a partition of $[a,y]$ with variation sum exceeding $V(x)-\varepsilon+|f(y)-f(x)|$. Thus $V(y)\ge V(x)-\varepsilon+|f(y)-f(x)|$. Letting $\varepsilon\downarrow0$ gives the assertion.

:::

:::

::: {.pf-step #s3-2}

$(V + f)(y) - (V + f)(x) = (V(y) - V(x)) + (f(y) - f(x)) \ge |f(y)-f(x)| + (f(y)-f(x)) \ge 0$.

::: pf-proof

Set $u=f(y)-f(x)$. Step [](#s3-1){.pf-ref} gives $V(y)-V(x)\ge|u|$, so the increment of $V+f$ is at least $|u|+u\ge0$.

:::

:::

::: {.pf-step #s3-3}

$(V - f)(y) - (V - f)(x) = (V(y) - V(x)) - (f(y) - f(x)) \ge |f(y)-f(x)| - (f(y)-f(x)) \ge 0$.

::: pf-proof

With the same $u$, step [](#s3-1){.pf-ref} gives an increment of $V-f$ at least $|u|-u\ge0$.

:::

:::

::: pf-qed

Steps [](#s3-2){.pf-ref} and [](#s3-3){.pf-ref} prove that both functions have nonnegative increments for every $x<y$.

:::

:::

:::

::: {.pf-step #s4}

The functions $g=(V+f)/2$ and $h=(V-f)/2$ are increasing and satisfy $\boxed{f=g-h}$.

::: pf-proof

Step [](#s3){.pf-ref} gives monotonicity of $V+f$ and $V-f$, preserved by multiplication by $1/2>0$. Subtracting the definitions gives $g-h=f$ pointwise.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} constructs the required difference of increasing functions.

:::

:::

:::
