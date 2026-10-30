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
"Derrick's theorem" Consider the functional
$$
E[\phi] = \int d^dx \left( \frac{1}{2}K_{ab}(\phi)\sum_{i=1}^{d} \partial_i\phi^a\partial_i\phi^b + V(\phi) \right), \tag{20}
$$
where $\phi = \phi(x_1, \ldots, x_d) \in C^2(\RR^d)$, $K_{ab}(\phi)$ is a positive-definite matrix for any $\phi$, i.e.,
$$
K_{ab}(\phi)\partial_i\phi^a\partial_j\phi^b \geqslant 0, \tag{21}
$$
where the equality implies $\phi = 0$, and $V(\phi) \geqslant 0$, $V(\phi) = 0 \Rightarrow \phi = 0$. Suppose $\phi_0(x)$ is a non-zero extremum of $E[\phi]$. Consider the configurations of the form $\phi_\lambda(x) = \phi_0(\lambda x)$, obtaining from $\phi_0(x)$ by stretching the coordinates by a factor of $\lambda$.

(a) Show that $E(\lambda) \equiv E[\phi_\lambda]$ must satisfy
$$
\evaluated{\frac{dE}{d\lambda}}_{\lambda=1} = 0. \tag{22}
$$

(b) Using the notations
$$
\Gamma = \int d^dx\, \frac{1}{2}K_{ab}(\phi_0)\sum_{i=1}^{d} \partial_i\phi_0^a\partial_i\phi_0^b, \quad \Pi = \int d^dx\, V(\phi_0), \tag{23}
$$
show that the above relation implies
$$
(2 - d)\Gamma - d\Pi = 0. \tag{24}
$$

(c) Give a conclusion about the existence of $\phi_0$, if

(a) $d > 2$ (b) $d = 2$ (c) $d = 1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

Since $\phi_0$ is an extremum of $E$, one has
$$
\boxed{
\evaluated{
\frac{dE(\lambda)}{d\lambda}
}_{\lambda=1}=0.
}
$$


::: pf-proof

An extremum has zero derivative along every differentiable admissible curve through it. Apply this to the curve $\lambda\mapsto\phi_\lambda$ from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Part (a) follows.


::: pf-proof

This is step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

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

::: {.pf-step #s1-6}

Hence the gradient contribution to $E(\lambda)$ is
$$
\lambda^{2-d}\Gamma.
$$


::: pf-proof

The two derivatives in the quadratic gradient term contribute $\lambda^2$, while step [](#s1-4){.pf-ref} contributes $\lambda^{-d}$. After changing variables, the remaining integral is exactly $\Gamma$.

:::

:::

::: {.pf-step #s1-7}

The potential contribution to $E(\lambda)$ is
$$
\lambda^{-d}\Pi.
$$


::: pf-proof

The potential contains no derivatives, so only the measure factor $\lambda^{-d}$ from step [](#s1-4){.pf-ref} appears.

:::

:::

::: {.pf-step #s1-8}

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

Add the contributions from steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Differentiating and setting $\lambda=1$ gives
$$
E'(1)
=
(2-d)\Gamma-d\Pi.
$$


::: pf-proof

Differentiate the two powers of $\lambda$ in step [](#s1-8){.pf-ref} and evaluate at $1$.

:::

:::

::: {.pf-step #s1-10}

Combining steps [](#s1-2){.pf-ref} and [](#s1-9){.pf-ref} gives
$$
\boxed{
(2-d)\Gamma-d\Pi=0.
}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives $E'(1)=0$, while step [](#s1-9){.pf-ref} computes that derivative explicitly.

:::

:::

::: {.pf-step #s1-11}

Part (b) follows.


::: pf-proof

This is step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

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

::: {.pf-step #s1-13}

If $d>2$, no nonzero extremum can exist.


::: pf-proof

For $d>2$, both coefficients in
$$
(2-d)\Gamma-d\Pi=0
$$
are strictly negative. By step [](#s1-12){.pf-ref}, the identity can hold only if
$$
\Gamma=\Pi=0.
$$
The hypotheses on the kinetic and potential terms then force the trivial configuration, contradicting the assumed nonzero extremum.

:::

:::

::: {.pf-step #s1-14}

If $d=2$, no nonzero extremum can exist.


::: pf-proof

Step [](#s1-10){.pf-ref} becomes
$$
-2\Pi=0,
$$
so $\Pi=0$. Since $V\geq0$ and $V(\phi)=0$ only for $\phi=0$, continuity forces $\phi_0=0$, again contradicting nontriviality.

:::

:::

::: {.pf-step #s1-15}

If $d=1$, the Derrick condition is
$$
\boxed{\Gamma=\Pi}.
$$


::: pf-proof

Set $d=1$ in step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

Therefore the scaling argument does not exclude nonzero extrema in one spatial dimension.


::: pf-proof

The equality $\Gamma=\Pi$ is compatible with positive values of both terms, so no contradiction follows.

:::

:::

::: {.pf-step #s1-17}

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

Combine steps [](#s1-13){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

Part (c) follows.


::: pf-proof

This is step [](#s1-17){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-11){.pf-ref}, and [](#s1-18){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
