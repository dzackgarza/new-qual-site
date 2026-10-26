---
schema: qual/card@1
id: P-TRIV-CA33
kind: problem
title: Poles and residues of the Gamma function at nonpositive integers
classification:
  areas: [complex-analysis]
  topics: []
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
---

::: {.problem}
The Gamma function $\Gamma(z) = \int_0^\infty x^{z-1} e^{-x}\,\mathrm{d}x$ is originally defined only for $t > 0$; it can however be analytically continued to negative values of $z$.
Show that, as $z \to -n$, where $n \in \mathbb{N}_0$, $\Gamma(z)$ has poles; compute the order and the residue of these poles.
:::

::: {.remark}
Erratum: the source's condition "$t > 0$" involves a variable that does not occur in the problem.
The defining integral converges exactly for $\operatorname{Re} z > 0$: at $z = 0$ the integrand behaves like $x^{-1}$ near $x = 0$ and the integral diverges.
The intended condition is $\operatorname{Re} z > 0$.
:::

::: pf

::: pf-step

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

::: pf-step

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

Iterate the functional equation from step <1>1:
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

::: pf-step

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

Separate the factor $z+n$ from the denominator in step <1>2. For $n=0$ the
product is empty and equals $1$.

:::

:::

::: pf-step

The numerator in step <1>3 is holomorphic and nonzero at $z=-n$:
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

::: pf-step

The remaining denominator factor in step <1>3 is nonzero at $z=-n$:
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

::: pf-step

Therefore $z=-n$ is a simple pole of $\Gamma$.


::: pf-proof

By steps <1>3--<1>5, near $z=-n$ the numerator and the product of all
denominator factors except $z+n$ are holomorphic and nonzero. Thus the only
vanishing factor is the first power of $z+n$, giving a pole of order $1$.

:::

:::

::: pf-step

The residue at $z=-n$ is
$$
\boxed{
\operatorname{Res}_{z=-n}\Gamma(z)
=
\frac{(-1)^n}{n!}.
}
$$


::: pf-proof

Using step <1>3,
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
Apply steps <1>4 and <1>5:
$$
\operatorname{Res}_{z=-n}\Gamma(z)
=
\frac1{(-1)^n n!}
=
\frac{(-1)^n}{n!}.
$$

:::

:::

::: pf-step

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

Steps <1>6 and <1>7 give the order and residue for arbitrary $n\in\NN_0$.

:::

:::

::: pf-qed

Step <1>8 is the required conclusion.

:::

:::
