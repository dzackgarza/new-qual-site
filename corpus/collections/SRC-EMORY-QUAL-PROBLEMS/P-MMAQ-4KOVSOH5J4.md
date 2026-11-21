---
schema: qual/card@1
id: P-MMAQ-4KOVSOH5J4
kind: problem
title: No finite group is the union of conjugates of a proper subgroup; a transitive
  action on more than one point has a fixed-point-free element
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Groups (6) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAG6, whose solution repeats this counting argument."
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked. (a) The conjugates of H number [G:N_G(H)], which
    is at most [G:H] because N_G(H) contains H; each has |H| elements and all contain the identity,
    so the union has at most 1 + [G:N_G(H)](|H|-1) elements, and that is at most
    1 + [G:H](|H|-1) = |G| - ([G:H]-1) < |G| since H is proper. The union is therefore proper. (b)
    If every element fixed a point then G would be the union of the stabilizers, which are all
    conjugate to G_x by transitivity, and G_x is proper because |X| > 1 and the action is
    transitive; that contradicts (a). The bound in (a) is the classical one and the counting of the
    identity once is what makes the strict inequality work. Nothing outside the exercise checked.
---

::: {.problem}
Let $G$ be a finite group.

(a) Prove that if $H < G$ is a proper subgroup, then $G$ is not the union of conjugates of $H$.

(b) Suppose that $G$ acts transitively on a set $X$ with $\cardinality{X} > 1$.
Prove that there exists an element of $G$ with no fixed points in $X$.
:::

::: {.remark title="Variations"}
For $G=\Sym(X)$ with $\cardinality{X}=n>1$, part (b) gives a permutation of $X$ with no fixed point. The proof of part (b) applies unchanged, because $\Sym(X)$ acts transitively on $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #no-union-of-conjugates}
(a) $G \neq \bigcup_{g \in G} gHg^{-1}$ for $H < G$ proper.

::: pf-proof

::: pf-step
The number of distinct conjugates of $H$ is $[G : N_G(H)] \le [G : H]$.

::: pf-proof
The conjugates of $H$ are indexed by $G/N_G(H)$, and $N_G(H) \supseteq H$, so $[G : N_G(H)] \le [G : H]$.
:::

:::

::: pf-step
Each conjugate has $\cardinality{H}$ elements, and all contain the identity.

::: pf-proof
$\cardinality{gHg^{-1}} = \cardinality{H}$, and $1 \in gHg^{-1}$ for all $g$.
:::

:::

::: pf-step
Hence $\abs{\bigcup_g gHg^{-1}} \le 1 + [G:H](\cardinality{H} - 1) = 1 + \cardinality{G} - [G:H] < \cardinality{G}$.

::: pf-proof
The union has at most $1 + (\text{number of conjugates})(\cardinality{H} - 1)$ elements (counting the identity once), and $[G:H] > 1$ since $H$ is proper.
:::

:::

::: pf-step
Hence the union is a proper subset of $G$.

::: pf-proof
It has fewer than $\cardinality{G}$ elements.
:::

:::

:::

:::

::: {.pf-step #fixed-point-free-element-exists}
(b) A transitive action on $\cardinality{X} > 1$ has a fixed-point-free element.

::: pf-proof

::: pf-step
Suppose every $g \in G$ fixes some point of $X$.

::: pf-proof
Assume this for contradiction.
:::

:::

::: pf-step
Then $G = \bigcup_{x \in X} G_x$, where $G_x$ is the stabilizer of $x$.

::: pf-proof
Every element fixes some point, so every element lies in some stabilizer.
:::

:::

::: pf-step
The stabilizers $G_x$ are all conjugate (since the action is transitive).

::: pf-proof
$G_{gx} = g G_x g^{-1}$.
:::

:::

::: pf-step
Hence $G$ is a union of conjugates of the proper subgroup $G_x$ (proper since $\cardinality{X} > 1$ and the action is transitive).

::: pf-proof
$G_x$ is proper because the orbit of $x$ is all of $X$ with $\cardinality{X} > 1$, so $G_x \neq G$.
:::

:::

::: pf-step
This contradicts step [](#no-union-of-conjugates){.pf-ref}.

::: pf-proof
Step [](#no-union-of-conjugates){.pf-ref} says $G$ is not a union of conjugates of a proper subgroup.
:::

:::

:::

:::

::: pf-qed
Step [](#no-union-of-conjugates){.pf-ref} proves part (a); step [](#fixed-point-free-element-exists){.pf-ref} proves part (b).
:::

:::
:::
