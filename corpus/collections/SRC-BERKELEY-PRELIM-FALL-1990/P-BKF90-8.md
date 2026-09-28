---
schema: qual/card@1
id: P-BKF90-8
kind: problem
title: $\frac1n\int_0^nxf(x)\,dx\to0$ for integrable continuous $f\ge0$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 in the deterministic MinerU Flash extraction assets/attachments/Fall90_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Split the weighted integral at a fixed tail cutoff, controlled the compact
    part by 1/n, and bounded the tail using x/n <= 1.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous, nonnegative, and satisfy
\[
\int_0^\infty f(x)\,dx<\infty.
\]
Prove that
\[
\frac1n\int_0^n x f(x)\,dx\longrightarrow0
\qquad(n\to\infty).
\]
:::

::: {.solution}
<1>1. For every $\varepsilon>0$, there exists $A>0$ such that
$$
\int_A^\infty f(x)\,dx<\frac{\varepsilon}{2}.
$$

::: {.proof}
Because $f\ge0$ and
$$
\int_0^\infty f(x)\,dx<\infty,
$$
the tails of this improper integral tend to $0$.
:::

<1>2. For the number $A$ from step <1>1, put
$$
C\coloneqq\int_0^A x f(x)\,dx.
$$
Then $C$ is finite.

::: {.proof}
The function $x\mapsto xf(x)$ is continuous on the compact interval $[0,A]$, so its integral there is finite.
:::

<1>3. If $n\ge A$, then
$$
0\le
\frac1n\int_0^n xf(x)\,dx
\le
\frac Cn+\int_A^\infty f(x)\,dx.
$$

::: {.proof}
Since $f\ge0$,
$$
\begin{aligned}
\frac1n\int_0^n xf(x)\,dx
&=\frac1n\int_0^A xf(x)\,dx
 +\frac1n\int_A^n xf(x)\,dx\\
&=\frac Cn+\int_A^n\frac{x}{n}f(x)\,dx.
\end{aligned}
$$
For $A\le x\le n$, one has $0\le x/n\le1$. Hence
$$
\int_A^n\frac{x}{n}f(x)\,dx
\le
\int_A^n f(x)\,dx
\le
\int_A^\infty f(x)\,dx.
$$
:::

<1>4. For all sufficiently large $n$,
$$
0\le
\frac1n\int_0^n xf(x)\,dx
<\varepsilon.
$$

::: {.proof}
Choose $n\ge A$ so large that
$$
\frac Cn<\frac{\varepsilon}{2}.
$$
Then steps <1>1 and <1>3 give
$$
0\le
\frac1n\int_0^n xf(x)\,dx
<
\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
=\varepsilon.
$$
:::

<1>5. Therefore
$$
\boxed{\lim_{n\to\infty}\frac1n\int_0^n xf(x)\,dx=0}.
$$

::: {.proof}
Step <1>4 is the $\varepsilon$-criterion for convergence to $0$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
