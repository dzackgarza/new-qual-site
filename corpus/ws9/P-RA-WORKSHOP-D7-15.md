---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-15
kind: problem
title: 'A series that is uniformly convergent away from zero but not near zero'
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - series-of-functions
relations: []
review: draft
---

::: {.problem title="?"}
(June 2009 #4b) Prove that the series $$x^2+\frac{x^2}{1+x^2}+\frac{x^2}{(1+x^2)^2}+\frac{x^2}{(1+x^2)^3}+\cdots$$ converges uniformly on $[a,\infty)$ for every $a>0$; but not uniformly on $[0,b]$ for any $b>0$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Prove $\sum_{k=0}^\infty \frac{x^2}{(1+x^2)^k}$ converges uniformly on $[a, \infty)$ for each $a > 0$ but not uniformly on $[0, b]$ for any $b > 0$.

<1>1. The series is geometric with ratio $1/(1+x^2)$: $\sum_{k=0}^\infty \frac{x^2}{(1+x^2)^k} = x^2 \sum_{k=0}^\infty \left(\frac{1}{1+x^2}\right)^k$.
    Proof: factor $x^2$ out of every term.

<1>2. Pointwise sum: $S(x) = \lim_N \sum_{k=0}^N \frac{x^2}{(1+x^2)^k}$ equals $1 + x^2$ for $x \neq 0$ and $0$ at $x = 0$.
    Proof: for $x \neq 0$, the ratio $1/(1+x^2) \in (0,1)$ and the geometric formula gives $x^2 \cdot \frac{1}{1 - 1/(1+x^2)} = x^2 \cdot \frac{1+x^2}{x^2} = 1 + x^2$. At $x = 0$ every term is $0$.

<1>3. The $N$-th tail is $R_N(x) := \sum_{k=N+1}^\infty \frac{x^2}{(1+x^2)^k} = \frac{1}{(1+x^2)^N}$ for $x \neq 0$, and $R_N(0) = 0$.
    Proof: geometric tail: $\frac{x^2}{(1+x^2)^{N+1}} \cdot \frac{1}{1 - 1/(1+x^2)} = \frac{x^2}{(1+x^2)^{N+1}} \cdot \frac{1+x^2}{x^2} = \frac{1}{(1+x^2)^N}$.

<1>4. Uniform convergence on $[a, \infty)$ for $a > 0$: $\sup_{x \ge a} |R_N(x)| \le \frac{1}{(1+a^2)^N} \to 0$.
    Proof: for $x \ge a$, $1 + x^2 \ge 1 + a^2$, so $R_N(x) = (1+x^2)^{-N} \le (1+a^2)^{-N}$ by <1>3; and $(1+a^2)^{-N} \to 0$ since $1 + a^2 > 1$.

<1>5. No uniform convergence on $[0, b]$ for $b > 0$: $\sup_{x \in [0,b]} |R_N(x)| = 1$ for every $N$.
    Proof: by <1>3, $R_N(0) = 0$ but $R_N(x) = (1+x^2)^{-N} \to 1$ as $x \to 0^+$; in fact $\sup_{x \in (0,b]} (1+x^2)^{-N} = 1$ (approached as $x \to 0$). So the suprema of the tails do not tend to $0$, which is exactly the negation of uniform convergence. (Equivalently, the pointwise limit $S$ of <1>2 is discontinuous at $0$ while partial sums are continuous.)

<1>6. Q.E.D.
    Proof: <1>4 and <1>5 are the two claims.

:::
