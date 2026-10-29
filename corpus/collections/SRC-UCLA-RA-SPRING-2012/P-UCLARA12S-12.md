---
schema: qual/card@1
id: P-UCLARA12S-12
kind: problem
title: Entire functions of exponential derivative growth with prescribed zeros
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Show that the only entire function $f$ satisfying both
$$
|f'(z)|\le e^{|z|}
$$
and
$$
f\!\left(\frac{n}{\sqrt{1+|n|}}\right)=0
\qquad\text{for every }n\in\ZZ
$$
is the zero function.
:::

::: {.solution}

For $n\in\NN$, set
$$
a_n\coloneqq\frac{n}{\sqrt{1+n}}.
$$
The prescribed zero set contains $0$ and the two points $\pm a_n$ for every $n\ge1$.

::: pf

::: {.pf-step #s1-1}

Every such function satisfies
$$
\abs{f(z)}\le \abs z e^{\abs z}
$$
for all $z\in\CC$.


::: pf-proof

The condition with $n=0$ gives $f(0)=0$. Integrating $f'$ along the radial segment $t\mapsto tz$, $0\le t\le1$, gives
$$
f(z)
=
\int_0^1 zf'(tz)\,dt.
$$
Therefore
$$
\abs{f(z)}
\le
\abs z\int_0^1 e^{t\abs z}\,dt
\le
\abs z e^{\abs z}.
$$

:::

:::

::: {.pf-step #s1-2}

If $f\not\equiv0$, then there are an integer $m\ge1$ and an entire function $g$ with $g(0)\ne0$ such that
$$
f(z)=z^m g(z).
$$
Moreover, for every $R\ge1$,
$$
\max_{\abs z=R}\log\abs{g(z)}
\le
R.
$$


::: pf-proof

Since $f$ is nonzero and $f(0)=0$, its zero at $0$ has some finite multiplicity $m\ge1$, so $f(z)=z^m g(z)$ with $g$ entire and $g(0)\ne0$. On $\abs z=R\ge1$, step [](#s1-1){.pf-ref} gives
$$
\abs{g(z)}
=
\frac{\abs{f(z)}}{R^m}
\le
R^{1-m}e^R
\le
e^R.
$$
Taking logarithms proves the claim.

:::

:::

::: {.pf-step #s1-3}

If $N_g(r)$ denotes the number of zeros of $g$ in $\{\abs z\le r\}$, counted with multiplicity, then for every $R>0$ for which $g$ has no zero on $\abs z=R$,
$$
N_g(R/2)\log2
\le
R-\log\abs{g(0)}.
$$


::: pf-proof

Jensen's formula gives
$$
\sum_{\substack{g(\zeta)=0\\0<\abs\zeta<R}}
\log\frac{R}{\abs\zeta}
=
\frac1{2\pi}\int_0^{2\pi}
\log\abs{g(Re^{i\theta})}\,d\theta
-\log\abs{g(0)}.
$$
Every zero with $\abs\zeta\le R/2$ contributes at least $\log2$ to the sum. By step [](#s1-2){.pf-ref}, the integral average is at most $R$. This yields the stated inequality.

:::

:::

::: {.pf-step #s1-4}

For every sufficiently large $R$, the prescribed zeros force
$$
N_g(R/2)\ge \frac{R^2}{8}-1.
$$


::: pf-proof

For $n\ge1$,
$$
a_n
=
\frac{n}{\sqrt{1+n}}
\le
\sqrt n.
$$
Hence whenever
$$
1\le n\le\frac{R^2}{4},
$$
one has $a_n\le R/2$. Except for the zero at $0$, division by $z^m$ does not remove any prescribed zero, so each positive $a_n$ in this range remains a zero of $g$. Thus
$$
N_g(R/2)
\ge
\left\lfloor\frac{R^2}{4}\right\rfloor.
$$
In particular this is at least $R^2/8-1$ for all sufficiently large $R$.

:::

:::

::: {.pf-step #s1-5}

The assumption $f\not\equiv0$ is impossible.


::: pf-proof

Choose arbitrarily large radii $R$ for which $g$ has no zero on the circle $\abs z=R$; this is possible because the zero set of a nonzero entire function is discrete. Combining steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} gives
$$
\left(\frac{R^2}{8}-1\right)\log2
\le
R-\log\abs{g(0)}.
$$
The left-hand side grows quadratically in $R$, whereas the right-hand side grows linearly. This fails for all sufficiently large $R$, a contradiction.

:::

:::

::: {.pf-step #s1-6}

Therefore $\boxed{f\equiv0}$.


::: pf-proof

Step [](#s1-5){.pf-ref} rules out every nonzero entire function satisfying the two hypotheses.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
