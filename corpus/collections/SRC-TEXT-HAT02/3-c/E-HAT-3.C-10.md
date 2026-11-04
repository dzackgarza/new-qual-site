---
schema: qual/card@1
id: E-HAT-3.C-10
kind: problem
title: Product of maps in an H-space
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 10; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    All three parts read and checked. (a) is right and the repaired line now names the Künneth
    identification that turns $\delta_{f,g}^*$ into $f^*\otimes g^*$, which is the only use of the
    hypothesis that $H^*(X;R)$ is free and finitely generated — the original left that hypothesis
    dangling. (b) is right: the induction is on the product formula, and primitivity of the degree
    three generator of $S^3$ is now justified rather than waved at, since the mixed terms would
    have bidegree $(i,j)$ with $i,j>0$ and $i+j=3$ while $H^1=H^2=0$. (c) is right: properness
    from the leading term, the proper homotopy to $a_nx^nb_n$, degree $+1$ for left and right
    multiplication by a nonzero quaternion, degree $n$ for the $n$-th power by (b), hence
    $\deg\widehat P=n$; the closing step now says why a proper map missing a point has degree
    zero, namely that it lands in a contractible $S^4\setminus\{0\}$. Cited and not re-proved:
    the degree formula for radial extensions and Hatcher Theorem 1.8.
---

::: {.problem}
Let $X$ be a path-connected H-space with $H^*(X; R)$ free and finitely generated in each dimension.
For maps $f, g: X \to X$, the product $fg: X \to X$ is defined by $(fg)(x) = f(x)g(x)$, using the H-space product.

(a) Show that $(fg)^*(\alpha) = f^*(\alpha) + g^*(\alpha)$ for primitive elements $\alpha \in H^*(X; R)$.

(b) Deduce that the $k$-th power map $x \mapsto x^k$ induces the map $\alpha \mapsto k\alpha$ on primitive elements $\alpha$.
In particular the quaternionic $k$-th power map $S^3 \to S^3$ has degree $k$.

(c) Show that every polynomial $a_n x^n b_n + \dotsb + a_1 x b_1 + a_0$ of nonzero degree with coefficients in $\quaternions$ has a root in $\quaternions$.
[See Theorem 1.8.]
:::

::: {.solution}
Let $\mu:X\times X\to X$ be the H-space multiplication and let
$$
\delta_{f,g}:X\to X\times X,
\qquad
\delta_{f,g}(x)=(f(x),g(x)).
$$
Then $fg=\mu\circ\delta_{f,g}$.

::: pf

::: pf-step

If $\alpha$ is primitive, then
$$
(fg)^*(\alpha)=f^*(\alpha)+g^*(\alpha).
$$

::: pf-proof

Primitivity means
$$
\mu^*(\alpha)=\alpha\times1+1\times\alpha.
$$
Therefore
$$
(fg)^*(\alpha)
=\delta_{f,g}^*\mu^*(\alpha)
=\delta_{f,g}^*(\alpha\times1)+\delta_{f,g}^*(1\times\alpha)
=f^*(\alpha)\otimes1+1\otimes g^*(\alpha)
=f^*(\alpha)+g^*(\alpha).
$$
The penultimate step is the Künneth identification $H^*(X\times X;R)\cong H^*(X;R)\otimes H^*(X;R)$ under which $\delta_{f,g}^*$ becomes $f^*\otimes g^*$; this is the only place the hypothesis that $H^*(X;R)$ is free and finitely generated in each dimension is used, and without it $\times$ and $\otimes$ are not the same.

:::

:::

::: pf-step

The $k$th-power map sends every primitive class $\alpha$ to $k\alpha$.

::: pf-proof

Induct on $k$ using part 1. For the identity map $P_1$, $P_1^*(\alpha)=\alpha$. Since $P_{k+1}=P_k\cdot\operatorname{id}$,
$$
P_{k+1}^*(\alpha)=P_k^*(\alpha)+\alpha=(k+1)\alpha.
$$
On $S^3$, a generator $\alpha$ of $H^3(S^3;\ZZ)$ is primitive: by the Künneth formula the mixed terms of $\mu^*(\alpha)$ would have bidegree $(i,j)$ with $i,j>0$ and $i+j=3$, and $H^i(S^3)=0$ for $i=1,2$, so there are none. Since $H^3(S^3;\ZZ)=\ZZ\cdot\alpha$, the degree of a self-map of $S^3$ is read off on $\alpha$, so the quaternionic power map $q\mapsto q^k$ has degree $k$.

:::

:::

::: pf-step

Every quaternionic polynomial
$$
P(x)=a_nx^nb_n+\cdots+a_1xb_1+a_0,
\qquad a_n,b_n\ne0,
$$
has a root.

::: pf-proof

View $\quaternions$ as $\RR^4$. Since the leading term dominates as $\norm{x}\to\infty$, $P$ is proper and extends to a map of one-point compactifications
$$
\widehat P:S^4\to S^4.
$$
The proper homotopy
$$
P_t(x)=a_nx^nb_n+t(a_{n-1}x^{n-1}b_{n-1}+\cdots+a_0),
\qquad 0\le t\le1,
$$
shows that $\widehat P$ has the same degree as the leading map $x\mapsto a_nx^nb_n$.

Left and right multiplication by a nonzero quaternion are orientation-preserving linear automorphisms of $\RR^4$, so they have degree $+1$. Radially, the map $x\mapsto x^n$ has boundary map $S^3\to S^3$, $q\mapsto q^n$, whose degree is $n$ by part 2. Hence
$$
\deg\widehat P=n\ne0.
$$
If $P$ had no root, then $0\notin P(\quaternions)$, and since $\widehat P(\infty)=\infty$ the compactified map would miss $0$ altogether: it would land in $S^4\setminus\{0\}\cong\RR^4$, which is contractible, so $\widehat P$ would be null-homotopic and have degree $0$, contradicting $\deg\widehat P=n\ne0$. Thus $P(x)=0$ for some $x\in\quaternions$.

:::

:::

:::

:::
