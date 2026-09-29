---
schema: qual/card@1
id: P-BERK85S-04
kind: problem
title: Taylor coefficients of a function with one simple pole on the unit circle have a limit
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Subtracted the principal part at z=1, then used Cauchy's coefficient
    estimate on a circle of radius rho with 1<rho<R to show that the
    remaining Taylor coefficients tend to zero.
---

::: {.problem}
Let $R>1$ and let $f$ be analytic on $|z|<R$ except for a simple pole at $z=1$. Suppose
\[
f(z)=\sum_{n=0}^\infty a_nz^n
\qquad(|z|<1).
\]
Show that
\[
\lim_{n\to\infty}a_n
\]
exists.
:::

::: {.solution}
Let
$$
c\coloneqq\operatorname{Res}_{z=1}f(z).
$$

::: pf

::: {.pf-step #g-is-holomorphic}
The function
$$
g(z)\coloneqq f(z)-\frac{c}{z-1}
$$
extends holomorphically to the whole disk $\abs{z}<R$.

::: pf-proof
Because $z=1$ is a simple pole of $f$ with residue $c$, its Laurent
expansion near $1$ has the form
$$
f(z)=\frac{c}{z-1}+h(z),
$$
where $h$ is holomorphic near $1$. Thus $g=h$ near the puncture, so the
singularity of $g$ at $1$ is removable. Away from $1$, both terms defining
$g$ are holomorphic on $\abs{z}<R$.
:::

:::

::: {.pf-step #bn-tends-to-zero}
Write
$$
g(z)=\sum_{n=0}^{\infty}b_nz^n
$$
near $0$. Then
$$
b_n\longrightarrow0.
$$

::: pf-proof
Choose any $\rho$ with
$$
1<\rho<R.
$$
By step [](#g-is-holomorphic){.pf-ref}, $g$ is holomorphic on a neighborhood of the closed disk
$\abs{z}\leq\rho$. Set
$$
M_\rho\coloneqq\max_{\abs{z}=\rho}\abs{g(z)}.
$$
Cauchy's coefficient formula gives
$$
b_n
=
\frac{1}{2\pi i}
\int_{\abs{z}=\rho}
\frac{g(z)}{z^{n+1}}\,dz,
$$
and hence
$$
\abs{b_n}
\leq
\frac{M_\rho}{\rho^n}.
$$
Since $\rho>1$, the right-hand side tends to $0$.
:::

:::

::: {.pf-step #an-formula}
For every $n\geq0$,
$$
a_n=b_n-c.
$$

::: pf-proof
For $\abs{z}<1$,
$$
\frac{c}{z-1}
=
-\frac{c}{1-z}
=
-c\sum_{n=0}^{\infty}z^n.
$$
Since $f=g+c/(z-1)$, comparison with the Maclaurin series of $f$ gives
$a_n=b_n-c$.
:::

:::

::: {.pf-step #limit-boxed}
Therefore
$$
\boxed{
\lim_{n\to\infty}a_n
=
-\operatorname{Res}_{z=1}f(z)
}.
$$

::: pf-proof
By step [](#an-formula){.pf-ref},
$$
a_n=b_n-c,
$$
and step [](#bn-tends-to-zero){.pf-ref} gives $b_n\to0$.
:::

:::

::: pf-qed
Step [](#limit-boxed){.pf-ref} proves, in particular, that the required limit exists.
:::

:::
:::
