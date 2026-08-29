---
schema: qual/card@1
id: P-RAF11D
kind: problem
title: "Convolution with L^1 kernel preserves weak L^2 convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $K \in L^1(\mathbb{R}^d)$ with Lebesgue measure.
Suppose that $\psi_n \in L^2(\mathbb{R}^d)$ is a sequence of functions such that $\psi_n \to \psi$ (weak $L^2$ convergence), and also with the property that $\psi_n \equiv 0$ for $|x| > 1$.
Show that
$$
f_n(x) = \int_{\mathbb{R}^d} K(x-y)\,\psi_n(y)\,dy
$$
converges to
$$
f(x) = \int_{\mathbb{R}^d} K(x-y)\,\psi(y)\,dy
$$
strongly in $L^2(\mathbb{R}^d)$.
:::

::: {.solution}
<1>1. $f_n = K * \psi_n$ and $f = K * \psi$.
Proof: definition of convolution.

<1>2. $f_n - f = K * (\psi_n - \psi)$.
Proof: <1>1 and linearity of convolution.

<1>3. Since $\psi_n \to \psi$ weakly in $L^2$ and $\psi_n \equiv 0$ for $|x| > 1$, the sequence $\psi_n$ is bounded in $L^2$ (by the uniform boundedness principle) and supported in the unit ball.
Proof: weakly convergent sequences are bounded, and the support condition.

<1>4. For fixed $x$, $f_n(x) - f(x) = \int K(x - y)(\psi_n(y) - \psi(y))\,dy = \langle \psi_n - \psi, \overline{K(x - \cdot)} \rangle$.
Proof: <1>2, writing the integral as an inner product.

<1>5. Since $\psi_n \to \psi$ weakly and $K(x - \cdot) \in L^2$ (as $K \in L^1$ and the support of $\psi_n$ is bounded, $K(x - \cdot)$ restricted to the unit ball is in $L^2$), we get $f_n(x) \to f(x)$ pointwise.
Proof: <1>4 and weak convergence.

<1>6. To get strong $L^2$ convergence, note that the operator $T_K : L^2 \to L^2$, $\psi \mapsto K * \psi$ is compact (since $K \in L^1$ and the functions are supported in a fixed compact set, $T_K$ is a Hilbert–Schmidt-type operator, or more directly, $T_K$ is the limit of finite-rank operators).
Proof: convolution with an $L^1$ kernel on a bounded domain is compact.

<1>7. A compact operator maps weakly convergent sequences to strongly convergent sequences.
Proof: standard fact (a compact operator is completely continuous).

<1>8. Hence $f_n = T_K \psi_n \to T_K \psi = f$ strongly in $L^2$.
Proof: <1>6 and <1>7.

<1>9. Q.E.D.
Proof: <1>8.
:::
