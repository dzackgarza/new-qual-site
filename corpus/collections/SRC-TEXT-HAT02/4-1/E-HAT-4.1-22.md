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
- event: source-corrected
  by: claude
  date: 2026-11-02
  note: >-
    The statement printed the book's bracketed hint twice, "[Use the results on simplicial approximations
    to maps and spaces in §2.C.]" repeated. AT.txt:17908-17909 prints it once, so this was a duplication
    introduced when the hint was restored, not two printed hints; one copy is removed. No other statement
    text is touched, and the "if and only if" reading of the exercise is unchanged.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 22 of §4.1, printed p. 359, with the bracketed hint printed once,
    checked at PDF page 368 of the held book. Checked both directions. Forward: the inductive
    construction adds countably many cells at each stage, the kernels being countable because
    $\pi_n$ of a countable CW complex is countable — every map $S^n\to K$ has compact image, hence
    lies in one of countably many finite subcomplexes, each with countable homotopy groups by
    simplicial approximation against a finite simplicial model. Converse: a countable CW approximation
    $K\to X$ transfers the homotopy groups, every class lies in the image from a finite subcomplex,
    and there are countably many of those. No defect in the mathematics. The printed page is added,
    the card having had none.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.1 Exercise 22, Proposition A.1 and the simplicial approximation results of §2.C. One repair:
    step `s2` justified "a compact subset of a CW complex lies in a finite subcomplex" by saying the
    cells it does not meet have an open complement, which is false — the complement of a single open
    cell is not open, and the cells a compact set misses are in any case not what bounds their number.
    The step now carries Hatcher's own argument from Proposition A.1: a compact set meets only
    finitely many cells, since one point in each of infinitely many would form an infinite closed
    discrete subset of a compact space; the closures of the cells met are then finitely many cells by
    closure-finiteness, and their union is the finite subcomplex. Steps `s1`, `s3` and `s4` are
    unchanged and correct: a CW approximation transfers the homotopy groups; there are countably many
    finite subcomplexes and countability of each one's pi_n goes through a finite simplicial model,
    simplicial approximation over countably many triangulations, and a countable union of finite sets.
    The forward direction, which is the card's first solution block, was re-read and left unchanged:
    countably many cells at each stage because pi_1(X) and each kernel and each pi_{n+1}(X) are
    countable, and pi_n of a countable CW complex is countable by the same compactness argument. The
    card carries its two directions in two solution blocks, as delivered; merging them is a
    formatting change and none was made. Not checked: no recomputation of any cardinality.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.1 Exercise 22, both directions. Forward: a countable CW complex is built
    stage by stage, adding one 1-cell per generator of $\pi_1(X)$, countably many $(n+1)$-cells per
    countable generating set of the kernel of $\pi_n(K_n)\to\pi_n(X)$, and countably many
    $(n+1)$-spheres realizing the elements of $\pi_{n+1}(X)$, with $\pi_n(K_n)$ countable because
    every class comes from a finite subcomplex and there are countably many of those. Converse: a
    weak equivalence $K\to X$ identifies the homotopy groups, and $\pi_n(K)$ is a countable union of
    the countable $\pi_n(L)$ over finite subcomplexes $L$, which are countable by simplicial
    approximation. Both are correct. One correction: the solution carried no statement of what the
    retained sets contain, and now records that none holds a solution — Sam's §4.1 has no entry for
    Exercise 22 and Proudfoot's Homework #6 covers Exercises 4, 11, 12, 14 and 15.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    One correction after an independent reading, in the forward direction: it passed from the countable
    stages $K_n$ to their union and asserted that the map on homotopy groups is an isomorphism without
    saying why $\pi_i(K)$ is the colimit of the $\pi_i(K_n)$. The step now runs the compactness
    argument the converse already used: a map $S^i\to K$ has compact image, hence lies in a finite
    subcomplex and so in some single $K_n$ (Proposition A.1), which identifies the colimit; and each
    $K_n$ with $n\ge i$ maps to $X$ by an isomorphism on $\pi_i$, so the limit is $\pi_i(X)$.
---

::: {.problem}
Show that a path-connected space $X$ has a CW approximation with countably many cells if and only if $\pi_n(X)$ is countable for all $n$.
[Use the results on simplicial approximations to maps and spaces in §2.C.]
:::

::: {.solution}
The exercise is §4.1 Exercise 22, where the hint is printed in brackets. No retained solution set holds a solution: Sam's §4.1 has no entry for the exercise, and Proudfoot's Homework #6 covers Exercises 4, 11, 12, 14 and 15. Both directions below are the card's.

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
produces a CW complex with countably many cells and a map $K\to X$ inducing isomorphisms on every homotopy group. The passage to the union uses compactness: a map $S^i\to K$ has compact image and so lies in a finite subcomplex, hence in some single $K_n$ (Proposition A.1), which identifies $\pi_i(K)$ with the direct limit of the $\pi_i(K_n)$; each $K_n$ with $n\ge i$ maps to $X$ by an isomorphism on $\pi_i$, so the limit is $\pi_i(X)$ and the map is an isomorphism there. Hence $K\to X$ is a CW approximation, and
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

Every map $\sigma:S^n\to K$ has compact image, and Hatcher's Proposition A.1 says that a compact subspace of a CW complex is contained in a finite subcomplex. The reason is that a compact $C$ can meet only finitely many cells: if it met infinitely many, choosing one point in each of them would give an infinite set meeting each closed cell in a finite, hence closed, subset, so closed in $K$ by the weak topology, and discrete, so an infinite closed discrete subspace of the compact space $C$. The cells met are therefore finitely many, their closures are finitely many cells in all by closure-finiteness, and the union of those closures is a finite subcomplex containing $C$.

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
