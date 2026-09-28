---
schema: qual/card@1
id: D-IA5FS
kind: definition
title: Logarithmic derivative
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Poles
  - Zeros
relations:
- kind: variant-of
  target: D-WHYOA
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open and let $f$ be [[D-7DFVJ|meromorphic]] on $\Omega$ and not identically zero on any connected component of $\Omega$.
The \dfn{logarithmic derivative} of $f$ is the meromorphic function on $\Omega$
$$
\partial_{\log}f\coloneqq\frac{f'}{f}.
$$
:::

::: {.proposition}
Let $f$ be as in the definition and let $z_0\in\Omega$ be a [[D-65VIK|zero of order $m$]] or a [[D-AUD6K|pole of order $m$]] of $f$.
Then $f'/f$ has a simple pole at $z_0$ with residue $m$ in the first case and $-m$ in the second.
At every other point of $\Omega$, $f'/f$ is holomorphic.
:::

::: {.proof}
Near $z_0$ write $f(z)=(z-z_0)^{k}h(z)$ with $h$ holomorphic near $z_0$ and $h(z_0)\neq0$, where $k=m$ at a zero and $k=-m$ at a pole.
Then, for $z\neq z_0$ near $z_0$,
$$
\frac{f'(z)}{f(z)}=\frac{k}{z-z_0}+\frac{h'(z)}{h(z)},
$$
and $h'/h$ is holomorphic near $z_0$.
At a point where $f$ is holomorphic and nonzero, $f'/f$ is holomorphic.
:::
