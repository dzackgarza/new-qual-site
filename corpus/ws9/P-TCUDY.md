---
schema: qual/card@1
id: P-TCUDY
kind: problem
title: Recall that the inner product on $L^2(\mathbb{R}^d)$ is given by
classification:
  areas:
  - real-analysis
  topics:
  - weak-convergence
  - l2
  - hilbert-spaces
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Recall that the inner product on $L^2(\mathbb{R}^d)$ is given by
$$(f,g) = \int_{\mathbb{R}^d} f(x)\overline{g(x)}dx, \text{ for } f,g \in L^2(\mathbb{R}^d),$$
which induces the $L^2$-norm
$$\|f\|_{L^2} = (f,f)^{1/2}.$$

a. If the sequence of functions $\{f_n\}_{n=1}^\infty$ in $L^2(\mathbb{R}^d)$ satisfy that $\|f_n\|_{L^2}=1$, show that there exists a subsequence of functions $\{f_{n_j}\}_{j=1}^\infty$ such that $f_{n_j}$ converges weakly to some function $f$ in $L^2(\mathbb{R}^d)$, i.e.,
$$(f_{n_j}, g) \to (f,g) \text{ for all } g \in L^2(\mathbb{R}^d).$$
b. If $f_n \to f$ weakly in $L^2(\mathbb{R}^d)$ and $\|f_n\|_{L^2} \to \|f\|_{L^2}$ as $n \to \infty$, show that $\|f_n - f\|_{L^2} \to 0$ as $n \to \infty$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** (a) Show $\|f_n\|_{L^2} = 1$ implies some subsequence converges weakly in $L^2(\mathbb R^d)$; (b) weak + norm convergence implies strong convergence.

<1>1. (a) There is a subsequence $f_{n_j}$ and $f \in L^2$ with $(f_{n_j}, g) \to (f, g)$ for all $g \in L^2$.
    <2>1. $L^2(\mathbb R^d)$ is a Hilbert space, and the closed unit ball of a Hilbert space is weakly compact: every bounded sequence has a weakly convergent subsequence.
        Proof: this is the Banach–Alaoglu theorem in the Hilbert-space setting (or: $L^2$ is separable, so by the diagonal argument using the countable dense set $\{e_k\}$, extract a subsequence with $(f_{n_j}, e_k)$ convergent for all $k$; define $f$ via the Riesz representation theorem and extend to all $g \in L^2$ by density and the uniform bound $\|f_{n_j}\| = 1$).
    <2>2. The sequence $f_n$ is bounded: $\|f_n\|_{L^2} = 1$ for all $n$.
    <2>3. Q.E.D.
        Proof: <2>1 applied to the bounded sequence of <2>2 gives the subsequence.

<1>2. (b) If $f_n \rightharpoonup f$ weakly and $\|f_n\| \to \|f\|$, then $\|f_n - f\| \to 0$.
    <2>1. $\|f_n - f\|^2 = \|f_n\|^2 - 2\operatorname{Re}(f_n, f) + \|f\|^2$.
        Proof: expand the inner product.
    <2>2. $(f_n, f) \to (f, f) = \|f\|^2$.
        Proof: weak convergence $f_n \rightharpoonup f$ applied to the test vector $g = f$.
    <2>3. $\|f_n - f\|^2 \to \|f\|^2 - 2\|f\|^2 + \|f\|^2 = 0$.
        Proof: <2>1 with <2>2 and the hypothesis $\|f_n\| \to \|f\|$.
    <2>4. Q.E.D.
        Proof: <2>3 shows $\|f_n - f\| \to 0$, i.e. strong convergence. (This is the standard "weak convergence plus norm convergence implies strong convergence" — the parallelogram-law variant.)

:::
