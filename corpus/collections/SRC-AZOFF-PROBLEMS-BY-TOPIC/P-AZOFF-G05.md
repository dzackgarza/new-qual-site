---
schema: qual/card@1
id: P-AZOFF-G05
kind: problem
title: $\int_0^\infty\frac{x^2}{(x^2+a^2)^2}\,dx$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Integrated z^2/(z^2+a^2)^2 over an upper semicircle. The arc integral
    tends to zero, the only enclosed singularity is the double pole at ia
    with residue -i/(4a), and evenness gives the half-line value pi/(4a).
---

::: {.problem}
Let $a > 0$ . Evaluate $\begin{array} { r } { \int _ { 0 } ^ { \infty } \frac { x ^ { 2 } } { ( x ^ { 2 } + a ^ { 2 } ) ^ { 2 } } d x } \end{array}$
:::

::: {.solution}
Set
$$
F(z)=\frac{z^2}{(z^2+a^2)^2}.
$$
For $R>a$, let $C_R$ be the positively oriented contour consisting of
$[-R,R]$ and the upper semicircle of radius $R$.

::: pf

::: {.pf-step #s1}

The only pole of $F$ inside $C_R$ is the double pole at $z=ia$, and
$$
\Res(F;ia)
=
-\frac{i}{4a}.
$$

::: pf-proof

Factor
$$
(z^2+a^2)^2
=
(z-ia)^2(z+ia)^2.
$$
Thus
$$
(z-ia)^2F(z)
=
\frac{z^2}{(z+ia)^2}.
$$
For a double pole,
$$
\Res(F;ia)
=
\left.
\frac{d}{dz}
\left(
\frac{z^2}{(z+ia)^2}
\right)
\right|_{z=ia}.
$$
Differentiating,
$$
\frac{d}{dz}
\left(
\frac{z^2}{(z+ia)^2}
\right)
=
\frac{2z}{(z+ia)^2}
-\frac{2z^2}{(z+ia)^3}.
$$
At $z=ia$ this becomes
$$
\begin{aligned}
\Res(F;ia)
&=
\frac{2ia}{(2ia)^2}
-\frac{2(ia)^2}{(2ia)^3}\\
&=
-\frac{i}{2a}
+\frac{i}{4a}\\
&=
-\frac{i}{4a}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The integral over the upper semicircular arc tends to zero as
$R\to\infty$.

::: pf-proof

On $\abs{z}=R$,
$$
\abs{z^2+a^2}
\geq
R^2-a^2.
$$
Hence
$$
\abs{F(z)}
\leq
\frac{R^2}{(R^2-a^2)^2}.
$$
The arc has length $\pi R$, so
$$
\abs{
\int_{\text{arc}}F(z)\,dz
}
\leq
\frac{\pi R^3}{(R^2-a^2)^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s3}

The whole-line integral is
$$
\int_{-\infty}^{\infty}
\frac{x^2}{(x^2+a^2)^2}\,dx
=
\frac{\pi}{2a}.
$$

::: pf-proof

By the residue theorem and step [](#s1){.pf-ref},
$$
\int_{C_R}F(z)\,dz
=
2\pi i
\left(-\frac{i}{4a}\right)
=
\frac{\pi}{2a}.
$$
Split the contour into the real segment and arc, let $R\to\infty$, and
use step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The requested value is
$$
\boxed{
\int_0^{\infty}
\frac{x^2}{(x^2+a^2)^2}\,dx
=
\frac{\pi}{4a}.
}
$$

::: pf-proof

The integrand is even, so step [](#s3){.pf-ref} is twice the half-line integral.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the requested evaluation.

:::

:::

:::
