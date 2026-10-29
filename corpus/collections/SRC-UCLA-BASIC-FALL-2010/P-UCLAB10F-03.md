---
schema: qual/card@1
id: P-UCLAB10F-03
kind: problem
title: Derive the two-variable Taylor theorem from the one-variable theorem
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Suppose $f:\RR\to\RR$ and $g:\RR^2\to\RR$ have continuous derivatives through order three.

(a) State Taylor's theorem with remainder for each of $f$ and $g$.

(b) Using the statement for $f$, prove the statement for $g$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The one-variable Taylor theorem with third-order Lagrange remainder states that for any $a,h\in\RR$, there exists $\theta\in(0,1)$ such that
\[
f(a+h)
=
f(a)
+f'(a)h
+\frac12f''(a)h^2
+\frac16f'''(a+\theta h)h^3.
\]


::: pf-proof

This is the ordinary one-variable Taylor theorem through degree $2$ with Lagrange remainder. The hypotheses hold because $f$ has continuous derivatives through order $3$.

:::

:::

::: {.pf-step #s1-2}

The corresponding two-variable statement is: for
\[
p=(a,b)\in\RR^2
\]
and increment
\[
u=(h,k)\in\RR^2,
\]
there exists $\theta\in(0,1)$ such that
\[
\begin{aligned}
g(a+h,b+k)
&=
g(a,b)
+g_x(a,b)h
+g_y(a,b)k\\
&\quad
+\frac12\Bigl(
g_{xx}(a,b)h^2
+2g_{xy}(a,b)hk
+g_{yy}(a,b)k^2
\Bigr)\\
&\quad
+\frac16\Bigl(
g_{xxx}(p+\theta u)h^3
+3g_{xxy}(p+\theta u)h^2k\\
&\qquad\qquad
+3g_{xyy}(p+\theta u)hk^2
+g_{yyy}(p+\theta u)k^3
\Bigr).
\end{aligned}
\]


::: pf-proof

This is the two-variable Taylor theorem through total degree $2$ with third-order Lagrange remainder along the line segment from $p$ to $p+u$.

:::

:::

::: {.pf-step #s1-3}

Define the one-variable function
\[
\phi(t)=g(a+th,b+tk),
\qquad
0\le t\le1.
\]
Then
\[
\phi'(t)
=
g_x(a+th,b+tk)h
+g_y(a+th,b+tk)k.
\]


::: pf-proof

Apply the chain rule to the composition of $g$ with the affine path
\[
t\mapsto(a+th,b+tk).
\]

:::

:::

::: {.pf-step #s1-4}

One has
\[
\phi''(t)
=
g_{xx}h^2
+2g_{xy}hk
+g_{yy}k^2,
\]
where all derivatives of $g$ are evaluated at $(a+th,b+tk)$.


::: pf-proof

Differentiate the formula in step [](#s1-3){.pf-ref}. Since $g$ has continuous second derivatives,
\[
g_{xy}=g_{yx},
\]
so the two mixed terms combine to give $2g_{xy}hk$.

:::

:::

::: {.pf-step #s1-5}

One has
\[
\phi'''(t)
=
g_{xxx}h^3
+3g_{xxy}h^2k
+3g_{xyy}hk^2
+g_{yyy}k^3,
\]
again with all derivatives evaluated at $(a+th,b+tk)$.


::: pf-proof

Differentiate the formula in step [](#s1-4){.pf-ref}. Continuity of the third-order partial derivatives implies equality of mixed third partials, so the terms of type $h^2k$ combine with coefficient $3$, and similarly for the terms of type $hk^2$.

:::

:::

::: {.pf-step #s1-6}

Applying the one-variable theorem from step [](#s1-1){.pf-ref} to $\phi$ at $t=0$ with increment $1$ gives
\[
\phi(1)
=
\phi(0)
+\phi'(0)
+\frac12\phi''(0)
+\frac16\phi'''(\theta)
\]
for some $\theta\in(0,1)$.


::: pf-proof

The function $\phi$ has continuous derivatives through order $3$ because $g$ does and the path is affine. Therefore the hypotheses of step [](#s1-1){.pf-ref} apply.

:::

:::

::: {.pf-step #s1-7}

Substituting steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} into step [](#s1-6){.pf-ref} yields exactly the two-variable Taylor formula in step [](#s1-2){.pf-ref}.


::: pf-proof

One has
\[
\phi(0)=g(a,b),
\qquad
\phi(1)=g(a+h,b+k).
\]
The values of $\phi'(0)$ and $\phi''(0)$ are the linear and quadratic terms in step [](#s1-2){.pf-ref}. The value $\phi'''(\theta)$ is the cubic directional expression from step [](#s1-5){.pf-ref} evaluated at
\[
(a+\theta h,b+\theta k)
=
p+\theta u.
\]
Thus step [](#s1-6){.pf-ref} becomes precisely the formula stated in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} states the one-variable theorem, step [](#s1-2){.pf-ref} states the two-variable theorem, and steps [](#s1-3){.pf-ref} through [](#s1-7){.pf-ref} derive the latter from the former.

:::

:::

:::
