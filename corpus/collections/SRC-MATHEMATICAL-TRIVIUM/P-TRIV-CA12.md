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
Compute $\int_0^{\infty} \frac{1}{1 + x^2}\, \mathrm{d}x$.
:::

::: {.solution}

Let
$$
F(z)=\frac1{1+z^2}
=
\frac1{(z-i)(z+i)}.
$$

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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
theorem and step [](#s1-1){.pf-ref},
$$
\int_{C_R}F(z),dz
=
2\pi i\cdot\frac1{2i}
=
\pi.
$$

:::

:::

::: {.pf-step #s1-3}

On the semicircular arc $\Gamma_R$,
$$
\abs{F(z)}
\leq
\frac1{R^2-1}.
$$


::: pf-proof

For $\abs{z}=R$,
$$
\abs{1+z^2}
\geq
\abs{\abs{z}^2-1}
=
R^2-1
$$
by the reverse triangle inequality. Taking reciprocals gives the bound.

:::

:::

::: {.pf-step #s1-4}

The arc integral tends to zero:
$$
\int_{\Gamma_R}F(z),dz
\longrightarrow0
$$
as $R\to\infty$.


::: pf-proof

The length of $\Gamma_R$ is $\pi R$. By the $ML$ estimate and step [](#s1-3){.pf-ref},
$$
\abs{
\int_{\Gamma_R}F(z),dz
}
\leq
\frac{\pi R}{R^2-1}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
\int_{-\infty}^{\infty}
\frac{dx}{1+x^2}
=
\pi.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\int_{-R}^{R}\frac{dx}{1+x^2}
+
\int_{\Gamma_R}F(z),dz
=
\pi.
$$
Let $R\to\infty$ and use step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

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
Apply step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required value.

:::

:::

:::
