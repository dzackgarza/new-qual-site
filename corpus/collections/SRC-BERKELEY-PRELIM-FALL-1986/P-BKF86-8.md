---
schema: qual/card@1
id: P-BKF86-8
kind: problem
title: A continuous function with nonnegative upper right Dini derivative is nondecreasing
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
---

::: {.problem}
Let $f$ be a continuous real-valued function on $[0,1]$ such that, for each $x_0\in[0,1)$,
\[
\limsup_{x\to x_0^+}\frac{f(x)-f(x_0)}{x-x_0}\ge 0.
\]
Prove that $f$ is nondecreasing.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that there exist $0\leq a<b\leq1$ such that
$$
f(a)>f(b).
$$

::: {.proof}
This is precisely the negation of the assertion that $f$ is nondecreasing.
:::

<1>2. There is an $\varepsilon>0$ such that the continuous function
$$
g(x)=f(x)+\varepsilon x
$$
satisfies $g(a)>g(b)$ and
$$
\limsup_{x\to x_0^+}\frac{g(x)-g(x_0)}{x-x_0}\geq\varepsilon>0
$$
for every $x_0\in[0,1)$.

::: {.proof}
By step <1>1,
$$
\frac{f(a)-f(b)}{b-a}>0.
$$
Choose
$$
0<\varepsilon<\frac{f(a)-f(b)}{b-a}.
$$
Then
$$
g(a)-g(b)
=f(a)-f(b)-\varepsilon(b-a)>0.
$$
For every $x_0\in[0,1)$,
$$
\frac{g(x)-g(x_0)}{x-x_0}
=
\frac{f(x)-f(x_0)}{x-x_0}+\varepsilon.
$$
Taking the upper limit as $x\to x_0^+$ and using the hypothesis on $f$ gives
$$
\limsup_{x\to x_0^+}\frac{g(x)-g(x_0)}{x-x_0}
=
\limsup_{x\to x_0^+}\frac{f(x)-f(x_0)}{x-x_0}+\varepsilon
\geq\varepsilon>0.
$$
:::

<1>3. The function $g$ has a point $c\in[a,b)$ such that
$$
\limsup_{x\to c^+}\frac{g(x)-g(c)}{x-c}\leq0.
$$

::: {.proof}
Since $g$ is continuous, it attains a maximum on the compact interval $[a,b]$. Let $c$ be a point where this maximum is attained. Step <1>2 gives $g(a)>g(b)$, so $c\neq b$ and hence $c\in[a,b)$.

For every $x\in(c,b]$,
$$
g(x)\leq g(c).
$$
Thus
$$
\frac{g(x)-g(c)}{x-c}\leq0
$$
for all $x>c$ sufficiently close to $c$. Taking the upper limit proves the claim.
:::

<1>4. The assumption in step <1>1 is impossible.

::: {.proof}
Since $c<b\leq1$, one has $c\in[0,1)$. Step <1>2 applied at $x_0=c$ gives
$$
\limsup_{x\to c^+}\frac{g(x)-g(c)}{x-c}\geq\varepsilon>0,
$$
contradicting step <1>3.
:::

<1>5. The function $f$ is nondecreasing on $[0,1]$.

::: {.proof}
By step <1>4, there do not exist $a<b$ with $f(a)>f(b)$. Hence for every $a<b$ in $[0,1]$ one has $f(a)\leq f(b)$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
