---
schema: qual/card@1
id: P-BKS00-5
kind: problem
title: Convergence of the Babylonian iteration for $\sqrt a$
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
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Positivity is preserved, AM-GM puts every x_n with n at least 1
    above sqrt(a), and the recurrence is then decreasing. The positive
    fixed-point equation gives the limit sqrt(a).
---

::: {.problem}
Let $a>0$ and $x_0>0$. Define recursively
\[
x_n=\frac12\left(x_{n-1}+\frac{a}{x_{n-1}}\right),
\qquad n\ge1.
\]
Prove that $(x_n)$ converges, and find its limit.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every term $x_n$ is positive.

::: pf-proof

The initial value $x_0$ is positive. If $x_{n-1}>0$, then
$$
x_n
=
\frac12\left(x_{n-1}+\frac{a}{x_{n-1}}\right)
>0,
$$
because $a>0$. Induction gives $x_n>0$ for every $n\geq0$.

:::

:::

::: {.pf-step #s2}

For every $n\geq1$,
$$
x_n\geq\sqrt a.
$$

::: pf-proof

By step [](#s1){.pf-ref}, $x_{n-1}>0$. The arithmetic-geometric mean inequality
therefore gives
$$
x_n
=
\frac12\left(x_{n-1}+\frac{a}{x_{n-1}}\right)
\geq
\sqrt{x_{n-1}\frac{a}{x_{n-1}}}
=
\sqrt a.
$$

:::

:::

::: {.pf-step #s3}

The tail $(x_n)_{n\geq1}$ is nonincreasing and bounded below,
so $(x_n)$ converges.

::: pf-proof

For $n\geq1$, step [](#s2){.pf-ref} gives $x_n^2\geq a$. Hence
$$
\begin{aligned}
x_{n+1}-x_n
&=
\frac12\left(x_n+\frac{a}{x_n}\right)-x_n\\
&=
\frac{a-x_n^2}{2x_n}
\leq
0,
\end{aligned}
$$
where the denominator is positive by step [](#s1){.pf-ref}. Thus the tail is
nonincreasing. Step [](#s2){.pf-ref} bounds it below by $\sqrt a$, so the monotone
convergence theorem for real sequences gives a limit
$$
L=\lim_{n\to\infty}x_n
$$
with $L\geq\sqrt a>0$.

:::

:::

::: {.pf-step #s4}

The limit is
$$
\boxed{L=\sqrt a}.
$$

::: pf-proof

Letting $n\to\infty$ in the defining recurrence, with $x_n\to L$ by
step [](#s3){.pf-ref}, gives
$$
L
=
\frac12\left(L+\frac{a}{L}\right),
$$
because $L>0$. Therefore
$$
2L^2=L^2+a,
$$
so $L^2=a$. Since $L>0$, it follows that $L=\sqrt a$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves convergence, and step [](#s4){.pf-ref} gives the requested limit.

:::

:::

:::
