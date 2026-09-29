---
schema: qual/card@1
id: E-SS8.EX-16
kind: problem
title: Automorphisms of the disc through the Cayley transform
classification:
  areas:
  - complex-analysis
  topics:
  - Automorphisms
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
16. Let

$$
f (z) = \frac {i - z}{i + z} \quad \mathrm{and} \quad f ^ {- 1} (w) = i \frac {1 - w}{1 + w}.
$$

(a) Given $\theta \in \mathbb { R }$ , find real numbers $a , b , c ,$ d such that ad $- b c = 1$ , and so that for any $z \in \mathbb { H }$

$$
\frac {a z + b}{c z + d} = f ^ {- 1} \left(e ^ {i \theta} f (z)\right).
$$

(b) Given $\alpha \in \mathbb { D }$ find real numbers $a , b , c ,$ d so that ad $- b c = 1$ , and so that for any $z \in \mathbb { H }$

$$
\frac {a z + b}{c z + d} = f ^ {- 1} \left(\psi_ {\alpha} (f (z))\right),
$$

with $\psi _ { \alpha }$ defined in Section 2.1.

(c) Prove that if g is an automorphism of the unit disc, then there exist real numbers $a , b , c ,$ d such that ad $- b c = 1$ and so that for any $z \in \mathbb { H }$

$$
\frac {a z + b}{c z + d} = f ^ {- 1} \circ g \circ f (z).
$$

[Hint: Use parts (a) and (b).]
:::

::: {.solution}
**Goal.** Express disc automorphisms, conjugated by the Cayley transform $f$, as real Möbius transformations of the upper half-plane.

::: pf

::: pf-step

$f(z) = \frac{i-z}{i+z}$ maps $\HH$ to $\DD$, with inverse $f^{-1}(w) = i\frac{1-w}{1+w}$.

::: pf-proof

the Cayley transform; $f$ sends the upper half-plane to the unit disk and $f^{-1}$ is its inverse.

:::

:::

::: {.pf-step #s2}

(a) For $\theta \in \RR$, find real $a,b,c,d$ with $ad - bc = 1$ and $\frac{az+b}{cz+d} = f^{-1}(e^{i\theta} f(z))$.

::: pf-proof

::: pf-step

$e^{i\theta} f(z)$ is a rotation of the disk, an automorphism of $\DD$.

::: pf-proof

multiplication by $e^{i\theta}$ preserves $\DD$.

:::

:::

::: pf-step

The composition $f^{-1} \circ (\text{rotation by } \theta) \circ f$ is a Möbius transformation of $\HH$ with real coefficients.

::: pf-proof

$f$ and $f^{-1}$ have real coefficients, and the rotation $w \mapsto e^{i\theta} w$ conjugates to a real Möbius map (the stabilizer of $i$ in $\mathrm{PSL}_2(\RR)$).

:::

:::

::: pf-step

Explicitly, $f^{-1}(e^{i\theta} f(z)) = \frac{\cos(\theta/2)\, z + \sin(\theta/2)}{-\sin(\theta/2)\, z + \cos(\theta/2)}$.

::: pf-proof

the rotation by $\theta$ corresponds, under the Cayley transform, to the matrix $\begin{pmatrix} \cos(\theta/2) & \sin(\theta/2) \\ -\sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$, which has determinant $1$ and real entries.

:::

:::

:::

:::

::: {.pf-step #s3}

(b) For $\alpha \in \DD$, find real $a,b,c,d$ with $ad - bc = 1$ and $\frac{az+b}{cz+d} = f^{-1}(\psi_\alpha(f(z)))$.

::: pf-proof

::: pf-step

$\psi_\alpha(w) = \frac{w - \alpha}{1 - \bar\alpha w}$ is the disc automorphism sending $\alpha$ to $0$.

::: pf-proof

this is the standard automorphism of $\DD$ (Section 2.1).

:::

:::

::: pf-step

$f^{-1} \circ \psi_\alpha \circ f$ is a real Möbius transformation of $\HH$.

::: pf-proof

it is an automorphism of $\HH$ (conjugate of an automorphism of $\DD$), and every automorphism of $\HH$ is a real Möbius transformation $\frac{az+b}{cz+d}$ with $ad - bc = 1$.

:::

:::

::: pf-step

The coefficients are real and satisfy $ad - bc = 1$.

::: pf-proof

$\mathrm{Aut}(\HH) \cong \mathrm{PSL}_2(\RR)$, realized by matrices of determinant $1$.

:::

:::

:::

:::

::: {.pf-step #s4}

(c) Every automorphism $g$ of $\DD$ conjugates to a real Möbius transformation of $\HH$.

::: pf-proof

::: pf-step

Every $g \in \mathrm{Aut}(\DD)$ factors as $g = \psi_\alpha \circ (\text{rotation})$.

::: pf-proof

$\mathrm{Aut}(\DD) = \theset{e^{i\theta}\psi_\alpha : \theta \in \RR, \alpha \in \DD}$ (every automorphism is a rotation composed with a $\psi_\alpha$).

:::

:::

::: pf-step

Hence $f^{-1} \circ g \circ f = (f^{-1} \circ \psi_\alpha \circ f) \circ (f^{-1} \circ R_\theta \circ f)$ is a product of real Möbius maps.

::: pf-proof

by steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, each factor is a real Möbius transformation.

:::

:::

::: pf-step

The product is a real Möbius transformation $\frac{az+b}{cz+d}$ with $ad - bc = 1$.

::: pf-proof

$\mathrm{PSL}_2(\RR)$ is closed under composition, and the determinant multiplies to $1$.

:::

:::

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} answer (a), (b), and (c).

:::

:::

:::
