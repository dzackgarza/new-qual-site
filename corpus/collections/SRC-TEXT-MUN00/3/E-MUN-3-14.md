---
schema: qual/card@1
id: E-MUN-3-14
kind: problem
title: The converse relation of an order relation, and the converse of the least upper bound theorem
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 14, printed p. 29: for a relation
    C on A, D is defined by (b,a) in D iff (a,b) in C; (a) C is symmetric iff C = D,
    (b) D is an order relation if C is, (c) the converse of the theorem of Exercise 13.
    The stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.14,
    printed pp. 35-36 (tmp/sources/munkres-solutions-whitman.pdf). His three parts are
    the ones below; (c) is the greatest-lower-bound-to-least-upper-bound mirror of
    Exercise 13, through the set of upper bounds.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the cited published solution: Dan Whitman,
    Topology, Second Edition by James Munkres: Solutions Manual (2019), Exercise 3.14, printed
    pp. 35-36. Checked against Munkres §3 Exercise 14, whose number is read from the collection
    index. Each part re-read: (a) is the chain (a,b) in C iff (b,a) in C iff (a,b) in D, and its
    converse uses C = D once; (b) transfers the three axioms of an order relation to the converse
    relation by reversing the pairs; (c) takes the set of upper bounds of a bounded-above set,
    which is nonempty and bounded below, applies inf, and shows the infimum is the least upper
    bound. Not claimed: the converse of (c), which is Exercise 13 and is not reproved here.
---

::: {.exercise}

If $C$ is a relation on a set $A$, define a new relation $D$ on $A$ by letting $(b, a) \in D$ if $(a, b) \in C$.

(a) Show that $C$ is symmetric if and only if $C = D$.

(b) Show that if $C$ is an order relation, $D$ is also an order relation.

(c) Prove the converse of the theorem in Exercise 13.
:::

::: {.solution}
The argument is transcribed from the published solution of Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.14 (`tmp/sources/munkres-solutions-whitman.pdf`); the three parts are his. It is checked against Munkres, Topology (2000), §3 Exercise 14.

::: pf

::: {.pf-step #parta}
$C$ is symmetric if and only if $C=D$.

:::: pf-proof

::: {.pf-step #symimplieseq}
If $C$ is symmetric then $C=D$.

::: pf-proof
For any $a,b$: $(a,b)\in C$ iff $(b,a)\in C$ by symmetry, and $(b,a)\in C$ iff $(a,b)\in D$ by the definition of the converse relation. Hence $(a,b)\in C$ iff $(a,b)\in D$ for all pairs, that is $C=D$.
:::

:::

::: {.pf-step #eqimpliessym}
If $C=D$ then $C$ is symmetric.

::: pf-proof
Let $(a,b)\in C$. Then $(b,a)\in D$ by the definition of $D$, so $(b,a)\in C$ because $C=D$.
:::

:::

:::

:::

::: {.pf-step #partb}
If $C$ is an order relation then so is $D$.

:::: pf-proof

::: {.pf-step #dnoneflexive}
Not $(a,a)\in D$ for any $a$.

::: pf-proof
$(a,a)\in D$ would mean $(a,a)\in C$ by the definition of $D$, which is excluded by nonreflexivity of $C$.
:::

:::

::: {.pf-step #dcomparable}
For $a\ne b$, $aDb$ or $bDa$.

::: pf-proof
Comparability of $C$ gives $aCb$ or $bCa$; the first says $bDa$ and the second says $aDb$.
:::

:::

::: {.pf-step #dtransitive}
If $aDb$ and $bDc$ then $aDc$.

::: pf-proof
$aDb$ means $bCa$, and $bDc$ means $cCb$; transitivity of $C$ gives $cCa$, which is $aDc$.
:::

:::

:::

:::

::: {.pf-step #partc}
The greatest lower bound property implies the least upper bound property.

::: pf-proof
Suppose $A$ has the greatest lower bound property, and let $A_0\subseteq A$ be nonempty and bounded above. Let $B_0$ be the set of upper bounds of $A_0$, which is nonempty by hypothesis. Every $a\in A_0$ satisfies $a\le x$ for all $x\in B_0$, so each $a$ is a lower bound of $B_0$ and $B_0$ is bounded below; let $c=\inf B_0$. For $x\in A_0$ every $y\in B_0$ has $x\le y$, so $x$ is a lower bound of $B_0$ and hence $x\le c$: the element $c$ is an upper bound of $A_0$. If $y$ is any upper bound of $A_0$ then $y\in B_0$ and $c\le y$. So $c$ is the least upper bound of $A_0$.
:::

:::

::: {.pf-step}
Parts (a), (b) and (c) hold.

::: pf-proof
Step [](#parta){.pf-ref} is (a), step [](#partb){.pf-ref} is (b), and step [](#partc){.pf-ref} is (c):
$$
\boxed{C=D\iff C\text{ symmetric};\quad C\text{ order}\implies D\text{ order};\quad \text{glb}\implies\text{lub}.}
$$
In (c) only the greatest lower bound property is assumed, and only for the set $B_0$ of upper bounds of $A_0$.
:::

:::

:::
:::
