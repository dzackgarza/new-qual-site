---
schema: qual/card@1
id: E-BAZND
kind: problem
title: Uncountable powers of the line are not normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 32 Exercise 9, printed pp. 206-207,
    whose parts (a)-(d) are the skeleton the card fills in; the proof is A. H. Stone's, as the
    printed statement says. No published solution of it was located, and the book's own printed
    outline is the only published source: Orellana's Section 32 stops at Exercise 5, "Doug's World"
    stops at Problem 32.7, and the sets that do not reach Chapter 4 are those listed in the
    COMPLAINTS.md entry for this batch. What is supplied beyond the printed outline: (b) the
    description of X - P_n as the union of the cylinders fixing two distinct coordinates at one
    value m other than n, and the argument that P_1 cap P_2 is empty because a point of it would be
    an injection of the uncountable J into Z_+; (c) the recursion, including that x_i lies in P_1
    and that the finite set C_i may be absorbed into B_i because J is uncountable and only finitely
    many alpha_j have been used; (d) the compatibility of the two coordinate prescriptions on
    B cap B_{i+1}, for which x_{i+1}(alpha_j) = j = y(alpha_j) on B_i.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: dbFin, "Section 32: Problem 9 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-32-normal-spaces/problem-9-solution/ (read
    2026-11-10; kept at tmp/sources/dbfin/section-32-normal-spaces/problem-9-solution.txt), checked
    against Munkres, Topology (2000), Section 32 Exercise 9, printed pp. 206-207, whose parts (a)-(d)
    are the skeleton A. H. Stone's proof leaves to the reader. Its (a) refines the basis U(x,B) to
    the cylinders of a finite set of coordinates; its (b) shows P_n closed by exhibiting the
    cylinder U(y,{j,k}) at a repetition with value other than n, and P_1 cap P_2 empty because a
    point of P_n is constant equal to n on an uncountable set of coordinates and so cannot lie in
    any P_m for m different from n; its (c) is the printed recursion, with B_n enlarged so that
    U(x^n,B_n) is inside U; its (d) builds z explicitly, equal to j on B_i, 1 on B_{i+1} - B_i and
    2 elsewhere, and checks both coordinate conditions. Corrections: the source's (b) writes the
    definition of P_n as "x_j != n != x_k implies x_j != x_k", which is a garbled form of
    "injective off x^{-1}(n)"; the card keeps the printed definition. The source's (d) writes z_j =
    1 on B_{i+1} - B_i, which is right, but states the conclusion as z in U(y,B) cap U; the card
    states both memberships. This supersedes the previous note, which recorded that only the book's
    outline had been found.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with eleven steps, one for each move of the proof, each carrying a `pf-proof`; the claims
    are the prose's own, distributed and not weakened, and the exercise statement is untouched.
    Cited by number only: the definition of the product topology, the closedness of
    $\ZZ_+$ in $\RR$, and the fact that a closed subspace of a normal space is normal (proved
    in the last step). Checked: that $B_{i+1}\subseteq A$ makes $B\cap B_{i+1}$ contained in
    $B_i$, which is what makes the two coordinate prescriptions compatible, and that
    $\mathbf x_i$ and $\mathbf y$ lie in $P_1$ and $P_2$ respectively.
---

::: {.exercise}

Prove the following.

Theorem.
If $J$ is uncountable, then $\RR^J$ is not normal.

Proof.
(This proof is due to A. H. Stone, as adapted in [S-S].) Let $X = (\ZZ_+)^J$; it will suffice to show that $X$ is not normal, since $X$ is a closed subspace of $\RR^J$.
We use functional notation for the elements of $X$, so that the typical element of $X$ is a function $\mathbf{x}: J \to \ZZ_+$.

(a) If $\mathbf{x} \in X$ and if $B$ is a finite subset of $J$, let $U(\mathbf{x}, B)$ denote the set consisting of all those elements $\mathbf{y}$ of $X$ such that $\mathbf{y}(\alpha) = \mathbf{x}(\alpha)$ for $\alpha \in B$.
Show the sets $U(\mathbf{x}, B)$ are a basis for $X$.

(b) Define $P_n$ to be the subset of $X$ consisting of those $\mathbf{x}$ such that on the set $J - \mathbf{x}^{-1}(n)$, the map $\mathbf{x}$ is injective.
Show that $P_1$ and $P_2$ are closed and disjoint.

