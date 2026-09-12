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

2. Let H be a Hilbert space equipped with an inner product $( \cdot , \cdot )$ and a norm $| | \cdot | | = ( \cdot , \cdot ) ^ { \frac { 1 } { 2 } }$ Recall the following: A sequence $\{ f _ { k } \} \subset { \mathcal { H } }$ is said converge to $f \in \mathcal H$ if $\vert \vert f _ { k } - f \vert \vert  0$ . A sequence $\{ f _ { k } \} \subset { \mathcal { H } }$ is said converge weakly to $f \in { \mathcal { H } }$ if $( f _ { k } , g )  ( f , g )$ for any $g \in { \mathcal { H } }$ . Prove the following statements:

(a) $\{ f _ { k } \}$ converges to f if and only if $\vert \vert f _ { k } \vert \vert  \vert \vert f \vert \vert$ and $\{ f _ { k } \}$ converges weakly to $f .$

(b) If H is a finite dimensional Hilbert space, then the weak convergence implies convergence.
Give a counter example to show that weak convergence does not necessarily imply convergence in an infinite dimensional Hilbert space.

(c) If a sequence $\{ f _ { k } \}$ converges weakly to $f ,$ then there exists a subsequence $\{ f _ { k _ { n } } \}$ such that

$$
\frac { f _ { k _ { 1 } } + \cdots + f _ { k _ { n } } } { n }
$$

converges to $f .$ (You may use the fact that a weakly convergent sequence is a bounded sequence.)

::: solution
<1>1. Prove part (a).
::: proof
If $f_k\to f$ in norm, then continuity of the norm gives
\[
\|f_k\|\to\|f\|,
\]
and for every $g\in H$,
\[
|\langle f_k-f,g\rangle|
\le \|f_k-f\|\,\|g\|\to0,
\]
so $f_k\rightharpoonup f$.

Conversely, assume $f_k\rightharpoonup f$ and
\[
\|f_k\|\to\|f\|.
\]
Then
\[
\begin{aligned}
\|f_k-f\|^2
&=\|f_k\|^2+\|f\|^2
-2\operatorname{Re}\langle f_k,f\rangle.
\end{aligned}
\]
Weak convergence gives
\[
\langle f_k,f\rangle\to\|f\|^2,
\]
and the norm hypothesis gives $\|f_k\|^2\to\|f\|^2$. Hence
\[
\|f_k-f\|\to0.
\]
This proves the equivalence.
:::

<1>2. Prove part (b).
::: proof
Suppose first that $H$ is finite dimensional, and let
\[
e_1,\dots,e_N
\]
be an orthonormal basis. If $f_k\rightharpoonup f$, then for each $j$,
\[
\langle f_k-f,e_j\rangle\to0.
\]
Therefore
\[
\|f_k-f\|^2
=\sum_{j=1}^N|\langle f_k-f,e_j\rangle|^2
\longrightarrow0.
\]
Thus weak convergence implies norm convergence in finite dimension.

In infinite dimension, let $(e_n)$ be an orthonormal sequence. Then
\[
\|e_n\|=1
\]
for all $n$, so $(e_n)$ cannot converge to $0$ in norm. But for every $g\in H$, Bessel's inequality implies
\[
\sum_{n=1}^\infty|\langle g,e_n\rangle|^2\le\|g\|^2,
\]
hence
\[
\langle e_n,g\rangle\to0.
\]
Thus $e_n\rightharpoonup0$ but not strongly.
:::

<1>3. Reduce part (c) to a weakly null bounded sequence.
::: proof
Set
\[
u_k:=f_k-f.
\]
Then $u_k\rightharpoonup0$. By the allowed boundedness fact, there is $M<\infty$ such that
\[
\|u_k\|\le M
\qquad\text{for all }k.
\]

We inductively select a subsequence $(u_{k_n})$. Choose $k_1$ arbitrarily. Having chosen
\[
k_1<\cdots<k_{n-1},
\]
weak convergence to $0$ implies
\[
\langle u_k,u_{k_j}\rangle\to0
\qquad(k\to\infty)
\]
for each $j<n$. Hence we can choose $k_n>k_{n-1}$ so large that
\[
|\langle u_{k_n},u_{k_j}\rangle|\le\frac1n
\qquad(1\le j<n).
\]
:::

<1>4. Show that the Cesàro means of the selected subsequence converge in norm.
::: proof
Let
\[
A_n:=\frac1n\sum_{j=1}^n u_{k_j}.
\]
Then
\[
\begin{aligned}
\|A_n\|^2
&=\frac1{n^2}\left(
\sum_{j=1}^n\|u_{k_j}\|^2
+2\operatorname{Re}\sum_{1\le j<\ell\le n}
\langle u_{k_j},u_{k_\ell}\rangle
\right)\\
&\le \frac{M^2}{n}
+\frac2{n^2}\sum_{\ell=2}^n\frac{\ell-1}{\ell}\\
&\le \frac{M^2}{n}+\frac2n.
\end{aligned}
\]
Hence $\|A_n\|\to0$. Since $u_{k_j}=f_{k_j}-f$,
\[
\frac{f_{k_1}+\cdots+f_{k_n}}n-f=A_n\to0
\]
in norm. Therefore
\[
\boxed{
\frac{f_{k_1}+\cdots+f_{k_n}}n\longrightarrow f.}
\]
:::
:::
