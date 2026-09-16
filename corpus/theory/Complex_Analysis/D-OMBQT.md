---
schema: qual/card@1
id: D-OMBQT
kind: definition
title: Principal value of the complex logarithm
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
relations: []
review: draft
---

::: {.definition}
For $z\in\CC\setminus\{0\}$, let $\Arg(z)\in(-\pi,\pi]$ be the \dfn{principal argument} of $z$, the unique $\theta\in(-\pi,\pi]$ with $z=\abs{z}e^{i\theta}$.
The \dfn{principal value of the logarithm} is
$$
\log(z)\coloneqq\ln\abs{z}+i\Arg(z),\qquad z\in\CC\setminus\{0\},
$$
where $\ln$ is the real natural logarithm.
:::

::: {.remark}
In polar form $z=re^{i\theta}$ with $r>0$ and $\theta\in(-\pi,\pi]$, this reads $\log(z)=\ln r+i\theta$.
It satisfies $e^{\log(z)}=z$, restricts to the [[D-4CSPM|principal branch]] $\Log$ on $\CC\setminus(-\infty,0]$, and is discontinuous at every point of $(-\infty,0)$, where $\Arg$ jumps from values near $-\pi$ to $\pi$.
:::
