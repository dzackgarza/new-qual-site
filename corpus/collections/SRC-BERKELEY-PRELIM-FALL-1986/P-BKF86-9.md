---
schema: qual/card@1
id: P-BKF86-9
kind: problem
title: Evaluate $\int_0^\infty \frac{\log x}{(x^2+1)(x^2+4)}\,dx$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
---

::: {.problem}
Evaluate
\[
\int_0^\infty\frac{\log x}{(x^2+1)(x^2+4)}\,dx.
\]
:::

::: {.solution}
Let
$$
I=\int_0^\infty\frac{\log x}{(x^2+1)(x^2+4)}\,dx
$$
and, for $a>0$, let
$$
J(a)=\int_0^\infty\frac{\log x}{x^2+a^2}\,dx.
$$

<1>1. One has
$$
I=\frac13\bigl(J(1)-J(2)\bigr).
$$

::: {.proof}
The partial-fraction identity
$$
\frac1{(x^2+1)(x^2+4)}
=
\frac13\left(\frac1{x^2+1}-\frac1{x^2+4}\right)
$$
gives the claim after integration.
:::

<1>2. The integral
$$
K=\int_0^\infty\frac{\log t}{1+t^2}\,dt
$$
converges and satisfies $K=0$.

::: {.proof}
Near $0$, the absolute value is bounded by $\abs{\log t}$, whose integral over $(0,1]$ is finite. For $t\geq1$,
$$
\frac{\log t}{1+t^2}\leq\frac{\log t}{t^2},
$$
whose integral over $[1,\infty)$ is finite. Thus $K$ is absolutely convergent.

Split the integral at $1$. In the first part, substitute $t=1/u$:
$$
\begin{aligned}
\int_0^1\frac{\log t}{1+t^2}\,dt
&=
-\int_1^\infty\frac{\log u}{1+u^2}\,du.
\end{aligned}
$$
Therefore the integrals over $(0,1)$ and $(1,\infty)$ cancel, so $K=0$.
:::

<1>3. For every $a>0$,
$$
J(a)=\frac{\pi\log a}{2a}.
$$

::: {.proof}
Substitute $x=at$. Then
$$
\begin{aligned}
J(a)
&=
\frac1a\int_0^\infty\frac{\log a+\log t}{1+t^2}\,dt\\
&=
\frac{\log a}{a}\int_0^\infty\frac{dt}{1+t^2}
+
\frac1a\int_0^\infty\frac{\log t}{1+t^2}\,dt.
\end{aligned}
$$
The first integral is $\pi/2$, and the second is $0$ by step <1>2. Hence
$$
J(a)=\frac{\pi\log a}{2a}.
$$
:::

<1>4. The required value is
$$
\boxed{
\int_0^\infty\frac{\log x}{(x^2+1)(x^2+4)}\,dx
=-\frac{\pi\log2}{12}
}.
$$

::: {.proof}
By step <1>3,
$$
J(1)=0,
\qquad
J(2)=\frac{\pi\log2}{4}.
$$
Substituting these values into step <1>1 gives
$$
I
=
\frac13\left(0-\frac{\pi\log2}{4}\right)
=
-\frac{\pi\log2}{12}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required evaluation.
:::
:::
