---
schema: qual/card@1
id: P-RASP16G
kind: problem
title: "Weak convergence in C_0 is uniform boundedness plus pointwise convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - C0 Spaces
  - Locally Compact Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $X$ be a locally compact Hausdorff topological vector space.
Let $f \in C_0(X)$ and $f_k \in C_0(X)$ ($k = 1, 2, \ldots$). Prove that $f_k \to f$ weakly in $C_0(X)$ if and only if $\sup_{k \geq 1} \|f_k\|_u < \infty$ and $f_k \to f$ pointwise on $X$.
:::

::: {.solution}
<1>1. Duality for $C_0(X)$:
<2>1. By the Riesz–Markov–Kakutani Representation Theorem, the continuous dual space $C_0(X)^*$ is isometrically isomorphic to $M(X)$, the Banach space of regular complex Borel measures on $X$ equipped with the total variation norm $\|\mu\| = |\mu|(X)$.
Proof: Riesz–Markov–Kakutani Representation Theorem on locally compact Hausdorff spaces.
<2>2. Thus $f_k \to f$ weakly in $C_0(X)$ if and only if $\int_X f_k\,d\mu \to \int_X f\,d\mu$ for every $\mu \in M(X)$.
Proof: definition of weak convergence.

<1>2. Forward direction ($\implies$): Weak convergence implies uniform boundedness and pointwise convergence:
<2>1. In any normed space, every weakly convergent sequence $\{f_k\}$ is norm-bounded.
Viewing each $f_k$ as a linear functional on the dual space $C_0(X)^*$, the principle of uniform boundedness implies:
\[
\sup_{k \ge 1} \|f_k\|_u = \sup_{k \ge 1} \sup_{\|\mu\| \le 1} \left|\int_X f_k\,d\mu\right| < \infty.
\]
Proof: Uniform Boundedness Principle (Banach–Steinhaus).
<2>2. For each fixed point $x \in X$, the Dirac point mass $\delta_x \in M(X)$ is a bounded Radon measure with $\|\delta_x\| = 1$.
Proof: definition of Dirac measure.
<2>3. Applying weak convergence to $\mu = \delta_x$ yields:
\[
f_k(x) = \int_X f_k\,d\delta_x \xrightarrow{k \to \infty} \int_X f\,d\delta_x = f(x).
\]
Thus $f_k(x) \to f(x)$ pointwise on $X$.
Proof: definition of integration against Dirac delta.

<1>3. Reverse direction ($\impliedby$): Uniform boundedness and pointwise convergence imply weak convergence:
<2>1. Assume $\sup_{k \ge 1} \|f_k\|_u \le M < \infty$ and $f_k(x) \to f(x)$ for all $x \in X$.
Proof: hypothesis.
<2>2. Let $\mu \in M(X)$ be an arbitrary regular complex Borel measure.
Then $|\mu|(X) < \infty$, so the constant function $g(x) \equiv M$ is in $L^1(X, |\mu|)$.
Proof: finiteness of total variation for measures in $M(X)$.
<2>3. For all $k \ge 1$ and $x \in X$, $|f_k(x)| \le M$.
Proof: <2>1.
<2>4. By the Lebesgue Dominated Convergence Theorem:
\[
\lim_{k \to \infty} \int_X f_k(x)\,d\mu(x) = \int_X \lim_{k \to \infty} f_k(x)\,d\mu(x) = \int_X f(x)\,d\mu(x).
\]
Proof: Dominated Convergence Theorem applied with dominating function $g \equiv M$.
<2>5. Since this holds for all $\mu \in M(X) \cong C_0(X)^*$, $f_k \to f$ weakly in $C_0(X)$.
Proof: <1>1.

<1>4. Conclusion:
$f_k \to f$ weakly in $C_0(X)$ if and only if $\sup_{k \ge 1} \|f_k\|_u < \infty$ and $f_k \to f$ pointwise. Q.E.D.
Proof: <1>2 and <1>3.
:::
