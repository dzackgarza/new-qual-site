---
schema: qual/card@1
id: P-WMJZB
kind: problem
title: "Weak and strong convergence in Hilbert space, with Banach-Saks subsequence means"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the Spring 2017 JHU analysis qualifying exam in the preserved packet; the title was repaired from degraded OCR.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
2. Let H be a Hilbert space equipped with an inner product $( \cdot , \cdot )$ and a norm $\norm{  \cdot }  = ( \cdot , \cdot ) ^ { \frac { 1 } { 2 } }$ Recall the following: A sequence $\{ f _ { k } \} \subset { \mathcal { H } }$ is said converge to $f \in \mathcal H$ if $\norm{  f _ { k } - f }  \to 0$ . A sequence $\{ f _ { k } \} \subset { \mathcal { H } }$ is said converge weakly to $f \in { \mathcal { H } }$ if $( f _ { k } , g ) \to ( f , g )$ for any $g \in { \mathcal { H } }$ . Prove the following statements:

(a) $\{ f _ { k } \}$ converges to f if and only if $\norm{  f _ { k } }  \to \norm{  f } $ and $\{ f _ { k } \}$ converges weakly to $f .$

(b) If H is a finite dimensional Hilbert space, then the weak convergence implies convergence.
Give a counter example to show that weak convergence does not necessarily imply convergence in an infinite dimensional Hilbert space.

(c) If a sequence $\{ f _ { k } \}$ converges weakly to $f ,$ then there exists a subsequence $\{ f _ { k _ { n } } \}$ such that

$$
\frac { f _ { k _ { 1 } } + \cdots + f _ { k _ { n } } } { n }
$$

converges to $f .$ (You may use the fact that a weakly convergent sequence is a bounded sequence.)
:::

::: {.solution}

::: pf

::: pf-step

Prove part (a).

::: pf-proof

If $f_k\to f$ in norm, then continuity of the norm gives
$$
\norm{f_k}\to\norm{f},
$$
and for every $g\in H$,
$$
\abs{\langle f_k-f,g\rangle}
\le \norm{f_k-f}\,\norm{g}\to0,
$$
so $f_k\rightharpoonup f$.

Conversely, assume $f_k\rightharpoonup f$ and
$$
\norm{f_k}\to\norm{f}.
$$
Then
$$
\begin{aligned}
\norm{f_k-f}^2
&=\norm{f_k}^2+\norm{f}^2
-2\operatorname{Re}\langle f_k,f\rangle.
\end{aligned}
$$
Weak convergence gives
$$
\langle f_k,f\rangle\to\norm{f}^2,
$$
and the norm hypothesis gives $\norm{f_k}^2\to\norm{f}^2$. Hence
$$
\norm{f_k-f}\to0.
$$
This proves the equivalence.

:::

:::

::: pf-step

Prove part (b).

::: pf-proof

Suppose first that $H$ is finite dimensional, and let
$$
e_1,\dots,e_N
$$
be an orthonormal basis. If $f_k\rightharpoonup f$, then for each $j$,
$$
\langle f_k-f,e_j\rangle\to0.
$$
Therefore
$$
\norm{f_k-f}^2
=\sum_{j=1}^N\abs{\langle f_k-f,e_j\rangle}^2
\longrightarrow0.
$$
Thus weak convergence implies norm convergence in finite dimension.

In infinite dimension, let $(e_n)$ be an orthonormal sequence. Then
$$
\norm{e_n}=1
$$
for all $n$, so $(e_n)$ cannot converge to $0$ in norm. But for every $g\in H$, Bessel's inequality implies
$$
\sum_{n=1}^\infty\abs{\langle g,e_n\rangle}^2\le\norm{g}^2,
$$
hence
$$
\langle e_n,g\rangle\to0.
$$
Thus $e_n\rightharpoonup0$ but not strongly.

:::

:::

::: pf-step

Reduce part (c) to a weakly null bounded sequence.

::: pf-proof

Set
$$
u_k:=f_k-f.
$$
Then $u_k\rightharpoonup0$. A weakly convergent sequence is bounded, so there is $M<\infty$ such that
$$
\norm{u_k}\le M
\qquad\text{for all }k.
$$

We inductively select a subsequence $(u_{k_n})$. Choose $k_1$ arbitrarily. Having chosen
$$
k_1<\cdots<k_{n-1},
$$
weak convergence to $0$ implies
$$
\langle u_k,u_{k_j}\rangle\to0
\qquad(k\to\infty)
$$
for each $j<n$. Hence we can choose $k_n>k_{n-1}$ so large that
$$
\abs{\langle u_{k_n},u_{k_j}\rangle}\le\frac1n
\qquad(1\le j<n).
$$

:::

:::

::: pf-step

Show that the Cesàro means of the selected subsequence converge in norm.

::: pf-proof

Let
$$
A_n:=\frac1n\sum_{j=1}^n u_{k_j}.
$$
Then
$$
\begin{aligned}
\norm{A_n}^2
&=\frac1{n^2}\left(
\sum_{j=1}^n\norm{u_{k_j}}^2
+2\operatorname{Re}\sum_{1\le j<\ell\le n}
\langle u_{k_j},u_{k_\ell}\rangle
\right)\\
&\le \frac{M^2}{n}
+\frac2{n^2}\sum_{\ell=2}^n\frac{\ell-1}{\ell}\\
&\le \frac{M^2}{n}+\frac2n.
\end{aligned}
$$
Hence $\norm{A_n}\to0$. Since $u_{k_j}=f_{k_j}-f$,
$$
\frac{f_{k_1}+\cdots+f_{k_n}}n-f=A_n\to0
$$
in norm. Therefore
$$
\boxed{
\frac{f_{k_1}+\cdots+f_{k_n}}n\longrightarrow f.}
$$

:::

:::

:::

:::
