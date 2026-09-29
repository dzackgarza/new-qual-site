---
schema: qual/card@1
id: P-AZOFF-G10
kind: problem
title: $\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Integrated exp(iz)/(z^2+a^2)^2 over an upper semicircle. The large arc
    vanishes, the only enclosed singularity is the double pole at ia with
    residue -i e^(-a)(a+1)/(4a^3), and real parts plus evenness give
    pi e^(-a)(a+1)/(4a^3).
---

::: {.problem}
Let $a > 0$ . Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \cos x } { ( x ^ { 2 } + a ^ { 2 } ) ^ { 2 } } } d x$
:::

::: {.solution}
Set
$$
F(z)=\frac{e^{iz}}{(z^2+a^2)^2}.
$$
For $R>a$, integrate $F$ over the positively oriented upper semicircle with
diameter $[-R,R]$.

::: pf

::: {.pf-step #s1}

The only pole of $F$ inside the contour is the double pole at
$z=ia$, and
$$
\Res(F;ia)
=
-\frac{i e^{-a}(a+1)}{4a^3}.
$$

::: pf-proof

Factor
$$
(z^2+a^2)^2
=
(z-ia)^2(z+ia)^2.
$$
For the double pole at $ia$,
$$
\Res(F;ia)
=
\left.
\frac{d}{dz}
\left(
\frac{e^{iz}}{(z+ia)^2}
\right)
\right|_{z=ia}.
$$
Differentiating gives
$$
\frac{d}{dz}
\left(
\frac{e^{iz}}{(z+ia)^2}
\right)
=
\frac{i e^{iz}}{(z+ia)^2}
-\frac{2e^{iz}}{(z+ia)^3}.
$$
At $z=ia$,
$$
\begin{aligned}
\Res(F;ia)
&=
\frac{i e^{-a}}{(2ia)^2}
-\frac{2e^{-a}}{(2ia)^3}\\
&=
-\frac{i e^{-a}}{4a^2}
-\frac{i e^{-a}}{4a^3}\\
&=
-\frac{i e^{-a}(a+1)}{4a^3}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The integral over the upper semicircular arc tends to zero as
$R\to\infty$.

::: pf-proof

For $z$ in the upper half-plane,
$$
\abs{e^{iz}}\leq1.
$$
On $\abs{z}=R$,
$$
\abs{z^2+a^2}
\geq
R^2-a^2.
$$
Therefore
$$
\abs{F(z)}
\leq
\frac1{(R^2-a^2)^2}.
$$
The arc has length $\pi R$, so the ML estimate gives
$$
\abs{
\int_{\text{arc}}F(z)\,dz
}
\leq
\frac{\pi R}{(R^2-a^2)^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
\int_{-\infty}^{\infty}
\frac{e^{ix}}{(x^2+a^2)^2}\,dx
=
\frac{\pi e^{-a}(a+1)}{2a^3}.
$$

::: pf-proof

By the residue theorem and step [](#s1){.pf-ref},
$$
\begin{aligned}
\int_{C_R}F(z)\,dz
&=
2\pi i\Res(F;ia)\\
&=
2\pi i
\left(
-\frac{i e^{-a}(a+1)}{4a^3}
\right)\\
&=
\frac{\pi e^{-a}(a+1)}{2a^3}.
\end{aligned}
$$
The real-axis integrand is absolutely integrable because its modulus is
$(x^2+a^2)^{-2}$. Split the contour into the real segment and the arc, let
$R\to\infty$, and use step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The whole-line cosine integral is
$$
\int_{-\infty}^{\infty}
\frac{\cos x}{(x^2+a^2)^2}\,dx
=
\frac{\pi e^{-a}(a+1)}{2a^3}.
$$

::: pf-proof

Take real parts in step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The requested value is
$$
\boxed{
\int_0^{\infty}
\frac{\cos x}{(x^2+a^2)^2}\,dx
=
\frac{\pi e^{-a}(a+1)}{4a^3}.
}
$$

::: pf-proof

The integrand in step [](#s4){.pf-ref} is even, so its whole-line integral is twice the
half-line integral.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the requested evaluation.

:::

:::

:::
