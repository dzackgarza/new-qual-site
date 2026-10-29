---
schema: qual/card@1
id: P-PRACT20-W5-17
kind: problem
title: A cancellative semigroup with finite cyclic subsemigroups is a group
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 17).
---

::: {.problem}
Let $G$ be a non-empty set with a binary operation which is associative and fully cancellative (i.e. $xz = yz \implies x = y$ and $zx = zy \implies x = y$ for all $x, y, z \in G$). Further assume that $\{x^n : n = 1, 2, 3, \ldots\}$ is finite for all $x \in G$. Show that $G$ is a group.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x\in G$, there is an integer $r\ge1$ such that
$$
x^{r+1}=x.
$$


::: pf-proof

The set of positive powers of $x$ is finite, so there exist integers
$$
1\le m<n
$$
with
$$
x^m=x^n.
$$
Using associativity, write both sides with a common left factor $x$ and apply
left cancellation:
$$
x x^{m-1}=x x^{n-1}
\quad\Longrightarrow\quad
x^{m-1}=x^{n-1}.
$$
Repeating this cancellation $m-1$ times gives
$$
x=x^{n-m+1}.
$$
Set
$$
r=n-m\ge1.
$$

:::

:::

::: {.pf-step #s1-2}

For the integer $r$ from step [](#s1-1){.pf-ref}, the element
$$
e_x=x^r
$$
is idempotent:
$$
e_x^2=e_x.
$$


::: pf-proof

From step [](#s1-1){.pf-ref},
$$
x^{r+1}=x.
$$
Multiplying both sides on the right by $x^{r-1}$ when $r>1$ gives
$$
x^{2r}=x^r.
$$
When $r=1$, the relation is already
$$
x^2=x.
$$
Thus in every case
$$
(x^r)^2=x^r.
$$

:::

:::

::: {.pf-step #s1-3}

Any idempotent element $e\in G$ is a two-sided identity for all of
$G$.


::: pf-proof

Suppose
$$
e^2=e.
$$
For any $a\in G$,
$$
e(ea)=e^2a=ea=e a.
$$
Left cancellation of the common factor $e$ gives
$$
ea=a.
$$
Similarly,
$$
(ae)e=ae^2=ae=a e.
$$
Right cancellation of the common factor $e$ gives
$$
ae=a.
$$
Hence $e$ is a global two-sided identity.

:::

:::

::: {.pf-step #s1-4}

The set $G$ has a two-sided identity element $e$.


::: pf-proof

Choose any $x\in G$, which is possible because $G$ is nonempty. Step [](#s1-2){.pf-ref}
produces an idempotent $e_x$, and step [](#s1-3){.pf-ref} shows that $e_x$ is a global
identity. Denote it by $e$.

:::

:::

::: {.pf-step #s1-5}

Every $x\in G$ has a two-sided inverse.


::: pf-proof

Fix $x\in G$ and choose $r\ge1$ as in step [](#s1-1){.pf-ref}. By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
$$
x^r=e.
$$
If $r=1$, then $x=e$, so $x$ is its own inverse.

If $r\ge2$, set
$$
y=x^{r-1}.
$$
Associativity gives
$$
xy=x^r=e
$$
and
$$
yx=x^r=e.
$$
Thus $y$ is a two-sided inverse of $x$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{G\text{ is a group}}.
$$


::: pf-proof

Associativity is assumed. Step [](#s1-4){.pf-ref} supplies an identity, and step [](#s1-5){.pf-ref}
supplies a two-sided inverse for every element. These are precisely the
remaining group axioms.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
