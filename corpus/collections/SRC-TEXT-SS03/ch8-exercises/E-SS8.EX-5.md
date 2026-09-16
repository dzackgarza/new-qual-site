---
schema: qual/card@1
id: E-SS8.EX-5
kind: problem
title: "SS 8.5: A conformal map from the half-disc to the upper half-plane"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
5. Prove that $f ( z ) = - { \textstyle \frac { 1 } { 2 } } ( z + 1 / z )$ is a conformal map from the half-disc $\left\{ z = x + i y : | z | < 1 , \ y > 0 \right\}$ to the upper half-plane.

[Hint: The equation $f ( z ) = w$ reduces to the quadratic equation $z ^ { 2 } + 2 w z + 1 = 0$ 2 which has two distinct roots in C whenever w $\neq \pm 1$ . This is certainly the case if $w \in \mathbb { H } . ]$
:::

::: {.solution}
Let
\[
D_+=\{z:|z|<1,\ \Im z>0\},
\qquad
f(z)=-\frac12\left(z+\frac1z\right).
\]
For $z=x+iy\in D_+$,
\[
\Im\left(z+\frac1z\right)
=y-\frac{y}{|z|^2}
=y\left(1-|z|^{-2}\right)<0,
\]
so $\Im f(z)>0$. Hence $f(D_+)\subseteq\mathbb H$.

If $f(z)=f(w)$, then
\[
z+z^{-1}=w+w^{-1},
\]
so
\[
(z-w)\left(1-\frac1{zw}\right)=0.
\]
Since $|zw|<1$, the second factor cannot vanish; therefore $z=w$. Thus $f$ is injective.

Now fix $\eta\in\mathbb H$. The equation $f(z)=\eta$ is
\[
z^2+2\eta z+1=0.
\]
Its two roots are reciprocal. They are nonreal because $\eta\notin\mathbb R$. Exactly one root lies in the upper half-plane, since if $z$ is nonreal then $1/z$ has imaginary part of the opposite sign. Let $z$ be the upper-half-plane root. If $|z|>1$, then the formula above gives
\[
\Im f(z)<0,
\]
contrary to $f(z)=\eta\in\mathbb H$. Thus $|z|<1$, so $z\in D_+$. Therefore $f$ is surjective onto $\mathbb H$.

Finally
\[
f'(z)=-\frac12(1-z^{-2}),
\]
and $f'(z)=0$ only at $z=\pm1$, neither of which lies in $D_+$. Hence $f$ is conformal from $D_+$ onto $\mathbb H$.
:::