(c) Suppose $U$ and $V$ are open sets containing $P_1$ and $P_2$, respectively.
Given a sequence $\alpha_1, \alpha_2, \ldots$ of distinct elements of $J$, and a sequence

$$
0 = n_0 < n_1 < n_2 < \dots
$$

of integers, for each $i \geq 1$ let us set

$$
B_i = \theset{\alpha_1, \dots, \alpha_{n_i}}
$$

and define $\mathbf{x}_i \in X$ by the equations

$$
\begin{array}{ll}
\mathbf{x}_i(\alpha_j) = j & \text{for } 1 \leq j \leq n_{i-1}, \\
\mathbf{x}_i(\alpha) = 1 & \text{for all other values of } \alpha.
\end{array}
$$

Show that one can choose the sequences $\alpha_j$ and $n_j$ so that for each $i$, one has the inclusion

$$
U(\mathbf{x}_i, B_i) \subset U.
$$

[Hint: To begin, note that $\mathbf{x}_1(\alpha) = 1$ for all $\alpha$; now choose $B_1$ so that $U(\mathbf{x}_1, B_1) \subset U$.]

(d) Let $A$ be the set $\theset{\alpha_1, \alpha_2, \ldots}$ constructed in (c). Define $\mathbf{y}: J \to \ZZ_+$ by the equations

$$
\mathbf{y}(\alpha_j) = j \quad \text{for } \alpha_j \in A,
$$

$$
\mathbf{y}(\alpha) = 2 \quad \text{for all other values of } \alpha.
$$

Choose $B$ so that $U(\mathbf{y}, B) \subset V$.
Then choose $i$ so that $B \cap A$ is contained in the set $B_i$.
Show that

$$
U(\mathbf{x}_{i+1}, B_{i+1}) \cap U(\mathbf{y}, B)
$$

is not empty.
:::

::: {.solution}

Let $X=(\ZZ_+)^J$, with each factor discrete.

::: pf

::: pf-step

In the product topology the sets
$$
U(\mathbf x,B)=\{\mathbf y:\mathbf y(\alpha)=\mathbf x(\alpha)\text{ for all }\alpha\in B\},
$$
with $B\subset J$ finite, form a basis.

::: pf-proof

A basis element of the product $\prod_{\alpha}(\ZZ_+)_\alpha$ is a product $\prod_\alpha V_\alpha$ with each $V_\alpha$ open in the discrete factor $\ZZ_+$ and $V_\alpha=\ZZ_+$ for all but finitely many $\alpha$. Since every subset of a discrete space is open, $V_\alpha$ may be replaced by the singleton $\{\mathbf x(\alpha)\}$ at each of the finitely many constrained coordinates; what remains is exactly $U(\mathbf x,B)$ with $B$ the finite set of constrained coordinates. Every $U(\mathbf x,B)$ is itself such a product, hence open, and it contains $\mathbf x$. So the family is a basis for the topology.

:::

:::

::: pf-step

Each $P_n$ is closed: if $\mathbf x\notin P_n$ then $\mathbf x$ is not injective on $J\setminus\mathbf x^{-1}(n)$, so there are distinct $\alpha,\beta\in J$ and an integer $m\ne n$ with
$$
\mathbf x(\alpha)=\mathbf x(\beta)=m,
$$
and then $U(\mathbf x,\{\alpha,\beta\})$ is an open neighbourhood of $\mathbf x$ inside $X\setminus P_n$.

::: pf-proof

$\mathbf x\notin P_n$ says exactly that the restriction of $\mathbf x$ to $J\setminus\mathbf x^{-1}(n)$ is not injective, that is, that two distinct coordinates outside $\mathbf x^{-1}(n)$ carry one value $m$; being outside $\mathbf x^{-1}(n)$ means $m\ne n$. If $\mathbf y\in U(\mathbf x,\{\alpha,\beta\})$ then $\mathbf y(\alpha)=\mathbf y(\beta)=m\ne n$, so $\mathbf y$ also fails to be injective off $\mathbf y^{-1}(n)$ and $\mathbf y\notin P_n$. Thus $U(\mathbf x,\{\alpha,\beta\})\subseteq X\setminus P_n$, and $X\setminus P_n$ is open.

:::

:::

::: pf-step

