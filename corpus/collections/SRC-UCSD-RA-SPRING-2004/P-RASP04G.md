---
schema: qual/card@1
id: P-RASP04G
kind: problem
title: "Unitary equivalence of multiplication operators and functional calculus"
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
  note: Checked against Problem 7 of the official UCSD Spring 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f, g : X \to [-1,1]$ be measurable functions and $U : L^2(X, \mu) \to L^2(X, \mu)$ be a unitary map such that $UM_fU^{-1} = M_g$.
Let $\mathcal{H}$ denote the collection of bounded Borel measurable functions $\varphi : [-1,1] \to \mathbb{R}$ such that $UM_{\varphi \circ f}U^{-1} = M_{\varphi \circ g}$.
Show:

(a) $\varphi \in \mathcal{H}$ if $\varphi(x) = \sum_{n=0}^{N} \alpha_n x^n$ is a polynomial with $\alpha_n \in \mathbb{R}$.

(b) $C([-1,1], \mathbb{R}) \subset \mathcal{H}$.

(c) $\mathcal{H}$ contains all bounded real measurable functions.

Hints: 1. The results of the previous exercise are useful.
2. For (a) show $\varphi(M_f) = M_{\varphi \circ f}$.
3. For (c), notice that $UM_{\varphi \circ f}U^{-1} = M_{\varphi \circ g}$ iff
$$
UM_{\varphi \circ f}U^{-1}h = M_{\varphi \circ g}h \quad \text{for all } h \in L^2(\mu).
$$

4. You do not have to prove (b) if you can prove (c).
:::

::: solution
<1>1. Polynomials belong to $\mathcal H$.
::: proof
For every integer $n\ge0$,
\[
M_f^n=M_{f^n}.
\]
Hence for a polynomial
\[
p(t)=\sum_{n=0}^N\alpha_nt^n,
\]
we have
\[
p(M_f)=\sum_{n=0}^N\alpha_nM_f^n=M_{p\circ f}.
\]
Using $UM_fU^{-1}=M_g$,
\[
\begin{aligned}
UM_{p\circ f}U^{-1}
&=Up(M_f)U^{-1}\\
&=p(UM_fU^{-1})\\
&=p(M_g)\\
&=M_{p\circ g}.
\end{aligned}
\]
Thus every real polynomial lies in $\mathcal H$.
:::

<1>2. Every continuous function belongs to $\mathcal H$.
::: proof
Let $\varphi\in C([-1,1])$. By the Weierstrass approximation theorem there are real polynomials $p_n$ such that
\[
\|p_n-\varphi\|_\infty\longrightarrow0.
\]
For multiplication operators,
\[
\|M_{p_n\circ f}-M_{\varphi\circ f}\|
\le \|p_n-\varphi\|_\infty,
\]
and similarly with $g$. Since $p_n\in\mathcal H$ by Step 1,
\[
UM_{p_n\circ f}U^{-1}=M_{p_n\circ g}.
\]
Passing to the operator-norm limit gives
\[
UM_{\varphi\circ f}U^{-1}=M_{\varphi\circ g}.
\]
Therefore
\[
C([-1,1],\mathbb R)\subseteq\mathcal H.
\]
:::

<1>3. $\mathcal H$ is closed under bounded pointwise convergence.
::: proof
Suppose $\varphi_n\in\mathcal H$, $\varphi_n(t)\to\varphi(t)$ for every $t\in[-1,1]$, and
\[
\sup_n\|\varphi_n\|_\infty<\infty.
\]
Fix $h\in L^2(\mu)$. By the preceding exercise,
\[
M_{\varphi_n\circ f}U^{-1}h
\longrightarrow
M_{\varphi\circ f}U^{-1}h
\]
in $L^2$, and likewise
\[
M_{\varphi_n\circ g}h
\longrightarrow
M_{\varphi\circ g}h.
\]
Since $U$ is continuous and $\varphi_n\in\mathcal H$,
\[
\begin{aligned}
UM_{\varphi\circ f}U^{-1}h
&=\lim_n UM_{\varphi_n\circ f}U^{-1}h\\
&=\lim_n M_{\varphi_n\circ g}h\\
&=M_{\varphi\circ g}h.
\end{aligned}
\]
Thus $\varphi\in\mathcal H$.
:::

<1>4. Indicators of all Borel sets belong to $\mathcal H$.
::: proof
First let $O\subseteq[-1,1]$ be open. Define
\[
\varphi_n(t)=\min\{1,n\,d(t,O^c)\}.
\]
Then $\varphi_n\in C([-1,1])$, $0\le\varphi_n\le1$, and
\[
\varphi_n(t)\longrightarrow\mathbf1_O(t)
\]
pointwise. By Steps 2 and 3,
\[
\mathbf1_O\in\mathcal H.
\]

Let
\[
\mathcal A:=\{E\subseteq[-1,1]: E\text{ Borel and }\mathbf1_E\in\mathcal H\}.
\]
The class $\mathcal H$ contains constants and is closed under sums, differences, and products, because conjugation respects the corresponding multiplication-operator identities. Hence $\mathcal A$ is closed under complements and finite intersections.

If $E_k\in\mathcal A$, let
\[
F_n=\bigcup_{k=1}^nE_k.
\]
Finite unions belong to $\mathcal A$, and
\[
\mathbf1_{F_n}\longrightarrow\mathbf1_{\cup_{k\ge1}E_k}
\]
pointwise with uniform bound $1$. Step 3 therefore shows that the countable union also belongs to $\mathcal A$. Thus $\mathcal A$ is a sigma-algebra containing every open set, so it contains every Borel subset of $[-1,1]$.
:::

<1>5. Pass from indicators to bounded Borel functions.
::: proof
Every bounded real Borel function is a bounded pointwise limit of Borel simple functions. Each such simple function is a finite linear combination of Borel indicators, hence belongs to $\mathcal H$ by Step 4. Applying Step 3 once more gives
\[
\boxed{\mathcal H\text{ contains every bounded real Borel measurable function}.}
\]
:::
:::
