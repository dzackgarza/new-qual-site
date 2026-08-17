---
schema: qual/card@1
id: P-4ZZYV
kind: problem
title: "Let $f$ be entire and suppose that $\\lim_{z \\rightarrow \\infty} f(z) = \\infty$. Show that $f$ is a polynomial."
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - singularities
relations: []
review: draft
solved: true
---

::: problem
Let $f$ be entire and suppose that $\lim_{z \rightarrow \infty} f(z) = \infty$.
Show that $f$ is a polynomial.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that if $f$ is entire and $\lim_{z \to \infty} f(z) = \infty$, then $f$ is a polynomial.

<1>1. Define $g(w) := f\qty(\frac{1}{w})$ for $w \neq 0$; then $g$ is holomorphic on $\CC \setminus \theset{0}$.
Proof: Composition of the holomorphic maps $w \mapsto 1/w$ and $f$.

<1>2. $w = 0$ is a pole of $g$, not an essential singularity.
<2>1. $\lim_{w \to 0} g(w) = \infty$.
Proof: As $w \to 0$, $1/w \to \infty$ in modulus, and $\lim_{z \to \infty} f(z) = \infty$ by hypothesis.
<2>2. $0$ is not essential.
Proof: If $0$ were an essential singularity, then by Casorati--Weierstrass the values $g(w)$ would be dense in $\CC$ for $w$ near $0$, contradicting $\abs{g(w)} \to \infty$; equivalently $1/g$ is bounded near $0$ with limit $0$, a removable singularity, so $g$ has a pole.

<1>3. $g$ has a pole of some order $m \geq 1$ at $0$, so its Laurent expansion is $g(w) = \sum_{k=-m}^{\infty} c_k w^k$.
Proof: By <1>2, the Laurent series about $0$ has only finitely many negative powers, the most negative being $-m$.

<1>4. For $z \neq 0$, $f(z) = \sum_{k=-m}^{\infty} c_k z^{-k} = \sum_{k=0}^{m} c_{-k} z^k + \sum_{j=1}^{\infty} c_j z^{-j}$.
Proof: Substitute $w = 1/z$ into <1>3.

<1>5. The tail $\sum_{j=1}^{\infty} c_j z^{-j}$ vanishes: $c_j = 0$ for all $j \geq 1$.
Proof: $f$ is entire, so its Laurent expansion about $z = 0$ (which is <1>4, valid for $z \neq 0$ and hence on a punctured neighborhood of $0$) has no negative powers of $z$; the terms $c_j z^{-j}$ are exactly the negative powers.

<1>6. $f$ is a polynomial.
Proof: <1>4 and <1>5 give $f(z) = \sum_{k=0}^{m} c_{-k} z^k$, a polynomial of degree at most $m$.

<1>7. Q.E.D. Proof: <1>6 is the claim.
:::
