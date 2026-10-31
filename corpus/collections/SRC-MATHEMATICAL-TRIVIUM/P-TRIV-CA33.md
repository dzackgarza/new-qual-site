---
schema: qual/card@1
id: P-TRIV-CA33
kind: problem
title: Poles and residues of the Gamma function at nonpositive integers
classification:
  areas: [complex-analysis]
  topics:
  - Gamma Function
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 33, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow against Complex Analysis Problem 33 on page 18 of the source PDF and added an erratum remark for the source's t > 0.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints the domain of the Gamma integral as t > 0, a variable absent from the problem; the statement now reads Re z > 0.
---

::: {.problem}
The Gamma function $\Gamma(z) = \int_0^\infty x^{z-1} e^{-x}\,\mathrm{d}x$ is originally defined only for $\operatorname{Re} z > 0$; it can however be analytically continued to negative values of $z$.
Show that, as $z \to -n$, where $n \in \NN_0$, $\Gamma(z)$ has poles; compute the order and the residue of these poles.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $\operatorname{Re}z>0$, the Gamma function satisfies
$$
\Gamma(z+1)
=
z\Gamma(z).
$$


::: pf-proof

Starting from
$$
\Gamma(z+1)
=
\int_0^\infty
x^z e^{-x}\,dx,
$$
integrate by parts with
$$
u=x^z,
\qquad
dv=e^{-x}\,dx.
$$
Then
$$
du=z x^{z-1}\,dx,
\qquad
v=-e^{-x}.
$$
The boundary term vanishes for $\operatorname{Re}z>0$, so
$$
\Gamma(z+1)
=
z
\int_0^\infty
x^{z-1}e^{-x}\,dx
=
z\Gamma(z).
$$

:::

:::

::: {.pf-step #s1-2}

For every integer $n\geq0$,
$$
\Gamma(z)
=
\frac{
\Gamma(z+n+1)
}{
z(z+1)\cdots(z+n)
}
$$
wherever the denominator is nonzero.


::: pf-proof

Iterate the functional equation from step [](#s1-1){.pf-ref}:
$$
\Gamma(z+n+1)
=
(z+n)(z+n-1)\cdots z\,\Gamma(z).
$$
Solving for $\Gamma(z)$ gives the displayed formula. Since the numerator is
holomorphic for
$$
\operatorname{Re}(z+n+1)>0,
$$
this identity also gives the meromorphic continuation across successive
left half-planes.

:::

:::

::: {.pf-step #s1-3}

Fix $n\in\NN_0$. In a neighborhood of $z=-n$,
$$
\Gamma(z)
=
\frac{
\Gamma(z+n+1)
}{
(z+n)
\displaystyle\prod_{k=0}^{n-1}(z+k)
}.
$$


::: pf-proof

Separate the factor $z+n$ from the denominator in step [](#s1-2){.pf-ref}. For $n=0$ the
product is empty and equals $1$.

:::

:::

::: {.pf-step #s1-4}

The numerator in step [](#s1-3){.pf-ref} is holomorphic and nonzero at $z=-n$:
$$
\Gamma((-n)+n+1)
=
\Gamma(1)
=1.
$$


::: pf-proof

The Gamma integral at $1$ gives
$$
\Gamma(1)
=
\int_0^\infty e^{-x}\,dx
=1.
$$

:::

:::

::: {.pf-step #s1-5}

The remaining denominator factor in step [](#s1-3){.pf-ref} is nonzero at $z=-n$:
$$
\prod_{k=0}^{n-1}(-n+k)
=
(-1)^n n!.
$$


::: pf-proof

The factors are
$$
-n,-(n-1),\ldots,-1.
$$
Their product is $(-1)^n n!$. For $n=0$, both sides equal $1$ by the empty
product convention.

:::

:::

::: {.pf-step #s1-6}

Therefore $z=-n$ is a simple pole of $\Gamma$.


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref}, near $z=-n$ the numerator and the product of all
denominator factors except $z+n$ are holomorphic and nonzero. Thus the only
vanishing factor is the first power of $z+n$, giving a pole of order $1$.

:::

:::

::: {.pf-step #s1-7}

The residue at $z=-n$ is
$$
\boxed{
\operatorname{Res}_{z=-n}\Gamma(z)
=
\frac{(-1)^n}{n!}.
}
$$


::: pf-proof

Using step [](#s1-3){.pf-ref},
$$
\begin{aligned}
\operatorname{Res}_{z=-n}\Gamma(z)
&=
\lim_{z\to-n}
(z+n)\Gamma(z)\\
&=
\frac{
\Gamma(1)
}{
\displaystyle\prod_{k=0}^{n-1}(-n+k)
}.
\end{aligned}
$$
Apply steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref}:
$$
\operatorname{Res}_{z=-n}\Gamma(z)
=
\frac1{(-1)^n n!}
=
\frac{(-1)^n}{n!}.
$$

:::

:::

::: {.pf-step #s1-8}

Hence every nonpositive integer is a simple pole of $\Gamma$, with
residue
$$
\boxed{
\operatorname{Res}_{z=-n}\Gamma(z)
=
\frac{(-1)^n}{n!}
},
\qquad
n\in\NN_0.
$$


::: pf-proof

Steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref} give the order and residue for arbitrary $n\in\NN_0$.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
