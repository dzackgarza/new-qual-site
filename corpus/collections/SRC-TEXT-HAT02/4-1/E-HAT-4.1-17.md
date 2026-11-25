---
schema: qual/card@1
id: E-HAT-4.1-17
kind: problem
title: "Connectivity of products and smash products"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 17; the stored statement matches.
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
    Read against the book (AT.txt:17890-17891 for the statement). Correct: replacing X and Y by CW models
    with no cells in dimensions 1..m and 1..n is legitimate, the relative cells of the product are the
    products e^p x e^q with p,q > 0 hence of dimension at least m+n+2, and Corollary 4.12 (no relative
    cells in dimensions at most m+n+1 implies (m+n+1)-connected) gives the pair. For the smash product the
    card's claim that the quotient CW structure has positive cells only in dimensions at least m+n+2 is
    what carries the conclusion, and it is correct since the 0-skeleton of X ^ Y is a point. Not checked:
    no independent verification of Corollary 4.12 beyond its statement.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps and made the model replacement a lemma with its
    source named: Hatcher's CW approximation theorem builds an approximation by attaching one cell
    per generator of the homotopy groups of the target, so an m-connected space has an approximation
    with a single 0-cell and no cells in dimensions 1 through m, and Whitehead makes it a homotopy
    equivalence. Re-read in the retained text: the exercise statement (Section 4.1 Exercise 17) and
    Corollary 4.12, whose printed statement is "A CW pair (X,A) is n-connected if all the cells in
    X - A have dimension greater than n", exactly the form applied. Also made explicit why the
    bound survives m = 0 or n = 0, where "no cells in dimensions 1,...,m" is vacuous and the only
    requirement is a single 0-cell. Not checked this session: the printed page numbers of the
    exercise and of the corollary, which the earlier reading recorded as 358 and the corollary
    unnumbered in the text.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.1 Exercise 17,
    Corollary 4.12 (statement "A CW pair (X,A) is n connected if all the cells in
    X - A have dimension greater than n"), and the CW approximation construction of §4.1. Two
    repairs. (1) Step `model` asserted that no (i+1)-cells are needed at stage i <= m without saying
    why the kernel being killed is trivial; the step now runs the induction: a Z_i with no cells of
    dimension <= i has one 0-cell and trivial pi_i by cellular approximation, so the kernel is trivial
    and the (i+2)-cells of stage i realize pi_{i+1}(X) = 0 for i+1 <= m. (2) The proof silently
    replaced X and Y by the models, and the conclusion is stated about the given X and Y; the step now
    records that a homotopy equivalence of pairs preserves k-connectedness and that the pair and the
    smash product computed with the models are homotopy equivalent to the originals, and fixes the
    convention that later steps use X and Y for the models. Steps `product-cells`, `dimension`,
    `pair`, `smash-cells` and `smash` are unchanged and correct, and `smash` is right that for a pair
    with A a point pi_i(Z,*) = pi_i(Z). Not checked: neither assertion recomputed; no retained
    solution set covers the exercise and none was searched for again.

- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.1 Exercise 17. The proof is correct: the product cells outside the wedge
    are the products of positive-dimensional cells, which have dimension at least $m+n+2$ because the
    models have no cells in dimensions $1$ through $m$ and $1$ through $n$; Corollary 4.12 makes the
    pair $(X\times Y,X\vee Y)$ $(m+n+1)$-connected; the quotient by that subcomplex has one cell per
    cell outside it plus the collapsed $0$-cell, so the same corollary applied to
    $(X\wedge Y,\ast)$ makes the smash product $(m+n+1)$-connected. One repair, in step `model`: it
    paraphrased the cell-attachment construction of the CW approximation with shifting indices and
    never quoted a statement. The step now applies Proposition 4.15 to the $m$-connected pair
    $(X,x_0)$, which gives the model with a single $0$-cell and no cells in dimensions $1,\dots,m$
    directly, and Whitehead's theorem identifies it with $X$. The retained-set sentence is accurate:
    Sam's §4.1 has no entry for Exercise 17 and Proudfoot's Homework #6 covers Exercises 4, 11, 12,
    14 and 15.
---

::: {.problem}
Show that if $X$ and $Y$ are CW complexes with $X$ $m$-connected and $Y$ $n$-connected, then $(X \times Y, X \vee Y)$ is $(m+n+1)$-connected, as is the smash product $X \wedge Y$.
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 4.1 Exercise 17. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 17, and Corollary 4.12 was read in the retained text in the form used below.

Say that a CW complex $Z$ is $k$-connected if $\pi_{i}(Z)=0$ for $0\leq i\leq k$, and that a CW pair $(Z,A)$ is $k$-connected if $\pi_{i}(Z,A)=0$ for $i\leq k$.

::: pf

::: {.pf-step #model}
If $X$ is $m$-connected and $Y$ is $n$-connected, then each is homotopy equivalent to a CW complex with a single $0$-cell and no cells in dimensions $1,\dots,m$ respectively $1,\dots,n$.

::: pf-proof
The pair $(X,x_0)$ is $m$-connected: for $i\ge1$ its homotopy groups are those of $X$, and $\pi_0(X,x_0)=0$ because $X$ is path-connected. Proposition 4.15, applied to that CW pair with $A=\{x_0\}$, gives a CW pair $(Z,x_0)\simeq(X,x_0)$ rel $x_0$ all of whose cells outside $x_0$ have dimension greater than $m$. Such a $Z$ has the single $0$-cell $x_0$ and no cells in dimensions $1,\dots,m$, and the homotopy equivalence $Z\to X$ is a weak homotopy equivalence between CW complexes, hence a homotopy equivalence by Whitehead's theorem. The same applies to $Y$.

Because a homotopy equivalence of pairs preserves $k$-connectedness, it is enough to prove the two assertions for models $X',Y'$ obtained this way: a homotopy equivalence of pairs $(X'\times Y',X'\vee Y')\to(X\times Y,X\vee Y)$ and a homotopy equivalence $X'\wedge Y'\to X\wedge Y$ transfer each conclusion back. In the steps below $X$ and $Y$ denote these models.
:::

:::

::: {.pf-step #product-cells}
In the product CW structure on $X\times Y$, the cells are the products $e^{p}\times e^{q}$ of cells of $X$ and of $Y$, and those not contained in $X\vee Y$ are exactly those with $p\geq1$ and $q\geq1$.

::: pf-proof
The product of two CW complexes carries the CW structure whose open cells are the products of open cells, of dimension $p+q$; this is the standard product cell structure. A cell $e^{p}\times e^{q}$ lies in $X\times\{y_{0}\}$ when $q=0$, and in $\{x_{0}\}\times Y$ when $p=0$; with $x_{0},y_{0}$ the basepoints and the chosen models having a single $0$-cell, $e^{0}=\{x_{0}\}$ and $e^{0}=\{y_{0}\}$. So $X\vee Y$ contains exactly the cells with $p=0$ or $q=0$, and the remaining ones have $p,q\geq1$.
:::

:::

::: {.pf-step #dimension}
Every cell of $X\times Y$ outside $X\vee Y$ has dimension at least $m+n+2$.

::: pf-proof
By step [](#product-cells){.pf-ref} such a cell is $e^{p}\times e^{q}$ with $p\geq1$ and $q\geq1$, and by step [](#model){.pf-ref} there are no cells of $X$ of dimension $1,\dots,m$, so $p\geq m+1$ (for $m=0$ this reads $p\geq1$, which is what was assumed); likewise $q\geq n+1$. The dimension is $p+q\geq(m+1)+(n+1)=m+n+2$.
:::

:::

::: {.pf-step #pair}
$(X\times Y,\,X\vee Y)$ is $(m+n+1)$-connected.

::: pf-proof
Corollary 4.12 (Hatcher, §4.1) states that a CW pair $(Z,A)$ is $k$-connected if all cells of $Z-A$ have dimension greater than $k$. Here the cells outside $X\vee Y$ have dimension at least $m+n+2>m+n+1$ by step [](#dimension){.pf-ref}, and $(X\times Y,X\vee Y)$ is a CW pair. So the pair is $(m+n+1)$-connected.
:::

:::

::: {.pf-step #smash-cells}
$X\wedge Y=(X\times Y)/(X\vee Y)$ is a CW complex with a single $0$-cell, and its positive-dimensional cells have dimension at least $m+n+2$.

::: pf-proof
$X\vee Y$ is a subcomplex of $X\times Y$, so the pair has the homotopy extension property and the quotient is the CW complex obtained by collapsing that subcomplex, with one cell for each cell outside $X\vee Y$ together with the collapsed $0$-cell. By steps [](#product-cells){.pf-ref} and [](#dimension){.pf-ref} those cells have dimension at least $m+n+2$, hence are all positive-dimensional.
:::

:::

::: {.pf-step #smash}
$X\wedge Y$ is $(m+n+1)$-connected.

::: pf-proof
Apply Corollary 4.12 to the CW pair $\bigl(X\wedge Y,\{x_{0}\}\bigr)$: the cells outside the basepoint have dimension at least $m+n+2>m+n+1$ by step [](#smash-cells){.pf-ref}, so the pair is $(m+n+1)$-connected. For a pair with $A$ a point, $\pi_{i}(Z,\ast)=\pi_{i}(Z)$, so $\pi_{i}(X\wedge Y)=0$ for $i\leq m+n+1$.
:::

:::

::: {.pf-step}
$(X\times Y,\,X\vee Y)$ and $X\wedge Y$ are both $(m+n+1)$-connected.

::: pf-proof
Steps [](#pair){.pf-ref} and [](#smash){.pf-ref} give the two conclusions. For $i\leq m+n+1$ the pair's vanishing gives in particular that $\pi_{i}(X\vee Y)\to\pi_{i}(X\times Y)$ is surjective, with kernel the image of $\pi_{i+1}$ of the pair.
:::

:::

:::

:::
