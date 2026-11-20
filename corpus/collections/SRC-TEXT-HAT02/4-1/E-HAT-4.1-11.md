---
schema: qual/card@1
id: E-HAT-4.1-11
kind: problem
title: "Contractibility from nullhomotopic inclusions"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 11; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Read against the book (AT.txt:17863-17865 and 17869-17870 for the statement, 25888-25889 for
    Proposition A.1, 17284-17287 for Whitehead). The argument is correct and complete: path-connectedness
    from the nullhomotopies, compact image of S^n lying in a finite subcomplex and hence in one X_i,
    nullhomotopy of the inclusion giving nullhomotopy of f, all pi_n vanishing, and Whitehead giving
    X ~ *. The S^infinity and infinite-suspension examples are the book's. Not checked: nothing was
    recomputed; the reading is of the written argument and its citations.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Added the path-connectedness argument
    as its own step (two points lie in a common X_k, and the nullhomotopy of X_k -> X_{k+1}
    supplies paths to a common point). Checked the compactness step: a compact subset of a CW
    complex meets finitely many open cells, so it lies in a finite subcomplex, whose finitely many
    cells lie in finitely many X_i, so the image lies in the largest of them. Then the composite
    S^n -> X_i -> X is nullhomotopic because X_i -> X_{i+1} is, and Whitehead's theorem applies
    since both X and the point are CW complexes. The examples now have their reason: the inclusion
    Y -> Sigma Y factors through the cone CY, which is contractible. Statement unchanged; the card
    says the argument is its own.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The card said no retained solution set covers this exercise, and that is false: Sam's set,
    retained as `tmp/sources/hatcher-solutions-sam-2008.pdf`, solves it at §4.1 Exercise 11 on
    printed p. 17, and Proudfoot's sheet 6, retained as `tmp/sources/uoregon-
    proudfoot-634-hw6.md`, solves it on p. 1. The rendered sentence now cites both and says what
    the card adds. Found by screening the residue's absence claims against the solution sets
    inventoried in `wiki/topology/resources/solutions.md`; no step of the proof changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.1 Exercise 11, printed p. 358,
    Proposition A.1 (printed p. 520) for compact images, and Theorem 4.5 for Whitehead. Repair: step
    `groups` concluded pi_n(X) = 0 from a nullhomotopy, but step `null` produces only a free one, and
    the passage from a free nullhomotopy of a based map to a vanishing based class is not free when
    n >= 1. The step now runs that passage: the change-of-basepoint isomorphism beta_gamma, taken along
    the path the nullhomotopy traces at the basepoint, sends [f] to the class of a constant map, and
    X is path-connected by step `path`, so [f] = 0. The remaining steps are unchanged and correct: the
    two points of `path` meet in a common X_k and the nullhomotopy of X_k -> X_{k+1} supplies both
    paths to one point; `finite` is Proposition A.1 plus the finiteness of the cells and the
    increasingness of the sequence; `null` composes the nullhomotopy of the inclusion; `whitehead`
    applies Theorem 4.5 to X -> *. The examples stand: Y -> Sigma Y factors through the cone CY.
    Not checked: nothing recomputed; no retained solution set was re-read in this pass.
---

::: {.problem}
Show that a CW complex is contractible if it is the union of an increasing sequence of subcomplexes $X_1 \subset X_2 \subset \cdots$ such that each inclusion $X_i \hookrightarrow X_{i+1}$ is nullhomotopic, a condition sometimes expressed by saying $X_i$ is contractible in $X_{i+1}$.
An example is $S^\infty$, or more generally the infinite suspension $S^\infty X$ of any CW complex $X$, the union of the iterated suspensions $S^n X$.
:::

::: {.solution}
A compact source maps into a finite subcomplex of the CW complex $X$, hence into some $X_i$; the nullhomotopy of $X_i\hookrightarrow X_{i+1}$ then kills any map out of $S^n$, so all homotopy groups of $X$ vanish, and Whitehead's theorem makes $X$ contractible. The argument is that of retained solutions: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.1 Exercise 11**, printed p. 17 of `tmp/sources/hatcher-solutions-sam-2008.pdf`, and **Nicholas Proudfoot, *Math 634: Algebraic Topology I*, Fall 2015, homework 6, §4.1 Exercise 11**, p. 1 (`tmp/sources/uoregon-proudfoot-634-hw6.md`), both running Whitehead's theorem through cellular approximation and the finiteness of the cells a compact image meets. The path-connectedness step and the reasons for the two examples are the card's.

::: pf

::: {.pf-step #path}
$X$ is path-connected.

::: pf-proof
Let $x,y\in X$. Since $X=\bigcup_iX_i$, there are $i,j$ with $x\in X_i$ and $y\in X_j$; taking $k\ge\max(i,j)$ both lie in $X_k$. The inclusion $X_k\hookrightarrow X_{k+1}$ is nullhomotopic, so there is a point $p\in X_{k+1}$ and paths from $x$ to $p$ and from $y$ to $p$; concatenating gives a path in $X$ from $x$ to $y$.
:::

:::


::: {.pf-step #finite}
For a based map $f\colon S^n\to X$ with $n\ge1$ there is $i$ with $f(S^n)\subseteq X_i$.

::: pf-proof
$S^n$ is compact and $X$ is a CW complex, so $f(S^n)$ meets only finitely many open cells, and therefore lies in a finite subcomplex $K$ of $X$: the union of the closures of those finitely many cells is a finite subcomplex containing the image. Each cell of $X$ lies in some $X_i$, since $X=\bigcup_iX_i$, so the finitely many cells of $K$ lie in $X_{i_1},\dots,X_{i_m}$ with $i_1,\dots,i_m$ finite in number, and $K\subseteq X_i$ for $i=\max(i_1,\dots,i_m)$ using that the sequence is increasing.
:::

:::


::: {.pf-step #null}
With $f(S^n)\subseteq X_i$ as in step [](#finite){.pf-ref}, $f$ is nullhomotopic.

::: pf-proof
$f$ is the composite $S^n\to X_i\hookrightarrow X$. The inclusion $X_i\hookrightarrow X_{i+1}$ is nullhomotopic by hypothesis, so the composite $S^n\to X_i\to X_{i+1}$ is nullhomotopic, and composing further with the inclusion $X_{i+1}\hookrightarrow X$ keeps it nullhomotopic. So $f\simeq\ast$.
:::

:::


::: {.pf-step #groups}
$\pi_n(X)=0$ for all $n\ge1$, and $\pi_0(X)$ is a point.

::: pf-proof
Every element of $\pi_n(X)$ is represented by a based map $S^n\to X$ with $n\ge1$, and steps [](#finite){.pf-ref} and [](#null){.pf-ref} produce a free nullhomotopy of it. That suffices: if $H$ is such a nullhomotopy and $\gamma(t)=H(s_0,t)$ is the path it traces at the basepoint, then the change-of-basepoint map sends $[f]$ to the class of a constant map, and $\beta_\gamma$ is an isomorphism, so $[f]=0$ and every element is the identity. $\pi_0(X)$ is a point by step [](#path){.pf-ref}.
:::

:::


::: {.pf-step #whitehead}
$X$ is contractible.

::: pf-proof
The map $X\to\ast$ induces isomorphisms on all $\pi_n$ for $n\ge0$ by step [](#groups){.pf-ref}, and both $X$ and the point are CW complexes, so Whitehead's theorem gives that $X\to\ast$ is a homotopy equivalence; hence $X\simeq\ast$.
:::

:::


::: {.pf-step #examples}
$S^\infty$ and the infinite suspension $S^\infty X$ of any CW complex satisfy the hypothesis, hence are contractible.

::: pf-proof
$S^\infty=\bigcup_nS^n$ with $S^n\hookrightarrow S^{n+1}$ nullhomotopic, since the inclusion of the equator is nullhomotopic in the next sphere; the subcomplexes $S^n$ are CW subcomplexes and the sequence is increasing with union $S^\infty$. For $S^\infty X=\bigcup_nS^nX$ the same holds with $S^nX$ the $n$-fold suspension of $X$: the inclusion $S^nX\hookrightarrow S^{n+1}X=\Sigma(S^nX)$ is the inclusion of $Y$ into its suspension $\Sigma Y=CY\cup_YCY$, which is nullhomotopic because it factors through either cone $CY$, a contractible space. So the hypothesis applies to the increasing union of subcomplexes.
:::

:::


::: {.pf-step #conclusion}
$X$ is contractible.

::: pf-proof
Steps [](#finite){.pf-ref} through [](#whitehead){.pf-ref} prove the assertion for any such union, and step [](#examples){.pf-ref} records the examples the statement names.
:::

:::

:::
:::
