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

<1>1. The function $h$ is integrable on $[0,\infty)$:
$$
\int_0^\infty h(x)\,dx<\infty.
$$

::: {.proof}
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

<1>2. For every integer $n\geq1$, there exists $x_n\geq n$ such that
$$
x_nh(x_n)<\frac1n.
$$

::: {.proof}
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
contradicting step <1>1. Therefore such an $x_n$ exists.
:::

<1>3. The sequence from step <1>2 satisfies
$$
x_n\longrightarrow\infty.
$$

::: {.proof}
By construction,
$$
x_n\geq n.
$$
Since $n\to\infty$, the same is true of $x_n$.
:::

<1>4. One has
$$
x_n\abs{f(x_n)}
\longrightarrow0.
$$

::: {.proof}
By the definition of $h$,
$$
\abs{f(x_n)}
\leq
h(x_n).
$$
Therefore step <1>2 gives
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

<1>5. One also has
$$
x_n\abs{f(-x_n)}
\longrightarrow0.
$$

::: {.proof}
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

<1>6. Consequently,
$$
\boxed{
x_nf(x_n)\to0
\qquad\text{and}\qquad
x_nf(-x_n)\to0.
}
$$

::: {.proof}
Steps <1>4--<1>5 show convergence of the absolute values of the two
displayed expressions to zero, which implies convergence of the
expressions themselves to zero.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>3 and <1>6 give all required properties of the sequence.
:::
:::
