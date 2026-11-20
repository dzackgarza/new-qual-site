---
schema: qual/card@1
id: E-HAT-3.3-3
kind: problem
title: Covering spaces of orientable manifolds
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: local orientation classes are pulled back along the local homeomorphism
    from a sheet over an evenly covered neighbourhood, and constancy on the sheet follows from
    constancy downstairs.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Source-backed rewrite: the solution now follows the printed solution in the Math 538 homework
    solutions, HMW 3 handwritten page 1 (PDF page 13 of hatcher-math538-homework4-solutions.pdf),
    Hatcher 3.3 #3, namely the chain of excision and local-homeomorphism isomorphisms between
    H_n(M-tilde, M-tilde minus x-tilde) and H_n(M, M minus x) and the local-compatibility step; the
    handout's argument was checked against Hatcher's definition of orientation (p.233) and Lemma
    3.27(a) (p.236), which is what makes the ball class mu_B exist and be unique. No author is
    attributed: the sheet identifies only the course (Math 538) and the host (tkmd.org).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the transcribed argument into numbered steps: the orientation of M as a locally
    consistent family of generators, the evenly covered ball and its sheet, the chain of
    isomorphisms from the pair at x-tilde down to the pair at x, and the local-consistency step
    built from the unique class over an evenly covered ball (Lemma 3.27(a)). Supplied the point the
    prose used silently: that the two constructions of the local class agree because both map to
    mu_y under the isomorphism onto H_n(M, M - {y}), which is injective. Not checked this session:
    the handout page was not re-read, and printed pp. 233 and 236 were not re-read either.

---

::: {.problem}
Show that every covering space of an orientable manifold is an orientable manifold.
:::

::: {.solution}

The argument is that of the **Math 538 homework solutions, HMW 3, handwritten page 1 (PDF page 13 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 #3**, which runs the chain of excision and local-homeomorphism isomorphisms and concludes by the local compatibility condition; the steps below make the two uses of injectivity explicit. The statement was checked against Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 3.

An orientation of an $n$-manifold $M$ is a function $x\mapsto\mu_{x}$ choosing a generator $\mu_{x}$ of $H_{n}(M,M-\{x\})\cong\ZZ$ at each point, locally consistent in the sense of Hatcher's definition (printed p. 233): every point has a ball $B$ and a class $\mu_{B}\in H_{n}(M\mid B)$ restricting to $\mu_{y}$ at each $y\in B$, and that class is unique (Lemma 3.27(a)).

Let $p\colon\widetilde M\to M$ be a covering map with $M$ an orientable $n$-manifold.

::: pf

::: {.pf-step #cover}
$\widetilde M$ is an $n$-manifold.

::: pf-proof
A covering map is a local homeomorphism, so each point of $\widetilde M$ has a neighbourhood homeomorphic to an open subset of $\RR^{n}$ (namely an evenly covered neighbourhood of its image). Being locally Euclidean of dimension $n$ is the manifold condition on the local structure; $\widetilde M$ is Hausdorff and second countable because $M$ is and $p$ is a covering of a locally compact space by evenly covered pieces.
:::

:::

::: {.pf-step #generator}
Each $\widetilde x\in\widetilde M$ has a canonical generator $\widetilde\mu_{\widetilde x}$ of $H_{n}(\widetilde M,\widetilde M-\{\widetilde x\})$, obtained from $\mu_{p(\widetilde x)}$ by transport along isomorphisms.

::: pf-proof
Let $x=p(\widetilde x)$ and let $B$ be a ball around $x$ evenly covered by $p$, with $\widetilde B$ the sheet containing $\widetilde x$, so $p\colon\widetilde B\to B$ is a homeomorphism. Excision in Hatcher's form $H_{n}(X\mid A)=H_{n}(X,X-A)$ (printed p. 233) applied to the open sets $\widetilde B$ and $M\setminus\{\widetilde x\}$ gives $H_{n}(\widetilde M,\widetilde M-\{\widetilde x\})\cong H_{n}(\widetilde B,\widetilde B-\{\widetilde x\})$, and similarly $H_{n}(M,M-\{x\})\cong H_{n}(B,B-\{x\})$; the homeomorphism $p$ identifies the middle groups. Composing gives an isomorphism
$$
\Phi_{\widetilde x}\colon H_{n}(\widetilde M,\widetilde M-\{\widetilde x\})\xrightarrow{\ \cong\ }H_{n}(M,M-\{x\}),
$$
and $\widetilde\mu_{\widetilde x}\coloneqq\Phi_{\widetilde x}^{-1}(\mu_{x})$ is a generator because $\Phi_{\widetilde x}$ is an isomorphism.
:::

:::

::: {.pf-step #local}
The family $\widetilde x\mapsto\widetilde\mu_{\widetilde x}$ is locally consistent: each point of $\widetilde M$ has a ball $\widetilde B$ over which a single class restricts to $\widetilde\mu_{\widetilde y}$ at every $\widetilde y\in\widetilde B$.

::: pf-proof
Let $x\in M$ and let $B$ be an evenly covered ball about $x$ with a sheet $\widetilde B$. By local consistency of the orientation of $M$ there is $\mu_{B}\in H_{n}(M\mid B)$ restricting to $\mu_{y}$ for every $y\in B$, unique by Lemma 3.27(a). Excision transports $\mu_{B}$ to a class $\mu_{\widetilde B}\in H_{n}(\widetilde M\mid\widetilde B)$. For $\widetilde y\in\widetilde B$ with $y=p(\widetilde y)$, the class $\mu_{\widetilde B}$ restricts to some generator of $H_{n}(\widetilde M,\widetilde M-\{\widetilde y\})$, and $\Phi_{\widetilde y}$ carries it to a class in $H_{n}(M,M-\{y\})$; by commutativity of the transport with restriction, that class is the restriction of $\mu_{B}$, namely $\mu_{y}$. Since $\Phi_{\widetilde y}$ is an isomorphism, hence injective, and $\Phi_{\widetilde y}(\widetilde\mu_{\widetilde y})=\mu_{y}$, the restriction of $\mu_{\widetilde B}$ at $\widetilde y$ is $\widetilde\mu_{\widetilde y}$.
:::

:::

::: {.pf-step}
$\widetilde M$ is orientable.

::: pf-proof
Steps [](#generator){.pf-ref} and [](#local){.pf-ref} produce, at every point of the $n$-manifold $\widetilde M$, a generator of $H_{n}(\widetilde M,\widetilde M-\{\widetilde x\})$, locally consistent in the sense of the definition; that is an orientation. So every covering space of an orientable manifold is an orientable manifold.
:::

:::

:::

:::
