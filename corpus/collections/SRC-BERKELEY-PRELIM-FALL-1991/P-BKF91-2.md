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

::: pf

::: {.pf-step #s1}

The function $f$ is injective.

::: pf-proof

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

:::

::: pf-step

The function $f$ is either strictly increasing or strictly decreasing.

::: pf-proof

A continuous injective real-valued function on an interval is strictly monotone. Apply this standard theorem to the interval $\RR$ using step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

If $f$ is strictly increasing, then
$$
\lim_{x\to\infty}f(x)=\infty,
\qquad
\lim_{x\to-\infty}f(x)=-\infty.
$$

::: pf-proof

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

:::

::: {.pf-step #s4}

If $f$ is strictly decreasing, then
$$
\lim_{x\to\infty}f(x)=-\infty,
\qquad
\lim_{x\to-\infty}f(x)=\infty.
$$

::: pf-proof

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

:::

::: {.pf-step #s5}

The range of $f$ is all of $\RR$.

::: pf-proof

Let $y\in\RR$. In either monotonicity case, steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that there exist $a<b$ such that $y$ lies between $f(a)$ and $f(b)$. Since $f$ is continuous, the intermediate value theorem gives $c\in[a,b]$ with
$$
f(c)=y.
$$
Thus every real number lies in the range of $f$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves that $f(\RR)=\RR$.

:::

:::

:::
