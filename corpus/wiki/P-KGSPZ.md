---
schema: qual/card@1
id: P-KGSPZ
kind: problem
title: $\lim_n\int f^n$ is $\infty$ or $\mu(f^{-1}(1))$
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - measure-theory
relations: []
review: draft
solved: true
---

::: problem
Let $(X, \mathcal M, \mu)$ be a measure space and suppose $f$ is a measurable function on $X$.
Show that
$$
\lim _{n \rightarrow \infty} \int_{X} f^{n} ~d \mu =
\begin{cases}
\infty & \text{or} \\
\mu(f\inv(1)),
\end{cases}
$$
and characterize the collection of functions of each type.
:::
::: {.solution}
> **AI-Generated Solution**

**Honesty note:** the card states no hypothesis on the sign of $f$; for signed $f$ and odd $n$, $\int f^n$ need not be defined.
The standard statement (proved here) is for $f \ge 0$: $\lim_n \int f^n = \infty$ if $\mu\{f > 1\} > 0$, and $= \mu\{f = 1\}$ otherwise.

<1>1. Let $A = \{x : f(x) = 1\}$ and $B = \{x : f(x) > 1\}$.
Proof: definitions.

<1>2. If $\mu(B) > 0$: $\int f^n \to \infty$.
Proof: $B = \bigcup_k \{f \ge 1 + 1/k\}$, so some $C \subseteq B$ has $\mu(C) > 0$ and $f \ge 1 + \delta$ on $C$ for $\delta = 1/k$; then $\int f^n \ge (1+\delta)^n\mu(C) \to \infty$.

<1>3. If $\mu(B) = 0$: $\int f^n \to \mu(A)$.
<2>1. $f^n = 1$ on $A$ and $f^n \to 0$ pointwise on $\{f < 1\}$.
Proof: on $\{0 \le f < 1\}$, $f^n \to 0$; $f = 1$ on $A$.
<2>2. $\int f^n = \mu(A) + \int_{\{f < 1\}} f^n$.
Proof: additivity over the disjoint sets $A$ and $\{f < 1\}$ (the remaining set $\{f > 1\} = B$ has measure $0$). <2>3. $\int_{\{f < 1\}} f^n \to 0$.
Proof: on $\{f < 1\}$, $0 \le f^n \le f^{n_0}$ for $n \ge n_0$; dominated convergence applies on each finite-measure truncation $\{f < 1\} \cap \{|x| \le R\}$ (dominated by $f^{n_0} \le 1$ there), giving $\int_{\{f<1\}\cap\{|x|\le R\}} f^n \to 0$ for each $R$; then $\limsup_n \int_{\{f<1\}} f^n \le \limsup_n \int_{\{f<1\}\cap\{|x|>R\}} f^n \le \mu\{f<1\}\cap\{|x|>R\}$, which $\to 0$ as $R \to \infty$ when $\mu\{f < 1\} < \infty$ — if $\mu\{f < 1\} = \infty$, use instead the dominated convergence on the whole space when $\int_{\{f<1\}} f < \infty$ (dominating by $f \in L^1$), and if neither holds, the standard formulation assumes $\mu(X) < \infty$ (e.g. probability space), in which case the constant $1$ dominates and the conclusion is immediate.
We record the finite-measure formulation: Proof: if $\mu(X) < \infty$: $f^n \le 1$ pointwise on $\{f < 1\}$, dominated by the constant $1 \in L^1$; DCT gives $\int f^n \to \mu(A)$.
If $\mu(X) = \infty$ but $f \in L^1$: dominated by $f$.
The general statement needs one of these; otherwise $\int_{\{f<1\}} f^n = \infty$ for all $n$ is possible (e.g. $f$ decaying slowly), and the dichotomy fails.
<2>4. Q.E.D. Proof: <2>2 and <2>3 give $\int f^n \to \mu(A)$.

<1>4. Q.E.D.: the dichotomy $\lim_n \int f^n = \infty$ (iff $\mu\{f > 1\} > 0$) or $\mu\{f = 1\}$ (iff $f \le 1$ a.e.), under the standard hypotheses ($f \ge 0$, plus finiteness of the ambient measure or $f \in L^1$ when $\mu\{f = 1\}$ case needs DCT). Proof: <1>2 and <1>3.
:::
