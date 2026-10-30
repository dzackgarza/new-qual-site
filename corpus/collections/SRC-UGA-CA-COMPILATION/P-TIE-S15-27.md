---
schema: qual/card@1
id: P-TIE-S15-27
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx$ and $\int_0^\infty\frac{\log x}{(1+x^2)^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 27.
---

::: {.problem}
Compute the following integrals.
(i) $\displaystyle\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx$, where $0<a<n$.

(ii) $\displaystyle\int_0^\infty \frac{\log x}{(1+x^2)^2}\,dx$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $0<a<n$,
$$
\boxed{
\int_0^\infty
\frac{x^{a-1}}{1+x^n}\,dx
=
\frac{\pi}{n}
\csc\frac{\pi a}{n}.
}
$$


::: pf-proof

Set
$$
t=x^n.
$$
Then
$$
dx
=
\frac1n t^{1/n-1}\,dt
$$
and therefore
$$
x^{a-1}dx
=
\frac1n t^{a/n-1}\,dt.
$$
Thus
$$
\int_0^\infty
\frac{x^{a-1}}{1+x^n}\,dx
=
\frac1n
\int_0^\infty
\frac{t^{a/n-1}}{1+t}\,dt.
$$
Since
$$
0<\frac an<1,
$$
Euler's beta integral gives
$$
\int_0^\infty
\frac{t^{a/n-1}}{1+t}\,dt
=
\Gamma\left(\frac an\right)
\Gamma\left(1-\frac an\right).
$$
The reflection formula then gives
$$
\Gamma\left(\frac an\right)
\Gamma\left(1-\frac an\right)
=
\frac{\pi}{\sin(\pi a/n)}.
$$
Multiplying by $1/n$ proves the formula.

:::

:::

::: {.pf-step #s1-2}

For $0<s<4$, define
$$
J(s)
\coloneqq
\int_0^\infty
\frac{x^{s-1}}{(1+x^2)^2}\,dx.
$$
Then
$$
J(s)
=
\frac{\pi(2-s)}
{4\sin(\pi s/2)}.
$$


::: pf-proof

Use the substitution
$$
t=x^2.
$$
Then
$$
J(s)
=
\frac12
\int_0^\infty
\frac{t^{s/2-1}}{(1+t)^2}\,dt
=
\frac12
B\left(\frac s2,2-\frac s2\right).
$$
Hence
$$
\begin{aligned}
J(s)
&=
\frac12
\Gamma\left(\frac s2\right)
\Gamma\left(2-\frac s2\right)\\
&=
\frac12
\left(1-\frac s2\right)
\Gamma\left(\frac s2\right)
\Gamma\left(1-\frac s2\right).
\end{aligned}
$$
The reflection formula gives
$$
\Gamma\left(\frac s2\right)
\Gamma\left(1-\frac s2\right)
=
\frac{\pi}{\sin(\pi s/2)}.
$$
Therefore
$$
J(s)
=
\frac{\pi(2-s)}
{4\sin(\pi s/2)}.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
\int_0^\infty
\frac{\log x}{(1+x^2)^2}\,dx
=
-\frac\pi4.
}
$$


::: pf-proof

For $s$ in a small closed interval around $1$, the derivative of the integrand in step [](#s1-2){.pf-ref} is
$$
\frac{x^{s-1}\log x}{(1+x^2)^2},
$$
and it is dominated by an integrable function near both $0$ and $\infty$. Hence differentiation under the integral sign gives
$$
J'(1)
=
\int_0^\infty
\frac{\log x}{(1+x^2)^2}\,dx.
$$
Differentiate the closed form from step [](#s1-2){.pf-ref}:
$$
J(s)
=
\frac\pi4
(2-s)
\csc\frac{\pi s}{2}.
$$
At $s=1$,
$$
\cot\frac\pi2=0,
$$
so
$$
J'(1)
=
-\frac\pi4.
$$
This is the desired value.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} evaluates part (i), and step [](#s1-3){.pf-ref} evaluates part (ii).

:::

:::

:::
