---
schema: qual/card@1
id: P-BKF00-5
kind: problem
title: Does a finite limit of $f(x)/x^2$ force $f''(0)$ to exist?
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    The counterexample x^3 sin(1/x) has f(x)/x^2 tending to 0, while the
    difference quotient for f' at 0 oscillates between subsequential limits.
---

::: {.problem}
Let $f:(-1,1)\to\mathbb R$ be differentiable and suppose
\[
\lim_{x\to0}\frac{f(x)}{x^2}
\]
exists and is finite. Must $f''(0)$ exist? Give a proof or a counterexample.
:::

::: {.solution}
<1>1. Define $f:(-1,1)\to\RR$ by
$$
f(x)=
\begin{cases}
x^3\sin(1/x),&x\neq0,\\
0,&x=0.
\end{cases}
$$
Then $f$ is differentiable on $(-1,1)$, with $f'(0)=0$ and
$$
f'(x)=3x^2\sin(1/x)-x\cos(1/x)
$$
for $x\neq0$.

::: {.proof}
For $x\neq0$, the displayed derivative follows from the product and chain
rules. At $0$,
$$
\frac{f(h)-f(0)}{h}=h^2\sin(1/h),
$$
whose absolute value is at most $h^2$ and therefore tends to $0$. Hence
$f'(0)=0$.
:::

<1>2. The hypothesis of the problem holds, with
$$
\lim_{x\to0}\frac{f(x)}{x^2}=0.
$$

::: {.proof}
For $x\neq0$,
$$
\frac{f(x)}{x^2}=x\sin(1/x),
$$
whose absolute value is at most $\abs{x}$. The squeeze theorem gives the
stated limit.
:::

<1>3. The second derivative $f''(0)$ does not exist, so the answer is
$$
\boxed{\text{no}}.
$$

::: {.proof}
By step <1>1, if $f''(0)$ existed, it would be the limit as $h\to0$ of
$$
\frac{f'(h)-f'(0)}{h}
=3h\sin(1/h)-\cos(1/h).
$$
For
$$
h_n=\frac{1}{2\pi n}
\qquad\text{and}\qquad
k_n=\frac{1}{(2n+1)\pi},
$$
both sequences tend to $0$, while
$$
3h_n\sin(1/h_n)-\cos(1/h_n)=-1
$$
and
$$
3k_n\sin(1/k_n)-\cos(1/k_n)=1.
$$
Thus the difference quotient for $f'$ at $0$ has two distinct
subsequential limits and cannot converge.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 give a differentiable counterexample satisfying the
hypothesis but not the asserted conclusion.
:::
:::
