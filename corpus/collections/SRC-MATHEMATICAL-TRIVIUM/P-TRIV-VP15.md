---
schema: qual/card@1
id: P-TRIV-VP15
kind: problem
title: Derrick's theorem
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 15, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
”Derrick’s theorem” Consider the functional

$$
E [ \phi ] = \int d ^ { d } x \left( \frac { 1 } { 2 } K _ { a b } ( \phi ) \sum _ { i = 1 } ^ { d } \partial _ { i } \phi ^ { a } \partial _ { i } \phi ^ { b } + V ( \phi ) \right) ,\tag{20}
$$

where $\phi = \phi ( x _ { 1 } , . . . , x _ { d } ) \in C ^ { 2 } ( \mathbb { R } ^ { d } ) , K _ { a b } ( \phi )$ is a positive-definite matrix for any $\phi ,$ i.e.,

$$
K _ { a b } ( \phi ) \partial _ { i } \phi ^ { a } \partial _ { j } \phi ^ { b } \geqslant 0 ,\tag{21}
$$

where the equality implies $\phi = 0$ , and $V ( \phi ) \geqslant 0 , V ( \phi ) = 0 \Rightarrow \phi = 0$ Suppose $\phi _ { 0 } ( x )$ is a non-zero extremum of $E [ \phi ]$ . Consider the configurations of the form $\phi _ { \lambda } ( x ) = \phi _ { 0 } ( \lambda x )$ , obtaining from $\phi _ { 0 } ( x )$ by stretching the coordinates by a factor of λ.

(a) Show that $E ( \lambda ) \equiv E [ \phi _ { \lambda } ]$ must satisfy

$$
\left. \frac { d { E } } { d { \lambda } } \right| _ { \lambda = 1 } = 0 .\tag{22}
$$

(b) Using the notations

$$
\Gamma = \int d ^ { d } x \frac { 1 } { 2 } K _ { a b } ( \phi _ { 0 } ) \sum _ { i = 1 } ^ { d } \partial _ { i } \phi _ { 0 } ^ { a } \partial _ { i } \phi _ { 0 } ^ { b } , ~ \Pi = \int d ^ { d } x V ( \phi _ { 0 } ) ,\tag{23}
$$

show that the above relation implies

$$
( 2 - d ) \Gamma - d \Pi = 0 .\tag{24}
$$

(c) Give a conclusion about the existence of $\phi _ { 0 }$ , if

$$
( \mathrm { a } ) d > 2 \qquad \quad ( \mathrm { b } ) d = 2 \qquad \quad ( \mathrm { c } ) d = 1
$$
:::

::: pf

::: pf-step

The scaling family satisfies
$$
\phi_\lambda(x)=\phi_0(\lambda x),
\qquad
\phi_1=\phi_0.
$$


::: pf-proof

This is the definition of the one-parameter family in the problem.

:::

:::

::: pf-step

Since $\phi_0$ is an extremum of $E$, one has
$$
\boxed{
\left.
\frac{dE(\lambda)}{d\lambda}
\right|_{\lambda=1}=0.
}
$$


::: pf-proof

An extremum has zero derivative along every differentiable admissible curve through it. Apply this to the curve $\lambda\mapsto\phi_\lambda$ from step <1>1.

:::

:::

::: pf-step

Part (a) follows.


::: pf-proof

This is step <1>2.

:::

:::

::: pf-step

Under the change of variables
$$
y=\lambda x,
$$
the volume element transforms as
$$
d^dx=\lambda^{-d}d^dy.
$$


::: pf-proof

The dilation $x\mapsto y=\lambda x$ has Jacobian determinant $\lambda^d$.

:::

:::

::: pf-step

The derivatives of the scaled field satisfy
$$
\partial_i\phi_\lambda^a(x)
=
\lambda\,
\partial_i\phi_0^a(\lambda x).
$$


::: pf-proof

Apply the chain rule to $\phi_0^a(\lambda x)$.

:::

:::

::: pf-step

Hence the gradient contribution to $E(\lambda)$ is
$$
\lambda^{2-d}\Gamma.
$$


::: pf-proof

The two derivatives in the quadratic gradient term contribute $\lambda^2$, while step <1>4 contributes $\lambda^{-d}$. After changing variables, the remaining integral is exactly $\Gamma$.

:::

:::

::: pf-step

The potential contribution to $E(\lambda)$ is
$$
\lambda^{-d}\Pi.
$$


::: pf-proof

The potential contains no derivatives, so only the measure factor $\lambda^{-d}$ from step <1>4 appears.

:::

:::

::: pf-step

Therefore
$$
\boxed{
E(\lambda)
=
\lambda^{2-d}\Gamma
+
\lambda^{-d}\Pi.
}
$$


::: pf-proof

Add the contributions from steps <1>6--<1>7.

:::

:::

::: pf-step

Differentiating and setting $\lambda=1$ gives
$$
E'(1)
=
(2-d)\Gamma-d\Pi.
$$


::: pf-proof

Differentiate the two powers of $\lambda$ in step <1>8 and evaluate at $1$.

:::

:::

::: pf-step

Combining steps <1>2 and <1>9 gives
$$
\boxed{
(2-d)\Gamma-d\Pi=0.
}
$$


::: pf-proof

Step <1>2 gives $E'(1)=0$, while step <1>9 computes that derivative explicitly.

:::

:::

::: pf-step

Part (b) follows.


::: pf-proof

This is step <1>10.

:::

:::

::: pf-step

One has
$$
\Gamma\geq0,
\qquad
\Pi\geq0.
$$


::: pf-proof

The positive-definiteness hypothesis makes the gradient integrand defining $\Gamma$ nonnegative, and $V(\phi)\geq0$ makes the potential integrand defining $\Pi$ nonnegative.

:::

:::

::: pf-step

If $d>2$, no nonzero extremum can exist.


::: pf-proof

For $d>2$, both coefficients in
$$
(2-d)\Gamma-d\Pi=0
$$
are strictly negative. By step <1>12, the identity can hold only if
$$
\Gamma=\Pi=0.
$$
The hypotheses on the kinetic and potential terms then force the trivial configuration, contradicting the assumed nonzero extremum.

:::

:::

::: pf-step

If $d=2$, no nonzero extremum can exist.


::: pf-proof

Step <1>10 becomes
$$
-2\Pi=0,
$$
so $\Pi=0$. Since $V\geq0$ and $V(\phi)=0$ only for $\phi=0$, continuity forces $\phi_0=0$, again contradicting nontriviality.

:::

:::

::: pf-step

If $d=1$, the Derrick condition is
$$
\boxed{\Gamma=\Pi}.
$$


::: pf-proof

Set $d=1$ in step <1>10.

:::

:::

::: pf-step

Therefore the scaling argument does not exclude nonzero extrema in one spatial dimension.


::: pf-proof

The equality $\Gamma=\Pi$ is compatible with positive values of both terms, so no contradiction follows.

:::

:::

::: pf-step

The dimension-by-dimension conclusion is
$$
\boxed{
\begin{array}{c|c}
d>2&\text{no nonzero extremum}\\
d=2&\text{no nonzero extremum}\\
d=1&\text{not excluded; necessarily }\Gamma=\Pi
\end{array}
}
$$


::: pf-proof

Combine steps <1>13--<1>16.

:::

:::

::: pf-step

Part (c) follows.


::: pf-proof

This is step <1>17.

:::

:::

::: pf-qed

Steps <1>3, <1>11, and <1>18 establish parts (a), (b), and (c), respectively.

:::

:::
