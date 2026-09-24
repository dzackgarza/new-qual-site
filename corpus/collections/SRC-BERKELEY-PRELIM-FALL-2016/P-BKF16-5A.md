---
schema: qual/card@1
id: P-BKF16-5A
kind: problem
title: No holomorphic $f$ on $\mathbb C\setminus\{0\}$ with $\lvert f(z)\rvert\ge\lvert z\rvert^{-1/2}$
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
    Independently checked the retained Fall 2016 solution packet: the
    reciprocal extends across zero, and a large-circle Cauchy estimate
    forces its derivative to vanish identically.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked nonvanishing of f, removability of g=1/f at zero, the Cauchy
    derivative estimate on large circles, and the final contradiction.
---

::: {.problem}
Is there a function f(z) analytic in C \ {0} such that $\begin{array} { r } { | f ( z ) | \geq \frac { 1 } { \sqrt { | z | } } } \end{array}$ for all $z \neq 0 ?$
:::

::: {.solution}
<1>1. If such a function $f$ existed, then
$$
g(z)\coloneqq\frac1{f(z)}
$$
would be holomorphic on $\CC\setminus\{0\}$ and satisfy
$$
\abs{g(z)}
\le
\sqrt{\abs z}.
$$

::: {.proof}
The assumed lower bound is strictly positive for every $z\ne0$, so
$f(z)\ne0$ throughout the punctured plane. Hence $g=1/f$ is
holomorphic there. Taking reciprocals in
$$
\abs{f(z)}
\ge
\frac1{\sqrt{\abs z}}
$$
gives the displayed upper bound.
:::

<1>2. The singularity of $g$ at $0$ is removable, and its holomorphic
extension satisfies
$$
g(0)=0.
$$

::: {.proof}
Step <1>1 gives
$$
\abs{g(z)}
\le
\sqrt{\abs z}
\longrightarrow
0
$$
as $z\to0$. In particular, $g$ is bounded on a punctured neighborhood
of $0$. Riemann's removable singularity theorem therefore extends $g$
holomorphically across $0$, and the displayed limit forces the
extension to have value $0$ there.
:::

<1>3. For every fixed $z\in\CC$ and every
$$
R>2\abs z,
$$
the entire extension of $g$ satisfies
$$
\abs{g'(z)}
\le
\frac4{\sqrt R}.
$$

::: {.proof}
On the circle
$$
C_R=\{s:\abs s=R\},
$$
step <1>1 gives
$$
\abs{g(s)}\le\sqrt R.
$$
Cauchy's formula for the derivative gives
$$
g'(z)
=
\frac1{2\pi i}
\oint_{C_R}
\frac{g(s)}{(s-z)^2}\,ds.
$$
For $s\in C_R$,
$$
\abs{s-z}
\ge
R-\abs z
>
\frac R2.
$$
Since $C_R$ has length $2\pi R$, the estimation lemma yields
$$
\begin{aligned}
\abs{g'(z)}
&\le
\frac1{2\pi}
(2\pi R)
\frac{\sqrt R}{(R/2)^2}\\
&=
\frac4{\sqrt R}.
\end{aligned}
$$
:::

<1>4. The function $g$ is constant on $\CC$.

::: {.proof}
Fix $z\in\CC$. The estimate in step <1>3 holds for arbitrarily large
$R$. Letting $R\to\infty$ gives
$$
\abs{g'(z)}=0.
$$
Thus $g'(z)=0$ for every $z$, so the entire function $g$ is constant.
:::

<1>5. No function satisfying the hypothesis exists.

::: {.proof}
By steps <1>2 and <1>4, the constant function $g$ must satisfy
$$
g(z)=g(0)=0
$$
for every $z$. But on $\CC\setminus\{0\}$,
$$
g(z)=\frac1{f(z)},
$$
which can never equal $0$. This contradiction proves nonexistence.
:::

<1>6. Therefore the answer is
$$
\boxed{\text{no}}.
$$

::: {.proof}
Step <1>5 excludes every possible holomorphic function with the stated
lower bound.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 answers the question.
:::
:::
