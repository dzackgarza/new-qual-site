---
schema: qual/card@1
id: E-FZXFR
kind: exercise
title: "- Is it the case that $f\\in L^1$ implies $\\hat f\\in L^1$?"
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - l1
  - counterexamples
relations: []
review: draft
solved: true
---

::: exercise
- Is it the case that $f\in L^1$ implies $\hat f\in L^1$?

- Show that if $f, \hat f \in L^1$ then $f$ is bounded, uniformly continuous, and vanishes at infinity.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (1) Decide whether $f \in L^1(\RR)$ forces $\hat f \in L^1(\RR)$; (2) show that if $f, \hat f \in L^1$ then $f$ is bounded, uniformly continuous, and vanishes at infinity.

<1>1. $f \in L^1$ does **not** imply $\hat f \in L^1$.
<2>1. Take $f = \chi_{[-1,1]}$, an $L^1$ function.
Proof: $\|f\|_1 = 2 < \infty$.
<2>2. $\hat f(\xi) = \frac{2\sin(\xi)}{\xi}$ (up to the convention-dependent constant), which is not integrable.
Proof: compute $\hat f(\xi) = \int_{-1}^{1} e^{-ix\xi}\,dx = 2\sin(\xi)/\xi$; and $\int |\sin(\xi)/\xi|\,d\xi = \infty$ since $|\sin(\xi)| \geq 1/2$ on a fixed fraction of each period.
<2>3. Q.E.D. Proof: <2>1 and <2>2 exhibit an $L^1$ function whose Fourier transform is not in $L^1$.
<1>2. If $f, \hat f \in L^1$, then $f$ is bounded and uniformly continuous.
<2>1. Fourier inversion holds: $f(x) = \int \hat f(\xi) e^{ix\xi}\,d\xi$ for a.e. $x$ (up to the convention constant).
Proof: the inversion theorem applies because both $f$ and $\hat f$ are integrable.
<2>2. The function $x \mapsto \int \hat f(\xi) e^{ix\xi}\,d\xi$ is bounded by $\|\hat f\|_1$ and is uniformly continuous.
Proof: $|\int \hat f(\xi) e^{ix\xi}\,d\xi| \leq \int |\hat f(\xi)|\,d\xi = \|\hat f\|_1$; and $|\int \hat f(\xi)(e^{i(x+h)\xi} - e^{ix\xi})\,d\xi| \leq \int |\hat f(\xi)|\,|e^{ih\xi} - 1|\,d\xi \to 0$ as $h \to 0$ by dominated convergence ($|e^{ih\xi} - 1| \leq 2$ and $\hat f \in L^1$), uniformly in $x$.
<2>3. Q.E.D. Proof: <2>1 identifies $f$ (a.e.) with the function in <2>2, so $f$ is bounded and uniformly continuous after modification on a null set.
<1>3. Under the same hypotheses, $f$ vanishes at infinity.
Proof: by <1>2<2>1, $|f(x)| \leq \int_{|\xi| \geq R} |\hat f(\xi)|\,d\xi + \int_{|\xi| < R} |\hat f(\xi)| |e^{ix\xi} - 1|\,d\xi$; for fixed $R$, the second term has an integrable dominating function, so its integral over any large interval can be controlled — more directly: $\hat f \in L^1$ implies $\int \hat f(\xi) e^{ix\xi}\,d\xi$ is a uniform limit (as a Fourier integral of an $L^1$ function) of functions with compact Fourier support; each such function tends to $0$ as $|x| \to \infty$ (by the Riemann–Lebesgue lemma applied on the compact interval, or by an integration-by-parts estimate on the smooth truncation), and uniformity of the convergence transfers the vanishing to the limit.
<1>4. Q.E.D. Proof: <1>1 answers (1) negatively; <1>2 and <1>3 prove the claims in (2).
:::
