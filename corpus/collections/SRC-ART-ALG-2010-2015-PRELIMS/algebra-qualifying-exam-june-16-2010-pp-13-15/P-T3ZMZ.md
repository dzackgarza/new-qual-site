---
schema: qual/card@1
id: P-T3ZMZ
kind: problem
title: $A/mA \cong A \otimes_{\mathbb{Z}} (\mathbb{Z}/m\mathbb{Z})$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Tensor Products
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked June 2010 Rings and Modules 3 on PDF page 14, including the positive integer m and the order of the tensor factors."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked representative independence and balancing, descent through mA, both inverse identities, and the case m=1."
---

::: problem
Let $A$ be a $\mathbb{Z}$-module, and suppose $m \in \mathbb{Z}^+$.
Prove that $A/mA \cong A \otimes_{\mathbb{Z}} (\mathbb{Z}/m\mathbb{Z})$.
:::

::: solution
Write $T=A\otimes_{\mathbb Z}(\mathbb Z/m\mathbb Z)$
and $\bar r=r+m\mathbb Z$. The inverse isomorphisms are
$$
\begin{aligned}
\Phi:A/mA&\longrightarrow T,
&a+mA&\longmapsto a\otimes\bar1,\\
\Psi:T&\longrightarrow A/mA,
&a\otimes\bar r&\longmapsto ra+mA.
\end{aligned}
$$

<1>1. The displayed formula defines a $\mathbb Z$-linear map $\Psi$.

::: proof
The map $\beta:A\times(\mathbb Z/m\mathbb Z)\to A/mA$
given by $\beta(a,\bar r)=ra+mA$ is independent of the
representative $r$: replacing $r$ by $r+mk$ changes $ra$
by $m(ka)\in mA$. The map is additive in both variables.
For $s\in\mathbb Z$ it satisfies
$$
\beta(sa,\bar r)=r(sa)+mA=(rs)a+mA
=\beta(a,s\bar r).
$$
Thus it is balanced. The defining universal property of
the tensor product gives an additive map $\Psi$ with
the asserted formula. Every additive homomorphism of
abelian groups is $\mathbb Z$-linear, so this is a module map.
:::

<1>2. The formula for $\Phi$ descends to $A/mA$, and
the maps are inverse.

::: proof
The map $\eta:A\to T$, $a\mapsto a\otimes\bar1$,
is additive. If $a=mb$, balancing gives
$\eta(a)=(mb)\otimes\bar1=b\otimes\bar m=0$.
Thus $mA$ lies in its kernel, and $\eta$ descends to
the $\mathbb Z$-linear map $\Phi$ on $A/mA$.

For every coset, one has
$\Psi\Phi(a+mA)=a+mA$.
For every elementary tensor, balancing gives
$$
\Phi\Psi(a\otimes\bar r)=(ra)\otimes\bar1
=a\otimes\bar r.
$$
Elementary tensors generate $T$ additively, so the latter
identity holds on all of $T$. Both composites are the
identity, proving the isomorphism. When $m=1$, the same
formulas apply and both modules are zero.
:::
:::
