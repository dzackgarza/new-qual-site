---
schema: qual/card@1
id: P-CASP23D
kind: problem
title: "Injectivity from derivative condition and fixed-point rigidity for self-maps of D"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Injective Functions
  - Fixed Points
  - Automorphisms
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be analytic on $\DD$.
Prove the following statements.

(a) If $\abs{f'(z) - f'(0)} < \abs{f'(0)}$ for all $z \in \DD$, then $f(z)$ is injective.

(b) If $\abs{f(z)} < 1$ for all $z \in \DD$ and $f(z)$ has two distinct fixed points, then $f(z) = z$.
:::

::: {.solution}
(a) Since
$$
\abs{f'(z)-f'(0)}<\abs{f'(0)},
$$
we have $f'(0)\ne0$ and
$$
\operatorname{Re}\frac{f'(z)}{f'(0)}>0
$$
for every $z\in\DD$. If $z_1\ne z_2$, the line segment joining them
lies in $\DD$, and
$$
\frac{f(z_2)-f(z_1)}{f'(0)(z_2-z_1)}
=\int_0^1
\frac{f'(z_1+t(z_2-z_1))}{f'(0)}\,dt.
$$
The real part of the right-hand side is positive, so it is nonzero. Hence
$f(z_2)\ne f(z_1)$, proving injectivity.

(b) Let $a\ne b$ be two fixed points. Choose a disk automorphism $\phi$ with
$\phi(a)=0$ and set
$$
F=\phi\circ f\circ\phi^{-1}.
$$
Then $F:\DD\to\DD$ fixes $0$ and also the nonzero point
$\phi(b)$. Schwarz's lemma gives $\abs{F(z)}\le\abs{z}$, and equality at the nonzero
fixed point forces
$$
F(z)=e^{i\theta}z.
$$
Since $F(\phi(b))=\phi(b)\ne0$, we get $e^{i\theta}=1$. Thus $F$ and hence
$f$ are the identity.
:::
