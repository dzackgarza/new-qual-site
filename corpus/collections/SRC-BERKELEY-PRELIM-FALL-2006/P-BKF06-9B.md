---
schema: qual/card@1
id: P-BKF06-9B
kind: problem
title: Convergence of the iteration $z_{n+1}=1+1/z_n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 9B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Mobius-conjugacy argument, including
    the exceptional fixed point beta and the fact that a full sequence in the
    problem never encounters zero.
---

::: {.problem}
Let $z_0,z_1,\ldots$ be a sequence of complex numbers satisfying
\[
z_{n+1}=1+\frac1{z_n}
\]
for every $n\ge0$.
Prove that the sequence converges.
:::

::: {.solution}
Define
$$
F(z)=1+\frac1z=\frac{z+1}{z}
$$
for $z\ne0$, and set
$$
\alpha=\frac{1+\sqrt5}{2},
\qquad
\beta=\frac{1-\sqrt5}{2}.
$$

::: pf

::: {.pf-step #s1}

The numbers $\alpha$ and $\beta$ are the two fixed points of
$F$, and
$$
\alpha+\beta=1,
\qquad
\alpha\beta=-1.
$$

::: pf-proof

The fixed-point equation is
$$
z=1+\frac1z,
$$
equivalently
$$
z^2-z-1=0.
$$
Its two roots are the displayed numbers. Their sum and product follow
from the quadratic equation.

:::

:::

::: {.pf-step #s2}

If $z_0=\beta$, then
$$
z_n=\beta
$$
for every $n$, so the sequence converges.

::: pf-proof

By step [](#s1){.pf-ref}, $F(\beta)=\beta$. The recurrence therefore makes the
sequence constant.

:::

:::

::: {.pf-step #s3}

Suppose $z_0\ne\beta$. Then no term $z_n$ equals $\beta$.

::: pf-proof

First, every $z_n$ is nonzero because the recurrence is assumed to
hold for every $n$ and therefore $1/z_n$ must be defined.

For $z\ne0$, using step [](#s1){.pf-ref},
$$
\begin{aligned}
F(z)-\beta
&=
\frac{z+1-\beta z}{z}
\\
&=
\frac{\alpha z+1}{z}
\\
&=
\frac{\alpha(z-\beta)}{z},
\end{aligned}
$$
because $-\alpha\beta=1$. Hence $F(z)=\beta$ if and only if
$z=\beta$. If some $z_n$ equaled $\beta$, repeated application of
this implication backwards would force $z_0=\beta$, contrary to the
assumption.

:::

:::

::: {.pf-step #s4}

For $z\ne0,\beta$, define
$$
W(z)=\frac{z-\alpha}{z-\beta}.
$$
Then
$$
W(F(z))
=
\frac{\beta}{\alpha}W(z).
$$

::: pf-proof

Using step [](#s1){.pf-ref},
$$
\begin{aligned}
W(F(z))
&=
\frac{F(z)-\alpha}{F(z)-\beta}
\\
&=
\frac{z+1-\alpha z}{z+1-\beta z}
\\
&=
\frac{\beta z+1}{\alpha z+1}.
\end{aligned}
$$
Also
$$
\beta(z-\alpha)=\beta z-\alpha\beta=\beta z+1
$$
and
$$
\alpha(z-\beta)=\alpha z-\alpha\beta=\alpha z+1.
$$
Therefore
$$
\frac{\beta z+1}{\alpha z+1}
=
\frac{\beta}{\alpha}
\frac{z-\alpha}{z-\beta},
$$
as claimed.

:::

:::

::: {.pf-step #s5}

Under the assumption $z_0\ne\beta$, if
$$
w_n=W(z_n),
$$
then
$$
w_n=
\left(\frac{\beta}{\alpha}\right)^n w_0
\longrightarrow0.
$$

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} and the recurrence give
$$
w_{n+1}=\frac{\beta}{\alpha}w_n,
$$
so the displayed formula follows by induction. Moreover
$$
\alpha>1
$$
and, since $\alpha\beta=-1$,
$$
\left|\frac{\beta}{\alpha}\right|
=
\frac1{\alpha^2}
<
1.
$$
Hence $w_n\to0$.

:::

:::

::: {.pf-step #s6}

Under the assumption $z_0\ne\beta$,
$$
z_n\longrightarrow\alpha.
$$

::: pf-proof

Solving
$$
w=\frac{z-\alpha}{z-\beta}
$$
for $z$ gives
$$
z=\frac{\beta w-\alpha}{w-1}.
$$
By step [](#s5){.pf-ref}, $w_n\to0$. Therefore
$$
z_n
=
\frac{\beta w_n-\alpha}{w_n-1}
\longrightarrow
\frac{-\alpha}{-1}
=
\alpha.
$$

:::

:::

::: {.pf-step #s7}

Every sequence satisfying the recurrence for all $n\ge0$
converges.

::: pf-proof

If $z_0=\beta$, use step [](#s2){.pf-ref}. Otherwise use step [](#s6){.pf-ref}. These two
cases are exhaustive.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required conclusion.

:::

:::

:::
