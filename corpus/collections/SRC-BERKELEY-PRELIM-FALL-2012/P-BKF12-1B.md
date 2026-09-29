---
schema: qual/card@1
id: P-BKF12-1B
kind: problem
title: Machin's formula $\pi/4=4\arctan\frac15-\arctan\frac1{239}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 1B in the retained Fall 2012 Berkeley prelim exam
    and independently reviewed the retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the tangent computations, the branch determination, and the
    convergence-rate comparison for the arctangent series.
---

::: {.problem}
Prove that

$$
\frac{\pi}{4}=4\arctan\frac{1}{5}-\arctan\frac{1}{239}.
$$

In 1706 John Machin used this formula to calculate $\pi$ to 100 decimal places.
Explain briefly why he did not use the simpler formula $\frac{\pi}{4}=\arctan1$.
:::

::: {.solution}
Set
$$
\alpha\coloneqq\arctan\frac15,
\qquad
\beta\coloneqq\arctan\frac1{239}.
$$

::: pf

::: {.pf-step #s1}

One has
$$
\tan(2\alpha)=\frac5{12},
\qquad
\tan(4\alpha)=\frac{120}{119}.
$$

::: pf-proof

The double-angle identity gives
$$
\tan(2\alpha)
=\frac{2(1/5)}{1-(1/5)^2}
=\frac5{12}.
$$
Applying the same identity again,
$$
\tan(4\alpha)
=\frac{2(5/12)}{1-(5/12)^2}
=\frac{120}{119}.
$$

:::

:::

::: {.pf-step #s2}

The angle $4\alpha-\beta$ lies in $(0,\pi/2)$.

::: pf-proof

Since $0<1/239<1/5$, monotonicity of $\arctan$ gives
$0<\beta<\alpha$, and hence $4\alpha-\beta>0$.

Also $0<\alpha<\pi/4$, so $0<4\alpha<\pi$. By step [](#s1){.pf-ref},
$\tan(4\alpha)=120/119>0$. On the interval $(0,\pi)$ the tangent is
positive only on $(0,\pi/2)$, so $4\alpha<\pi/2$. Therefore
$4\alpha-\beta<\pi/2$.

:::

:::

::: {.pf-step #s3}

One has
$$
\tan(4\alpha-\beta)=1.
$$

::: pf-proof

By step [](#s1){.pf-ref} and the subtraction formula for tangent,
$$
\begin{aligned}
\tan(4\alpha-\beta)
&=
\frac{\frac{120}{119}-\frac1{239}}
{1+\frac{120}{119\cdot239}}\\
&=
\frac{120\cdot239-119}{119\cdot239+120}\\
&=
\frac{28561}{28561}
=1.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

Machin's identity is
$$
\boxed{
\frac\pi4
=4\arctan\frac15-\arctan\frac1{239}
}.
$$

::: pf-proof

By step [](#s2){.pf-ref}, the angle $4\alpha-\beta$ belongs to $(0,\pi/2)$.
Step [](#s3){.pf-ref} says that its tangent is $1$. The unique angle in
$(0,\pi/2)$ with tangent $1$ is $\pi/4$. Substituting the definitions
of $\alpha$ and $\beta$ gives the displayed identity.

:::

:::

::: {.pf-step #s5}

The Taylor series for $\arctan\frac15$ and $\arctan\frac1{239}$
converge geometrically, whereas the truncation error of the Taylor
series for $\arctan1$ after $N$ terms is of order $1/N$.

::: pf-proof

For $0<x\le1$,
$$
\arctan x
=\sum_{k=0}^{\infty}
(-1)^k\frac{x^{2k+1}}{2k+1}.
$$
At $x=1$, the alternating-series error after truncation is controlled
only by the next reciprocal odd integer, so the error decreases on the
order of $1/N$ after $N$ terms. For $x=1/5$, the term magnitudes acquire
the factor $5^{-(2k+1)}$, and for $x=1/239$ they acquire
$239^{-(2k+1)}$. Thus the two arctangent series in step [](#s4){.pf-ref} converge
geometrically fast, whereas the series for $\arctan 1$ converges only
at reciprocal speed.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the identity, and step [](#s5){.pf-ref} gives the requested reason
for Machin's computational choice.

:::

:::

:::
