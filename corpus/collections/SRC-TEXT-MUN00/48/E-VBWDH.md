---
schema: qual/card@1
id: E-VBWDH
kind: problem
title: Uniform boundedness principle
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The printed theorem asks for a nonempty open set, so the complete metric space X must be nonempty.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: Arthur Lei Qiu, MAT 327 Problem Set 4 solutions (the file
    327ps6sol.pdf on the course page https://www.math.toronto.edu/laithy/3272023/ of MAT327, Introduction to
    Topology, 2023; retrieved into tmp/sources/munkres-solutions-mat327-ps6sol.pdf), Question 1, Problem 1(b),
    PDF p. 1. That argument is the one on the card: the sets A_N of points at which every function of the family
    is bounded by N are closed, their union is the whole space by pointwise boundedness, and the Baire property
    of a complete metric space gives one of them a nonempty interior. The sheet proves the statement for a
    locally compact Hausdorff space or a complete metric space at once; the complete metric case is the
    exercise. Checked against Munkres, Topology (2000), §48 Exercise 10, printed p. 299, with Theorem 48.2. What
    was corrected: the printed hypothesis omits that X is nonempty, and the statement is false for the empty
    space, where there is no nonempty open set to find; the card states the exercise as printed and opens with
    the empty case and the assumption that X is nonempty.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, and the retained sheet is now cited in the solution
    section as well as here, with its own titles: "MAT327 Problem Set 4 Solutions, Arthur Lei
    Qiu, Question 1, Problem 1(b)", PDF p. 1, read in the retained file. Pages verified: the
    definition of a Baire space on printed p. 294, in the closed-set form the argument uses;
    Theorem 48.2 on printed p. 296; and the exercise on printed p. 299. The nonemptiness
    caveat of the earlier correction is kept and its use is now located: the contradiction in
    the Baire step is that X, being nonempty and open in itself, has nonempty interior, while
    the union of the A_N would have empty interior. Also written out: the identification
    A_N = intersection of the preimages of [-N,N], and that pointwise boundedness puts x into
    A_N for every N at least a bound. No repair to the statement.
---

::: {.exercise}

Prove the following.

Theorem (Uniform boundedness principle).
Let $X$ be a complete metric space, and let $\mathcal{F}$ be a subset of $\mathcal{C}(X, \RR)$ such that for each $a \in X$, the set

$$
\mathcal{F}_a = \theset{f(a) \mid f \in \mathcal{F}}
$$

is bounded.
Then there is a nonempty open set $U$ of $X$ on which the functions in $\mathcal{F}$ are uniformly bounded, that is, there is a number $M$ such that $\abs{f(x)} \leq M$ for all $x \in U$ and all $f \in \mathcal{F}$.
[Hint: Let $A_N = \theset{x \mid \abs{f(x)} \leq N \text{ for all } f \in \mathcal{F}}$.]
:::

::: {.solution}
The argument is the retained published solution, **Arthur Lei Qiu, *MAT 327 Problem Set 4 Solutions* (University of Toronto, 2023), Question 1, Problem 1(b), PDF p. 1** (`tmp/sources/munkres-solutions-mat327-ps6sol.pdf`), restructured into steps; that sheet proves the statement at once for a locally compact Hausdorff space or a complete metric space, of which the exercise is the second case. The empty space is dealt with first, as it must be: the printed hypothesis omits that $X$ is nonempty.

Throughout, $X$ is a complete metric space and $\mathcal{F}\subset\mathcal{C}(X,\RR)$ is such that $\mathcal{F}_a=\theset{f(a) \mid f\in\mathcal{F}}$ is bounded for every $a\in X$; the exercise is §48 Exercise 10 (printed p. 299), and the tool is the Baire category theorem, that a compact Hausdorff space or a complete metric space is a Baire space (Theorem 48.2, printed p. 296), a Baire space being one in which every countable collection of closed sets with empty interior has a union with empty interior (the definition of §48, printed p. 294).

::: pf

::: {.pf-step #empty}
The printed statement is false for $X=\varnothing$, and the theorem is proved below under the additional hypothesis that $X$ is nonempty.

::: pf-proof
For $X=\varnothing$ the set $\mathcal{C}(X,\RR)$ has exactly one element, the empty function, and the hypothesis "$\mathcal{F}_a$ is bounded for each $a\in X$" is vacuous, so any $\mathcal{F}\subset\mathcal{C}(X,\RR)$ satisfies it; but $\varnothing$ has no nonempty open subset, so no $U$ as required exists. With $X$ nonempty, every $A_N$ for $N$ at least a bound for $\mathcal{F}_a$ at one point $a$ is nonempty, so the sets below are the ones to use.
:::

:::

::: {.pf-step #closed}
For each $N\in\ZZ_+$ the set $A_N=\theset{x\in X \mid \abs{f(x)}\le N\text{ for every }f\in\mathcal{F}}$ is closed in $X$.

::: pf-proof
$A_N=\bigcap_{f\in\mathcal{F}}f^{\inverseof{}}([-N,N])$: a point lies in every one of those preimages exactly when $\abs{f(x)}\le N$ for every $f$. Each $f$ is continuous and $[-N,N]$ is closed in $\RR$, so each preimage is closed, and an intersection of closed sets is closed.
:::

:::

::: {.pf-step #cover}
$X=\bigcup_{N\in\ZZ_+}A_N$.

::: pf-proof
Let $x\in X$. The set $\mathcal{F}_x$ is bounded, so there is $M$ with $\abs{f(x)}\le M$ for every $f\in\mathcal{F}$; taking $N\in\ZZ_+$ with $N\ge M$ gives $x\in A_N$.
:::

:::

::: {.pf-step #nonempty-interior}
Some $A_N$ has nonempty interior.

::: pf-proof
Suppose not, that every $A_N$ has empty interior. The family $\{A_N\}$ is countable and consists of closed sets with empty interior, so by the definition of a Baire space its union has empty interior in $X$. But that union is $X$ by step [](#cover){.pf-ref}, and $X$ has nonempty interior in itself because it is nonempty and open; this contradiction shows that some $A_N$ has nonempty interior. Completeness of $X$ is used exactly here, through Theorem 48.2 (printed p. 296).
:::

:::

::: {.pf-step}
There is a nonempty open $U\subset X$ and a number $M$ with $\abs{f(x)}\le M$ for all $x\in U$ and all $f\in\mathcal{F}$.

::: pf-proof
By step [](#nonempty-interior){.pf-ref} choose $N$ such that $A_N$ has nonempty interior and let $U$ be that interior, which is a nonempty open set with $U\subset A_N$. For $x\in U\subset A_N$ and $f\in\mathcal{F}$ the definition of $A_N$ gives $\abs{f(x)}\le N$, so the assertion holds with $M=N$.
:::

:::

:::
:::
