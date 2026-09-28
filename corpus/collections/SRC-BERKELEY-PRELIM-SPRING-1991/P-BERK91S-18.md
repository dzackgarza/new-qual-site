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

<1>1. For every $n$,
$$
x_n<a<y_n.
$$

::: {.proof}
An increasing sequence converging to $a$ cannot have a term at least
$a$: if $x_n\ge a$, strict increase would give $x_{n+1}>a$, contrary
to convergence to $a$. Thus $x_n<a$. The same argument applied to the
decreasing sequence $(y_n)$ gives $y_n>a$.
:::

<1>2. For every $n$,
$$
\abs{
\frac{f(y_n)-f(x_n)}{y_n-x_n}-f'(a)
}
\le
\max\{\abs{\varepsilon(x_n)},\abs{\varepsilon(y_n)}\}.
$$

::: {.proof}
Using the expansion above at $x_n$ and $y_n$ gives
$$
f(y_n)-f(x_n)
=f'(a)(y_n-x_n)
+\varepsilon(y_n)(y_n-a)
+\varepsilon(x_n)(a-x_n).
$$
By step <1>1,
$$
y_n-x_n=(y_n-a)+(a-x_n)>0.
$$
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

<1>3. The secant quotients converge to $f'(a)$.

::: {.proof}
Since $x_n\to a$ and $y_n\to a$,
$$
\varepsilon(x_n)\to0,
\qquad
\varepsilon(y_n)\to0.
$$
The bound in step <1>2 therefore tends to zero, so
$$
\lim_{n\to\infty}
\frac{f(y_n)-f(x_n)}{y_n-x_n}
=f'(a).
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required limit.
:::
:::
