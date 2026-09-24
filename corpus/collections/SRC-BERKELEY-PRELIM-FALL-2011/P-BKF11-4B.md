---
schema: qual/card@1
id: P-BKF11-4B
kind: problem
title: Limit of ratios of the recurrence $u_n=3u_{n-1}+u_{n-2}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 4B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the characteristic roots, the constants determined by the initial
    conditions, and the ratio limit using the smaller root's decay.
---

::: {.problem}
The sequence $(u_n)$ is defined by
$$
u_0=0,\qquad u_1=1,\qquad u_n=3u_{n-1}+u_{n-2}.
$$
Calculate
$$
\lim_{n\to\infty}\frac{u_n}{u_{n-1}}.
$$
:::

::: {.solution}
Put
$$
r_+\coloneqq\frac{3+\sqrt{13}}2,
\qquad
r_-\coloneqq\frac{3-\sqrt{13}}2.
$$

<1>1. The numbers $r_+$ and $r_-$ are the two distinct roots of
$$
r^2-3r-1=0,
$$
and
$$
\abs{r_-}<r_+.
$$

::: {.proof}
The quadratic formula gives exactly the displayed values. Since
$\sqrt{13}>3$,
$$
r_+>0,
\qquad
r_-<0.
$$
Moreover,
$$
\abs{r_-}
=\frac{\sqrt{13}-3}{2}
<\frac{\sqrt{13}+3}{2}
=r_+.
$$
:::

<1>2. For every $n\ge0$,
$$
u_n=\frac{r_+^n-r_-^n}{\sqrt{13}}.
$$

::: {.proof}
Because $r_+$ and $r_-$ are distinct roots of the characteristic
equation, every sequence of the form
$$
v_n=Ar_+^n+Br_-^n
$$
satisfies $v_n=3v_{n-1}+v_{n-2}$. The initial condition $u_0=0$
requires
$$
A+B=0,
$$
and $u_1=1$ requires
$$
Ar_++Br_-=1.
$$
Thus
$$
A(r_+-r_-)=1.
$$
Since $r_+-r_-=\sqrt{13}$, one obtains
$$
A=\frac1{\sqrt{13}},
\qquad
B=-\frac1{\sqrt{13}},
$$
which gives the claimed formula. The recurrence and the two initial
values determine the sequence uniquely.
:::

<1>3. The ratio satisfies
$$
\frac{u_n}{u_{n-1}}
=r_+
\frac{1-(r_-/r_+)^n}
     {1-(r_-/r_+)^{n-1}}
$$
for $n\ge2$.

::: {.proof}
Step <1>2 gives
$$
\frac{u_n}{u_{n-1}}
=\frac{r_+^n-r_-^n}{r_+^{n-1}-r_-^{n-1}}.
$$
Factoring $r_+^n$ from the numerator and $r_+^{n-1}$ from the
denominator yields the displayed expression.
:::

<1>4. Therefore
$$
\boxed{
\lim_{n\to\infty}\frac{u_n}{u_{n-1}}
=\frac{3+\sqrt{13}}2
}.
$$

::: {.proof}
By step <1>1,
$$
\abs{r_-/r_+}<1.
$$
Hence both powers of $r_-/r_+$ in step <1>3 tend to $0$. Taking the
limit there gives $r_+=(3+\sqrt{13})/2$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested limit.
:::
:::
