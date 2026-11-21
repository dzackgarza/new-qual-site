---
schema: qual/card@1
id: E-QJLUO
kind: problem
title: Separating compact sets from closed sets in completely regular spaces
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
audit:
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source states f(A)={0} and f(B)={1}. For an empty set, its image is empty; the intended assertion is pointwise separation.'
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S33.pdf, Exercise 33.8, page 2 of the file
    (tmp/sources/munkres-solutions-poulsen-S33.pdf, Internet Archive snapshot 20200331153844),
    checked against Munkres, Topology (2000), Section 33 Exercise 8, printed p. 213, Exercise 18.8
    (the maximum of finitely many continuous real-valued functions is continuous) and Theorem 33.1.
    Moller's construction is the card's: finitely many functions g_i with A inside the union of the
    sets {g_i < 1/2} and g_i equal to 1 on B, then g the sum (the card takes the maximum), then
    f = 2 max{0, g - 1/2}. No correction to the mathematics was needed; the maximum is used in place
    of the sum because it keeps the values in [0,1] without dividing by the number of terms.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that complete regularity separates a point from
    a closed set not containing it, that finitely many of the open sets where u_a > 1/2
    cover the compact A, and that u = max u_a and f = max(0, 1 - 2u) have the required
    values. The argument is the card's own; no retained set is cited on the card. Notation
    repaired: the earlier prose wrote \nu_a and \nu(x) where the functions are u_a and u.
    Munkres §33 Exercise 4(a), printed p. 212.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The solution section said "the argument is the card's own ... no retained solution set is
    cited", contradicting the card's own solution-written event of 2026-11-10, which records the
    transcription from Möller's S33 set, Exercise 33.8, PDF p. 2. It also cited §33 Exercise 4(a),
    whereas the card's statement is Exercise 8 of §33: re-read in the retained book, printed
    p. 213 (PDF p. 228) prints "8. Let X be completely regular; let A and B be disjoint closed
    subsets of X. Show that if A is compact, there is a continuous function f: X -> [0,1] such that
    f(A) = {0} and f(B) = {1}.". The retained file was re-read and does contain Ex. 33.8. The
    solution section now names the set and the step at which the card departs from it (maximum in
    place of sum). The 2026-11-18 review note above is left as it was written; this event is the
    correction.
---

::: {.exercise}

Let $X$ be completely regular; let $A$ and $B$ be disjoint closed subsets of $X$.
Show that if $A$ is compact, there is a continuous function $f: X \to [0, 1]$ such that $f(a)=0$ for every $a\in A$ and $f(b)=1$ for every $b\in B$.
:::

::: {.solution}
The argument is transcribed from the retained solution of Jesper Michael Moller, *Solutions to exercises in Munkres*, file S33.pdf, Exercise 33.8, page 2 of the file (`tmp/sources/munkres-solutions-poulsen-S33.pdf`, Internet Archive snapshot 20200331153844), with one change of detail: where Moller sums the finitely many functions $g_i$ the card takes their maximum, which keeps the values in $[0,1]$ without dividing by the number of terms. It is checked against Munkres, Topology (2000), §33 Exercise 8, with the definition of complete regularity in §33 and Exercise 18.8 for the continuity of a maximum of finitely many real-valued continuous functions.

::: pf

::: {.pf-step #trivial}
If $A=\varnothing$ or $B=\varnothing$ the claim holds.

::: pf-proof
If $A=\varnothing$ the constant function $f\equiv1$ is continuous with $f(A)=\varnothing\subset\{1\}$ and $f(B)\subset\{1\}$. If $B=\varnothing$ the constant function $f\equiv0$ has $f(A)\subset\{0\}$ and $f(B)=\varnothing\subset\{1\}$.
:::

:::

::: {.pf-step #pieces}
Assume $A$ and $B$ nonempty. For each $a\in A$ there is a continuous $u_{a}:X\to[0,1]$ with $u_{a}(a)=1$ and $u_{a}=0$ on $B$.

::: pf-proof
By complete regularity applied to the point $a$ and the neighbourhood $X-B$ of it, which is open because $B$ is closed and does not contain $a$, there is a continuous function into $[0,1]$ taking the value $0$ at $a$ and $1$ on $X-(X-B)=B$. Taking $u_{a}=1-\varphi_{a}$ for that $\varphi_{a}$ gives $u_{a}(a)=1$ and $u_{a}=0$ on $B$.
:::

:::

::: {.pf-step #cover}
The open sets $U_{a}=\{x\mid u_{a}(x)>\tfrac12\}$ cover $A$, and finitely many of them do.

::: pf-proof
$a\in U_{a}$ because $u_{a}(a)=1>\tfrac12$, so the family covers $A$. It is a family of open sets of $X$, so its traces on the compact subspace $A$ cover $A$; hence finitely many traces cover $A$, that is $A\subset U_{a_{1}}\cup\dots\cup U_{a_{n}}$.
:::

:::

::: {.pf-step #u}
$u=\max\{u_{a_{1}},\dots,u_{a_{n}}\}$ is continuous, vanishes on $B$, and exceeds $\tfrac12$ on $A$.

::: pf-proof
A maximum of finitely many continuous real-valued functions is continuous. On $B$ every $u_{a_{i}}$ vanishes, so $u=0$ there. On $A$ at least one $u_{a_{i}}$ exceeds $\tfrac12$ by step [](#cover){.pf-ref}, so $u>\tfrac12$ there.
:::

:::

::: {.pf-step #function}
$f=\max\{0,1-2u\}$ is continuous, $f:X\to[0,1]$, $f=0$ on $A$ and $f=1$ on $B$.

::: pf-proof
$f$ is a composite of continuous functions, so continuous. Since $0\le u\le1$, the value $1-2u$ lies in $[-1,1]$, so $f$ takes values in $[0,1]$. On $A$ one has $u>\tfrac12$, so $1-2u<0$ and $f=0$; on $B$ one has $u=0$, so $f=1$.
:::

:::

::: {.pf-step}
The claim holds.

::: pf-proof
Steps [](#trivial){.pf-ref} and [](#function){.pf-ref} cover the two cases and give the required separating function.
:::

:::

:::
:::
