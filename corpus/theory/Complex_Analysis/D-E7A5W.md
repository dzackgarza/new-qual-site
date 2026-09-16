---
schema: qual/card@1
id: D-E7A5W
kind: definition
title: Holomorphic and entire functions
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Entire Functions
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open, let $f\colon\Omega\to\CC$, and let $z_0\in\Omega$.
The function $f$ is \dfn{complex differentiable}, or \dfn{holomorphic}, at $z_0$ if the limit
$$
f'(z_0)\coloneqq\lim_{\substack{h\to0\\ h\in\CC\setminus\{0\}}}\frac{f(z_0+h)-f(z_0)}{h}
$$
exists.
The function $f$ is holomorphic on $\Omega$ if it is holomorphic at every point of $\Omega$, and a function $f\colon\CC\to\CC$ that is holomorphic on $\CC$ is \dfn{entire}.
:::

::: {.proposition}
Let $\Omega\subseteq\CC$ be open, $f\colon\Omega\to\CC$, and $z_0\in\Omega$.
Then $f$ is holomorphic at $z_0$ if and only if there exist $\alpha\in\CC$ and a function $\psi$, defined for $h\in\CC$ with $z_0+h\in\Omega$, such that $\psi(h)\to0$ as $h\to0$ and
$$
f(z_0+h)-f(z_0)=\alpha h+h\,\psi(h).
$$
In this case $\alpha=f'(z_0)$.
:::

::: {.proof}
If $f'(z_0)$ exists, put $\alpha\coloneqq f'(z_0)$, $\psi(0)\coloneqq0$, and $\psi(h)\coloneqq\frac{f(z_0+h)-f(z_0)}{h}-\alpha$ for $h\neq0$; then $\psi(h)\to0$ and the identity holds.
Conversely, dividing the identity by $h\neq0$ gives $\frac{f(z_0+h)-f(z_0)}{h}=\alpha+\psi(h)\to\alpha$, so $f'(z_0)$ exists and equals $\alpha$.
:::

::: {.remark}
See [@SS03].
:::
