---
schema: qual/card@1
id: E-MUN-11-3
kind: problem
title: Whether the comparable elements of a point form a maximal chain
classification:
  areas:
  - topology
  topics:
  - Maximum Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §11 Exercise 3 and Examples 1 and 2 of §11,
    printed pp. 68-70; the stored statement matches, and the two examples are described on
    the card so that it stands alone.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    The printed definition of B in the exercise omits x itself: since x is not strictly
    below or above itself, B as printed does not contain x. Dan Whitman records the same
    reading on his printed p. 120 and repairs it by adjoining x. The card states the
    printed set and this repair explicitly rather than answering about a set that does not
    contain the point it was built from.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.3,
    printed pp. 120-121 (tmp/sources/munkres-solutions-whitman.pdf). The answer - Example
    2 succeeds, Example 1 fails - and both witnesses are his: the disc of radius 2 centred
    at (1,0) is comparable with the unit disc at the origin but is not centred there, and
    in Example 2 the comparable points of (0,y_0) are exactly the horizontal line through
    it.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the transcribed answer into numbered steps, and strengthened one inference while
    doing so. The earlier text concluded that the procedure fails in Example 1 from the fact that
    the comparable set contains a disc not centred at the origin, whereas the concentric family is
    a maximal chain; that does not by itself exclude the comparable set from being some other
    maximal chain. The card now exhibits two discs, of radius 2 centred at (1,0) and at (-1,0),
    each of which properly contains the unit disc at the origin and each of which fails to contain
    the other's centre, so the comparable set contains an incomparable pair and is not simply
    ordered at all. Checked: both containments by the triangle inequality with a strict inequality,
    both failures of containment at the other's centre, and in Example 2 that comparability is
    exactly the relation of lying on a common horizontal line and being distinct, that the whole
    line is a maximal chain (any further point is incomparable with two points of the line), and
    that the comparable set is exactly that line. The claim about the printed set omitting x, and
    the two examples, are the earlier reading's.
---

::: {.exercise}

Let $A$ be a set with a strict partial order $\prec$; let $x \in A$. Suppose that we wish to find a maximal simply ordered subset $B$ of $A$ that contains $x$. One plausible way of attempting to define $B$ is to let $B$ equal the set of all those elements of $A$ that are comparable with $x$;
$$
B = \{y \mid y \in A \text{ and either } x \prec y \text{ or } y \prec x\}.
$$
But this will not always work. In which of Examples 1 and 2 will this procedure succeed and in which will it not?
:::

::: {.solution}

The answer and the printed-set observation are those of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.3, printed pp. 120--121** (`tmp/sources/munkres-solutions-whitman.pdf`); the verification of Example 1 below replaces his reason by an incomparable pair, which is what the failure of the procedure actually requires, and the maximality in Example 2 is verified in full.

First, the set as printed omits $x$: since $\prec$ is a strict partial order, $x\prec x$ never holds, and $y=x$ satisfies neither clause. The candidate is therefore the set printed together with $x$, and it is that repaired set that is judged below.

::: pf

