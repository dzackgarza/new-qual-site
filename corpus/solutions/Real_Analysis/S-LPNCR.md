---
schema: qual/card@1
id: S-LPNCR
kind: solution
title: Solution to P-7Q5AM
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Hilbert Spaces
  - Functional Analysis
relations:
- kind: solves
  target: P-7Q5AM
review: draft
---

::: solution
**Goal:** Prove that the unit sphere $S$ of an infinite-dimensional real Hilbert space $H$ is weakly dense in the closed unit ball $B$ in (a), and construct operators $T_n$ with $\|T_n\| = 1$ converging strongly to 0 in (b).

<1>1. Part (a): Weak density of $S$ in $B$.
    *Proof:*
    <2>1. Let $x_0 \in B$, so $\|x_0\| \le 1$. If $\|x_0\| = 1$, then $x_0 \in S$, and the constant sequence $x_n = x_0$ converges to $x_0$.
    <2>2. Assume $\|x_0\| < 1$, and let $c = \sqrt{1 - \|x_0\|^2} > 0$.
    <2>3. Since $H$ is infinite-dimensional, the orthogonal complement $x_0^\perp$ is infinite-dimensional.
    <2>4. Choose an orthonormal sequence $\{e_n\}_{n=1}^\infty \subset x_0^\perp$.
    <2>5. Define $x_n = x_0 + c e_n$ for $n \ge 1$.
    <2>6. Since $\langle x_0, e_n \rangle = 0$ and $\|e_n\| = 1$, we have $\|x_n\|^2 = \|x_0\|^2 + c^2 = \|x_0\|^2 + (1 - \|x_0\|^2) = 1$, so $x_n \in S$ for all $n$.
    <2>7. For any fixed $y \in H$, Bessel's inequality gives $\sum_{n=1}^\infty |\langle y, e_n \rangle|^2 \le \|y\|^2 < \infty$, which implies $\lim_{n \to \infty} \langle y, e_n \rangle = 0$.
    <2>8. Thus $\lim_{n \to \infty} \langle x_n, y \rangle = \langle x_0, y \rangle + c \lim_{n \to \infty} \langle e_n, y \rangle = \langle x_0, y \rangle$, so $x_n \rightharpoonup x_0$ weakly.
    <2>9. Therefore $S$ is weakly dense in $B$.

<1>2. Part (b): Rank-1 operators of norm 1 converging strongly to 0.
    *Proof:*
    <2>1. Fix an orthonormal sequence $\{e_n\}_{n=1}^\infty$ in $H$, and fix a unit vector $u \in H$ with $\|u\| = 1$ (e.g. $u = e_1$).
    <2>2. Define the linear operators $T_n(x) = \langle x, e_n \rangle u$ for all $x \in H$.
    <2>3. By Cauchy–Schwarz, $\|T_n(x)\| = |\langle x, e_n \rangle| \|u\| \le \|x\| \|e_n\| = \|x\|$, so $\|T_n\| \le 1$.
    <2>4. Evaluating at $e_n$ gives $\|T_n(e_n)\| = |\langle e_n, e_n \rangle| \|u\| = 1$, so $\|T_n\| = 1$ for all $n \ge 1$.
    <2>5. For any fixed $x \in H$, Bessel's inequality gives $\lim_{n \to \infty} |\langle x, e_n \rangle| = 0$, so $\lim_{n \to \infty} \|T_n(x)\| = 0$.
    <2>6. Thus $T_n(x) \to 0$ strongly for all $x \in H$.
:::
