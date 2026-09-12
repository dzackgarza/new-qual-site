---
schema: qual/card@1
id: E-XNYTJ
kind: problem
title: Monotone pointwise convergence to a continuous limit is uniform
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Uniform Convergence
relations: []
review: draft
---

::: {.exercise}

(a) Prove the following partial converse to the uniform limit theorem.

Theorem.
Let $f_n: X \to \mathbb{R}$ be a sequence of continuous functions, with $f_n(x) \to f(x)$ for each $x \in X$.
If $f$ is continuous, and if the sequence $f_n$ is monotone increasing, and if $X$ is compact, then the convergence is uniform.
[We say that $f_n$ is monotone increasing if $f_n(x) \leq f_{n+1}(x)$ for all $n$ and $x$.]

(b) Give examples to show that this theorem fails if you delete the requirement that $X$ be compact, or if you delete the requirement that the sequence be monotone.
[Hint: See the exercises of §21.]
:::

::: {.solution}
(a) This is Dini's theorem. Fix \(\varepsilon>0\). Since \(f_n\uparrow f\), define
\[
U_n=\{x\in X:f(x)-f_n(x)<\varepsilon\}.
\]
Because \(f-f_n\) is continuous, \(U_n\) is open. The sets are increasing, since \(f_n\le f_{n+1}\), and pointwise convergence implies \(\bigcup_nU_n=X\). Compactness gives a finite subcover; since the family is increasing, there is some \(N\) with \(U_N=X\). Thus for all \(x\in X\),
\[
0\le f(x)-f_N(x)<\varepsilon.
\]
For every \(n\ge N\), monotonicity gives
\[
0\le f(x)-f_n(x)\le f(x)-f_N(x)<\varepsilon,
\]
uniformly in \(x\). Hence \(f_n\to f\) uniformly.

(b) Compactness is necessary. On \(X=\mathbb R\), let
\[
f_n(x)=\frac{n}{n+|x|}.
\]
Each \(f_n\) is continuous, \(f_n(x)\uparrow 1\) for each fixed \(x\), but
\[
\sup_x |1-f_n(x)|=1,
\]
so convergence is not uniform.

Monotonicity is also necessary even on a compact domain. On \([0,1]\), let
\[
f_n(x)=x^n(1-x).
\]
Then \(f_n\to0\) pointwise and the limit is continuous, but this particular sequence actually converges uniformly, so instead use the standard moving-spike example: choose continuous triangular functions \(g_n:[0,1]\to[0,1]\) supported in \((\frac1{n+1},\frac1{n-1})\) with \(g_n(1/n)=1\). Then \(g_n(x)\to0\) for every fixed \(x\), because each \(x>0\) lies in only finitely many supports and \(g_n(0)=0\); but \(\sup g_n=1\) for all \(n\). Thus convergence is not uniform.
:::
