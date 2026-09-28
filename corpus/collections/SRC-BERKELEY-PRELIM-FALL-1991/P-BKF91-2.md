---
schema: qual/card@1
id: P-BKF91-2
kind: problem
title: A continuous distance-expanding map $\mathbb R\to\mathbb R$ is surjective
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Used the expansion inequality to obtain injectivity and endpoint growth,
    then strict monotonicity and the intermediate value theorem to prove
    surjectivity.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and suppose
\[
|f(x)-f(y)|\ge |x-y|
\]
for all $x,y\in\mathbb R$. Prove that the range of $f$ is all of $\mathbb R$.
:::

::: {.solution}
<1>1. The function $f$ is injective.

::: {.proof}
If $x\ne y$, then
$$
\abs{x-y}>0.
$$
The hypothesis gives
$$
\abs{f(x)-f(y)}\ge\abs{x-y}>0,
$$
so $f(x)\ne f(y)$.
:::

<1>2. The function $f$ is either strictly increasing or strictly decreasing.

::: {.proof}
A continuous injective real-valued function on an interval is strictly monotone. Apply this standard theorem to the interval $\RR$ using step <1>1.
:::

<1>3. If $f$ is strictly increasing, then
$$
\lim_{x\to\infty}f(x)=\infty,
\qquad
\lim_{x\to-\infty}f(x)=-\infty.
$$

::: {.proof}
For $x>0$, monotonicity gives $f(x)>f(0)$, so the hypothesis with $y=0$ yields
$$
f(x)-f(0)=\abs{f(x)-f(0)}\ge x.
$$
Thus $f(x)\ge f(0)+x\to\infty$.

For $x<0$, monotonicity gives $f(x)<f(0)$, so
$$
f(0)-f(x)=\abs{f(x)-f(0)}\ge -x.
$$
Hence $f(x)\le f(0)+x\to-\infty$ as $x\to-\infty$.
:::

<1>4. If $f$ is strictly decreasing, then
$$
\lim_{x\to\infty}f(x)=-\infty,
\qquad
\lim_{x\to-\infty}f(x)=\infty.
$$

::: {.proof}
For $x>0$, one has $f(x)<f(0)$, and therefore
$$
f(0)-f(x)=\abs{f(x)-f(0)}\ge x,
$$
so $f(x)\le f(0)-x\to-\infty$.

For $x<0$, one has $f(x)>f(0)$, and hence
$$
f(x)-f(0)=\abs{f(x)-f(0)}\ge -x,
$$
so $f(x)\ge f(0)-x\to\infty$ as $x\to-\infty$.
:::

<1>5. The range of $f$ is all of $\RR$.

::: {.proof}
Let $y\in\RR$. In either monotonicity case, steps <1>3 and <1>4 show that there exist $a<b$ such that $y$ lies between $f(a)$ and $f(b)$. Since $f$ is continuous, the intermediate value theorem gives $c\in[a,b]$ with
$$
f(c)=y.
$$
Thus every real number lies in the range of $f$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves that $f(\RR)=\RR$.
:::
:::
