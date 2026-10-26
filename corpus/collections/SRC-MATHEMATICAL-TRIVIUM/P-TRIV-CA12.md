---
schema: qual/card@1
id: P-TRIV-CA12
kind: problem
title: $\int_0^\infty \frac{dx}{1+x^2}$ by residues
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute $\int _ { 0 } ^ { \infty } \frac { 1 } { 1 + x ^ { 2 } } \mathrm { d } x ;$
:::

Let
$$
F(z)=\frac1{1+z^2}
=
\frac1{(z-i)(z+i)}.
$$

::: pf

::: pf-step

The function $F$ has a simple pole at $z=i$ with residue
$$
\operatorname{Res}_{z=i}F(z)
=
\frac1{2i}.
$$


::: pf-proof

Since
$$
F(z)=\frac1{(z-i)(z+i)},
$$
one has
$$
\operatorname{Res}_{z=i}F(z)
=
\lim_{z\to i}
\frac{z-i}{(z-i)(z+i)}
=
\frac1{2i}.
$$

:::

:::

::: pf-step

Let $C_R$ be the positively oriented contour consisting of
$[-R,R]$ and the upper semicircle
$$
\Gamma_R=\{Re^{it}:0\leq t\leq\pi\},
$$
where $R>1$. Then
$$
\int_{C_R}F(z),dz
=
\pi.
$$


::: pf-proof

The only pole of $F$ inside the upper semicircle is $z=i$. By the residue
theorem and step <1>1,
$$
\int_{C_R}F(z),dz
=
2\pi i\cdot\frac1{2i}
=
\pi.
$$

:::

:::

::: pf-step

On the semicircular arc $\Gamma_R$,
$$
|F(z)|
\leq
\frac1{R^2-1}.
$$


::: pf-proof

For $|z|=R$,
$$
|1+z^2|
\geq
\bigl||z|^2-1\bigr|
=
R^2-1
$$
by the reverse triangle inequality. Taking reciprocals gives the bound.

:::

:::

::: pf-step

The arc integral tends to zero:
$$
\int_{\Gamma_R}F(z),dz
\longrightarrow0
$$
as $R\to\infty$.


::: pf-proof

The length of $\Gamma_R$ is $\pi R$. By the $ML$ estimate and step <1>3,
$$
\left|
\int_{\Gamma_R}F(z),dz
\right|
\leq
\frac{\pi R}{R^2-1}
\longrightarrow0.
$$

:::

:::

::: pf-step

One has
$$
\int_{-\infty}^{\infty}
\frac{dx}{1+x^2}
=
\pi.
$$


::: pf-proof

By step <1>2,
$$
\int_{-R}^{R}\frac{dx}{1+x^2}
+
\int_{\Gamma_R}F(z),dz
=
\pi.
$$
Let $R\to\infty$ and use step <1>4.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\int_0^{\infty}
\frac{dx}{1+x^2}
=
\frac\pi2.
}
$$


::: pf-proof

The integrand is even, so
$$
\int_{-\infty}^{\infty}
\frac{dx}{1+x^2}
=
2
\int_0^{\infty}
\frac{dx}{1+x^2}.
$$
Apply step <1>5.

:::

:::

::: pf-qed

Step <1>6 is the required value.

:::

:::
