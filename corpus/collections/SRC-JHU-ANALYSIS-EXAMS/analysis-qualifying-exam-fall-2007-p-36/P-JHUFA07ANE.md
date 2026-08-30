---
schema: qual/card@1
id: P-JHUFA07ANE
kind: problem
title: "Membership examples separating L1 and L2"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

5) Give examples of functions f and g on R so that $f \in L ^ { 1 } \setminus L ^ { 2 }$ and $g \in L ^ { 2 } \setminus L ^ { 1 }$

::: {.solution}
<1>1. Construction and verification of $f \in L^1(\mathbb{R}) \setminus L^2(\mathbb{R})$:
<2>1. Define the function $f: \mathbb{R} \to \mathbb{R}$ by:
\[
f(x) = \frac{1}{\sqrt{x}} \mathbf{1}_{(0, 1]}(x) = \begin{cases} x^{-1/2} & \text{if } 0 < x \le 1, \\ 0 & \text{otherwise.} \end{cases}
\]
Proof: definition of $f$.
<2>2. **$L^1$ integrability:**
\[
\|f\|_{L^1} = \int_{-\infty}^\infty |f(x)| \, dx = \int_0^1 x^{-1/2} \, dx = \left[ 2x^{1/2} \right]_0^1 = 2 < \infty.
\]
Thus $f \in L^1(\mathbb{R})$.
Proof: integration of power functions.
<2>3. **Non-membership in $L^2$:**
\[
\|f\|_{L^2}^2 = \int_{-\infty}^\infty |f(x)|^2 \, dx = \int_0^1 x^{-1} \, dx = \lim_{\epsilon \to 0^+} \Big[ \ln x \Big]_\epsilon^1 = \lim_{\epsilon \to 0^+} (-\ln \epsilon) = +\infty.
\]
Thus $f \notin L^2(\mathbb{R})$.
Proof: divergence of harmonic integral near 0.

<1>2. Construction and verification of $g \in L^2(\mathbb{R}) \setminus L^1(\mathbb{R})$:
<2>1. Define the function $g: \mathbb{R} \to \mathbb{R}$ by:
\[
g(x) = \frac{1}{x} \mathbf{1}_{[1, \infty)}(x) = \begin{cases} x^{-1} & \text{if } x \ge 1, \\ 0 & \text{otherwise.} \end{cases}
\]
Proof: definition of $g$.
<2>2. **$L^2$ integrability:**
\[
\|g\|_{L^2}^2 = \int_{-\infty}^\infty |g(x)|^2 \, dx = \int_1^\infty x^{-2} \, dx = \left[ -x^{-1} \right]_1^\infty = 0 - (-1) = 1 < \infty.
\]
Thus $g \in L^2(\mathbb{R})$.
Proof: integration of $x^{-2}$ at infinity.
<2>3. **Non-membership in $L^1$:**
\[
\|g\|_{L^1} = \int_{-\infty}^\infty |g(x)| \, dx = \int_1^\infty x^{-1} \, dx = \lim_{R \to \infty} \Big[ \ln x \Big]_1^R = \lim_{R \to \infty} \ln R = +\infty.
\]
Thus $g \notin L^1(\mathbb{R})$.
Proof: divergence of harmonic integral at infinity.

<1>3. Conclusion:
$f(x) = x^{-1/2} \mathbf{1}_{(0, 1]}(x) \in L^1(\mathbb{R}) \setminus L^2(\mathbb{R})$ and $g(x) = x^{-1} \mathbf{1}_{[1, \infty)}(x) \in L^2(\mathbb{R}) \setminus L^1(\mathbb{R})$. Q.E.D.
Proof: <1>1 and <1>2.
:::
