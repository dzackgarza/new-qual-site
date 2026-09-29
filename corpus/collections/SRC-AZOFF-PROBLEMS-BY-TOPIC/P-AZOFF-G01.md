---
schema: qual/card@1
id: P-AZOFF-G01
kind: problem
title: $\int_0^\infty\frac{dx}{(1+x^2)(1+9x^2)}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Followed the source section's instruction to use complex-variable
    methods: integrated the rational function over an upper semicircle,
    showed the arc contribution tends to zero, summed the residues at i and
    i/3, and used evenness to recover the half-line integral.
---

::: {.problem}
Calculate $\textstyle \int _ { 0 } ^ { \infty } { \frac { d x } { ( 1 + x ^ { 2 } ) ( 1 + 9 x ^ { 2 } ) } }$
:::

::: {.solution}
Set
$$
F(z)=\frac1{(1+z^2)(1+9z^2)}.
$$
For $R>1$, let $C_R$ be the positively oriented contour consisting of the
interval $[-R,R]$ and the upper semicircle
$$
\Gamma_R=\{Re^{i\theta}:0\leq\theta\leq\pi\}.
$$

::: pf

::: {.pf-step #s1}

The only poles of $F$ inside $C_R$ are
$$
z=i
\qquad\text{and}\qquad
z=\frac i3,
$$
and
$$
\Res(F;i)
=
\frac{i}{16},
\qquad
\Res\left(F;\frac i3\right)
=
-\frac{3i}{16}.
$$

::: pf-proof

The poles are the zeros of
$$
(1+z^2)(1+9z^2),
$$
namely
$$
\pm i,
\qquad
\pm\frac i3.
$$
The two with positive imaginary part lie inside $C_R$ for $R>1$.

At $z=i$,
$$
\begin{aligned}
\Res(F;i)
&=
\frac1{(2i)(1+9i^2)}\\
&=
\frac1{-16i}
=
\frac{i}{16}.
\end{aligned}
$$
At $z=i/3$, using
$$
\frac{d}{dz}(1+9z^2)=18z,
$$
one gets
$$
\begin{aligned}
\Res\left(F;\frac i3\right)
&=
\frac1{
\left(1+(i/3)^2\right)
18(i/3)
}\\
&=
\frac1{(8/9)(6i)}\\
&=
-\frac{3i}{16}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The integral of $F$ over the semicircular arc tends to zero:
$$
\int_{\Gamma_R}F(z)\,dz\longrightarrow0
$$
as $R\to\infty$.

::: pf-proof

On $\Gamma_R$,
$$
\abs{1+z^2}\geq R^2-1
$$
and
$$
\abs{1+9z^2}\geq9R^2-1.
$$
Hence
$$
\abs{F(z)}
\leq
\frac1{(R^2-1)(9R^2-1)}.
$$
The arc has length $\pi R$, so the ML estimate gives
$$
\abs{
\int_{\Gamma_R}F(z)\,dz
}
\leq
\frac{\pi R}{(R^2-1)(9R^2-1)}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s3}

The integral over the whole real line is
$$
\int_{-\infty}^{\infty}
\frac{dx}{(1+x^2)(1+9x^2)}
=
\frac{\pi}{4}.
$$

::: pf-proof

By the residue theorem and step [](#s1){.pf-ref},
$$
\begin{aligned}
\int_{C_R}F(z)\,dz
&=
2\pi i
\left(
\frac{i}{16}
-\frac{3i}{16}
\right)\\
&=
2\pi i\left(-\frac{i}{8}\right)\\
&=
\frac{\pi}{4}.
\end{aligned}
$$
Splitting the contour integral,
$$
\int_{-R}^{R}F(x)\,dx
+
\int_{\Gamma_R}F(z)\,dz
=
\frac{\pi}{4}.
$$
Letting $R\to\infty$ and using step [](#s2){.pf-ref} gives the displayed real-line
integral.

:::

:::

::: {.pf-step #s4}

The requested integral is
$$
\boxed{
\int_0^{\infty}
\frac{dx}{(1+x^2)(1+9x^2)}
=
\frac{\pi}{8}.
}
$$

::: pf-proof

The integrand is even. Therefore step [](#s3){.pf-ref} gives
$$
2\int_0^{\infty}
\frac{dx}{(1+x^2)(1+9x^2)}
=
\frac{\pi}{4}.
$$
Divide by $2$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the requested value.

:::

:::

:::
