---
schema: qual/card@1
id: P-BKS14-4A
kind: problem
title: A Schwarz-lemma bound from two zeros
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked removability at the two zeros, boundary modulus identities for the reciprocal Blaschke factors, and the value g(0)=4f(0).
---

::: {.problem}
Let \(f\) be analytic on the closed unit disk and suppose \(|f(z)|\le 1\) there.
Assume
\[
f\!\left(\frac12\right)=f\!\left(\frac i2\right)=0.
\]
Prove that \(|f(0)|\le \frac14\).
:::

::: {.solution}
Define, away from the two apparent poles,
$$
g(z)
\coloneqq
\frac{z-2}{2z-1}
\frac{z-2i}{2z-i}
f(z).
$$

<1>1. The apparent singularity of $g$ at
$$
z=\frac12
$$
is removable.

::: {.proof}
Since
$$
f\left(\frac12\right)=0,
$$
the factor theorem for holomorphic functions gives a holomorphic function
$h_1$ near $1/2$ such that
$$
f(z)
=
\left(z-\frac12\right)h_1(z).
$$
Since
$$
2z-1
=
2\left(z-\frac12\right),
$$
the zero of $f$ cancels the denominator factor $2z-1$. The remaining
factors are holomorphic near $1/2$.
:::

<1>2. The apparent singularity of $g$ at
$$
z=\frac i2
$$
is removable.

::: {.proof}
Similarly,
$$
f\left(\frac i2\right)=0
$$
gives
$$
f(z)
=
\left(z-\frac i2\right)h_2(z)
$$
near $i/2$, with $h_2$ holomorphic. Since
$$
2z-i
=
2\left(z-\frac i2\right),
$$
the singularity cancels.
:::

<1>3. After filling in the removable singularities, $g$ is holomorphic on
the unit disk and continuous on its boundary.

::: {.proof}
The only possible singularities introduced by the displayed formula are
$1/2$ and $i/2$, which are removable by steps <1>1 and <1>2. All other
factors are rational functions with no further poles in the closed unit
disk, while $f$ is analytic there.
:::

<1>4. If
$$
\abs{z}=1,
$$
then
$$
\abs{z-2}
=
\abs{2z-1}
$$
and
$$
\abs{z-2i}
=
\abs{2z-i}.
$$

::: {.proof}
For $\abs{z}=1$,
$$
\begin{aligned}
\abs{z-2}^2
&=
(z-2)(\overline z-2)\\
&=
5-2(z+\overline z),
\end{aligned}
$$
while
$$
\begin{aligned}
\abs{2z-1}^2
&=
(2z-1)(2\overline z-1)\\
&=
5-2(z+\overline z).
\end{aligned}
$$
This proves the first equality.

Likewise,
$$
\abs{z-2i}^2
=
5+2i(z-\overline z)
=
\abs{2z-i}^2.
$$
:::

<1>5. On the unit circle,
$$
\abs{g(z)}
=
\abs{f(z)}
\leq
1.
$$

::: {.proof}
By step <1>4, each of the two rational factors defining $g$ has modulus
$1$ when $\abs{z}=1$. Multiplying their moduli with $\abs{f(z)}$ gives
the claim.
:::

<1>6. Throughout the unit disk,
$$
\abs{g(z)}
\leq
1.
$$

::: {.proof}
By step <1>3, $g$ is holomorphic in the disk and continuous on its
boundary. Step <1>5 bounds its boundary modulus by $1$. The maximum
modulus principle gives the same bound inside.
:::

<1>7. One has
$$
g(0)=4f(0).
$$

::: {.proof}
Substitution into the defining formula gives
$$
\begin{aligned}
g(0)
&=
\frac{-2}{-1}
\frac{-2i}{-i}
f(0)\\
&=
4f(0).
\end{aligned}
$$
:::

<1>8. Therefore
$$
\boxed{
\abs{f(0)}
\leq
\frac14
}.
$$

::: {.proof}
By steps <1>6 and <1>7,
$$
4\abs{f(0)}
=
\abs{g(0)}
\leq
1.
$$
Divide by $4$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required bound.
:::
:::
