---
schema: qual/card@1
id: P-BKF98-4
kind: problem
title: Sharp bound at $\log2$ for a holomorphic function with a prescribed zero
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Normalized by e^z and divided out the Blaschke factor for the prescribed
    zero. The maximum principle gives the sharp bound, attained by equality
    in the Blaschke quotient.
---

::: {.problem}
Let $f$ be analytic on a neighborhood of the closed unit disk, suppose
\[
f(-\log2)=0,
\]
and assume
\[
|f(z)|\le |e^z|
\]
for every $|z|=1$. How large can
\[
|f(\log2)|
\]
be?
:::

::: {.solution}

Set
$$
r\coloneqq\log2.
$$
Then
$$
0<r<1.
$$

::: pf

::: {.pf-step #g-normalized-bound}
The function
$$
g(z)\coloneqq e^{-z}f(z)
$$
is analytic on a neighborhood of the closed unit disk, satisfies
$$
g(-r)=0,
$$
and obeys
$$
\abs{g(z)}\leq1
$$
for $\abs z=1$.

::: pf-proof
The exponential never vanishes, so $g$ has the same domain of analyticity
as $f$. The prescribed zero gives
$$
g(-r)
=
e^r f(-r)
=0.
$$
On $\abs z=1$,
$$
\abs{g(z)}
=
e^{-\Re z}\abs{f(z)}
\leq
e^{-\Re z}\abs{e^z}
=1.
$$
:::

:::

::: {.pf-step #blaschke-factor-B}
Define
$$
B(z)\coloneqq\frac{z+r}{1+rz}.
$$
Then $B$ is analytic on a neighborhood of the closed unit disk,
$$
B(-r)=0,
$$
and
$$
\abs{B(z)}=1
$$
for $\abs z=1$.

::: pf-proof
The only pole of $B$ is at
$$
z=-\frac1r,
$$
whose modulus is greater than $1$ because $0<r<1$. Thus $B$ is analytic
near the closed unit disk. Its zero at $-r$ is immediate.

For $\abs z=1$,
$$
\abs{z+r}^2
=
1+r(z+\overline z)+r^2
$$
and
$$
\abs{1+rz}^2
=
1+r(z+\overline z)+r^2.
$$
Hence the two moduli are equal, so $\abs{B(z)}=1$.
:::

:::

::: {.pf-step #quotient-q-bounded}
The quotient
$$
q(z)\coloneqq\frac{g(z)}{B(z)}
$$
extends holomorphically across $z=-r$ and satisfies
$$
\abs{q(z)}\leq1
$$
throughout the closed unit disk.

::: pf-proof
Both $g$ and $B$ vanish at $-r$, while $B$ has a simple zero there.
Therefore $g/B$ has at worst a removable singularity at $-r$, and it
extends holomorphically.

On $\abs z=1$, steps [](#g-normalized-bound){.pf-ref} and [](#blaschke-factor-B){.pf-ref} give
$$
\abs{q(z)}
=
\frac{\abs{g(z)}}{\abs{B(z)}}
\leq1.
$$
The maximum modulus principle then gives the same bound throughout the unit
disk.
:::

:::

::: {.pf-step #g-at-r-bound}
One has
$$
\abs{g(r)}
\leq
\frac{2r}{1+r^2}.
$$

::: pf-proof
Step [](#quotient-q-bounded){.pf-ref} gives
$$
\abs{g(r)}
=
\abs{B(r)}\abs{q(r)}
\leq
\abs{B(r)}.
$$
Since $r$ is real,
$$
B(r)
=
\frac{2r}{1+r^2}.
$$
:::

:::

::: {.pf-step #f-at-log2-bound}
Therefore
$$
\abs{f(\log2)}
\leq
\boxed{
\frac{4\log2}{1+(\log2)^2}
}.
$$

::: pf-proof
Since $f(z)=e^zg(z)$ and $e^r=2$,
$$
\abs{f(r)}
=
2\abs{g(r)}.
$$
Apply step [](#g-at-r-bound){.pf-ref} and substitute $r=\log2$.
:::

:::

::: {.pf-step #bound-attained}
The bound in step [](#f-at-log2-bound){.pf-ref} is attained.

::: pf-proof
For any constant $C$ with $\abs C=1$, define
$$
f_C(z)
\coloneqq
C e^z B(z).
$$
By step [](#blaschke-factor-B){.pf-ref}, this function is analytic on a neighborhood of the closed
unit disk and satisfies
$$
f_C(-r)=0.
$$
On $\abs z=1$,
$$
\abs{f_C(z)}
=
\abs{e^z}\abs{B(z)}
=
\abs{e^z}.
$$
At $z=r$,
$$
\abs{f_C(r)}
=
2\frac{2r}{1+r^2},
$$
which is exactly the bound in step [](#f-at-log2-bound){.pf-ref}.
:::

:::

::: {.pf-step #largest-value}
The largest possible value is
$$
\boxed{
\frac{4\log2}{1+(\log2)^2}
}.
$$

::: pf-proof
Step [](#f-at-log2-bound){.pf-ref} gives the upper bound and step [](#bound-attained){.pf-ref} shows it is sharp.
:::

:::

::: pf-qed
Step [](#largest-value){.pf-ref} answers the question.
:::

:::

:::