$P_1$ and $P_2$ are disjoint: a point of $P_1\cap P_2$ would be an injective map $J\to\ZZ_+$, which is impossible for uncountable $J$.

::: pf-proof

Let $\mathbf x\in P_1\cap P_2$ and let $\alpha\ne\beta$ be two coordinates. If $\mathbf x(\alpha)=\mathbf x(\beta)=1$ then the repetition occurs off $\mathbf x^{-1}(2)$, contradicting $\mathbf x\in P_2$; if the common value is $2$ the repetition occurs off $\mathbf x^{-1}(1)$, contradicting $\mathbf x\in P_1$; if it is $m\ne1,2$ it occurs off both $\mathbf x^{-1}(1)$ and $\mathbf x^{-1}(2)$, contradicting either membership. So no two distinct coordinates carry the same value: $\mathbf x$ is injective. An injection of the uncountable set $J$ into the countable set $\ZZ_+$ does not exist, so $P_1\cap P_2=\varnothing$.

:::

:::

::: pf-step

For $i=1$: $\mathbf x_1\equiv1$ lies in $P_1\subset U$, so there is a finite $C_1\subset J$ with $U(\mathbf x_1,C_1)\subset U$; enumerating $C_1$ among distinct points $\alpha_1,\dots,\alpha_{n_1}$, with $n_1>0$, gives
$$
U(\mathbf x_1,B_1)\subset U(\mathbf x_1,C_1)\subset U,
\qquad B_1=\{\alpha_1,\dots,\alpha_{n_1}\}.
$$

::: pf-proof

The constant function $1$ has $\mathbf x_1^{-1}(1)=J$, so off that set (the empty set) it is injective, that is $\mathbf x_1\in P_1\subseteq U$. Since $U$ is open and the sets of step 1 are a basis, some $U(\mathbf x_1,C_1)$ with $C_1$ finite contains $\mathbf x_1$ and lies in $U$; enlarging $C_1$ shrinks $U(\mathbf x_1,C_1)$, so $C_1$ may be taken nonempty. Listing $C_1$ as the first $n_1$ of the $\alpha_j$'s gives $C_1\subseteq B_1$, and $U(\mathbf x_1,B_1)\subseteq U(\mathbf x_1,C_1)$ because prescribing more coordinates shrinks the set.

:::

:::

::: pf-step

For the recursion step: given $\alpha_1,\dots,\alpha_{n_{i-1}}$ and $\mathbf x_i$ defined by
$$
\mathbf x_i(\alpha_j)=j\ \ (1\le j\le n_{i-1}),
\qquad
\mathbf x_i(\alpha)=1\ \ \text{otherwise},
$$
one has $\mathbf x_i\in P_1\subset U$.

::: pf-proof

Off $\mathbf x_i^{-1}(1)=\{\alpha_1,\dots,\alpha_{n_{i-1}}\}$ the function $\mathbf x_i$ takes the values $1,2,\dots,n_{i-1}$ at the distinct points $\alpha_1,\dots,\alpha_{n_{i-1}}$, and those values are distinct, so $\mathbf x_i$ is injective there. Hence $\mathbf x_i\in P_1$, and $P_1\subseteq U$ by hypothesis.

:::

:::

::: pf-step

There is a finite $C_i\subset J$ with $U(\mathbf x_i,C_i)\subset U$, and since $J$ is uncountable while only finitely many $\alpha_j$ have been used, the list can be extended so that $C_i\subset B_i=\{\alpha_1,\dots,\alpha_{n_i}\}$ with $n_i>n_{i-1}$; then
$$
U(\mathbf x_i,B_i)\subset U.
$$

::: pf-proof

$U$ is open and contains $\mathbf x_i$ by step 5, so the basis of step 1 gives a finite $C_i$ with $\mathbf x_i\in U(\mathbf x_i,C_i)\subseteq U$. Only the finitely many points $\alpha_1,\dots,\alpha_{n_{i-1}}$ and the finitely many points of $C_i$ have been named; $J$ is uncountable, so there are distinct new points $\alpha_{n_{i-1}+1},\dots,\alpha_{n_i}$ completing $C_i$ to $B_i$, with $n_i>n_{i-1}$. Prescribing the extra coordinates shrinks the set, so $U(\mathbf x_i,B_i)\subseteq U(\mathbf x_i,C_i)\subseteq U$.

:::

:::

::: pf-step

