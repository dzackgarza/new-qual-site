---
schema: qual/card@1
id: D-4CSPM
kind: definition
title: Principal branch of the logarithm and of $z^\alpha$
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
relations: []
review: draft
---

::: {.definition}
Let $\Omega\coloneqq\CC\setminus(-\infty,0]$.
Every $z\in\Omega$ can be written uniquely as $z=re^{i\theta}$ with $r>0$ and $\theta\in(-\pi,\pi)$.
The \dfn{principal branch of the logarithm} is the function $\Log\colon\Omega\to\CC$ given by
$$
\Log(z)\coloneqq\log r+i\theta,
$$
where $\log r$ is the real natural logarithm.
For $\alpha\in\CC$, the \dfn{principal branch of $z^\alpha$} is the function on $\Omega$ given by
$$
z^{\alpha}\coloneqq e^{\alpha\Log(z)}.
$$
:::

::: {.remark title="Variations"}
Some sources extend $\Log$ to all of $\CC\setminus\theset{0}$: with the principal argument $\Arg(z)\in(-\pi,\pi]$, the unique $\theta\in(-\pi,\pi]$ with $z=\abs{z}e^{i\theta}$, the principal value of the logarithm is $\Log(z)\coloneqq\log\abs{z}+i\Arg(z)$.
It satisfies $e^{\Log(z)}=z$, restricts to the principal branch on $\CC\setminus(-\infty,0]$, and is discontinuous at every point of $(-\infty,0)$, where $\Arg$ jumps from values near $-\pi$ to $\pi$.
:::
