---
schema: qual/card@1
id: P-TRIV-CA13
kind: problem
title: $\int_{-\infty}^\infty \frac{dx}{1+x^6}$ by residues
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 13, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute $\int_{-\infty}^{\infty} \frac{1}{1 + x^6}\, \mathrm{d}x$.
:::

::: {.solution}

Let
$$
F(z)=\frac1{1+z^6}.
$$

::: pf

::: pf-step

The poles of $F$ in the upper half-plane are
$$
\zeta_1=e^{i\pi/6},
\qquad
\zeta_2=i,
\qquad
\zeta_3=e^{5i\pi/6}.
$$


::: pf-proof

The poles are the six roots
$$
e^{i(2k+1)\pi/6},
\qquad
k=0,1,\ldots,5,
$$
of $z^6=-1$. Exactly the three listed roots have positive imaginary part.

:::

:::

::: {.pf-step #s1-2}

If $\zeta^6=-1$, then
$$
\operatorname{Res}_{z=\zeta}F(z)
=
-\frac{\zeta}{6}.
$$


::: pf-proof

The pole is simple, so
$$
\operatorname{Res}_{z=\zeta}F(z)
=
\frac1{6\zeta^5}.
$$
Since $\zeta^6=-1$,
$$
\zeta^{-5}=-\zeta.
$$

:::

:::

::: {.pf-step #s1-3}

The sum of the residues in the upper half-plane is
$$
-\frac{i}{3}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\sum_{j=1}^{3}
\operatorname{Res}_{z=\zeta_j}F(z)
=
-\frac16
\left(
e^{i\pi/6}+i+e^{5i\pi/6}
\right).
$$
Since
$$
e^{i\pi/6}+e^{5i\pi/6}=i,
$$
the expression in parentheses is $2i$.

:::

:::

::: {.pf-step #s1-4}

Let $C_R$ be the positively oriented contour consisting of
$[-R,R]$ and the upper semicircle of radius $R$, with $R>1$. Then
$$
\int_{C_R}F(z)\,dz
=
\frac{2\pi}{3}.
$$


::: pf-proof

By the residue theorem and step [](#s1-3){.pf-ref},
$$
\int_{C_R}F(z)\,dz
=
2\pi i
\left(-\frac{i}{3}\right)
=
\frac{2\pi}{3}.
$$

:::

:::

::: {.pf-step #s1-5}

The integral over the upper semicircle tends to zero as
$R\to\infty$.


::: pf-proof

On $\abs{z}=R$,
$$
\abs{1+z^6}
\geq
R^6-1.
$$
The arc length is $\pi R$. Thus the $ML$ estimate gives
$$
\abs{
\int_{\Gamma_R}F(z)\,dz
}
\leq
\frac{\pi R}{R^6-1}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{dx}{1+x^6}
=
\frac{2\pi}{3}.
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives
$$
\int_{-R}^{R}\frac{dx}{1+x^6}
+
\int_{\Gamma_R}F(z)\,dz
=
\frac{2\pi}{3}.
$$
Let $R\to\infty$ and use step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required value.

:::

:::

:::
