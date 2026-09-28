---
title: The Schwarz lemma
order: 20
topics:
- Schwarz Lemma
- Fixed Points
---

# The Schwarz lemma

A holomorphic map $f\colon\DD\to\DD$ with $f(0)=0$ satisfies $\abs{f(z)}\leq\abs z$ and $\abs{f'(0)}\leq 1$, and equality in either bound, at a single $z\neq 0$ in the first, holds only for a rotation.

[[T-DAETF]]

[[T-VM6MJ]]

[[FF-5H4UZ]]

![](../../../../assets/assets/figures/2021-10-29_02-32-14.png)

::: {.proof title="Schwarz lemma"}
The proof applies the maximum modulus principle to $g(z) \coloneqq f(z)/z$.

- $\abs{g(z)} \leq 1$:

  - Expand $f$ at $z=0$ as $\sum_{k\geq 0} c_k z^k$.
    Since $f(0) = 0 = c_0$, the constant term vanishes.

  - So $g(z) \coloneqq f(z)/z$ is holomorphic on $\DD$, the singularity at $z=0$ being removable.

  - For $\abs z = r < 1$, $\abs{g(z)} = \abs{f(z)}/r \leq 1/r$ since $\abs{f(z)} < 1$.

  - By the maximum modulus principle $\abs{g(z)} \leq 1/r$ on the whole disc $\abs z \leq r$; let $r\to 1$ to get $\abs{g} \leq 1$.

- $\abs{f'(0)} \leq 1$, with equality only for a rotation:

  - Since $f(0)=0$, $g(0) = \lim_{z\to 0}{f(z)-f(0)\over z-0} = f'(0)$.

  - If $\abs{f'(0)} = 1$ then $\abs g$, which is at most $1$, has a maximum at the interior point $0$, so $g$ is constant and $f(z) = cz$ with $\abs c = 1$.

- $\abs{f(z_0)} = \abs{z_0}$ for some $z_0 \neq 0$ implies a rotation:

  - Then $\abs g$ has a maximum at the interior point $z_0$, so $g$ is constant and $f(z) = cz$ with $\abs c = 1$.
:::

::: {.proof title="Schwarz lemma, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-30-35.png)

![](../../../../assets/assets/figures/2021-12-14_16-30-46.png)
:::

::: {.remark title="Schwarz–Pick inequality"}
For $a\in\DD$ the [[D-MFPYG|Blaschke factor]] $\psi_a(z) = (a-z)/(1-\bar a z)$ is an automorphism of $\DD$ with $\psi_a(0)=a$, $\psi_a(a)=0$, and $\psi_a\circ\psi_a = \id$.
Let $f\colon\DD\to\DD$ be holomorphic, $a\in\DD$ and $b\coloneqq f(a)$.
Then $h\coloneqq\psi_b\circ f\circ\psi_a$ maps $\DD$ to $\DD$ with $h(0)=0$, and the Schwarz lemma applied to $h$ at $w=\psi_a(z)$ gives
$$
\abs{\psi_{f(a)}(f(z))} \leq \abs{\psi_a(z)}, \qquad z\in\DD
.$$
The same conjugation computes the automorphism group on [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors and automorphisms]].
:::

::: {.example title="Two fixed points"}
A holomorphic $f\colon\DD\to\DD$ with two distinct fixed points $a$ and $c$ is the identity.
The map $h\coloneqq\psi_a\circ f\circ\psi_a$ fixes $0$ and $z_0\coloneqq\psi_a(c)\neq 0$, so $\abs{h(z_0)}=\abs{z_0}$ and $h(z)=\lambda z$ with $\abs\lambda=1$ by the Schwarz lemma.
Since $h(z_0)=z_0\neq 0$, $\lambda = 1$, so $h=\id$ and $f=\psi_a\circ h\circ\psi_a=\id$.
:::

The Schwarz lemma also gives a proof of Liouville's theorem, on [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy estimates and Liouville]].

## Exercises

[[E-TJ3WM]] [[E-MIIW7]] [[E-ZSOC4]] [[E-DXQMY]] [[E-QFOOL]] [[E-FJHDQ]] [[E-ZGFJA]] [[E-XQX6X]] [[E-5QAVX]] [[E-TCONN]] [[E-VYIZJ]] [[E-5I2NN]] [[E-FUIDU]] [[E-JSPEB]] [[E-GPFKM]] [[E-XKMVX]] [[E-MCTII]] [[E-3OJLH]]
