---
schema: qual/card@1
id: P-BKF10-7A
kind: problem
title: Evaluation of $\int_{-\infty}^{\infty}\sin x/(x^2+4x+5)\,dx$ by residues
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 7A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the upper-half-plane pole, residue, direct semicircle decay,
    and extraction of the imaginary part.
---

::: {.problem}
Use residues to compute
$$
\int_{-\infty}^{\infty}\frac{\sin x}{x^2+4x+5}\,dx.
$$
:::

::: {.solution}
Consider
$$
F(z)\coloneqq\frac{e^{iz}}{z^2+4z+5}
=\frac{e^{iz}}{(z+2-i)(z+2+i)}.
$$

::: pf

::: {.pf-step #s1}

The only pole of $F$ in the upper half-plane is
$$
z_0=-2+i,
$$
and
$$
\operatorname{Res}_{z=z_0}F(z)
=\frac{e^{-1-2i}}{2i}.
$$

::: pf-proof

The denominator factors as
$$
(z+2-i)(z+2+i),
$$
so its poles are $-2+i$ and $-2-i$, of which only the first lies in the
upper half-plane. Since the pole is simple,
$$
\begin{aligned}
\operatorname{Res}_{z=-2+i}F(z)
&=\frac{e^{i(-2+i)}}{(-2+i)-(-2-i)}\\
&=\frac{e^{-1-2i}}{2i}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

Let $\Gamma_R$ be the upper semicircle $\abs{z}=R$. Then
$$
\int_{\Gamma_R}F(z)\,dz\longrightarrow0
$$
as $R\to\infty$.

::: pf-proof

For $z$ in the upper half-plane,
$$
\abs{e^{iz}}=e^{-\operatorname{Im}z}\le1.
$$
On $\abs{z}=R$, the reverse triangle inequality gives
$$
\abs{z+2\pm i}\ge R-\sqrt5.
$$
Thus, for $R>\sqrt5$,
$$
\abs{F(z)}
\le\frac1{(R-\sqrt5)^2}.
$$
Since $\Gamma_R$ has length $\pi R$, the ML estimate gives
$$
\abs{\int_{\Gamma_R}F(z)\,dz}
\le\frac{\pi R}{(R-\sqrt5)^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
\int_{-\infty}^{\infty}
\frac{e^{ix}}{x^2+4x+5}\,dx
=\frac{\pi}{e}e^{-2i}.
$$

::: pf-proof

For $R>\sqrt5$, integrate $F$ around the positively oriented contour
consisting of $[-R,R]$ and $\Gamma_R$. By step [](#s1){.pf-ref} and the residue
theorem,
$$
\int_{-R}^R F(x)\,dx
+\int_{\Gamma_R}F(z)\,dz
=2\pi i\frac{e^{-1-2i}}{2i}
=\frac{\pi}{e}e^{-2i}.
$$
The real-line integral converges absolutely because its integrand is
$O(x^{-2})$. Letting $R\to\infty$ and using step [](#s2){.pf-ref} gives the claim.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{\sin x}{x^2+4x+5}\,dx
=-\frac{\pi}{e}\sin2
}.
$$

::: pf-proof

For real $x$, the denominator is real, so the desired integral is the
imaginary part of the complex integral in step [](#s3){.pf-ref}. Since
$$
e^{-2i}=\cos2-i\sin2,
$$
its imaginary part is $-(\pi/e)\sin2$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the requested residue evaluation.

:::

:::

:::
