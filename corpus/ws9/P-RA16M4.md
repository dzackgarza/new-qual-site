---
schema: qual/card@1
id: P-RA16M4
kind: problem
title: 'UGA analysis qualifying exam, May 2016, problem 4'
classification:
  areas:
  - real-analysis
  topics:
  - mean-value-theorem
  - differentiation
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Suppose that $f:[0,2]\to\mathbb R$ is continuous on $[0,2]$, differentiable on $(0,2)$, and such that $f(0)=f(2)=0$ and $f(c)=1$ for some $c\in(0,2)$.
Prove that there is an $x\in(0,2)$ such that $|f'(x)|>1$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove there is $x \in (0,2)$ with $|f'(x)| > 1$, given $f$ continuous on $[0,2]$, differentiable on $(0,2)$, $f(0) = f(2) = 0$, $f(c) = 1$ for some $c \in (0,2)$.

<1>1. If $c > 1$: the MVT on $[c, 2]$ gives $x_2 \in (c,2)$ with $f'(x_2) = \frac{f(2) - f(c)}{2 - c} = \frac{-1}{2-c}$.
Proof: $f$ is continuous on $[c,2]$ and differentiable on $(c,2)$, so the Mean Value Theorem applies.
Since $c > 1$, $2 - c < 1$, so $|f'(x_2)| = \frac{1}{2-c} > 1$.

<1>2. If $c < 1$: the MVT on $[0, c]$ gives $x_1 \in (0,c)$ with $f'(x_1) = \frac{f(c) - f(0)}{c - 0} = \frac1c$.
Proof: $c < 1$ gives $1/c > 1$, so $|f'(x_1)| > 1$.

<1>3. If $c = 1$: assume for contradiction $|f'(x)| \le 1$ for all $x \in (0,2)$.
<2>1. $f(x) \le x$ for all $x \in [0,1]$.
Proof: MVT on $[0,x]$: $f(x) = f(x) - f(0) = f'(\xi)x \le x$ since $|f'| \le 1$.
<2>2. $f(x) \le 2 - x$ for all $x \in [1,2]$.
Proof: MVT on $[x, 2]$: $f(2) - f(x) = f'(\eta)(2-x)$, so $f(x) = -f'(\eta)(2-x) \le 2 - x$ since $|f'(\eta)| \le 1$.
<2>3. $f \le t$ pointwise where $t(x) = \min(x, 2-x)$ is the tent function, and $f(1) = 1 = t(1)$.
Proof: <2>1, <2>2, and $f(1) = 1$; $t(1) = \min(1, 1) = 1$.
<2>4. The left derivative of $f$ at $1$ satisfies $f'(1) \ge 1$.
Proof: for $x < 1$, $f(x) \le x = t(x)$ and $f(1) = t(1) = 1$, so $f(x) - f(1) \le x - 1$; dividing by the negative $x - 1$ reverses: $\frac{f(x) - f(1)}{x-1} \ge 1$; take $x \to 1^-$ (the limit is $f'(1)$ by differentiability).
<2>5. The right derivative of $f$ at $1$ satisfies $f'(1) \le -1$.
Proof: for $x > 1$, $f(x) \le 2 - x = t(x)$ and $f(1) = 1$, so $f(x) - f(1) \le (2-x) - 1 = -(x-1)$; dividing by $x - 1 > 0$: $\frac{f(x)-f(1)}{x-1} \le -1$; take $x \to 1^+$.
<2>6. Contradiction: $f'(1) \ge 1$ and $f'(1) \le -1$.
Proof: <2>4 and <2>5 give incompatible bounds on the same value $f'(1)$ (which exists since $f$ is differentiable on $(0,2)$). Hence $|f'| \le 1$ is impossible: some $x$ has $|f'(x)| > 1$.

<1>4. Q.E.D. Proof: <1>1 covers $c > 1$, <1>2 covers $c < 1$, and <1>3 covers $c = 1$; all cases yield the claim.
:::
