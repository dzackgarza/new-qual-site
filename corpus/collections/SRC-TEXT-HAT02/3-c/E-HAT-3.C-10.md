---
schema: qual/card@1
id: E-HAT-3.C-10
kind: problem
title: "Product of maps in an H-space"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 10; repaired part (c) to restore the source polynomial with coefficients on both sides.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X$ be a path-connected H-space with $H^*(X; R)$ free and finitely generated in each dimension.
For maps $f, g: X \to X$, the product $fg: X \to X$ is defined by $(fg)(x) = f(x)g(x)$, using the H-space product.

(a) Show that $(fg)^*(\alpha) = f^*(\alpha) + g^*(\alpha)$ for primitive elements $\alpha \in H^*(X; R)$.

(b) Deduce that the $k$-th power map $x \mapsto x^k$ induces the map $\alpha \mapsto k\alpha$ on primitive elements $\alpha$.
In particular the quaternionic $k$-th power map $S^3 \to S^3$ has degree $k$.

(c) Show that every polynomial $a_n x^n b_n + \dotsb + a_1 x b_1 + a_0$ of nonzero degree with coefficients in $\mathbb{H}$ has a root in $\mathbb{H}$.
[See Theorem 1.8.]
:::

::: {.solution}
Let $\mu:X\times X\to X$ be the H-space multiplication and let
\[
\delta_{f,g}:X\to X\times X,
\qquad
\delta_{f,g}(x)=(f(x),g(x)).
\]
Then $fg=\mu\circ\delta_{f,g}$.

<1>1. If $\alpha$ is primitive, then
\[
(fg)^*(\alpha)=f^*(\alpha)+g^*(\alpha).
\]
::: {.proof}
Primitivity means
\[
\mu^*(\alpha)=\alpha\times1+1\times\alpha.
\]
Therefore
\[
(fg)^*(\alpha)
=\delta_{f,g}^*\mu^*(\alpha)
=f^*(\alpha)+g^*(\alpha).
\]
:::

<1>2. The $k$th-power map sends every primitive class $\alpha$ to $k\alpha$.
::: {.proof}
Induct on $k$ using part 1. For the identity map $P_1$, $P_1^*(\alpha)=\alpha$. Since $P_{k+1}=P_k\cdot\operatorname{id}$,
\[
P_{k+1}^*(\alpha)=P_k^*(\alpha)+\alpha=(k+1)\alpha.
\]
On $S^3$, a generator of $H^3(S^3;\mathbb Z)$ is primitive for dimensional reasons. Hence the quaternionic power map $q\mapsto q^k$ has degree $k$.
:::

<1>3. Every quaternionic polynomial
\[
P(x)=a_nx^nb_n+\cdots+a_1xb_1+a_0,
\qquad a_n,b_n\ne0,
\]
has a root.
::: {.proof}
View $\mathbb H$ as $\mathbb R^4$. Since the leading term dominates as $|x|\to\infty$, $P$ is proper and extends to a map of one-point compactifications
\[
\widehat P:S^4\to S^4.
\]
The proper homotopy
\[
P_t(x)=a_nx^nb_n+t(a_{n-1}x^{n-1}b_{n-1}+\cdots+a_0),
\qquad 0\le t\le1,
\]
shows that $\widehat P$ has the same degree as the leading map $x\mapsto a_nx^nb_n$.

Left and right multiplication by a nonzero quaternion are orientation-preserving linear automorphisms of $\mathbb R^4$, so they have degree $+1$. Radially, the map $x\mapsto x^n$ has boundary map $S^3\to S^3$, $q\mapsto q^n$, whose degree is $n$ by part 2. Hence
\[
\deg\widehat P=n\ne0.
\]
If $P$ had no root, then $0\notin P(\mathbb H)$; a proper map missing a point has degree $0$, contradiction. Thus $P(x)=0$ for some $x\in\mathbb H$.
:::
:::