::: {.pf-step #omits}
As printed, $B=\{y\in A\mid x\prec y\ \text{or}\ y\prec x\}$ does not contain $x$.

::: pf-proof
A strict partial order is irreflexive, so $x\prec x$ fails; the element $y=x$ therefore satisfies neither alternative of the defining condition, and $x\notin B$. Adjoining $x$ gives the set the procedure intends, namely the elements comparable with $x$ together with $x$ itself.
:::

:::

::: {.pf-step #example1}
In Example 1, $A$ is the collection of circular regions of the plane ordered by proper inclusion, which is a strict partial order, and $x$ is the unit disc $C_{(0,0),1}$.

::: pf-proof
Proper inclusion of sets is irreflexive and transitive, hence a strict partial order; circular regions are the closed discs of the plane, and $x$ is one of them. This is the example the exercise refers to.
:::

:::

::: {.pf-step #two-discs}
Let $D_{+}=C_{(1,0),2}$ and $D_{-}=C_{(-1,0),2}$. Then $x\prec D_{+}$ and $x\prec D_{-}$.

::: pf-proof
If $\abs{p}<1$ then $\abs{p-(1,0)}\leq\abs{p}+\abs{(1,0)}<1+1=2$ by the triangle inequality, so $x\subset D_{+}$; and $(1,0)\in D_{+}$ while $(1,0)\notin x$, so the inclusion is proper. The same computation with $(-1,0)$ in place of $(1,0)$ gives $x\subset D_{-}$ properly.
:::

:::

::: {.pf-step #incomparable}
$D_{+}$ and $D_{-}$ are incomparable under proper inclusion.

::: pf-proof
$(1,0)\in D_{+}$ but $\abs{(1,0)-(-1,0)}=2$, so $(1,0)\notin D_{-}$ and $D_{+}\not\subseteq D_{-}$. Symmetrically $(-1,0)\in D_{-}$ while $\abs{(-1,0)-(1,0)}=2$, so $(-1,0)\notin D_{+}$ and $D_{-}\not\subseteq D_{+}$.
:::

:::

::: {.pf-step #example1-fails}
In Example 1 the procedure fails: the repaired set $B$ is not simply ordered.

::: pf-proof
By steps [](#two-discs){.pf-ref} the discs $D_{+}$ and $D_{-}$ both belong to $B$, and by step [](#incomparable){.pf-ref} they are incomparable, while $B$ also contains $x$. A simply ordered subset has every two of its elements comparable, so $B$ is not simply ordered; in particular it is not a maximal simply ordered subset containing $x$, and the procedure does not produce such a subset. Note also that $B$ is not contained in the chain of discs centred at the origin, since neither $D_{+}$ nor $D_{-}$ is centred there.
:::

:::

::: {.pf-step #example2}
In Example 2, $A=\RR^{2}$ with $(x_{0},y_{0})\prec(x_{1},y_{1})$ exactly when $y_{0}=y_{1}$ and $x_{0}<x_{1}$; this is a strict partial order.

::: pf-proof
Irreflexivity: $x_{0}<x_{0}$ fails. Transitivity: if $y_{0}=y_{1}$, $x_{0}<x_{1}$ and $y_{1}=y_{2}$, $x_{1}<x_{2}$, then $y_{0}=y_{2}$ and $x_{0}<x_{2}$. This is the example the exercise refers to.
:::

:::

::: {.pf-step #lines}
Two points of $\RR^{2}$ are comparable exactly when they are distinct and lie on a common horizontal line, and for each $c$ the line $L_{c}=\{(t,c)\mid t\in\RR\}$ is simply ordered.

::: pf-proof
If $(x_{0},y_{0})\prec(x_{1},y_{1})$ then $y_{0}=y_{1}$ and $(x_{0},y_{0})\neq(x_{1},y_{1})$; conversely, distinct points of a common horizontal line have $x_{0}\neq x_{1}$, and exactly one of $x_{0}<x_{1}$, $x_{1}<x_{0}$ holds by trichotomy, so exactly one of the two orders holds. On $L_{c}$ the relation is thus the order induced by the usual order of $\RR$ on the first coordinate, which is total, so $L_{c}$ is simply ordered.
:::

:::

::: {.pf-step #maximal}
Each $L_{c}$ is a maximal simply ordered subset.

::: pf-proof
Let $S\supset L_{c}$ be simply ordered and let $(u,v)\in S$. Since $(0,c)\in L_{c}\subset S$ and $S$ is simply ordered, $(u,v)$ and $(0,c)$ are comparable or equal; in each case $v=c$, by step [](#lines){.pf-ref} and the definition of $L_{c}$. Hence $S\subset L_{c}$, so $S=L_{c}$ and no larger simply ordered subset contains $L_{c}$.
:::

:::

::: {.pf-step #example2-succeeds}
In Example 2 the procedure succeeds: with $x=(0,y_{0})$ the repaired set $B$ equals $L_{y_{0}}$, which is a maximal simply ordered subset containing $x$.

::: pf-proof
Let $(u,v)\in B$. Then $(u,v)=x$, or $(u,v)\prec x$, or $x\prec(u,v)$; in the last two cases step [](#lines){.pf-ref} gives $v=y_{0}$, and in the first case too, so $B\subset L_{y_{0}}$. Conversely, if $(u,y_{0})\in L_{y_{0}}$ then either $u=0$ and $(u,y_{0})=x$, or $u<0$ and $(u,y_{0})\prec x$, or $u>0$ and $x\prec(u,y_{0})$, so $(u,y_{0})\in B$. Hence $B=L_{y_{0}}$, which contains $x$ and is maximal by step [](#maximal){.pf-ref}.
:::

:::

::: {.pf-step}
The procedure fails in Example 1 and succeeds in Example 2.

::: pf-proof
Steps [](#example1-fails){.pf-ref} and [](#example2-succeeds){.pf-ref}, with the repaired set of step [](#omits){.pf-ref}.
:::

:::

:::

:::
