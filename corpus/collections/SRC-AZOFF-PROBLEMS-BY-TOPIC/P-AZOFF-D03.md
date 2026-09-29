---
schema: qual/card@1
id: P-AZOFF-D03
kind: problem
title: Locally uniform limits of analytic functions are analytic
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Fixed an arbitrary point and a closed disk compactly contained in the
    unit disk. Uniform convergence on the boundary circle lets Cauchy's
    integral formula pass to the limit. The resulting Cauchy integral is
    holomorphic in the disk, so it equals g on a neighborhood of the chosen
    point. The source compilation contains no worked solution.
---

::: {.problem}
Suppose $( f _ { n } ) _ { n \in \mathbb { N } }$ is a sequence of analytic functions on $\mathbb { D } : = \{ z \in \mathbb { C } : | z | < 1 \}$ Show that if $\left( f _ { n } \right)$ converges to a function $g\colon \DD \to \CC$ uniformly on each compact subset of $\DD$, then $g$ is analytic on $\DD$.
:::

::: {.solution}
Let
$$
\DD=\{z\in\CC:\abs z<1\}
$$
and fix
$$
z_0\in\DD.
$$

::: pf

::: {.pf-step #s1}

Choose $R>0$ such that
$$
\overline{B(z_0,R)}\subseteq\DD.
$$
Then
$$
f_n\longrightarrow g
$$
uniformly on the circle
$$
\Gamma=\{\zeta\in\CC:\abs{\zeta-z_0}=R\}.
$$

::: pf-proof

Because $\DD$ is open, there is $R>0$ with the closed disk contained in
$\DD$. The circle $\Gamma$ is compact, so the hypothesis of uniform
convergence on every compact subset applies to $\Gamma$.

:::

:::

::: {.pf-step #s2}

For every $z$ with
$$
\abs{z-z_0}<R,
$$
one has
$$
g(z)
=
\frac{1}{2\pi i}
\int_\Gamma
\frac{g(\zeta)}{\zeta-z}\,d\zeta.
$$

::: pf-proof

Fix such a $z$. Cauchy's integral formula gives, for every $n$,
$$
f_n(z)
=
\frac{1}{2\pi i}
\int_\Gamma
\frac{f_n(\zeta)}{\zeta-z}\,d\zeta.
$$
Since $f_n(z)\to g(z)$ pointwise and step [](#s1){.pf-ref} gives uniform convergence on
$\Gamma$, we have
$$
\begin{aligned}
&\left|
\int_\Gamma
\frac{f_n(\zeta)-g(\zeta)}{\zeta-z}\,d\zeta
\right|\\
&\qquad\leq
\frac{\operatorname{length}(\Gamma)}
{\operatorname{dist}(z,\Gamma)}
\sup_{\zeta\in\Gamma}\abs{f_n(\zeta)-g(\zeta)}
\longrightarrow0.
\end{aligned}
$$
Passing to the limit in Cauchy's formula gives the displayed identity.

:::

:::

::: {.pf-step #s3}

The function
$$
G(z)
=
\frac{1}{2\pi i}
\int_\Gamma
\frac{g(\zeta)}{\zeta-z}\,d\zeta
$$
is holomorphic on
$$
B(z_0,R).
$$

::: pf-proof

Fix
$$
z\in B(z_0,R).
$$
For $h$ sufficiently small,
$$
\begin{aligned}
\frac{G(z+h)-G(z)}h
&=
\frac{1}{2\pi i}
\int_\Gamma
\frac{g(\zeta)}
{(\zeta-z-h)(\zeta-z)}
\,d\zeta.
\end{aligned}
$$
As $h\to0$, the integrand converges uniformly on $\Gamma$ to
$$
\frac{g(\zeta)}{(\zeta-z)^2},
$$
because $z$ has positive distance from $\Gamma$. Therefore
$$
G'(z)
=
\frac{1}{2\pi i}
\int_\Gamma
\frac{g(\zeta)}{(\zeta-z)^2}\,d\zeta.
$$
Thus the complex derivative exists at every point of the disk, so $G$ is
holomorphic there.

:::

:::

::: {.pf-step #s4}

The function $g$ is holomorphic on a neighborhood of $z_0$.

::: pf-proof

Step [](#s2){.pf-ref} says exactly that
$$
g(z)=G(z)
$$
for every
$$
z\in B(z_0,R).
$$
Step [](#s3){.pf-ref} shows that $G$ is holomorphic on this disk. Hence $g$ is
holomorphic there.

:::

:::

::: {.pf-step #s5}

The function $g$ is analytic on all of $\DD$.

::: pf-proof

The point $z_0\in\DD$ was arbitrary. By step [](#s4){.pf-ref}, every point of $\DD$ has
a neighborhood on which $g$ is holomorphic. Therefore $g$ is holomorphic,
hence analytic, on $\DD$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
