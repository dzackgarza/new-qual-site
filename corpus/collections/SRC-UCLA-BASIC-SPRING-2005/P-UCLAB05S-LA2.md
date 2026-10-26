---
schema: qual/card@1
id: P-UCLAB05S-LA2
kind: problem
title: Annihilators, spans, and the dual of a quotient
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra Problem 2 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Let $V$ be a finite-dimensional vector space, and let $V^*$ be its dual, the space of linear maps $\phi:V\to\mathbb C$.
For $W\subset V$, define
\[
W^\perp=\{\phi\in V^*: \phi(w)=0\text{ for every }w\in W\}.
\]
For $U\subset V^*$, define
\[
{}^\perp U=\{v\in V: \phi(v)=0\text{ for every }\phi\in U\}.
\]

(a) Show that for every subset $W\subset V$,
\[
{}^\perp(W^\perp)=\operatorname{span}(W).
\]

(b) Let $W\subset V$ be a linear subspace.
Give an explicit isomorphism between $(V/W)^*$ and $W^\perp$, and prove that it is an isomorphism.
:::

Let
$$
S\coloneqq\operatorname{span}(W).
$$

::: pf

::: pf-step

One has
$$
S\subseteq{}^\perp(W^\perp).
$$


::: pf-proof

Let $v\in S$. Then $v$ is a finite linear combination of elements of $W$. Every $\phi\in W^\perp$ vanishes on $W$, hence by linearity vanishes on every linear combination of elements of $W$. Thus $\phi(v)=0$ for every $\phi\in W^\perp$, so $v\in{}^\perp(W^\perp)$.

:::

:::

::: pf-step

If $v\notin S$, then there is a functional $\phi\in W^\perp$ such that $\phi(v)\ne0$.


::: pf-proof

Choose a basis $s_1,\ldots,s_r$ of $S$. Since $v\notin S$, the list
$$
s_1,\ldots,s_r,v
$$
is linearly independent, so it extends to a basis of $V$. Define $\phi\in V^*$ on this basis by
$$
\phi(s_i)=0,
\qquad
\phi(v)=1,
$$
and assign value $0$ to the remaining basis vectors. Then $\phi$ vanishes on $S$, hence on $W$, so $\phi\in W^\perp$, while $\phi(v)=1\ne0$.

:::

:::

::: pf-step

For every subset $W\subseteq V$,
$$
\boxed{{}^\perp(W^\perp)=\operatorname{span}(W)}.
$$


::: pf-proof

Step <1>1 gives one inclusion. If $v\notin S$, step <1>2 produces $\phi\in W^\perp$ with $\phi(v)\ne0$, so $v\notin{}^\perp(W^\perp)$. Thus ${}^\perp(W^\perp)\subseteq S$ as well.

:::

:::

::: pf-step

Let $W\le V$ and let
$$
\pi:V\to V/W
$$
be the quotient map. Define
$$
\Phi:(V/W)^*\longrightarrow W^\perp,
\qquad
\boxed{\Phi(\lambda)=\lambda\circ\pi}.
$$


::: pf-proof

For $w\in W$, one has $\pi(w)=W=0$ in $V/W$, so
$$
(\lambda\circ\pi)(w)=\lambda(0)=0.
$$
Hence $\lambda\circ\pi\in W^\perp$. The map $\Phi$ is linear because composition with the fixed linear map $\pi$ respects sums and scalar multiples.

:::

:::

::: pf-step

The map $\Phi$ is injective.


::: pf-proof

Suppose $\Phi(\lambda)=0$. Then $\lambda\circ\pi=0$. Since $\pi$ is surjective, every element of $V/W$ has the form $\pi(v)$, and therefore
$$
\lambda(\pi(v))=0
$$
for every $v\in V$. Thus $\lambda=0$.

:::

:::

::: pf-step

The map $\Phi$ is surjective.


::: pf-proof

Let $\phi\in W^\perp$. Define
$$
\lambda:V/W\to\CC,
\qquad
\lambda(v+W)\coloneqq\phi(v).
$$
If $v+W=v'+W$, then $v-v'\in W$, so
$$
\phi(v)-\phi(v')=\phi(v-v')=0.
$$
Hence $\lambda$ is well-defined. It is linear, and
$$
(\lambda\circ\pi)(v)=\lambda(v+W)=\phi(v)
$$
for every $v\in V$. Thus $\Phi(\lambda)=\phi$.

:::

:::

::: pf-step

Therefore
$$
\boxed{(V/W)^*\cong W^\perp}
$$
via $\lambda\mapsto\lambda\circ\pi$.


::: pf-proof

By steps <1>4--<1>6, $\Phi$ is a linear bijection.

:::

:::

::: pf-qed

Step <1>3 proves part (a), and step <1>7 proves part (b).

:::

:::
