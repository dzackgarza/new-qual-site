---
schema: qual/card@1
id: P-TCUDY
kind: problem
title: 'Weak convergence plus norm convergence implies strong convergence in $L^2$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved JHU May 2013 Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Recall that the inner product on $L^2(\mathbb{R}^d)$ is given by

$$(f, g) = \int_{\mathbb{R}^d} f(x) \overline{g(x)} \, dx, \quad \text{for } f, g \in L^2(\mathbb{R}^d),$$

which induces the $L^2$-norm

$$\|f\|_{L^2} = (f, f)^{1/2}.$$

(a) If the sequence of functions $\{f_n\}_{n=1}^\infty$ in $L^2(\mathbb{R}^d)$ satisfy that $\|f_n\|_{L^2} = 1$, show that there exists a subsequence of functions $\{f_{n_j}\}_{j=1}^\infty$ such that $f_{n_j}$ converges weakly to some function $f$ in $L^2(\mathbb{R}^d)$, i.e.,

$$(f_{n_j}, g) \to (f, g) \quad \text{for all } g \in L^2(\mathbb{R}^d).$$

(b) If $f_n \rightharpoonup f$ weakly in $L^2(\mathbb{R}^d)$ and $\|f_n\|_{L^2} \to \|f\|_{L^2}$ as $n \to \infty$, show that $\|f_n - f\|_{L^2} \to 0$ as $n \to \infty$.

::: {.solution}
<1>1. Prove part (a).
::: {.proof}
The space $L^2(\mathbb R^d)$ is a Hilbert space, hence reflexive. Therefore its closed unit ball is weakly compact. By the Eberlein--Smulian theorem, weak compactness in a Banach space is equivalent to weak sequential compactness.

Since every $f_n$ lies in the unit sphere, in particular in the closed unit ball, there is a subsequence $(f_{n_j})$ and some $f\in L^2(\mathbb R^d)$ such that
\[
f_{n_j}\rightharpoonup f.
\]
Equivalently,
\[
(f_{n_j},g)\longrightarrow(f,g)
\qquad\text{for every }g\in L^2(\mathbb R^d).
\]
:::

<1>2. Prove part (b).
::: {.proof}
Weak convergence gives
\[
(f_n,f)\longrightarrow(f,f)=\|f\|_2^2.
\]
Using the Hilbert-space norm identity,
\[
\begin{aligned}
\|f_n-f\|_2^2
&=\|f_n\|_2^2+\|f\|_2^2-2\operatorname{Re}(f_n,f).
\end{aligned}
\]
By hypothesis,
\[
\|f_n\|_2^2\longrightarrow\|f\|_2^2,
\]
and the weak-convergence term tends to $\|f\|_2^2$. Hence
\[
\|f_n-f\|_2^2\longrightarrow
\|f\|_2^2+\|f\|_2^2-2\|f\|_2^2=0.
\]
Therefore
\[
\boxed{\|f_n-f\|_2\to0.}
\]
:::
:::
