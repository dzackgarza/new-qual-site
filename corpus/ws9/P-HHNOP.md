---
schema: qual/card@1
id: P-HHNOP
kind: problem
title: "Let $X$ and $Y$ be Banach spaces."
classification:
  areas:
  - real-analysis
  topics:
  - functional-analysis
  - compactness
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $X$ and $Y$ be Banach spaces.
A bounded linear transformation $A:X\to Y$ is *compact* if for every bounded sequence $\{x_n\}\subseteq X$, the sequence $\{Ax_n\}$ has a convergent subsequence in $Y$.
Suppose $X$ is reflexive ($X^{**}=X$) and $X^*$ is separable.
Show that $A:X\to Y$ is compact if and only if for every bounded sequence $\{x_n\}\subseteq X$, there exists a subsequence $\{x_{n_j}\}$ and a vector $\phi\in X$ such that $x_{n_j} = \phi+r_{n_j}$ and $Ar_{n_j}\to 0$ in $Y$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (⟸) Suppose the subsequence condition holds.
Show $A$ is compact.
Proof: let $\{x_n\}$ be a bounded sequence in $X$.
By the hypothesis there are a subsequence $\{x_{n_j}\}$ and a vector $\phi \in X$ with $x_{n_j} = \phi + r_{n_j}$ and $Ar_{n_j} \to 0$ in $Y$.
Then $Ax_{n_j} = A\phi + Ar_{n_j} \to A\phi$, so $\{Ax_{n_j}\}$ converges in $Y$.
Every bounded sequence thus has a subsequence whose image under $A$ converges; this is exactly the definition of compactness.
<1>2. (⟹) Suppose $A$ is compact.
Let $\{x_n\}$ be bounded.
Show there are $x_{n_j}$ and $\phi$ with $x_{n_j} = \phi + r_{n_j}$ and $Ar_{n_j} \to 0$.
<2>1. Since $A$ is compact, $\{Ax_n\}$ has a convergent subsequence $\{Ax_{n_j}\}$; say $Ax_{n_j} \to y \in Y$.
<2>2. Since $X$ is reflexive and $X^*$ is separable, extract a weakly convergent subsubsequence $x_{n_{j_k}} \rightharpoonup \phi \in X$.
Proof: the closed unit ball of $X$ is weakly compact by Banach–Alaoglu (as $X^{**} = X$), and because $X^*$ is separable the weak topology is metrizable on bounded sets (a countable dense set $\{x_m^*\}$ yields the metric $\rho(u,v) = \sum_m 2^{-m}\min(1,|x_m^*(u-v)|)$). A weakly compact metrizable space is sequentially compact, so the bounded sequence $\{x_{n_j}\}$ has a weakly convergent subsequence; call its limit $\phi$.
<2>3. $A\phi = y$.
Proof: $A$ is bounded, hence continuous from the weak topology of $X$ to the weak topology of $Y$; so $x_{n_{j_k}} \rightharpoonup \phi$ gives $Ax_{n_{j_k}} \rightharpoonup A\phi$.
But $Ax_{n_{j_k}} \to y$ strongly, hence weakly, so weak limits coincide: $A\phi = y$.
<2>4. With $r_{n_{j_k}} := x_{n_{j_k}} - \phi$, we have $Ar_{n_{j_k}} = Ax_{n_{j_k}} - A\phi \to y - y = 0$, and $x_{n_{j_k}} = \phi + r_{n_{j_k}}$ by definition.
<1>3. Q.E.D.
:::
