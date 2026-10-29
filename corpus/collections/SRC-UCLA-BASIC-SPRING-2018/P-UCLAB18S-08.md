---
schema: qual/card@1
id: P-UCLAB18S-08
kind: problem
title: Asymptotics of the sine iteration
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Define $x_1=1$ and $x_{n+1}=\sin x_n$.
Prove that
$$
\lim_{n\to\infty}\sqrt n\,x_n
$$
exists and compute its value.

Hint: show that $x_{n+1}^{-2}-x_n^{-2}$ converges to a constant.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The sequence $(x_n)$ is positive, strictly decreasing, and converges to $0$.


::: pf-proof

Since $x_1=1\in(0,\pi)$ and $0<\sin x<x$ for every $x\in(0,\pi)$, induction gives
$$
0<x_{n+1}<x_n\le 1
$$
for every $n$. Hence $(x_n)$ decreases to some limit $L\ge0$. By continuity of $\sin$ and the recurrence,
$$
L=\sin L.
$$
The inequality $\sin x<x$ for $x>0$ implies that the only nonnegative solution is $L=0$.

:::

:::

::: {.pf-step #s1-2}

The increments of $y_n\coloneqq x_n^{-2}$ satisfy
$$
\lim_{n\to\infty}(y_{n+1}-y_n)=\frac13.
$$


::: pf-proof

By the recurrence,
$$
y_{n+1}-y_n
=\frac1{\sin^2 x_n}-\frac1{x_n^2}.
$$
As $x\to0$, Taylor's theorem gives
$$
\sin x=x-\frac{x^3}{6}+O(x^5),
$$
so
$$
\sin^2x=x^2-\frac{x^4}{3}+O(x^6).
$$
Therefore
$$
\frac1{\sin^2x}-\frac1{x^2}
=\frac{x^2-\sin^2x}{x^2\sin^2x}
=\frac{\frac13x^4+O(x^6)}{x^4+O(x^6)}
\longrightarrow\frac13.
$$
Since $x_n\to0$ by step [](#s1-1){.pf-ref}, the asserted increment limit follows.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\lim_{n\to\infty}\frac{y_n}{n}=\frac13.
$$


::: pf-proof

For $n\ge2$,
$$
y_n
=y_1+\sum_{k=1}^{n-1}(y_{k+1}-y_k).
$$
Divide by $n$:
$$
\frac{y_n}{n}
=\frac{y_1}{n}
+\frac{n-1}{n}\left(\frac1{n-1}\sum_{k=1}^{n-1}(y_{k+1}-y_k)\right).
$$
By step [](#s1-2){.pf-ref}, the sequence of increments converges to $1/3$, so its arithmetic means also converge to $1/3$. The first term tends to $0$ and $(n-1)/n\to1$, proving the claim.

:::

:::

::: {.pf-step #s1-4}

The requested limit is
$$
\boxed{\lim_{n\to\infty}\sqrt n\,x_n=\sqrt3}.
$$


::: pf-proof

Since $x_n>0$ and $y_n=x_n^{-2}$,
$$
\sqrt n\,x_n
=\sqrt{\frac{n}{y_n}}
=\frac1{\sqrt{y_n/n}}.
$$
Step [](#s1-3){.pf-ref} gives $y_n/n\to1/3$, hence continuity of the square-root function on $(0,\infty)$ gives the stated limit.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} computes the limit and therefore proves its existence.

:::

:::

:::
