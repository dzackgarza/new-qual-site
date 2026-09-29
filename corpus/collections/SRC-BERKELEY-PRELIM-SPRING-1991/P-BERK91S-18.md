---
schema: qual/card@1
id: P-BERK91S-18
kind: problem
title: Difference quotients along monotone sequences converging from opposite sides
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f$ be real-valued on an open interval containing $a$, and suppose $f$ is differentiable at $a$. If $(x_n)$ is increasing, $(y_n)$ is decreasing, and both sequences converge to $a$, prove that
\[
\lim_{n\to\infty}
\frac{f(y_n)-f(x_n)}{y_n-x_n}
=f'(a).
\]
:::

::: {.solution}
By differentiability at $a$, there is a function $\varepsilon$ defined
near $a$, with $\varepsilon(t)\to0$ as $t\to a$, such that
$$
f(t)-f(a)
=f'(a)(t-a)+\varepsilon(t)(t-a).
$$
Set $\varepsilon(a)\coloneqq0$.

::: pf

::: {.pf-step #s1}

For every $n$,
$$
x_n\le a\le y_n.
$$

::: pf-proof

For $m\ge n$, monotonicity gives $x_n\le x_m$ and $y_m\le y_n$.
Letting $m\to\infty$ gives $x_n\le a$ and $a\le y_n$.

:::

:::

::: {.pf-step #s2}

For every $n$,
$$
\abs{
\frac{f(y_n)-f(x_n)}{y_n-x_n}-f'(a)
}
\le
\max\{\abs{\varepsilon(x_n)},\abs{\varepsilon(y_n)}\}.
$$

::: pf-proof

Using the expansion above at $x_n$ and $y_n$ gives
$$
f(y_n)-f(x_n)
=f'(a)(y_n-x_n)
+\varepsilon(y_n)(y_n-a)
+\varepsilon(x_n)(a-x_n).
$$
The quotient in the problem is defined, so $y_n\ne x_n$. By step [](#s1){.pf-ref},
$$
y_n-x_n=(y_n-a)+(a-x_n)>0,
$$
and both summands are nonnegative.
Therefore
$$
\begin{aligned}
\abs{
\frac{f(y_n)-f(x_n)}{y_n-x_n}-f'(a)
}
&\le
\frac{
\abs{\varepsilon(y_n)}(y_n-a)
+\abs{\varepsilon(x_n)}(a-x_n)
}{y_n-x_n}\\
&\le
\max\{\abs{\varepsilon(x_n)},\abs{\varepsilon(y_n)}\}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

The secant quotients converge to $f'(a)$.

::: pf-proof

Since $x_n\to a$ and $y_n\to a$,
$$
\varepsilon(x_n)\to0,
\qquad
\varepsilon(y_n)\to0.
$$
The bound in step [](#s2){.pf-ref} therefore tends to zero, so
$$
\lim_{n\to\infty}
\frac{f(y_n)-f(x_n)}{y_n-x_n}
=f'(a).
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required limit.

:::

:::

:::
