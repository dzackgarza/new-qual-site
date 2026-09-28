---
schema: qual/card@1
id: D-LGP2Q
kind: definition
title: The Weierstrass $\wp$ function
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $\omega_1,\omega_2\in\CC$ be linearly independent over $\RR$, and let $\Lambda\coloneqq\ZZ\omega_1+\ZZ\omega_2$.
The \dfn{Weierstrass $\wp$ function} of $\Lambda$ is
$$
\wp(z)\coloneqq\frac{1}{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}\qty{\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}},\qquad z\in\CC\setminus\Lambda.
$$
:::

::: {.proposition}
The series defining $\wp$ converges absolutely and uniformly on compact subsets of $\CC\setminus\Lambda$, and $\wp$ is [[D-7DFVJ|meromorphic]] on $\CC$ with a [[D-AUD6K|pole of order $2$]] at each point of $\Lambda$ and no other poles.
:::

::: {.proof}
The number of $\omega\in\Lambda$ with $k\le\abs{\omega}<k+1$ is at most $Ck$ for a constant $C$ depending on $\Lambda$, so $\sum_{\omega\in\Lambda\setminus\{0\}}\abs{\omega}^{-3}<\infty$.
Fix $R>0$.
For $\abs{z}\le R$ and $\abs{\omega}\ge2R$,
$$
\abs{\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}}=\frac{\abs{z}\,\abs{2\omega-z}}{\abs{\omega}^2\abs{z-\omega}^2}\le\frac{R\cdot\frac52\abs{\omega}}{\abs{\omega}^2\cdot\frac14\abs{\omega}^2}=\frac{10R}{\abs{\omega}^3},
$$
so by the Weierstrass $M$-test the terms with $\abs{\omega}\ge2R$ converge absolutely and uniformly on $\abs{z}\le R$ to a holomorphic function.
The finitely many remaining terms are holomorphic on $\abs{z}<R$ away from $\Lambda$, and the term $(z-\omega)^{-2}$ (or $z^{-2}$ for $\omega=0$) gives a pole of order $2$ at each $\omega\in\Lambda$ with $\abs{\omega}<R$, all other terms being holomorphic near $\omega$.
:::
