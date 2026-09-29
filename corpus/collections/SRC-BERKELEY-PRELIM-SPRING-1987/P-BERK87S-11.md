---
schema: qual/card@1
id: P-BERK87S-11
kind: problem
title: The equation $ae^x=1+x+x^2/2$ has exactly one real root
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
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Rewrote the equation as g(x)=a for
    g(x)=e^{-x}(1+x+x^2/2). Its derivative is
    -(x^2/2)e^{-x}; integrating this derivative on any nontrivial interval
    gives strict decrease, while g tends to infinity at negative infinity
    and to zero at positive infinity.
---

::: {.problem}
Let $a>0$. Show that
\[
ae^x=1+x+\frac{x^2}{2}
\]
has exactly one real solution.
:::

::: {.solution}
Define
$$
g(x)\coloneqq e^{-x}\left(1+x+\frac{x^2}{2}\right).
$$
The given equation is equivalent to $g(x)=a$.

::: pf

::: {.pf-step #g-prime-formula}
For every $x\in\RR$,
$$
g'(x)=-\frac{x^2}{2}e^{-x}.
$$

::: pf-proof
Differentiating gives
$$
\begin{aligned}
g'(x)
&=e^{-x}(1+x)-e^{-x}\left(1+x+\frac{x^2}{2}\right)\\
&=-\frac{x^2}{2}e^{-x}.
\end{aligned}
$$
:::

:::

::: {.pf-step #g-strictly-decreasing}
The function $g$ is strictly decreasing on $\RR$.

::: pf-proof
If $x<y$, the fundamental theorem of calculus and step [](#g-prime-formula){.pf-ref} give
$$
g(y)-g(x)
=
-\frac12\int_x^y t^2e^{-t}\,dt.
$$
The integrand $t^2e^{-t}$ is nonnegative and is positive except at
$t=0$. Hence its integral over every nontrivial interval is strictly
positive, so $g(y)-g(x)<0$.
:::

:::

::: {.pf-step #g-endpoint-limits}
The endpoint limits of $g$ are
$$
\lim_{x\to-\infty}g(x)=+\infty,
\qquad
\lim_{x\to+\infty}g(x)=0.
$$

::: pf-proof
Since
$$
1+x+\frac{x^2}{2}
=
\frac{(x+1)^2+1}{2}
\geq
\frac12,
$$
we have $g(x)\geq \frac12e^{-x}$, which tends to $+\infty$ as
$x\to-\infty$.

As $x\to+\infty$, each of $e^{-x}$, $xe^{-x}$, and $x^2e^{-x}$ tends
to $0$, so $g(x)\to0$.
:::

:::

::: {.pf-step #unique-solution}
For every $a>0$, there exists exactly one $x\in\RR$ such that
$$
g(x)=a.
$$

::: pf-proof
By step [](#g-endpoint-limits){.pf-ref}, there exist real numbers $u<v$ with
$$
g(u)>a>g(v).
$$
The function $g$ is continuous, so the intermediate value theorem gives
some $x\in(u,v)$ with $g(x)=a$. Step [](#g-strictly-decreasing){.pf-ref} shows that $g$ is strictly
decreasing, so two distinct points cannot have the same value. Thus this
solution is unique.
:::

:::

::: pf-qed
The original equation is equivalent to $g(x)=a$, and step [](#unique-solution){.pf-ref} proves
that the latter equation has exactly one real solution.
:::

:::
:::
