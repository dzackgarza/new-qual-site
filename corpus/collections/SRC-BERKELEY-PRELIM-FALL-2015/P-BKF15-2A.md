---
schema: qual/card@1
id: P-BKF15-2A
kind: problem
title: A discontinuous function on the plane continuous on every line
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
    Independently checked the retained Fall 2015 solution packet and its
    parabola-based construction. The authored solution uses an explicit
    rational-function example with the same line-versus-parabola phenomenon.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked continuity away from the origin, continuity on every line through
    the origin, and failure of continuity along the parabola y=x^2.
---

::: {.problem}
Show that there is a real-valued function on the real plane that is not continuous, but is continuous when restricted to any straight line.
:::

::: {.solution}
Define
$$
f(x,y)\coloneqq
\begin{cases}
\dfrac{x^2y}{x^4+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
$$

::: pf

::: {.pf-step #s1}

The function $f$ is continuous at every point of
$$
\RR^2\setminus\{(0,0)\}.
$$

::: pf-proof

For $(x,y)\ne(0,0)$ one has
$$
x^4+y^2>0.
$$
Thus, away from the origin, $f$ is a quotient of polynomials with
nonzero denominator and is therefore continuous.

:::

:::

::: {.pf-step #s2}

The restriction of $f$ to every line through the origin is
continuous at the origin.

::: pf-proof

The vertical line $x=0$ satisfies
$$
f(0,y)=0
$$
for all $y$, so its restriction is continuous.

Every nonvertical line through the origin has the form
$$
y=mx
$$
for some $m\in\RR$. If $m=0$, again $f(x,0)=0$. If $m\ne0$, then for
$x\ne0$,
$$
\begin{aligned}
f(x,mx)
&=
\frac{x^2(mx)}{x^4+m^2x^2}\\
&=
\frac{mx}{x^2+m^2}.
\end{aligned}
$$
Hence
$$
\lim_{x\to0}f(x,mx)=0=f(0,0).
$$
Thus the restriction is continuous at the origin on every line through
the origin.

:::

:::

::: {.pf-step #s3}

The restriction of $f$ to every straight line in $\RR^2$ is
continuous.

::: pf-proof

If a line does not pass through the origin, step [](#s1){.pf-ref} shows that $f$ is
continuous at every point of the line, so its restriction is
continuous. If the line passes through the origin, step [](#s1){.pf-ref} gives
continuity away from the origin and step [](#s2){.pf-ref} gives continuity at the
origin.

:::

:::

::: {.pf-step #s4}

The function $f$ is not continuous at the origin.

::: pf-proof

Along the parabola
$$
y=x^2,
$$
for every $x\ne0$,
$$
f(x,x^2)
=
\frac{x^4}{x^4+x^4}
=
\frac12.
$$
Therefore
$$
\lim_{x\to0}f(x,x^2)=\frac12\ne0=f(0,0).
$$
Thus $f$ is not continuous at $(0,0)$.

:::

:::

::: {.pf-step #s5}

Hence there exists a real-valued function on the plane that is
continuous on every straight line but not continuous on the plane.

::: pf-proof

The displayed function has linewise continuity by step [](#s3){.pf-ref} and is not
continuous by step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required example.

:::

:::

:::