The function $\mathbf y$ defined by $\mathbf y(\alpha_j)=j$ on $A$ and $\mathbf y(\alpha)=2$ elsewhere lies in $P_2\subset V$, so there is a finite $B\subset J$ with $U(\mathbf y,B)\subset V$.

::: pf-proof

$\mathbf y^{-1}(2)=J\setminus A$, and on $A$ the values $\mathbf y(\alpha_j)=j$ are distinct, so $\mathbf y$ is injective off $\mathbf y^{-1}(2)$; hence $\mathbf y\in P_2\subseteq V$. $V$ is open, so the basis of step 1 gives a finite $B$ with $\mathbf y\in U(\mathbf y,B)\subseteq V$.

:::

:::

::: pf-step

Because $B\cap A$ is finite, there is $i$ with $B\cap A\subset B_i$.

::: pf-proof

$A=\{\alpha_1,\alpha_2,\dots\}$ and the sets $B_i=\{\alpha_1,\dots,\alpha_{n_i}\}$ increase with $i$ and exhaust $A$. A finite subset $B\cap A$ of the union therefore lies in some $B_i$: each of its finitely many points is some $\alpha_j$, and $B_i$ contains all $\alpha_j$ with $j\le n_i$.

:::

:::

::: pf-step

With such an $i$, the two coordinate prescriptions are compatible and
$$
U(\mathbf x_{i+1},B_{i+1})\cap U(\mathbf y,B)\ne\varnothing.
$$

::: pf-proof

A point of the intersection must satisfy $\mathbf z(\alpha)=\mathbf x_{i+1}(\alpha)$ on $B_{i+1}$ and $\mathbf z(\alpha)=\mathbf y(\alpha)$ on $B$. The two prescriptions can conflict only on $B\cap B_{i+1}$, and $B_{i+1}\subseteq A$, so $B\cap B_{i+1}=B\cap A\cap B_{i+1}\subseteq B_i$ by step 8; there $\mathbf x_{i+1}(\alpha_j)=j=\mathbf y(\alpha_j)$ because $j\le n_i$. On $B\setminus A$ only $\mathbf y$ prescribes a value, and $B\setminus A$ meets $B_{i+1}\subseteq A$ in nothing; on $B_{i+1}\setminus B$ only $\mathbf x_{i+1}$ prescribes one. So defining $\mathbf z$ to equal the common prescription on $B\cup B_{i+1}$ and $1$ elsewhere gives a function $J\to\ZZ_+$ lying in both sets.

:::

:::

::: pf-step

Hence every open $U\supset P_1$ and open $V\supset P_2$ intersect, so the disjoint closed sets $P_1,P_2$ are not separated by disjoint open sets, and $X$ is not normal.

::: pf-proof

Given such $U$ and $V$, steps 4--6 produce the sequences and step 7 produces $B$, after which steps 8 and 9 produce a point of $U(\mathbf x_{i+1},B_{i+1})\cap U(\mathbf y,B)\subseteq U\cap V$. So $U\cap V\ne\varnothing$ for every pair of open sets containing $P_1$ and $P_2$; since $P_1$ and $P_2$ are disjoint and closed by steps 2 and 3, they are closed sets that cannot be separated, and $X$ is not normal.

:::

:::

::: pf-step

Finally $X=(\ZZ_+)^J$ is closed in $\RR^J$, since
$$
X=\bigcap_{\alpha\in J}\pi_\alpha^{-1}(\ZZ_+)
$$
and $\ZZ_+$ is closed in $\RR$; a closed subspace of a normal space is normal, so $\RR^J$ is not normal for uncountable $J$.

::: pf-proof

Each $\pi_\alpha$ is continuous, so $\pi_\alpha^{-1}(\ZZ_+)$ is closed in $\RR^J$ when $\ZZ_+$ is closed in $\RR$; an intersection of closed sets is closed, and a point of $\RR^J$ lies in all of them exactly when every coordinate is a positive integer, which is $X$. For the last step: if $F,G$ are disjoint closed subsets of a closed subspace $A$ of a normal space $Y$, then $F,G$ are closed in $Y$ and have disjoint open neighbourhoods in $Y$, whose intersections with $A$ separate them in $A$; so $A$ is normal. If $\RR^J$ were normal, its closed subspace $X$ would be normal, which step 10 denies.

:::

:::

:::
:::