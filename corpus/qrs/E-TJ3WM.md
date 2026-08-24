---
schema: qual/card@1
id: E-TJ3WM
kind: exercise
title: Holomorphic automorphisms of $\CC$ are the maps $z\mapsto az+b$ with $a\neq
  0$
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Entire Functions
  - Singularities
relations: []
review: draft
---

::: {.exercise title="?"}
Show that $\Aut_\CC(\CC) = \ts{ z \mapsto az+b\st a\in \CC\units, b\in \CC }$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that the holomorphic automorphisms of $\CC$ are exactly the affine maps $z \mapsto az + b$ with $a \in \CC^{\times}$, $b \in \CC$.

<1>1. Every affine map $z \mapsto az + b$, $a \neq 0$, is a holomorphic automorphism of $\CC$.
Proof: It is entire, and its inverse $z \mapsto (z - b)/a$ is also entire; both are bijections of $\CC$ onto itself.

<1>2. Let $f \in \Aut_\CC(\CC)$.
Consider the singularity of $f$ at $\infty$.
Proof: $f$ is entire, so it has a power series expansion $f(z) = \sum_{n \ge 0} c_n z^n$ converging on all of $\CC$.
The nature of the singularity at $\infty$ is determined by the series.

<1>3. The singularity at $\infty$ is a pole, not an essential singularity.
Proof: If $\infty$ were an essential singularity, then by the Casorati–Weierstrass theorem (or the open mapping theorem on neighborhoods of $\infty$), $f$ would not be injective near $\infty$ — in fact $f(\CC)$ would be dense in $\CC$ and $f$ could not be injective on all of $\CC$.
More elementarily: $f$ is a bijection of $\CC$, so as $z \to \infty$ along any sequence, $f(z) \to \infty$ (otherwise a sequence $z_n \to \infty$ with $f(z_n)$ bounded would have a convergent subsequence $f(z_{n_k}) \to w$, and injectivity + open mapping would be violated — indeed $f(z_{n_k}) \to w$ with $z_{n_k} \to \infty$ is impossible for a biholomorphism of $\CC$). Hence $\infty$ is a pole of $f$.

<1>4. A pole at $\infty$ means $f$ is a polynomial.
Proof: If $\infty$ is a pole of order $m$, then $f(z) = \sum_{n=0}^m c_n z^n$ is a polynomial of degree $m$: the power series expansion has only finitely many nonzero terms.

<1>5. The polynomial $f$ has degree exactly 1. Proof: A polynomial of degree $d \ge 2$ is not injective on $\CC$ (the equation $f(z) = w$ has $d$ roots counting multiplicity for generic $w$; by the fundamental theorem of algebra it is not one-to-one).
A polynomial of degree $0$ is constant, not a bijection.
Since $f$ is a bijection, $d = 1$.

<1>6. Q.E.D. Proof: <1>1 and <1>5 show $\Aut_\CC(\CC)$ consists exactly of the maps $z \mapsto az + b$ with $a \neq 0$.
:::
