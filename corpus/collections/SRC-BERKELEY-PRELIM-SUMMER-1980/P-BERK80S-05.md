---
schema: qual/card@1
id: P-BERK80S-05
kind: problem
title: Boundedness of solutions of $x'=-x+y$, $y'=\log(20+x)-y$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 5 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the OCR-split constant in $\log(20+x)$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified positive-quadrant invariance, the scalar damped equation, coercivity of the potential, and the energy estimate bounding both variables.
---

::: {.problem}
Consider the differential equations

$$
\frac{dx}{dt}=-x+y,\qquad \frac{dy}{dt}=\log(20+x)-y.
$$

Let $x(t)$ and $y(t)$ be a solution defined for all $t\ge0$ with $x(0)>0$ and $y(0)>0$.
Prove that $x(t)$ and $y(t)$ are bounded.
:::

::: {.solution}
Set
$$
U(x)=\frac{x^2}{2}-(x+20)\log(x+20)+(x+20),
\qquad x>-20,
$$
so that
$$
U'(x)=x-\log(20+x),
$$
and set
$$
E(t)=\frac12(x'(t))^2+U(x(t)).
$$

<1>1. One has $x(t)>0$ and $y(t)>0$ for every $t\ge0$.

::: {.proof}
Variation of constants gives
$$
x(t)=e^{-t}\left(x(0)+\int_0^t e^s y(s)\,ds\right)
$$
and
$$
y(t)=e^{-t}\left(y(0)+\int_0^t e^s\log(20+x(s))\,ds\right).
$$
Suppose some variable vanishes at a positive time, and let $t_*$ be the
first such time. On $[0,t_*)$ both variables are positive, and $x(s)>0$
gives $\log(20+x(s))>0$. The two displayed formulas at $t=t_*$ then give
$x(t_*)>0$ and $y(t_*)>0$, a contradiction.
:::

<1>2. The function $x$ satisfies
$$
x''+2x'+U'(x)=0,
$$
and $E(t)\le E(0)$ for every $t\ge0$.

::: {.proof}
From
$$
x'=-x+y
$$
we have
$$
y=x'+x.
$$
Differentiating and using the second equation gives
$$
x''+x'=y'=\log(20+x)-y
=\log(20+x)-x'-x.
$$
Therefore
$$
x''+2x'+x-\log(20+x)=0,
$$
which is the displayed equation. Multiplying it by $x'$ yields
$$
E'(t)=\frac{d}{dt}\left(\frac12(x')^2+U(x)\right)=-2(x')^2\le0.
$$
:::

<1>3. The function $x$ is bounded on $[0,\infty)$.

::: {.proof}
As $x\to\infty$,
$$
U(x)=\frac{x^2}{2}-(x+20)\log(x+20)+(x+20)
\longrightarrow +\infty,
$$
because $(x+20)\log(x+20)=o(x^2)$. Thus the sublevel set
$$
\{x\ge0:U(x)\le E(0)\}
$$
is bounded. Since $x(t)>0$ by step <1>1 and $U(x(t))\le E(t)\le E(0)$ by
step <1>2, the function $x$ takes values in this set.
:::

<1>4. The functions $x'$ and $y$ are bounded on $[0,\infty)$.

::: {.proof}
Let
$$
m=\min_{x\ge0}U(x),
$$
which exists because $U$ is continuous on $[0,\infty)$ and tends to
$+\infty$ as $x\to\infty$. By step <1>2,
$$
\frac12(x'(t))^2
=E(t)-U(x(t))
\le E(0)-m,
$$
so $x'$ is bounded. Finally,
$$
y(t)=x'(t)+x(t),
$$
which is bounded by step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>3 and <1>4 show that $x(t)$ and $y(t)$ are bounded for $t\ge0$.
:::
:::
