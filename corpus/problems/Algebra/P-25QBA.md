---
schema: qual/card@1
id: P-25QBA
kind: problem
title: Translation-invariant subspaces of $L^1$ as convolution algebras relative to
  $L^2$
classification:
  areas:
  - algebra
  topics:
  - Convolution
  - Function Spaces
  - Algebras
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $M \subseteq L^1(\mathbb{R})$ be a closed, translation-invariant subspace.
(1) Prove that $M$ is a closed ideal in the convolution Banach algebra $(L^1(\mathbb{R}), *)$.
(2) Explain the connection with Wiener's Tauberian Theorem and the Fourier transform.
(3) Discuss its relation to $L^2(\mathbb{R})$ as a convolution module / algebra and the Plancherel transform.
:::

::: solution
**Goal:** Prove that closed translation-invariant subspaces of $L^1(\mathbb{R})$ are closed convolution ideals, and relate them to $L^2(\mathbb{R})$ through the Fourier transform and multiplier theory.

<1>1. Translation Invariance Implies Closed Convolution Ideal in $L^1(\mathbb{R})$:
    *Proof:*
    <2>1. Let $\tau_y f(x) = f(x - y)$ be the translation operator on $L^1(\mathbb{R})$.
    <2>2. Suppose $M \subseteq L^1(\mathbb{R})$ is a closed subspace such that $\tau_y(f) \in M$ for all $f \in M$ and $y \in \mathbb{R}$.
    <2>3. Let $f \in M$ and $g \in L^1(\mathbb{R})$. The convolution $g * f$ is given by the Bochner integral:
        $$(g * f)(x) = \int_\mathbb{R} g(y) f(x - y) \, dy = \int_\mathbb{R} g(y) \tau_y f(x) \, dy.$$
    <2>4. Approximating the integral by Riemann sums:
        $$S_n = \sum_{k} g(y_k) \tau_{y_k} f \cdot \Delta y_k.$$
        Since $M$ is a linear subspace, each finite sum $S_n \in M$.
    <2>5. Because the Riemann sums converge to $g * f$ in the $L^1$-norm and $M$ is **closed**, we have:
        $$g * f \in M.$$
    <2>6. Therefore, $M$ is a **closed two-sided ideal** in the commutative Banach algebra $(L^1(\mathbb{R}), *)$.

<1>2. Wiener's Tauberian Theorem and the Fourier Transform:
    *Proof:*
    <2>1. Under the Gelfand transform, the maximal ideal space of $L^1(\mathbb{R})$ is identified with $\mathbb{R}$ via the Fourier transform $\mathcal{F}(f)(\xi) = \hat{f}(\xi) = \int_\mathbb{R} f(x) e^{-i \xi x} dx$.
    <2>2. **Wiener's Tauberian Theorem:** A closed translation-invariant subspace $M \subseteq L^1(\mathbb{R})$ equals all of $L^1(\mathbb{R})$ if and only if the zero set:
        $$Z(M) \coloneqq \{\xi \in \mathbb{R} \mid \hat{f}(\xi) = 0 \ \forall f \in M\}$$
        is **empty** ($Z(M) = \varnothing$).
    <2>3. Every proper closed ideal $M$ corresponds to a closed subset $E = Z(M) \subset \mathbb{R}$.

<1>3. Relation to $L^2(\mathbb{R})$ as a Convolution Module:
    *Proof:*
    <2>1. By Young's Inequality for convolutions:
        $$\|f * g\|_{L^2} \le \|f\|_{L^1} \|g\|_{L^2} \quad \text{for } f \in L^1(\mathbb{R}), \; g \in L^2(\mathbb{R}).$$
    <2>2. Thus $L^2(\mathbb{R})$ is a **Banach module** over the convolution algebra $L^1(\mathbb{R})$.
    <2>3. Under the unitary Fourier-Plancherel transform $\mathcal{F}: L^2(\mathbb{R}) \xrightarrow{\sim} L^2(\mathbb{R})$:
        $$\mathcal{F}(f * g)(\xi) = \hat{f}(\xi) \cdot \hat{g}(\xi).$$
    <2>4. For a closed translation-invariant subspace $V \subseteq L^2(\mathbb{R})$, $V$ corresponds under Plancherel to a **multiplication invariant subspace** $L^2(E) = \{h \in L^2(\mathbb{R}) \mid h = 0 \text{ a.e. outside } E\}$ for some measurable set $E \subseteq \mathbb{R}$.
    <2>5. The action of $M \subset L^1$ on $L^2(\mathbb{R})$ maps $L^2(\mathbb{R})$ into the subspace supported on the complement of the zero set $Z(M)$.

<1>4. Conclusion:
    Closed translation-invariant subspaces of $L^1$ are closed convolution ideals characterized by their Fourier zero sets, acting boundedly on $L^2$ as spectral projection multipliers. Q.E.D.
:::
