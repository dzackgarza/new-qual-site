---
schema: qual/card@1
id: E-MUN-2-3
kind: problem
title: Preimage and image for arbitrary unions and intersections
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §2 Exercise 3, printed p. 21; the stored
    statement matches: (b), (c), (f) and (g) of Exercise 2 for arbitrary unions and
    intersections.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 2.3,
    printed pp. 13-14 (tmp/sources/munkres-solutions-whitman.pdf). His four parts are
    the card's; the injective case of (g) is his argument that the points x_0 witnessing
    y in each f(A_0) agree, and it is where the nonemptiness of the index collection is
    used.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the transcribed four-part answer into numbered steps, one for each of (b), (c), (f)
    and (g), with the element chases written out and the two directions of each equality separated.
    Supplied in the process: an explicit two-point counterexample for the failure of equality in
    (g) in place of the pointer to another card, and the empty-index case, where the inclusion of
    (g) still holds because the intersection of the empty family of subsets of B is B itself while
    the injective equality fails. The theorem content is the earlier reading's. Not re-read this
    session: the Whitman pages and Munkres printed p. 21.
---

::: {.exercise}

Show that (b), (c), (f), and (g) of Exercise 2 hold for arbitrary unions and intersections.
:::

::: {.solution}

The four parts are those of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 2.3** (`tmp/sources/munkres-solutions-whitman.pdf`); the index set is written $I$ below rather than as a collection $\mathcal{A}$, and the two additions are an explicit counterexample in (g) and the empty-index case.

Let $f\colon A\to B$, let $\{B_{i}\}_{i\in I}$ be a family of subsets of $B$ and $\{A_{i}\}_{i\in I}$ a family of subsets of $A$. Recall $f^{-1}(S)=\{x\in A\mid f(x)\in S\}$ and $f(T)=\{f(x)\mid x\in T\}$.

::: pf

::: {.pf-step #b}
$f^{-1}\bigl(\bigcup_{i}B_{i}\bigr)=\bigcup_{i}f^{-1}(B_{i})$.

::: pf-proof
For any $x\in A$, $x\in f^{-1}(\bigcup_{i}B_{i})$ means $f(x)\in\bigcup_{i}B_{i}$, which means $f(x)\in B_{i}$ for some $i\in I$, which means $x\in f^{-1}(B_{i})$ for that $i$, which means $x\in\bigcup_{i}f^{-1}(B_{i})$. Each step is an equivalence, so the two sets have the same elements. When $I$ is empty both sides are empty.
:::

:::

::: {.pf-step #c}
$f^{-1}\bigl(\bigcap_{i}B_{i}\bigr)=\bigcap_{i}f^{-1}(B_{i})$.

::: pf-proof
$x\in f^{-1}(\bigcap_{i}B_{i})$ means $f(x)\in B_{i}$ for every $i\in I$, that is $x\in f^{-1}(B_{i})$ for every $i$, that is $x\in\bigcap_{i}f^{-1}(B_{i})$; again every step is an equivalence. For empty $I$ both sides equal $A$.
:::

:::

::: {.pf-step #f}
$f\bigl(\bigcup_{i}A_{i}\bigr)=\bigcup_{i}f(A_{i})$.

::: pf-proof
If $y\in f(\bigcup_{i}A_{i})$ then $y=f(x)$ with $x\in A_{i}$ for some $i$, so $y\in f(A_{i})$ for that $i$ and $y$ lies in the union on the right. Conversely if $y\in f(A_{i})$ for some $i$ then $y=f(x)$ with $x\in A_{i}\subset\bigcup_{j}A_{j}$, so $y\in f(\bigcup_{i}A_{i})$.
:::

:::

::: {.pf-step #g-inclusion}
$f\bigl(\bigcap_{i}A_{i}\bigr)\subset\bigcap_{i}f(A_{i})$, for every index set $I$, including the empty one.

::: pf-proof
If $y\in f(\bigcap_{i}A_{i})$ then $y=f(x)$ for some $x$ lying in every $A_{i}$; for each $i$ that $x$ witnesses $y\in f(A_{i})$, so $y$ lies in the intersection. If $I$ is empty the left side is $f(A)$ (since $\bigcap_{i\in\emptyset}A_{i}=A$) and the right side is $B$ (since $\bigcap_{i\in\emptyset}f(A_{i})=B$), and $f(A)\subset B$.
:::

:::

::: {.pf-step #g-strict}
The inclusion of step [](#g-inclusion){.pf-ref} can be strict.

::: pf-proof
Take $A=\{1,2\}$, $B=\{*\}$, $f$ the constant map, $I=\{0,1\}$, $A_{0}=\{1\}$ and $A_{1}=\{2\}$. Then $\bigcap_{i}A_{i}=\varnothing$, so $f(\bigcap_{i}A_{i})=\varnothing$, while $f(A_{0})=f(A_{1})=\{*\}$ and hence $\bigcap_{i}f(A_{i})=\{*\}$. The two sides differ.
:::

:::

::: {.pf-step #g-injective}
If $f$ is injective and $I\neq\varnothing$, then $f\bigl(\bigcap_{i}A_{i}\bigr)=\bigcap_{i}f(A_{i})$.

::: pf-proof
One inclusion is step [](#g-inclusion){.pf-ref}. For the other, let $y\in\bigcap_{i}f(A_{i})$. For each $i\in I$ choose $a_{i}\in A_{i}$ with $f(a_{i})=y$; this uses the axiom of choice only for a family of nonempty sets, each $f(A_{i})$ being nonempty because $y$ lies in it. If $i,j\in I$ then $f(a_{i})=y=f(a_{j})$, so injectivity gives $a_{i}=a_{j}$; as $I$ is nonempty, pick $i_{0}\in I$ and let $a=a_{i_{0}}$. Then $a=a_{i}\in A_{i}$ for every $i$, so $a\in\bigcap_{i}A_{i}$ and $y=f(a)\in f(\bigcap_{i}A_{i})$.
:::

:::

::: {.pf-step #g-empty-index}
The hypothesis $I\neq\varnothing$ in step [](#g-injective){.pf-ref} cannot be dropped.

::: pf-proof
With $I=\varnothing$ the intersection of the empty family of subsets of $A$ is $A$ and that of $B$ is $B$, so the asserted equality would read $f(A)=B$; this fails for any non-surjective injective map, for instance the inclusion $\{1\}\to\{1,2\}$.
:::

:::

::: {.pf-step}
Parts (b), (c), (f) and (g) hold for arbitrary families, with the qualification in (g) that equality for intersections needs injectivity and a nonempty index set.

::: pf-proof
Steps [](#b){.pf-ref}, [](#c){.pf-ref}, [](#f){.pf-ref} give the three equalities, and steps [](#g-inclusion){.pf-ref}, [](#g-strict){.pf-ref}, [](#g-injective){.pf-ref} and [](#g-empty-index){.pf-ref} give the intersection statement with its exact hypotheses.
:::

:::

:::

:::
