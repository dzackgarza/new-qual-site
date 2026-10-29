---
schema: qual/card@1
id: P-JJHVX
kind: problem
title: Once complex differentiable implies holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: statement-edited
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The statement did not say what Omega is; it now says Omega is an open set. Its single bullet marker was removed.
---

::: {.problem}
Let $\Omega \subseteq \CC$ be open.
Show that if $f$ is once complex differentiable at each point of $\Omega$, then $f$ is holomorphic.
:::

::: {.solution}
Here holomorphic means analytic: locally given by a convergent power series.
For a closed triangle $T$ we write $\partial T$ for its positively oriented boundary.

::: pf

::: {.pf-step #goursat}
$\int_{\partial T} f\,dz = 0$ for every closed triangle $T \subset \Omega$.

::: pf-proof

::: {.pf-step #nested-sequence}
If $\abs{\int_{\partial T} f\,dz} = M$, there are nested closed triangles $T = T_0 \supset T_1 \supset \cdots$ with $\abs{\int_{\partial T_n} f\,dz} \geq M/4^n$, $\operatorname{diam}(T_n) = 2^{-n} d$ and $\operatorname{perim}(T_n) = 2^{-n} p$, where $d$ and $p$ are the diameter and perimeter of $T$.

::: pf-proof
Join the midpoints of the sides of $T_n$ to divide it into four congruent triangles.
The four boundary integrals sum to $\int_{\partial T_n} f\,dz$, because the interior edges cancel, so one of them has modulus at least $\frac14\abs{\int_{\partial T_n} f\,dz}$; let $T_{n+1}$ be that triangle.
:::

:::

::: {.pf-step #local-estimate}
Let $z_0 \in \bigcap_n T_n$, and write $f(z) = f(z_0) + f'(z_0)(z - z_0) + (z - z_0)\varepsilon(z)$ with $\varepsilon(z) \to 0$ as $z \to z_0$.
Then $\abs{\int_{\partial T_n} f\,dz} \leq \frac{dp}{4^n}\sup_{z \in T_n} \abs{\varepsilon(z)}$.

::: pf-proof
The intersection of nested nonempty compact sets is nonempty, and $z_0 \in T \subset \Omega$, so $f$ is complex differentiable at $z_0$.
The polynomial $f(z_0) + f'(z_0)(z - z_0)$ has a primitive, so its integral over the closed curve $\partial T_n$ vanishes.
On $\partial T_n$, $\abs{z - z_0} \leq \operatorname{diam}(T_n)$, and the length of $\partial T_n$ is $\operatorname{perim}(T_n)$.
:::

:::

::: pf-qed
By steps [](#nested-sequence){.pf-ref} and [](#local-estimate){.pf-ref}, $M \leq dp \sup_{z \in T_n}\abs{\varepsilon(z)}$ for every $n$.
Since $\operatorname{diam}(T_n) \to 0$ and $z_0 \in T_n$, the supremum tends to $0$, so $M = 0$.
:::

:::

:::

::: pf-step
$f$ is holomorphic on $\Omega$.

::: pf-proof
$f$ is continuous, being complex differentiable at every point.
On each open disc $D \subseteq \Omega$, step [](#goursat){.pf-ref} lets Morera's theorem apply, so $f$ is analytic on $D$.
:::

:::

:::
:::
