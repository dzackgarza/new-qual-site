---
schema: qual/card@1
id: P-AZOFF-G12
kind: problem
title: A contour integral equal to $\frac{\sin n\theta}{\sin\theta}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Factored the denominator as (z-e^(i theta))(z-e^(-i theta)). Both simple
    poles lie inside |z|=2, and the sum of their residues is
    sin(n theta)/sin(theta), so the residue theorem gives the stated
    normalized contour integral.
---

::: {.problem}
Let $n$ be a positive integer and $0 < \theta < \pi$ . Prove that

$$
{ \frac { 1 } { 2 \pi i } } \int _ { | z | = 2 } { \frac { z ^ { n } } { 1 - 2 z \cos \theta + z ^ { 2 } } } d z = { \frac { \sin n \theta } { \sin \theta } } .
$$
:::

::: {.solution}
Set
$$
F(z)
=
\frac{z^n}{1-2z\cos\theta+z^2}.
$$

::: pf

::: {.pf-step #s1}

The denominator factors as
$$
1-2z\cos\theta+z^2
=
(z-e^{i\theta})(z-e^{-i\theta}).
$$

::: pf-proof

Since
$$
e^{i\theta}+e^{-i\theta}=2\cos\theta
$$
and
$$
e^{i\theta}e^{-i\theta}=1,
$$
expanding the right-hand side gives
$$
z^2-2z\cos\theta+1.
$$

:::

:::

::: {.pf-step #s2}

The only poles of $F$ are the distinct simple poles
$$
e^{i\theta}
\qquad\text{and}\qquad
e^{-i\theta},
$$
and both lie inside the contour $\abs{z}=2$.

::: pf-proof

By step [](#s1){.pf-ref} these are the only zeros of the denominator. They are distinct
because $0<\theta<\pi$, and both have modulus $1<2$.

:::

:::

::: {.pf-step #s3}

The residue at $z=e^{i\theta}$ is
$$
\Res(F;e^{i\theta})
=
\frac{e^{in\theta}}{2i\sin\theta}.
$$

::: pf-proof

Using the factorization in step [](#s1){.pf-ref},
$$
\begin{aligned}
\Res(F;e^{i\theta})
&=
\frac{e^{in\theta}}
{e^{i\theta}-e^{-i\theta}}\\
&=
\frac{e^{in\theta}}{2i\sin\theta}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

The residue at $z=e^{-i\theta}$ is
$$
\Res(F;e^{-i\theta})
=
-\frac{e^{-in\theta}}{2i\sin\theta}.
$$

::: pf-proof

Again by step [](#s1){.pf-ref},
$$
\begin{aligned}
\Res(F;e^{-i\theta})
&=
\frac{e^{-in\theta}}
{e^{-i\theta}-e^{i\theta}}\\
&=
-\frac{e^{-in\theta}}{2i\sin\theta}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

The sum of the residues inside $\abs{z}=2$ is
$$
\frac{\sin(n\theta)}{\sin\theta}.
$$

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
$$
\begin{aligned}
\Res(F;e^{i\theta})
+\Res(F;e^{-i\theta})
&=
\frac{e^{in\theta}-e^{-in\theta}}
{2i\sin\theta}\\
&=
\frac{\sin(n\theta)}{\sin\theta}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s6}

One has
$$
\boxed{
\frac1{2\pi i}
\int_{\abs{z}=2}
\frac{z^n}
{1-2z\cos\theta+z^2}
\,dz
=
\frac{\sin(n\theta)}{\sin\theta}.
}
$$

::: pf-proof

By step [](#s2){.pf-ref}, the contour encloses exactly the two poles treated in
steps [](#s3){.pf-ref} and [](#s4){.pf-ref}. The residue theorem and step [](#s5){.pf-ref} give
$$
\int_{\abs{z}=2}F(z)\,dz
=
2\pi i
\frac{\sin(n\theta)}{\sin\theta}.
$$
Divide by $2\pi i$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the required identity.

:::

:::

:::
