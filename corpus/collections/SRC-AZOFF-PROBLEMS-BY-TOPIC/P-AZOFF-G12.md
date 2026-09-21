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
Let n be a positive integer and $0 < \theta < \pi$ . Prove that

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

<1>1. The denominator factors as
$$
1-2z\cos\theta+z^2
=
(z-e^{i\theta})(z-e^{-i\theta}).
$$

::: {.proof}
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

<1>2. The only poles of $F$ are the distinct simple poles
$$
e^{i\theta}
\qquad\text{and}\qquad
e^{-i\theta},
$$
and both lie inside the contour $\abs{z}=2$.

::: {.proof}
By step <1>1 these are the only zeros of the denominator. They are distinct
because $0<\theta<\pi$, and both have modulus $1<2$.
:::

<1>3. The residue at $z=e^{i\theta}$ is
$$
\Res(F;e^{i\theta})
=
\frac{e^{in\theta}}{2i\sin\theta}.
$$

::: {.proof}
Using the factorization in step <1>1,
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

<1>4. The residue at $z=e^{-i\theta}$ is
$$
\Res(F;e^{-i\theta})
=
-\frac{e^{-in\theta}}{2i\sin\theta}.
$$

::: {.proof}
Again by step <1>1,
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

<1>5. The sum of the residues inside $\abs{z}=2$ is
$$
\frac{\sin(n\theta)}{\sin\theta}.
$$

::: {.proof}
By steps <1>3 and <1>4,
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

<1>6. One has
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

::: {.proof}
By step <1>2, the contour encloses exactly the two poles treated in
steps <1>3 and <1>4. The residue theorem and step <1>5 give
$$
\int_{\abs{z}=2}F(z)\,dz
=
2\pi i
\frac{\sin(n\theta)}{\sin\theta}.
$$
Divide by $2\pi i$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required identity.
:::
:::
