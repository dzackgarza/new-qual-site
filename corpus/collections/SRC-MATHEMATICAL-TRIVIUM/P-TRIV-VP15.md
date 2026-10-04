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

::: {.solution}
<1>1. The scaling family satisfies
$$
\phi_\lambda(x)=\phi_0(\lambda x),
\qquad
\phi_1=\phi_0.
$$

::: {.proof}
This is the definition of the one-parameter family in the problem.
:::

<1>2. Since $\phi_0$ is an extremum of $E$, one has
$$
\boxed{
\left.
\frac{dE(\lambda)}{d\lambda}
\right|_{\lambda=1}=0.
}
$$

::: {.proof}
An extremum has zero derivative along every differentiable admissible curve through it. Apply this to the curve $\lambda\mapsto\phi_\lambda$ from step <1>1.
:::

<1>3. Part (a) follows.

::: {.proof}
This is step <1>2.
:::

<1>4. Under the change of variables
$$
y=\lambda x,
$$
the volume element transforms as
$$
d^dx=\lambda^{-d}d^dy.
$$

::: {.proof}
The dilation $x\mapsto y=\lambda x$ has Jacobian determinant $\lambda^d$.
:::

<1>5. The derivatives of the scaled field satisfy
$$
\partial_i\phi_\lambda^a(x)
=
\lambda\,
\partial_i\phi_0^a(\lambda x).
$$

::: {.proof}
Apply the chain rule to $\phi_0^a(\lambda x)$.
:::

<1>6. Hence the gradient contribution to $E(\lambda)$ is
$$
\lambda^{2-d}\Gamma.
$$

::: {.proof}
The two derivatives in the quadratic gradient term contribute $\lambda^2$, while step <1>4 contributes $\lambda^{-d}$. After changing variables, the remaining integral is exactly $\Gamma$.
:::

<1>7. The potential contribution to $E(\lambda)$ is
$$
\lambda^{-d}\Pi.
$$

::: {.proof}
The potential contains no derivatives, so only the measure factor $\lambda^{-d}$ from step <1>4 appears.
:::

<1>8. Therefore
$$
\boxed{
E(\lambda)
=
\lambda^{2-d}\Gamma
+
\lambda^{-d}\Pi.
}
$$

::: {.proof}
Add the contributions from steps <1>6--<1>7.
:::

<1>9. Differentiating and setting $\lambda=1$ gives
$$
E'(1)
=
(2-d)\Gamma-d\Pi.
$$

::: {.proof}
Differentiate the two powers of $\lambda$ in step <1>8 and evaluate at $1$.
:::

<1>10. Combining steps <1>2 and <1>9 gives
$$
\boxed{
(2-d)\Gamma-d\Pi=0.
}
$$

::: {.proof}
Step <1>2 gives $E'(1)=0$, while step <1>9 computes that derivative explicitly.
:::

<1>11. Part (b) follows.

::: {.proof}
This is step <1>10.
:::

<1>12. One has
$$
\Gamma\geq0,
\qquad
\Pi\geq0.
$$

::: {.proof}
The positive-definiteness hypothesis makes the gradient integrand defining $\Gamma$ nonnegative, and $V(\phi)\geq0$ makes the potential integrand defining $\Pi$ nonnegative.
:::

<1>13. If $d>2$, no nonzero extremum can exist.

::: {.proof}
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

<1>14. If $d=2$, no nonzero extremum can exist.

::: {.proof}
Step <1>10 becomes
$$
-2\Pi=0,
$$
so $\Pi=0$. Since $V\geq0$ and $V(\phi)=0$ only for $\phi=0$, continuity forces $\phi_0=0$, again contradicting nontriviality.
:::

<1>15. If $d=1$, the Derrick condition is
$$
\boxed{\Gamma=\Pi}.
$$

::: {.proof}
Set $d=1$ in step <1>10.
:::

<1>16. Therefore the scaling argument does not exclude nonzero extrema in one spatial dimension.

::: {.proof}
The equality $\Gamma=\Pi$ is compatible with positive values of both terms, so no contradiction follows.
:::

<1>17. The dimension-by-dimension conclusion is
$$
\boxed{
\begin{array}{c|c}
d>2&\text{no nonzero extremum}\\
d=2&\text{no nonzero extremum}\\
d=1&\text{not excluded; necessarily }\Gamma=\Pi
\end{array}
}
$$

::: {.proof}
Combine steps <1>13--<1>16.
:::

<1>18. Part (c) follows.

::: {.proof}
This is step <1>17.
:::

<1>19. Q.E.D.

::: {.proof}
Steps <1>3, <1>11, and <1>18 establish parts (a), (b), and (c), respectively.
:::
:::
