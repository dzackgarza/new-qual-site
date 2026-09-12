---
schema: qual/card@1
id: P-AMD-RNAYEXTP
kind: problem
title: Induced maps on $\pi_1(S^1)$ for $z^n$, antipodal, and $e^{2\pi i\sin\theta}$
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
For each of the following $f: S^1 \rightarrow S^1$, identify the corresponding $f_*: \mathbb{Z} \to \mathbb{Z}$:

1. $z\mapsto z^n$

2. $\bar{x} \mapsto -\bar{x}$

3. $e^{i\theta} \mapsto e^{2\pi i\sin\theta}$
:::

::: {.solution}
<1>1. For $f(z)=z^n$, the induced map is
$$
\boxed{f_*:\mathbb Z\to\mathbb Z,\qquad k\mapsto nk.}
$$
::: {.proof}
The map $z\mapsto z^n$ has degree $n$. Under the standard identification $\pi_1(S^1)\cong\mathbb Z$, a degree-$n$ map sends the generator to $n$ times the generator.
:::

<1>2. For the antipodal map $f(z)=-z$, the induced map is the identity:
$$
\boxed{f_*(k)=k.}
$$
::: {.proof}
The map $z\mapsto-z=e^{i\pi}z$ is a rotation of the circle, hence is homotopic to the identity through rotations $H_t(z)=e^{i\pi t}z$. Therefore it has degree $1$ and induces the identity on $\pi_1(S^1)$.
:::

<1>3. For
$$
f(e^{i\theta})=e^{2\pi i\sin\theta},
$$
the induced map is zero:
$$
\boxed{f_*(k)=0.}
$$
::: {.proof}
The map has a global real-valued lift through the universal covering $\mathbb R\to S^1$, namely
$$
\widetilde f(e^{i\theta})=2\pi\sin\theta.
$$
Equivalently, the homotopy
$$
H_t(e^{i\theta})=e^{2\pi i t\sin\theta}
$$
contracts $f$ to the constant map $1$. Hence $f$ has degree $0$ and induces the zero homomorphism on $\pi_1(S^1)$.
:::
:::
