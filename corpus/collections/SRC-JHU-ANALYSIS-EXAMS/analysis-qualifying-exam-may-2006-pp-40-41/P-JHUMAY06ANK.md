---
schema: qual/card@1
id: P-JHUMAY06ANK
kind: problem
title: "Boundedness of a weakly convergent sequence in $L^2([0,1])$"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

11. Suppose that $f _ { n }$ is a sequence of functions in $L ^ { 2 } ( [ 0 , 1 ] )$ that converges weakly to a function $f \in L ^ { 2 } ( [ 0 , 1 ] )$ . Either prove that lim $\begin{array} { r } { \operatorname* { s u p } _ { n \to \infty } \vert \vert f _ { n } \vert \vert _ { L ^ { 2 } ( [ 0 , 1 ] ) } < \infty } \end{array}$ or give a counter-example.

::: {.solution}
<1>1. Functional representation and operator norm:
<2>1. Let $H = L^2([0, 1])$ with standard inner product $\langle g, h \rangle = \int_0^1 g(x) \overline{h(x)} \, dx$.
For each $n \ge 1$, define the linear functional $\phi_n: H \to \mathbb{C}$ by:
\[
\phi_n(g) = \langle g, f_n \rangle = \int_0^1 g(x) \overline{f_n(x)} \, dx.
\]
::: {.proof}
definition of functional.
:::
<2>2. By the Cauchy–Schwarz inequality, each $\phi_n$ is a bounded linear functional on $H$, and its operator norm is:
\[
\|\phi_n\|_{H^*} = \sup_{\|g\|_{L^2} \le 1} |\langle g, f_n \rangle| = \|f_n\|_{L^2}.
\]
::: {.proof}
Riesz Representation Theorem / Cauchy–Schwarz equality condition with $g = f_n / \|f_n\|_{L^2}$.
:::

<1>2. Pointwise boundedness from weak convergence:
<2>1. By definition of weak convergence $f_n \rightharpoonup f$, for each fixed $g \in H$:
\[
\lim_{n \to \infty} \phi_n(g) = \lim_{n \to \infty} \langle g, f_n \rangle = \langle g, f \rangle.
\]
::: {.proof}
definition of weak convergence in a Hilbert space.
:::
<2>2. Because every convergent sequence in $\mathbb{C}$ is bounded, for each fixed $g \in H$:
\[
\sup_{n \ge 1} |\phi_n(g)| < \infty.
\]
::: {.proof}
convergence implies boundedness in metric spaces.
:::

<1>3. Application of the Uniform Boundedness Principle:
<2>1. Since $H = L^2([0, 1])$ is a complete normed space (Banach space), the Uniform Boundedness Principle (Banach–Steinhaus Theorem) implies that pointwise boundedness of $\{\phi_n\}$ implies uniform boundedness in operator norm:
\[
\sup_{n \ge 1} \|\phi_n\|_{H^*} < \infty.
\]
::: {.proof}
Uniform Boundedness Principle on Banach spaces.
:::
<2>2. Substituting $\|\phi_n\|_{H^*} = \|f_n\|_{L^2}$ from <1>1:
\[
\sup_{n \ge 1} \|f_n\|_{L^2([0, 1])} < \infty \implies \limsup_{n \to \infty} \|f_n\|_{L^2([0, 1])} < \infty.
\]
::: {.proof}
supremum bounds the limit superior.
:::

<1>4. Conclusion:
Every weakly convergent sequence in $L^2([0, 1])$ is norm-bounded, so $\limsup_{n \to \infty} \|f_n\|_{L^2} < \infty$. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
