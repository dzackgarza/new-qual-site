---
schema: qual/card@1
id: E-RZTZT
kind: problem
title: Components of R^omega in product, uniform, and box topologies
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) What are the components and path components of $\mathbb{R}^\omega$ (in the product topology)?

(b) Consider $\mathbb{R}^\omega$ in the uniform topology.
Show that $\mathbf{x}$ and $\mathbf{y}$ lie in the same component of $\mathbb{R}^\omega$ if and only if the sequence

$$
\mathbf{x} - \mathbf{y} = (x_1 - y_1, x_2 - y_2, \dots)
$$

is bounded.
[Hint: It suffices to consider the case where $\mathbf{y} = 0$.]

(c) Give $\mathbb{R}^\omega$ the box topology.
Show that $\mathbf{x}$ and $\mathbf{y}$ lie in the same component of $\mathbb{R}^\omega$ if and only if the sequence $\mathbf{x} - \mathbf{y}$ is "eventually zero."
[Hint: If $\mathbf{x} - \mathbf{y}$ is not eventually zero, show there is a homeomorphism $h$ of $\mathbb{R}^\omega$ with itself such that $h(\mathbf{x})$ is bounded and $h(\mathbf{y})$ is unbounded.]
:::

::: {.solution}
(a) In the product topology, $\mathbb R^\omega$ is path connected. Given $x,y\in\mathbb R^\omega$, the straight-line path
\[
\gamma(t)=((1-t)x_i+ty_i)_{i\ge1}
\]
is continuous coordinatewise, hence continuous into the product. Therefore there is one path component and one component: all of $\mathbb R^\omega$.

(b) In the uniform topology, translation is a homeomorphism, so it suffices to determine the component of $0$. Suppose $x=(x_i)$ is bounded, say $|x_i|\le M$. The straight-line path
\[
\gamma(t)=tx
\]
is uniformly continuous in the parameter with respect to the uniform metric, since for $s,t\in[0,1]$,
\[
\bar\rho(sx,tx)\le \min\{M|s-t|,1\}.
\]
Hence every bounded sequence lies in the path component of $0$.

Conversely, let
\[
B=\{x\in\mathbb R^\omega:x\text{ is bounded}\}.
\]
For any $x\in B$, every sufficiently small uniform ball about $x$ consists of bounded sequences; for any unbounded $x$, every uniform ball of radius $<1$ consists of unbounded sequences, since a uniformly bounded perturbation cannot turn an unbounded sequence into a bounded one. Thus $B$ is both open and closed in the uniform topology. The component of $0$ is therefore contained in $B$. Hence two points $x,y$ lie in the same component exactly when
\[
x-y
\]
is bounded; in fact these components are path components as well.

(c) In the box topology, if $x-y$ is eventually zero, then the two points differ in only finitely many coordinates. The straight-line path between them varies only in these finitely many coordinates, so it is continuous in the box topology. Thus they lie in the same path component.

Conversely, suppose $d=x-y$ is not eventually zero. By translation, take $y=0$. Choose infinitely many indices $i_k$ with $d_{i_k}\ne0$. Define positive scalars $a_i$ by
\[
a_{i_k}=\frac{k}{|d_{i_k}|},
\]
and $a_i=1$ at all other indices. The coordinatewise scaling
\[
h((z_i))=(a_i z_i)
\]
is a homeomorphism of the box product (its inverse scales by $a_i^{-1}$). Then
\[
h(0)=0
\]
is bounded, while $h(d)$ is unbounded since its $i_k$th coordinate has absolute value $k$.

If $0$ and $d$ lay in one box-connected subset, their images under $h$ would lie in one box-connected subset. Since the box topology is finer than the uniform topology, every box-connected set is also connected in the uniform topology. But part (b) says a bounded point and an unbounded point lie in different uniform components. Contradiction. Hence $x,y$ are in the same box component iff $x-y$ is eventually zero; these are again exactly the path components.
:::
