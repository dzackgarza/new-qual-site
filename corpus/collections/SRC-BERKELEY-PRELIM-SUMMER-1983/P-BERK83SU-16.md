---
schema: qual/card@1
id: P-BERK83SU-16
kind: problem
title: An orientation-preserving smooth map preserving orthogonality is holomorphic
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    At each point, orthogonality of the coordinate directions gives
    f_x perpendicular to f_y, while the orthogonal diagonal directions give
    equal lengths. Positive orientation then forces f_y to be the positive
    quarter-turn of f_x, which is exactly the Cauchy--Riemann system.
---

::: {.problem}
Let $\Omega\subset\mathbb R^2$ be open and let
\[
f:\Omega\to\mathbb R^2
\]
be smooth. Assume that $f$ preserves orientation and maps every pair of orthogonal curves to a pair of orthogonal curves.

Identifying $\mathbb R^2$ with $\mathbb C$, prove that $f$ is holomorphic.
:::

::: {.solution}
Write $f=(u,v)$. Fix $p\in\Omega$, and set
$$
a
=
Df_p(1,0)
=
\bigl(u_x(p),v_x(p)\bigr),
\qquad
b
=
Df_p(0,1)
=
\bigl(u_y(p),v_y(p)\bigr).
$$

::: pf

::: {.pf-step #s1}

The vectors $a$ and $b$ are orthogonal.

::: pf-proof

For $\abs{t}$ small enough that both points lie in $\Omega$, consider the
curves $t\mapsto p+t(1,0)$ and $t\mapsto p+t(0,1)$. They pass through
$p$ with tangent vectors $(1,0)$ and $(0,1)$, so they are orthogonal
at $p$.
Their images under $f$ have tangent vectors
$$
Df_p(1,0)=a
\qquad\text{and}\qquad
Df_p(0,1)=b.
$$
By the hypothesis that $f$ maps orthogonal curves to orthogonal
curves, $a\cdot b=0$.

:::

:::

::: {.pf-step #s2}

The vectors $a$ and $b$ have the same length.

::: pf-proof

The vectors $(1,1)$ and $(1,-1)$ are orthogonal. Curves through $p$
with these tangent vectors have image tangent vectors
$$
Df_p(1,1)=a+b,
\qquad
Df_p(1,-1)=a-b.
$$
Hence
$$
0
=
(a+b)\cdot(a-b)
=
\norm{a}^2-\norm{b}^2.
$$
Therefore $\norm{a}=\norm{b}$.

:::

:::

::: {.pf-step #s3}

One has
$$
b
=
\bigl(-v_x(p),u_x(p)\bigr).
$$

::: pf-proof

Orientation preservation gives
$$
\det Df_p
=
\det(a,b)
>
0.
$$
In particular, $a\neq0$. By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $b$ is one of the
two vectors obtained from $a$ by a quarter-turn:
$$
b
=
\pm\bigl(-v_x(p),u_x(p)\bigr).
$$
The positive choice satisfies
$$
\det
\begin{pmatrix}
u_x(p)&-v_x(p)\\
v_x(p)&u_x(p)
\end{pmatrix}
=
u_x(p)^2+v_x(p)^2
>
0,
$$
whereas the negative choice has negative determinant. Thus
orientation preservation forces the positive choice.

:::

:::

::: {.pf-step #s4}

The Cauchy--Riemann equations hold at $p$:
$$
u_x(p)=v_y(p),
\qquad
u_y(p)=-v_x(p).
$$

::: pf-proof

By the definition of $b$ and step [](#s3){.pf-ref},
$$
\bigl(u_y(p),v_y(p)\bigr)
=
\bigl(-v_x(p),u_x(p)\bigr).
$$
Equality of the two coordinates gives the displayed equations.

:::

:::

::: {.pf-step #s5}

The map $f$ is
$$
\boxed{\text{holomorphic on $\Omega$}}.
$$

::: pf-proof

The point $p\in\Omega$ was arbitrary, so step [](#s4){.pf-ref} gives the
Cauchy--Riemann equations throughout $\Omega$. Since $f$ is smooth,
the first partial derivatives of $u$ and $v$ are continuous.
Therefore the Cauchy--Riemann criterion implies that the
complex-valued map $f=u+iv$ is holomorphic on $\Omega$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
