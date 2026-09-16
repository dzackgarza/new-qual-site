---
schema: qual/card@1
id: P-JHUU67CA2
kind: problem
title: Meromorphic function with pole has no holomorphic logarithm
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the pole hypothesis and the full punctured-domain logarithm request with Problem 5 of the undated JHU exam on pages 6–7 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the nonvanishing local factor, the sign and multiplicity in the logarithmic derivative, and vanishing of the integral of a globally defined derivative without assuming simple connectedness."
---

::: {.problem}
Let $U$ be an open subset of $\mathbb{C}$.
Let $z_0$ be a point in $U$, and suppose that $f$ is a meromorphic function on $U$ with a pole at $z_0$.
Prove that there is no holomorphic function $g : U \setminus \{z_0\} \to \mathbb{C}$ such that $e^{g(z)} = f(z)$ for all $z \in U \setminus \{z_0\}$.
:::

::: {.solution}
<1>1. The logarithmic derivative of $f$ has a nonzero integral
around a sufficiently small circle about its pole.

::: {.proof}
Let $m\geq1$ be the order of the pole. The local Laurent
expansion gives
$$
f(z)=(z-z_0)^{-m}h(z),
$$
where $h$ is holomorphic near $z_0$ and $h(z_0)\ne0$
[@SS03]. Choose $r>0$ so that $\overline{D(z_0,r)}\subset U$
and $h$ is holomorphic and nonzero on a neighborhood of
this closed disk. On its punctured interior,
$$
\frac{f'(z)}{f(z)}=-\frac{m}{z-z_0}+\frac{h'(z)}{h(z)}.
$$
For the positively oriented circle $\gamma:|z-z_0|=r$,
Cauchy's theorem applied to the holomorphic function $h'/h$
and the circle parametrization give
$$
\int_\gamma\frac{f'}f\,dz=-2\pi i m\ne0.
$$
:::

<1>2. A holomorphic logarithm would force the same integral to vanish.

::: {.proof}
Suppose the required $g$ existed. On the punctured disk,
differentiation of $e^g=f$ gives $f'/f=g'$. But $g'$ has
the single-valued primitive $g$ there, so
$$
\int_\gamma g'(z)\,dz=0.
$$
Indeed, parametrizing the circle makes the integrand the
derivative of $g(\gamma(t))$, and the starting and ending
values agree. This uses the primitive, not simple
connectedness of the punctured domain. The zero integral
contradicts step <1>1, proving that no such $g$ exists.
:::
:::
