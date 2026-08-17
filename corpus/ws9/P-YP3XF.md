---
schema: qual/card@1
id: P-YP3XF
kind: problem
title: Determine whether there is a nonzero smooth compactly supported functi…
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - counterexamples
relations: []
review: draft
---

:::{.problem title="?"}
Determine whether there is a nonzero smooth compactly supported function on $\mathbb{R}$ whose Fourier transform is also compactly supported?
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Determine whether there is a nonzero smooth compactly supported function on $\mathbb R$ whose Fourier transform is also compactly supported.

<1>1. Answer: No — no such function exists (for $f \neq 0$; the zero function trivially has compactly supported transform).
    <2>1. Suppose $f \in C_c^\infty(\mathbb R)$, $f \neq 0$, and $\hat f$ is compactly supported.
    <2>2. Then $\hat f \in C_c(\mathbb R) \subseteq L^1(\mathbb R)$, so $f = \check{\hat f}$-type inversion holds everywhere: $f(x) = \int \hat f(\xi)e^{2\pi i x\xi}d\xi$.
        Proof: the Fourier inversion theorem applies since $\hat f$ is compactly supported hence integrable.
    <2>3. The right-hand side $\int \hat f(\xi)e^{2\pi i x\xi}d\xi$ extends to an entire function of $x \in \mathbb C$ (it is the Fourier transform of the compactly supported $\hat f$, and integrals against $e^{2\pi i x\xi}$ with $x$ complex are holomorphic).
        Proof: differentiate under the integral sign: $\frac{d}{dx}\int \hat f(\xi)e^{2\pi i x\xi}d\xi = \int \hat f(\xi)(2\pi i\xi)e^{2\pi ix\xi}d\xi$, valid since $\hat f$ is compactly supported (the derivatives are bounded integrable); iterating gives holomorphy on all of $\mathbb C$ (an entire function).
    <2>4. Hence $f$ itself is entire (agrees with an entire function on $\mathbb R$).
        Proof: <2>2 and <2>3.
    <2>5. An entire function with compact support on $\mathbb R$ is identically zero.
        Proof: if $f$ is entire and $f \equiv 0$ on $\mathbb R \setminus [-R, R]$, then by the identity theorem (zeros accumulate in $\mathbb R \setminus [-R,R]$), $f \equiv 0$ on $\mathbb C$, contradicting $f \neq 0$.
    <2>6. Q.E.D.
        Proof: <2>2–<2>5: assuming $f \neq 0$ leads to a contradiction, so no nonzero such function exists. (This is a manifestation of the uncertainty principle / Paley–Wiener: a function and its Fourier transform cannot both be compactly supported unless the function is zero.)

:::
