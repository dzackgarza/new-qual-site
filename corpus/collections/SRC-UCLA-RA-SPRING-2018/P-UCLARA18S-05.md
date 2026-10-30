---
schema: qual/card@1
id: P-UCLARA18S-05
kind: problem
title: Measures on $[0,1]$ with vanishing Stieltjes transform are zero
classification:
  areas:
  - real-analysis
  topics:
  - Borel Measures
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 5. Let $\mu$ be a real-valued Borel measure on $[0,1]$ such that
$$
\int_0^1\frac1{x+t}\,d\mu(t)=0
\qquad\text{for all }x>1.
$$
Show that $\mu=0$.
:::

::: {.solution}

For $k\ge0$, define the moments
$$
a_k=\int_0^1 t^k\,d\mu(t).
$$

::: pf

::: pf-step

For every $s\in(0,1)$,
$$
0
=
\int_0^1
\frac{s}{1+st}\,d\mu(t).
$$


::: pf-proof

Take
$$
x=\frac1s>1.
$$
Then
$$
\frac1{x+t}
=
\frac{s}{1+st}.
$$
Apply the hypothesis.

:::

:::

::: {.pf-step #s1-2}

For every fixed $s\in(0,1)$,
$$
\frac{s}{1+st}
=
\sum_{k=0}^{\infty}
(-1)^k s^{k+1}t^k
$$
uniformly for $t\in[0,1]$.


::: pf-proof

Since
$$
\abs{st}\le s<1,
$$
the geometric series
$$
\frac1{1+st}
=
\sum_{k=0}^{\infty}(-st)^k
$$
converges uniformly on $[0,1]$. Multiply by $s$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\sum_{k=0}^{\infty}
(-1)^k a_k s^{k+1}
=0
\qquad(0<s<1)}.
$$


::: pf-proof

Because $\mu$ is a finite signed Borel measure on the compact interval,
integration against $\mu$ is a continuous linear functional on
$$
C([0,1])
$$
for the sup norm. Thus the uniform convergence in step [](#s1-2){.pf-ref} allows
term-by-term integration:
$$
\begin{aligned}
0
&=
\int_0^1
\frac{s}{1+st}\,d\mu(t)\\
&=
\sum_{k=0}^{\infty}
(-1)^k s^{k+1}
\int_0^1t^k\,d\mu(t)\\
&=
\sum_{k=0}^{\infty}
(-1)^k a_k s^{k+1}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Every moment vanishes:
$$
\boxed{a_k=0\qquad(k\ge0)}.
$$


::: pf-proof

The power series
$$
F(s)
=
\sum_{k=0}^{\infty}
(-1)^k a_k s^{k+1}
$$
has radius of convergence at least $1$, since
$$
\abs{a_k}
\le
\totalvariation{\mu}([0,1]).
$$
By step [](#s1-3){.pf-ref}, $F(s)=0$ for every $s\in(0,1)$. The identity theorem for
power series therefore implies that every coefficient is zero:
$$
(-1)^ka_k=0.
$$

:::

:::

::: {.pf-step #s1-5}

For every polynomial $p$,
$$
\boxed{
\int_0^1 p(t)\,d\mu(t)=0}.
$$


::: pf-proof

Write
$$
p(t)
=
\sum_{k=0}^{N}c_kt^k.
$$
Then by linearity and step [](#s1-4){.pf-ref},
$$
\int_0^1p(t)\,d\mu(t)
=
\sum_{k=0}^{N}c_ka_k
=0.
$$

:::

:::

::: {.pf-step #s1-6}

For every continuous function $f\in C([0,1])$,
$$
\boxed{
\int_0^1 f(t)\,d\mu(t)=0}.
$$


::: pf-proof

By the Weierstrass approximation theorem, there are polynomials $p_n$
such that
$$
\norm{p_n-f}_\infty\to0.
$$
Since $\mu$ has finite total variation,
$$
\abs{
\int_0^1(f-p_n)\,d\mu
}
\le
\norm{f-p_n}_\infty
\totalvariation{\mu}([0,1])
\longrightarrow0.
$$
Step [](#s1-5){.pf-ref} gives
$$
\int_0^1p_n\,d\mu=0
$$
for every $n$, so the limit yields the claim.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{\mu=0}.
$$


::: pf-proof

A finite signed Borel measure on the compact Hausdorff space $[0,1]$ is
uniquely determined by the continuous linear functional
$$
f\longmapsto\int_0^1f\,d\mu
$$
on $C([0,1])$. Step [](#s1-6){.pf-ref} says this functional is identically zero.
Therefore the representing measure is the zero measure.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
