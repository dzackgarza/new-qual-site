---
schema: qual/card@1
id: P-PRACT20-W5-31
kind: problem
title: The integral $\int_0^{2\pi}\frac{dx}{10-8\cos x}$ by residues
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 31).
---

::: {.problem}
Using the substitution $z = e^{ix}$ (or otherwise), evaluate $\int_0^{2\pi} \frac{dx}{10 - 8\cos(x)}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Under the substitution
$$
z=e^{ix},
$$
one has
$$
dx=\frac{dz}{iz}
\qquad\text{and}\qquad
\cos x=\frac12\left(z+\frac1z\right).
$$


::: pf-proof

Differentiate $z=e^{ix}$ to obtain $dz=iz\,dx$. Also
$$
e^{ix}+e^{-ix}=2\cos x.
$$
As $x$ runs from $0$ to $2\pi$, $z$ traverses the unit circle once
counterclockwise.

:::

:::

::: pf-step

The real integral becomes
$$
\int_0^{2\pi}\frac{dx}{10-8\cos x}
=
\oint_{\abs{z}=1}
\frac{i\,dz}{2(2z-1)(z-2)}.
$$


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
10-8\cos x
=
10-4\left(z+\frac1z\right)
=
\frac{10z-4z^2-4}{z}.
$$
Thus
$$
\frac{dx}{10-8\cos x}
=
\frac{dz}{i(10z-4z^2-4)}.
$$
Since
$$
10z-4z^2-4
=-2(2z-1)(z-2),
$$
and $1/(-2i)=i/2$, the displayed contour integral follows.

:::

:::

::: {.pf-step #s1-3}

The only pole inside the unit circle is
$$
z=\frac12,
$$
and its residue is
$$
-\frac{i}{6}.
$$


::: pf-proof

The poles are $1/2$ and $2$, so only $1/2$ lies inside $\abs{z}=1$. For
$$
F(z)=\frac{i}{2(2z-1)(z-2)},
$$
one has
$$
\begin{aligned}
\operatorname{Res}\left(F,\frac12\right)
&=
\lim_{z\to1/2}
\frac{i(z-1/2)}{2(2z-1)(z-2)}\\
&=
\frac{i}{4(1/2-2)}\\
&=
-\frac{i}{6}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\int_0^{2\pi}\frac{dx}{10-8\cos x}
=\frac{\pi}{3}}.
$$


::: pf-proof

By the residue theorem and step [](#s1-3){.pf-ref},
$$
\oint_{\abs{z}=1}F(z)\,dz
=
2\pi i\left(-\frac{i}{6}\right)
=
\frac{\pi}{3}.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the requested value.

:::

:::

:::
