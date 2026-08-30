---
title: The Schwarz lemma
order: 20
problems:
  topics:
  - Schwarz Lemma
  - Fixed Points
---

# The Schwarz lemma

A holomorphic self-map of the disc fixing the origin cannot expand: it is bounded by the identity, and touching that bound anywhere forces it to *be* a rotation.
It is the source of every rigidity statement in the chapter.

[[T-DAETF]]

[[T-VM6MJ]]

[[FD-BIAA7]] [[FF-5H4UZ]]

![](../../../../assets/assets/figures/2021-10-29_02-32-14.png)

::: {.proof title="of Schwarz"}
\envlist

- Idea: apply the maximum modulus principle to $g(z) \da f(z)/z$.

- $\abs{g(z)} \leq 1$:

  - Expand $f$ at $z=0$ as $\sum_{k\geq 0} c_k z^k$.
    Since $f(0) = 0 = c_0$, the constant term vanishes.

  - So $g(z) \da f(z)/z$ is holomorphic on $\DD$, the singularity at $z=0$ being removable.

  - For $\abs z = r < 1$, $\abs{g(z)} = \abs{f(z)}/r \leq 1/r$ since $\abs{f(z)} \leq 1$.

  - By the maximum modulus principle $\abs{g(z)} \leq 1/r$ on the whole disc $\abs z \leq r$; let $r\to 1$ to get $\abs{g} \leq 1$.

- $\abs{f'(0)} \leq 1$, with equality only for a rotation:

  - Since $f(0)=0$, $g(0) = \lim_{z\to 0}{f(z)-f(0)\over z-0} = f'(0)$.

  - If $\abs{f'(0)} = 1$ then $\abs{g(0)} = 1$, an interior maximum, so $g$ is constant and $f(z) = cz$ with $\abs c = 1$.

- $\abs{f(z_0)} = \abs{z_0}$ for some $z_0 \neq 0$ implies a rotation:

  - Then $\abs{g(z_0)} = 1$ is again an interior maximum, so $g$ is constant and $f(z) = cz$ with $\abs c = 1$, that is $c = e^{i\theta}$.
:::

::: {.proof title="of Schwarz, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-30-35.png)

![](../../../../assets/assets/figures/2021-12-14_16-30-46.png)
:::

::: {.remark title="Why the normalization is not a restriction"}
The hypotheses $f(0)=0$ and $\abs f \leq 1$ look special, but a Blaschke factor moves any point of the disc to the origin, so a self-map with $f(a) = b$ is handled by pre- and post-composing with $\psi_a$ and $\psi_b$.
That composition is exactly how the automorphism group is computed on [[Complex_Analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors and automorphisms]], and it is also how the Schwarz–Pick estimates are derived.
:::

::: {.remark title="What it is used for"}
Three things, in rough order of frequency on an exam: bounding $\abs{f(z)}$ or $\abs{f'(0)}$ for a self-map of the disc, proving a map with too many fixed points is the identity, and proving Liouville, which is on [[Complex_Analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy estimates and Liouville]].
:::

## Exercises

[[E-TJ3WM]] [[E-MIIW7]] [[E-ZSOC4]] [[E-DXQMY]] [[E-QFOOL]] [[E-FJHDQ]] [[E-ZGFJA]] [[E-XQX6X]] [[E-5QAVX]] [[E-TCONN]] [[E-VYIZJ]] [[E-5I2NN]] [[E-FUIDU]] [[E-JSPEB]] [[E-GPFKM]] [[E-XKMVX]] [[E-MCTII]] [[E-3OJLH]]
