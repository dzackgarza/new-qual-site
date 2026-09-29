---
schema: qual/card@1
id: P-AGNONRATCURVE
kind: problem
title: A projective curve that is not rational
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Curves
  - Genus
  - Examples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; the source asks for an example of a projective curve that is not rational.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Find an example of a projective curve which is not rational.
:::

::: {.solution}
Consider the Fermat cubic
\[
C=V(x^3+y^3+z^3)\subseteq\mathbb P^2_{\mathbb C}.
\]

::: pf

::: pf-step
The curve $C$ is smooth.

::: pf-proof
The three partial derivatives of
\[
F=x^3+y^3+z^3
\]
are
\[
F_x=3x^2,
\qquad
F_y=3y^2,
\qquad
F_z=3z^2.
\]
Over $\mathbb C$, they vanish simultaneously only at
\[
x=y=z=0,
\]
which is not a point of projective space.  Hence the projective Jacobian criterion shows that $C$ is smooth.
:::

:::

::: pf-step
The genus of $C$ is
\[
g(C)=1.
\]

::: pf-proof
A smooth plane curve of degree $d$ has genus
\[
g=\frac{(d-1)(d-2)}2.
\]
For $d=3$ this gives
\[
g(C)=\frac{2\cdot1}{2}=1.
\]
:::

:::

::: {.pf-step #curve-not-rational}
The curve $C$ is not rational.

::: pf-proof
If $C$ were rational, its function field would be isomorphic to
\[
\mathbb C(t),
\]
so its smooth projective model would be $\mathbb P^1_{\mathbb C}$.  Equivalently, $C$ would be birational to $\mathbb P^1$.

Genus is a birational invariant of smooth projective curves, but
\[
g(C)=1
\qquad\text{and}\qquad
g(\mathbb P^1)=0.
\]
This is impossible.  Hence $C$ is not rational.
:::

:::

::: {.pf-step #final-example}
Therefore
\[
\boxed{V(x^3+y^3+z^3)\subseteq\mathbb P^2_{\mathbb C}}
\]
is a projective curve that is not rational.

::: pf-proof
It is projective by construction and nonrational by step [](#curve-not-rational){.pf-ref}.
:::

:::

::: pf-qed
Step [](#final-example){.pf-ref} is the requested example.
:::

:::
:::
