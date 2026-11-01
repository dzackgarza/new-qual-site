---
schema: qual/card@1
id: E-HAT-4.1-22
kind: problem
title: "Countable CW approximation for countable $\\pi_n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 22; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Hatcher, Algebraic Topology, Sec. 4.1, AT.txt:17908-17909, which prints
    "Show that a path-connected space X has a CW approximation with countably many cells iff
    pi_n(X) is countable for all n." The card read "if pi_n(X) is countable for all n", dropping the
    only-if half, and the earlier source-checked note claiming the stored statement matched was false.
    The iff is restored and the converse proved: a CW approximation transfers the homotopy groups,
    and the homotopy groups of a countable CW complex are a countable union of countable sets,
    because every map from S^n has compact image and so lands in a finite subcomplex, of which there
    are countably many, each with countable homotopy groups by simplicial approximation.

- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
---

::: {.problem}
Show that a path-connected space $X$ has a CW approximation with countably many cells if and only if $\pi_n(X)$ is countable for all $n$.
[Use the results on simplicial approximations to maps and spaces in §2.C.]
[Use the results on simplicial approximations to maps and spaces in §2.C.]
:::

::: {.solution}
We use the standard inductive construction of a CW approximation, keeping track of cardinalities.

Start with one $0$-cell and attach $1$-cells representing a generating set for $\pi_1(X)$. Since $\pi_1(X)$ is countable, only countably many $1$-cells are needed. Attach countably many $2$-cells to kill the kernel of the resulting map on $\pi_1$: the kernel is countable because the fundamental group of a countable CW complex is countable.

Inductively suppose a countable CW complex $K_n$ and a map
$$
f_n:K_n\to X
$$
have been constructed inducing isomorphisms on $\pi_i$ for $i<n$ and a surjection on $\pi_n$. The group $\pi_n(K_n)$ is countable: every map $S^n\to K_n$ has compact image, hence lies in a finite subcomplex. There are only countably many finite subcomplexes, and each has countable homotopy groups by cellular approximation using a countable simplicial model. Thus the kernel of
$$
(f_n)_*:\pi_n(K_n)\to\pi_n(X)
$$
is countable. Attach one $(n+1)$-cell for each element of a countable generating set of this kernel, extending the map to $X$ by a nullhomotopy. Then wedge on countably many $(n+1)$-spheres, mapped to representatives of $\pi_{n+1}(X)$, to make the next homotopy map surjective. These latter cells have constant attaching maps, so they preserve the isomorphisms already obtained in lower degrees.

At every stage only countably many cells are added. Taking the union
$$
K=\bigcup_n K_n
$$
produces a CW complex with countably many cells and a map $K\to X$ inducing isomorphisms on every homotopy group. Hence $K\to X$ is a CW approximation, and
$$
\boxed{X\text{ has a CW approximation with countably many cells}.}
$$
:::

::: {.solution}

Conversely, suppose $X$ has a CW approximation $K\to X$ with countably many cells. Then $X$ has countable homotopy groups.

::: pf

::: {.pf-step #s1}

$\pi_n(X)\cong\pi_n(K)$ for every $n\ge1$.

::: pf-proof

A CW approximation is by definition a weak homotopy equivalence $K\to X$, so the induced map $\pi_n(K)\to\pi_n(X)$ is an isomorphism for every $n\ge1$.

:::

:::

::: {.pf-step #s2}

$\pi_n(K)$ is the union of the images of the $\pi_n(L)$ over the finite subcomplexes $L\subseteq K$.

::: pf-proof

Every map $\sigma:S^n\to K$ has compact image. A compact subset of a CW complex meets only finitely many open cells, hence is contained in a finite subcomplex: the cells it does not meet have, by definition of the CW topology, an open complement, and the images of the attaching maps of the remaining cells together with the cells themselves form a finite subcomplex containing the image.

Hence every element $[\sigma]\in\pi_n(K)$ lies in the image of $\pi_n(L)\to\pi_n(K)$ for some finite subcomplex $L$.

:::

:::

::: {.pf-step #s3}

There are only countably many finite subcomplexes of $K$, and each has countable homotopy groups.

::: pf-proof

A finite subcomplex is determined by a finite set of cells, and $K$ has countably many cells, so there are countably many finite subcomplexes.

For countability of $\pi_n(L)$: a finite CW complex is homotopy equivalent to a finite simplicial complex $M$ (subdivide and use cellular approximation). Every map $S^n\to M$ is homotopic, after subdividing the source, to a simplicial map of some finite triangulation of $S^n$; there are countably many finite triangulations of $S^n$ and, for each, only finitely many simplicial maps $S^n\to M$. A countable union of finite sets is countable, so the set of homotopy classes $[S^n,M]=\pi_n(L)$ is countable.

:::

:::

::: {.pf-step #s4}

$\pi_n(X)$ is countable.

::: pf-proof

By steps [](#s1){.pf-ref}–[](#s3){.pf-ref}, $\pi_n(X)\cong\pi_n(K)$ is a countable union of countable sets, hence countable. As $n$ was arbitrary, $\pi_n(X)$ is countable for all $n\ge1$.

:::

:::

:::

:::
