---
schema: qual/card@1
id: P-AITX4
kind: problem
title: Convergence of integrals of $f(x^n)$ to $f(0)$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
If $f:[0,1]\to\mathbb{R}$ is continuous, prove that $$\displaystyle\lim_{n\to\infty}\int_0^1 f(x^n)\,dx=f(0).$$
:::

::: {.solution}
<1>1. $f(x^n) \to f(0)$ pointwise for every $x \in [0,1)$.

::: {.proof}
For each $x\in[0,1)$, the sequence $x^n$ converges to zero. Continuity of $f$ at zero implies $f(x^n)\to f(0)$.
:::

<1>2. For every $\varepsilon>0$ there exist $r\in(0,1)$ and $N\in\mathbb N$ such that $|f(x^n)-f(0)|<\varepsilon/2$ for every $x\in[0,r]$ and $n\ge N$.

::: {.proof}
Continuity at zero supplies $\eta>0$ such that $|f(t)-f(0)|<\varepsilon/2$ whenever $t\in[0,1]$ and $t<\eta$. Fix any $r\in(0,1)$. Choose $N$ so that $r^n<\eta$ for all $n\ge N$. Then $0\le x^n\le r^n<\eta$ whenever $x\in[0,r]$.
:::

<1>3. The integrals converge to $\boxed{f(0)}$.

::: {.proof}
Set $B=\max\{1,\|f\|_\infty\}$. Given $\varepsilon>0$, choose $r\in(0,1)$ sufficiently close to one that $2B(1-r)<\varepsilon/2$, then choose $N$ as in step <1>2 for this $r$. For $n\ge N$, additivity and the absolute integral bound give
\[
\begin{aligned}
\left|\int_0^1 f(x^n)\,dx-f(0)\right|
&\leq\int_0^r|f(x^n)-f(0)|\,dx
+\int_r^1|f(x^n)-f(0)|\,dx\\
&\leq r\frac{\varepsilon}{2}+2B(1-r)<\varepsilon.
\end{aligned}
\]
All integrands are continuous, so these are ordinary Riemann integrals.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 establishes the asserted limit.
:::
:::
