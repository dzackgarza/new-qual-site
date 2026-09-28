---
schema: qual/card@1
id: P-BERK80S-06
kind: problem
title: The integral of a branch of $\sqrt{z^2-1}$ around $\abs{z}=2$
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
  note: Checked against Problem 6 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the chosen exterior branch, its Laurent expansion, and the resulting contour integral.
---

::: {.problem}
Let $C$ denote the positively oriented circle $\abs{z}=2$, $z\in\CC$. Evaluate the integral

$$
\int_C\sqrt{z^2-1}\,dz
$$

where the branch of the square root is chosen so that $\sqrt{2^2-1}>0$.
:::

::: {.solution}
<1>1. On $\abs{z}>1$, the required branch is
$$
\sqrt{z^2-1}=z\sqrt{1-z^{-2}},
$$
where the second square root is the principal branch.

::: {.proof}
For $\abs{z}>1$, one has $\abs{z^{-2}}<1$, so $1-z^{-2}$ lies in the open
disk of radius $1$ centered at $1$. The principal square root is analytic
on this disk, so the displayed function is analytic on $\abs{z}>1$, and its
square is $z^2(1-z^{-2})=z^2-1$. At $z=2$ it gives
$$
2\sqrt{1-\frac14}=\sqrt3>0,
$$
so it is the branch required in the problem.
:::

<1>2. For $\abs{z}>1$, the branch of step <1>1 has Laurent expansion
$$
\sqrt{z^2-1}
=z-\frac1{2z}-\frac1{8z^3}-\cdots,
$$
whose coefficient of $z^{-1}$ is $-\tfrac12$.

::: {.proof}
For $\abs{w}<1$, the binomial series gives
$$
\sqrt{1-w}
=1-\frac12w-\frac18w^2-\cdots.
$$
Put $w=z^{-2}$ and multiply by $z$.
:::

<1>3. One has
$$
\int_C\sqrt{z^2-1}\,dz=\boxed{-\pi i}.
$$

::: {.proof}
The Laurent series of step <1>2 converges uniformly on the circle
$\abs{z}=2$, so termwise integration around the positively oriented circle
gives
$$
\int_C\sqrt{z^2-1}\,dz
=2\pi i\left(-\frac12\right)
=-\pi i.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested value.
:::
:::
