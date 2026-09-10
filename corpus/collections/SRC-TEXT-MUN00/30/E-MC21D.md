---
schema: qual/card@1
id: E-MC21D
kind: problem
title: Density of uncountable products of the line
classification:
  areas:
  - topology
  topics:
  - Countability
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

(a) Show that the product space $\mathbb{R}^I$, where $I = [0, 1]$, has a countable dense subset.

(b) Show that if $J$ has cardinality greater than $\mathcal{P}(\mathbb{Z}_+)$, then the product space $\mathbb{R}^J$ does not have a countable dense subset.
[Hint: If $D$ is dense in $\mathbb{R}^J$, define $f: J \to \mathcal{P}(D)$ by the equation $f(\alpha) = D \cap \pi_\alpha^{-1}((a, b))$, where $(a, b)$ is a fixed interval in $\mathbb{R}$.]
:::

::: {.solution}
(a) We construct a countable dense subset of \(\mathbb R^I\), \(I=[0,1]\). Choose an injection
\[
\iota:I\hookrightarrow\mathcal P(\mathbb Z_+).
\]
For every finite set \(F\subset\mathbb Z_+\) and every function
\[
\phi:\mathcal P(F)\to\mathbb Q,
\]
define \(d_{F,\phi}\in\mathbb R^I\) by
\[
d_{F,\phi}(t)=\phi(\iota(t)\cap F).
\]
There are only countably many such pairs \((F,\phi)\), so
\[
D=\{d_{F,\phi}\}
\]
is countable.

To see \(D\) is dense, let a basic open set prescribe nonempty open intervals \(U_1,\dots,U_n\) at distinct coordinates \(t_1,\dots,t_n\). Since the sets \(\iota(t_i)\) are distinct, there is a finite \(F\subset\mathbb Z_+\) such that their traces \(\iota(t_i)\cap F\) are pairwise distinct: for each pair choose one integer where the two subsets differ, and take the finite union of these witnesses. Choose rationals \(q_i\in U_i\), and define \(\phi\) on the distinct traces by \(\phi(\iota(t_i)\cap F)=q_i\), arbitrarily elsewhere. Then \(d_{F,\phi}\in D\) lies in the given basic open set. Hence \(D\) is dense.

(b) Let \(D\subset\mathbb R^J\) be countable and dense. Fix a nonempty proper open interval \(U=(0,1)\). For each \(\alpha\in J\), define
\[
F(\alpha)=D\cap\pi_\alpha^{-1}(U)\subset D.
\]
We claim \(F:J\to\mathcal P(D)\) is injective. If \(\alpha\ne\beta\), the basic open set
\[
\pi_\alpha^{-1}(U)\cap\pi_\beta^{-1}((2,3))
\]
is nonempty, so density of \(D\) gives \(d\in D\) with \(d_\alpha\in U\) and \(d_\beta\notin U\). Hence \(d\in F(\alpha)\setminus F(\beta)\). Thus
\[
|J|\le |\mathcal P(D)|=|\mathcal P(\mathbb Z_+)|.
\]
Therefore if \(J\) has larger cardinality than \(\mathcal P(\mathbb Z_+)\), \(\mathbb R^J\) cannot be separable.
:::
