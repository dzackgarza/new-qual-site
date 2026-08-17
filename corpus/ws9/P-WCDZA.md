---
schema: qual/card@1
id: P-WCDZA
kind: problem
title: "a. Prove the Riemann-Lebesgue Lemma: if $f \\in L^1(\\mathbb{R}^d)$, the…"
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - l1
  - convolution
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
a. Prove the Riemann-Lebesgue Lemma: if $f \in L^1(\mathbb{R}^d)$, then the Fourier transform of $f$,
$$\hat{f}(\xi) = \int_{\mathbb{R}^d} f(x)e^{-2\pi i x\cdot\xi}dx \to 0, \text{ as } |\xi| \to \infty.$$
b. Use part (a) to justify whether there exists a function $h \in L^1(\mathbb{R}^d)$ such that
$$f * h = f \text{ for all } f \in L^1(\mathbb{R}^d).$$
Here $f*h$ is the convolution of $f$ and $h$ defined by
$$(f*h)(x) = \int_{\mathbb{R}^d} f(x-y)h(y)dx.$$
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** (a) Prove the Riemann–Lebesgue lemma: $f \in L^1(\mathbb R^d) \Rightarrow \hat f(\xi) \to 0$ as $|\xi| \to \infty$; (b) use it to show there is no $h \in L^1$ with $f \ast h = f$ for all $f \in L^1$.

<1>1. (a) $\hat f(\xi) = \int f(x)e^{-2\pi i x\cdot\xi}dx \to 0$ as $|\xi| \to \infty$.
    <2>1. For $f = \chi_{[a,b]}$ (or a cube $\prod[a_j, b_j]$): $\hat f(\xi) = \prod_j \frac{e^{-2\pi i b_j \xi_j} - e^{-2\pi i a_j \xi_j}}{-2\pi i\xi_j}$, which is $O(1/|\xi_1|)$-decaying; $|\hat f(\xi)| \le \frac{C}{|\xi_1|}\prod_{j \ge 2}(b_j - a_j) \to 0$.
        Proof: direct computation of the Fourier transform of an indicator of a box; the denominator grows in $\xi_1$.
    <2>2. $\hat f \to 0$ for step functions (finite linear combinations of box indicators).
        Proof: <2>1 and linearity of the Fourier transform.
    <2>3. Step functions are dense in $L^1(\mathbb R^d)$: given $f \in L^1$ and $\varepsilon > 0$, choose a step function $s$ with $\|f - s\|_1 < \varepsilon/2$.
        Proof: standard approximation of $L^1$ functions by simple functions, then by step functions.
    <2>4. $|\hat f(\xi)| \le |\widehat{f - s}(\xi)| + |\hat s(\xi)| \le \|f - s\|_1 + |\hat s(\xi)| < \varepsilon/2 + |\hat s(\xi)|$.
        Proof: $|\hat g(\xi)| \le \|g\|_1$ for any $g \in L^1$, and the triangle inequality.
    <2>5. Since $|\hat s(\xi)| \to 0$ (by <2>2), choose $R$ with $|\hat s(\xi)| < \varepsilon/2$ for $|\xi| > R$; then $|\hat f(\xi)| < \varepsilon$ for $|\xi| > R$.
        Proof: <2>4 and the choice of $R$.
    <2>6. Q.E.D.
        Proof: <2>5 is $\hat f(\xi) \to 0$ as $|\xi| \to \infty$.

<1>2. (b) There is no $h \in L^1$ with $f \ast h = f$ for all $f \in L^1$.
    <2>1. If such $h$ existed, then for $f \in L^1 \cap L^2$ (say $f \in C_c^\infty$, dense in $L^1$): $\widehat{f \ast h}(\xi) = \hat f(\xi)\hat h(\xi) = \hat f(\xi)$, so $\hat f(\xi)(\hat h(\xi) - 1) = 0$ for all $\xi$.
        Proof: the Fourier transform converts convolution to multiplication.
    <2>2. For some $f$ with $\hat f \neq 0$ everywhere (e.g. $f$ a Gaussian), $\hat h(\xi) = 1$ for all $\xi$.
        Proof: <2>1 with such an $f$.
    <2>3. $\hat h(\xi) \to 0$ as $|\xi| \to \infty$ by the Riemann–Lebesgue lemma (<1>1), since $h \in L^1$ — contradicting $\hat h \equiv 1$.
        Proof: <2>2 says $\hat h \equiv 1$, which does not vanish at infinity.
    <2>4. Q.E.D.
        Proof: <2>1–<2>3 contradict; hence no such $h$ exists. (Convolution with $L^1$ cannot be the identity on $L^1$; the Dirac delta is not an $L^1$ function.)

:::
