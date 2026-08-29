---
schema: qual/card@1
id: E-KZB33
kind: exercise
title: Injective holomorphic maps have nonvanishing derivative
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Zeros
  - Conformal Maps
relations: []
review: draft
---

:::{.exercise}
Show that if $f$ is injective, then $f'$ is nowhere vanishing and thus $f$ is conformal.

:::

:::{.solution}
Contrapositive: if $f'(z_0)=0$ at some point, then $f$ fails injectivity in a neighborhood of $z_0$.
Without loss of generality, we can assume $f(0) = 0$ after changes of coordinates in the domain/codomain, since this won't affect injectivity or vanishing of derivatives.
If $z_0$ is a zero of $f$ of some order $n$, we can write $f(z) = z^n g(z)$ with $g(0) \neq 0$ and $g$ nonvanishing in some neighborhood of zero.
Choosing a branch of $z\mapsto z^{1\over n}$, write $g(z) = (h(z))^n$ for some $h$, then
\[
f(z) = z^n h(z)^n = (zh(z))^n
.\]
Write $H(z) \da zh(z)$, then $H'(z) = h(z) + zh'(z)$, so $H'(0)\neq 0$.
By the inverse function theorem, $H$ is invertible on a small neighborhood of $0$, making $f$ $n$-to-one for some $n$.
Writing $f(z) = \sum_{k\geq 0} c_k z^k$, we have $c_0 = 0$ since $f(0) = 0$ and $c_1 = 0$ if $f'(0) = 0$, making $n\geq 2$, so $f$ fails injectivity in this neighborhood.
:::

