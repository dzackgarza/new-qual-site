---
schema: qual/card@1
id: P-UCLAB02F-04
kind: problem
title: Derive the Leibniz series for $\pi/4$ by integration
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
By integrating the series
$$
\frac1{1+x^2}=1-x^2+x^4-x^6+x^8-\cdots,
$$
prove that
$$
\frac\pi4=1-\frac13+\frac15-\frac17+\frac19-\cdots.
$$
Justify carefully every step, especially taking the limit as $x\to1$ from below.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every integer $N\ge0$ and every real $t$,
$$
\frac1{1+t^2}
=
\sum_{k=0}^{N}(-1)^k t^{2k}
+
(-1)^{N+1}\frac{t^{2N+2}}{1+t^2}.
$$


::: pf-proof

Apply the finite geometric-series identity
$$
\frac1{1-r}
=
\sum_{k=0}^{N}r^k
+
\frac{r^{N+1}}{1-r}
$$
with $r=-t^2$.

:::

:::

::: {.pf-step #s1-2}

For $0\le x\le1$,
$$
\arctan x
=
\sum_{k=0}^{N}(-1)^k\frac{x^{2k+1}}{2k+1}
+
R_N(x),
$$
where
$$
R_N(x)
=
(-1)^{N+1}
\int_0^x\frac{t^{2N+2}}{1+t^2}\,dt.
$$


::: pf-proof

Integrate the finite identity from step [](#s1-1){.pf-ref} term by term on $[0,x]$. This is legitimate because only finitely many terms are involved. Since
$$
\int_0^x\frac{dt}{1+t^2}=\arctan x
$$
and
$$
\int_0^x t^{2k}\,dt=\frac{x^{2k+1}}{2k+1},
$$
the displayed formula follows.

:::

:::

::: {.pf-step #s1-3}

For $0\le x\le1$,
$$
\abs{R_N(x)}
\le
\frac{x^{2N+3}}{2N+3}.
$$


::: pf-proof

Because $1+t^2\ge1$ on $[0,1]$,
$$
\abs{R_N(x)}
\le
\int_0^x t^{2N+2}\,dt
=
\frac{x^{2N+3}}{2N+3}.
$$

:::

:::

::: pf-step

For every $0\le x<1$,
$$
\arctan x
=
\sum_{k=0}^{\infty}(-1)^k\frac{x^{2k+1}}{2k+1}.
$$


::: pf-proof

Fix $x<1$. By step [](#s1-3){.pf-ref},
$$
\abs{R_N(x)}
\le
\frac{x^{2N+3}}{2N+3}
\longrightarrow0.
$$
Letting $N\to\infty$ in the finite identity of step [](#s1-2){.pf-ref} gives the stated series.

:::

:::

::: {.pf-step #s1-5}

For every $N\ge0$,
$$
\abs{
\frac\pi4
-
\sum_{k=0}^{N}(-1)^k\frac1{2k+1}
}
\le
\frac1{2N+3}.
$$


::: pf-proof

Keep $N$ fixed in step [](#s1-2){.pf-ref} and let $x\to1^-$.
Continuity of $\arctan$ gives
$$
\arctan x\to\arctan1=\frac\pi4,
$$
and each of the finitely many polynomial terms satisfies
$$
\frac{x^{2k+1}}{2k+1}\to\frac1{2k+1}.
$$
Also, by step [](#s1-3){.pf-ref},
$$
\abs{R_N(x)}\le\frac{x^{2N+3}}{2N+3}\le\frac1{2N+3}.
$$
Therefore the limiting difference between $\pi/4$ and the $N$th partial sum has absolute value at most $1/(2N+3)$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
\frac\pi4
=
1-\frac13+\frac15-\frac17+\frac19-\cdots
}.
$$


::: pf-proof

Let
$$
S_N=\sum_{k=0}^{N}(-1)^k\frac1{2k+1}.
$$
By step [](#s1-5){.pf-ref},
$$
\abs{\frac\pi4-S_N}
\le
\frac1{2N+3}
\longrightarrow0.
$$
Hence $S_N\to\pi/4$, which is exactly the displayed series identity.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the claimed Leibniz series, and step [](#s1-5){.pf-ref} supplies the required justification of the limit as $x\to1^-$ without interchanging an infinite sum with that limit.

:::

:::

:::
