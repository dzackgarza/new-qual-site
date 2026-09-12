---
schema: qual/card@1
id: P-RASP06C
kind: problem
title: "Abel summation and convergence of power series at the boundary"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Spring 2006 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\{a_k\}$ be a sequence of complex numbers such that $\sum_{k=0}^{\infty} a_k$ is convergent.
Set $S_m^n := \sum_{i=m}^{n} a_i$.

(a) Show that, for $0 \leq x \leq 1$,
$$
\sum_{k=m}^{n} a_k x^k = \sum_{j=m}^{n-1} S_m^j (x^j - x^{j+1}) + S_m^n x^n.
$$

(b) Show that
$$
\lim_{x \to 1^-} \sum_{k=0}^{\infty} a_k x^k = \sum_{k=0}^{\infty} a_k.
$$

Hint: Estimate the left hand side of the formula in (b).
:::

::: solution
<1>1. Prove the finite summation-by-parts identity.
::: proof
Since
\[
a_k=S_m^k-S_m^{k-1}
\]
for $k>m$, with $a_m=S_m^m$, we have
\[
\begin{aligned}
\sum_{k=m}^n a_kx^k
&=S_m^m x^m+
\sum_{k=m+1}^n(S_m^k-S_m^{k-1})x^k\\
&=\sum_{j=m}^{n-1}S_m^j(x^j-x^{j+1})+S_m^nx^n.
\end{aligned}
\]
This is the desired formula.
:::

<1>2. Rewrite the Abel sum using ordinary partial sums.
::: proof
Let
\[
A_j:=\sum_{k=0}^j a_k,
\qquad
S:=\sum_{k=0}^\infty a_k.
\]
The sequence $(A_j)$ is bounded. For fixed $0\le x<1$, Step 1 with $m=0$ gives
\[
\sum_{k=0}^n a_kx^k
=\sum_{j=0}^{n-1}A_j(x^j-x^{j+1})+A_nx^n.
\]
Since $A_n$ is bounded and $x^n\to0$, letting $n\to\infty$ yields
\[
\sum_{k=0}^\infty a_kx^k
=(1-x)\sum_{j=0}^\infty A_jx^j.
\]
The series on the left converges absolutely because the convergent series $\sum a_k$ has bounded terms.
:::

<1>3. Pass to the boundary $x\uparrow1$.
::: proof
Because
\[
(1-x)\sum_{j=0}^\infty x^j=1,
\]
Step 2 gives
\[
\sum_{k=0}^\infty a_kx^k-S
=(1-x)\sum_{j=0}^\infty(A_j-S)x^j.
\]
Fix $\varepsilon>0$. Choose $N$ so large that
\[
|A_j-S|<\varepsilon
\qquad(j\ge N).
\]
Then
\[
\begin{aligned}
\left|\sum_{k=0}^\infty a_kx^k-S\right|
&\le (1-x)\sum_{j=0}^{N-1}|A_j-S|x^j\\
&\qquad +(1-x)\sum_{j=N}^\infty \varepsilon x^j.
\end{aligned}
\]
The second term is at most $\varepsilon$. The first is a finite sum multiplied by $1-x$, so it tends to $0$ as $x\uparrow1$. Therefore
\[
\limsup_{x\to1^-}
\left|\sum_{k=0}^\infty a_kx^k-S\right|
\le\varepsilon.
\]
Since $\varepsilon$ is arbitrary,
\[
\boxed{\lim_{x\to1^-}\sum_{k=0}^\infty a_kx^k
=\sum_{k=0}^\infty a_k.}
\]
:::
:::
