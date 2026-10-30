---
schema: qual/card@1
id: P-BKS21-5A
kind: problem
title: The integral $\int_0^\infty dx/(x^4+1)$ by residues
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2021 upper-half-plane residue calculation. The two poles, their residue sum, and the value $\pi/(2\sqrt2)$ are correct.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the upper-half-plane poles, the simple-pole residues, decay on the semicircular arc, and the final use of evenness.
---

::: {.problem}
Use residues to compute
$$
\int_0^{\infty}\frac{dx}{x^4+1}.
$$
:::

::: {.solution}

Set
$$
h(z)\coloneqq\frac{1}{z^4+1}.
$$

::: pf

::: {.pf-step #s1-1}

The poles of $h$ in the open upper half-plane are
$$
z_1=e^{i\pi/4}=\frac{1+i}{\sqrt2},
\qquad
z_2=e^{3i\pi/4}=\frac{-1+i}{\sqrt2}.
$$


::: pf-proof

The roots of $z^4+1=0$ are the fourth roots of $-1=e^{i(\pi+2\pi m)}$, namely
$$
e^{i(\pi/4+k\pi/2)}
\qquad(k=0,1,2,3).
$$
Exactly the roots with $k=0,1$ have positive imaginary part.

:::

:::

::: {.pf-step #s1-2}

The sum of the residues of $h$ at the poles in step [](#s1-1){.pf-ref} is
$$
\operatorname{Res}_{z=z_1}h+\operatorname{Res}_{z=z_2}h
=
-\frac{i}{2\sqrt2}.
$$


::: pf-proof

The roots of $z^4+1$ are simple, so
$$
\operatorname{Res}_{z=z_j}h
=
\frac{1}{4z_j^3}.
$$
Thus
$$
\operatorname{Res}_{z=z_1}h
=
\frac14e^{-3i\pi/4}
=
\frac{-1-i}{4\sqrt2},
$$
and
$$
\operatorname{Res}_{z=z_2}h
=
\frac14e^{-9i\pi/4}
=
\frac14e^{-i\pi/4}
=
\frac{1-i}{4\sqrt2}.
$$
Adding gives the claimed value.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_{-\infty}^{\infty}\frac{dx}{x^4+1}
=
\frac{\pi}{\sqrt2}.
$$


::: pf-proof

Integrate $h$ over the positively oriented contour consisting of $[-R,R]$ and the upper semicircle $\Gamma_R$, with $R>1$. By the residue theorem and step [](#s1-2){.pf-ref},
$$
\int_{-R}^{R}\frac{dx}{x^4+1}
+
\int_{\Gamma_R}h(z)\,dz
=
2\pi i\left(-\frac{i}{2\sqrt2}\right)
=
\frac{\pi}{\sqrt2}.
$$
For $z\in\Gamma_R$,
$$
\abs{z^4+1}
\geq
\abs{z}^4-1
=
R^4-1.
$$
Since $\Gamma_R$ has length $\pi R$,
$$
\abs{\int_{\Gamma_R}h(z)\,dz}
\leq
\frac{\pi R}{R^4-1}
\longrightarrow0.
$$
Letting $R\to\infty$ gives the displayed integral.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\displaystyle
\int_0^{\infty}\frac{dx}{x^4+1}
=
\frac{\pi}{2\sqrt2}
}.
$$


::: pf-proof

The integrand is even, so
$$
\int_{-\infty}^{\infty}\frac{dx}{x^4+1}
=
2\int_0^\infty\frac{dx}{x^4+1}.
$$
Apply step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value.

:::

:::

:::
