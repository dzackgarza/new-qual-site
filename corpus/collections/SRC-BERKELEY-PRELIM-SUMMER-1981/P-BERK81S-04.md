---
schema: qual/card@1
id: P-BERK81S-04
kind: problem
title: An integrable continuous function is $o(1/x)$ along a symmetric sequence
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
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Set h(x)=|f(x)|+|f(-x)| on [0,infinity). This h is integrable. For each
    n there must be x_n>=n with x_n h(x_n)<1/n; otherwise
    h(x)>=1/(nx) for every x>=n and the integral of h would diverge
    logarithmically. The same bound then forces both
    x_n f(x_n) and x_n f(-x_n) to tend to zero.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and suppose
\[
\int_{-\infty}^{\infty}|f(x)|\,dx<\infty.
\]
Show that there is a sequence $x_n\to\infty$ such that
\[
x_nf(x_n)\to0
\qquad\text{and}\qquad
x_nf(-x_n)\to0.
\]
:::

::: {.solution}
For $x\geq0$, define
$$
h(x)=\abs{f(x)}+\abs{f(-x)}.
$$

::: pf

::: {.pf-step #s1}

The function $h$ is integrable on $[0,\infty)$:
$$
\int_0^\infty h(x)\,dx<\infty.
$$

::: pf-proof

One has
$$
\begin{aligned}
\int_0^\infty h(x)\,dx
&=
\int_0^\infty\abs{f(x)}\,dx
+
\int_0^\infty\abs{f(-x)}\,dx\\
&=
\int_0^\infty\abs{f(x)}\,dx
+
\int_{-\infty}^0\abs{f(u)}\,du\\
&=
\int_{-\infty}^{\infty}\abs{f(u)}\,du,
\end{aligned}
$$
where the second integral uses the substitution $u=-x$. The final
quantity is finite by hypothesis.

:::

:::

::: {.pf-step #s2}

For every integer $n\geq1$, there exists $x_n\geq n$ such that
$$
x_nh(x_n)<\frac1n.
$$

::: pf-proof

Suppose no such $x_n$ existed for some fixed $n$. Then
$$
x h(x)\geq\frac1n
$$
for every $x\geq n$, so
$$
h(x)\geq\frac1{nx}
$$
for every $x\geq n$. Hence
$$
\int_n^\infty h(x)\,dx
\geq
\frac1n
\int_n^\infty\frac{dx}{x}
=
\infty,
$$
contradicting step [](#s1){.pf-ref}. Therefore such an $x_n$ exists.

:::

:::

::: {.pf-step #s3}

The sequence from step [](#s2){.pf-ref} satisfies
$$
x_n\longrightarrow\infty.
$$

::: pf-proof

By construction,
$$
x_n\geq n.
$$
Since $n\to\infty$, the same is true of $x_n$.

:::

:::

::: {.pf-step #s4}

One has
$$
x_n\abs{f(x_n)}
\longrightarrow0.
$$

::: pf-proof

By the definition of $h$,
$$
\abs{f(x_n)}
\leq
h(x_n).
$$
Therefore step [](#s2){.pf-ref} gives
$$
0
\leq
x_n\abs{f(x_n)}
\leq
x_nh(x_n)
<
\frac1n.
$$
The squeeze theorem gives the limit.

:::

:::

::: {.pf-step #s5}

One also has
$$
x_n\abs{f(-x_n)}
\longrightarrow0.
$$

::: pf-proof

Again,
$$
\abs{f(-x_n)}
\leq
h(x_n).
$$
Thus
$$
0
\leq
x_n\abs{f(-x_n)}
\leq
x_nh(x_n)
<
\frac1n,
$$
and the squeeze theorem applies.

:::

:::

::: {.pf-step #s6}

Consequently,
$$
\boxed{
x_nf(x_n)\to0
\qquad\text{and}\qquad
x_nf(-x_n)\to0.
}
$$

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} show convergence of the absolute values of the two
displayed expressions to zero, which implies convergence of the
expressions themselves to zero.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s6){.pf-ref} give all required properties of the sequence.

:::

:::

:::
