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
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared May 2006 problem 11 on PDF page 41 and restored the ordinary limsup notation."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Handled zero vectors in the norm-attainment argument, checked conjugation against the chosen inner-product convention and verified the hypotheses for uniform boundedness."
---

Suppose $f_n\in L^2([0,1])$ converges weakly to $f\in L^2([0,1])$. Prove that $\limsup_{n\to\infty}\|f_n\|_2<\infty$, or give a counterexample.

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
Cauchy–Schwarz gives $|\phi_n(g)|\leq\|g\|_2\|f_n\|_2$.
If $f_n\ne0$, the unit vector $g=f_n/\|f_n\|_2$
attains this bound. If $f_n=0$, then $\phi_n=0$ and
both norms are zero. Thus the norm identity holds for
every $n$ without division by a zero norm [@Fol13].
:::

<1>2. Pointwise boundedness from weak convergence:
<2>1. By definition of weak convergence $f_n \rightharpoonup f$, for each fixed $g \in H$:
\[
\lim_{n \to \infty} \phi_n(g) = \lim_{n \to \infty} \langle g, f_n \rangle = \langle g, f \rangle.
\]
::: {.proof}
For fixed $g$, the map $h\mapsto\langle h,g\rangle$
is bounded and linear. Weak convergence gives
$\langle f_n,g\rangle\to\langle f,g\rangle$.
Taking complex conjugates gives the displayed convergence
for $\phi_n(g)=\langle g,f_n\rangle$.
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
The domain $H$ is complete, each $\phi_n$ is bounded
and linear by <1>1, and <1>2 establishes pointwise
boundedness. These are exactly the hypotheses of the
uniform boundedness principle [@Fol13].
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
