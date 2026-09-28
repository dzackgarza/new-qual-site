---
schema: qual/card@1
id: P-BKF91-3
kind: problem
title: The contour integral $\frac1{2\pi i}\oint_{\abs z=1}\frac{z^{n-1}}{3z^n-1}\,dz$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Located all n simple poles inside the unit circle and computed the common
    residue 1/(3n), whose sum is 1/3.
---

::: {.problem}
Let $n$ be a positive integer. Evaluate
\[
I=\frac{1}{2\pi i}\int_C\frac{z^{n-1}}{3z^n-1}\,dz,
\]
where $C$ is the counterclockwise unit circle $|z|=1$.
:::

::: {.solution}
<1>1. The poles of
$$
R(z)\coloneqq\frac{z^{n-1}}{3z^n-1}
$$
are the $n$ roots of
$$
z^n=\frac13,
$$
and all of them lie inside $C$.

::: {.proof}
The equation $3z^n-1=0$ has exactly $n$ distinct roots. Every such root $\alpha$ satisfies
$$
\abs\alpha=3^{-1/n}<1,
$$
so every pole lies strictly inside the unit circle.
:::

<1>2. Each pole $\alpha$ has residue
$$
\operatorname{Res}(R;\alpha)=\frac{1}{3n}.
$$

::: {.proof}
The derivative of the denominator is
$$
3n z^{n-1}.
$$
At a root $\alpha$ of $3z^n-1$, one has $\alpha\ne0$, so this derivative is nonzero and the pole is simple. Therefore
$$
\operatorname{Res}(R;\alpha)
=
\frac{\alpha^{n-1}}{3n\alpha^{n-1}}
=
\frac1{3n}.
$$
:::

<1>3. The requested integral is
$$
\boxed{I=\frac13}.
$$

::: {.proof}
By the residue theorem and steps <1>1--<1>2,
$$
I
=
\sum_{3\alpha^n=1}\operatorname{Res}(R;\alpha)
=
n\cdot\frac1{3n}
=
\frac13.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the required value.
:::
:::
