---
schema: qual/card@1
id: E-NYYRX
kind: problem
title: Accumulation points of nets
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
---

::: {.exercise}

Let $(x_\alpha)_{\alpha \in J}$ be a net in $X$.
We say that $x$ is an accumulation point of the net $(x_\alpha)$ if for each neighborhood $U$ of $x$, the set of those $\alpha$ for which $x_\alpha \in U$ is cofinal in $J$.

Lemma.
The net $(x_\alpha)$ has the point $x$ as an accumulation point if and only if some subnet of $(x_\alpha)$ converges to $x$.

[Hint: To prove the implication $\Rightarrow$, let $K$ be the set of all pairs $(\alpha, U)$ where $\alpha \in J$ and $U$ is a neighborhood of $x$ containing $x_\alpha$. Define $(\alpha, U) \preceq (\beta, V)$ if $\alpha \preceq \beta$ and $V \subset U$. Show that $K$ is a directed set and use it to define the subnet.]
:::

::: {.solution}
Suppose first that \(x\) is an accumulation point of the net \((x_\alpha)_{\alpha\in J}\). Let \(K\) be the set of pairs \((\alpha,U)\) such that \(U\) is a neighborhood of \(x\) and \(x_\alpha\in U\). Define
\[
(\alpha,U)\preceq(\beta,V)
\iff \alpha\preceq\beta\text{ and }V\subset U.
\]
Given two pairs, choose \(\gamma\succeq\alpha,\beta\). Since the indices with \(x_\delta\in U\cap V\) are cofinal, choose \(\delta\succeq\gamma\) with \(x_\delta\in U\cap V\). Then \((\delta,U\cap V)\) is an upper bound, so \(K\) is directed.

Define \(\phi:K\to J\) by \(\phi(\alpha,U)=\alpha\). It is order preserving and cofinal: for every \(\alpha_0\in J\), choose any neighborhood \(U\) of \(x\), then use accumulation to find \(\alpha\succeq\alpha_0\) with \(x_\alpha\in U\). Thus \((x_{\phi(k)})_{k\in K}\) is a subnet. It converges to \(x\): if \(W\) is a neighborhood of \(x\), choose \(k_0=(\alpha,W)\in K\); whenever \(k\succeq k_0\), its neighborhood component is contained in \(W\), hence the corresponding net point lies in \(W\).

Conversely, if a subnet converges to \(x\), then for every neighborhood \(U\) of \(x\) and every \(\alpha_0\in J\), eventually the subnet lies in \(U\), and cofinality of the subnet map gives an original index \(\alpha\succeq\alpha_0\) with \(x_\alpha\in U\). Hence the set of such indices is cofinal, so \(x\) is an accumulation point.
:::
