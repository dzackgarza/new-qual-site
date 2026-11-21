---
schema: qual/card@1
id: E-MUN-3-4
kind: problem
title: The equivalence classes of a surjection correspond bijectively to its range
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
    Read against Munkres, Topology (2000), §3 Exercise 4, printed p. 28: for a
    surjective f : A -> B the relation a_0 ~ a_1 iff f(a_0) = f(a_1) is an equivalence
    relation, and its set A^* of classes is in bijective correspondence with B. The
    stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.4,
    printed pp. 20-21 (tmp/sources/munkres-solutions-whitman.pdf). Part (a) is his three
    property checks. Part (b) is his map g(C) = f(a) for a in C: well defined because
    elements of one class have equal images, injective because equal images put the two
    classes in one class (the classes partition A), and surjective because f is.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two parts, which is what Queue D asks for on this card. Part (a) is proved by three substeps and part (b) by a well-definedness step and the two bijectivity steps, all of which the prose had run together; the partition lemma the bijection uses is now a step of its own with its proof, since both injectivity and well-definedness appeal to it. Statement re-read against Munkres, Topology (2000), §3 Exercise 4, printed p. 28; the argument against Dan Whitman's set, Exercise 3.4, printed pp. 20-21. No statement repair.
---

::: {.exercise}

Let $f: A \to B$ be a surjective function. Let us define a relation on $A$ by setting $a_0 \sim a_1$ if
$$
f(a_0) = f(a_1).
$$
(a) Show that this is an equivalence relation.

(b) Let $A^*$ be the set of equivalence classes. Show there is a bijective correspondence of $A^*$ with $B$.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.4, printed pp. 20--21** (`tmp/sources/munkres-solutions-whitman.pdf`); the three checks of (a) and the map $g$ and its two checks in (b) are his. The statement is Munkres, *Topology*, 2nd ed. (2000), §3 Exercise 4, printed p. 28.

::: pf

::: {.pf-step #classes}
Every equivalence class of $\sim$ is nonempty, and two classes are either equal or disjoint; hence the classes partition $A$.

::: pf-proof
A class is the set of all $a'\in A$ with $a'\sim a$ for a fixed $a$, so it contains $a$ because $\sim$ is reflexive, and the classes are the equivalence classes of an equivalence relation, which partition $A$ by the standard lemma: if $C\cap D\ne\varnothing$ and $c\in C\cap D$, then every element of $C$ is related to $c$ and $c$ to every element of $D$, so by transitivity every element of $C$ lies in $D$ and conversely.
:::

:::

::: {.pf-step #part-a}
(a) The relation $\sim$ is an equivalence relation.

::: pf-proof

::: {.pf-step #reflexive}
For every $a\in A$, $a\sim a$.

::: pf-proof
$f(a)=f(a)$ is an equality of elements of $B$, so the defining condition of $\sim$ holds.
:::

:::

::: {.pf-step #symmetric}
If $a\sim b$ then $b\sim a$.

::: pf-proof
$a\sim b$ means $f(a)=f(b)$; the equality $f(b)=f(a)$ is the same statement read the other way, and it is the defining condition of $b\sim a$.
:::

:::

::: {.pf-step #transitive}
If $a\sim b$ and $b\sim c$ then $a\sim c$.

::: pf-proof
The hypotheses give $f(a)=f(b)$ and $f(b)=f(c)$, hence $f(a)=f(c)$ by transitivity of equality in $B$, which is the condition for $a\sim c$.
:::

:::

The three substeps establish reflexivity, symmetry and transitivity, which is the claim.
:::

:::

::: {.pf-step #part-b}
(b) The formula $g(C)=f(a)$ for $a\in C$ defines a bijection $g:A^*\to B$.

::: pf-proof

::: {.pf-step #well-defined}
For a class $C\in A^*$ and any $a,a'\in C$ one has $f(a)=f(a')$, so $g$ is well defined.

::: pf-proof
$a,a'\in C$ means $a\sim a'$, that is $f(a)=f(a')$, so the value prescribed for $g(C)$ does not depend on the representative chosen. The class $C$ is nonempty by step [](#classes){.pf-ref}, so a value is prescribed at all.
:::

:::

::: {.pf-step #injective}
$g$ is injective.

::: pf-proof
Suppose $g(C)=g(D)$ and choose $c\in C$, $d\in D$, which is possible by step [](#classes){.pf-ref}. Then $f(c)=g(C)=g(D)=f(d)$, so $c\sim d$. Since $d$ is related to $c$, it lies in the class of $c$, namely $C$; so $d\in C\cap D$ and $C=D$ because distinct classes are disjoint by step [](#classes){.pf-ref}.
:::

:::

::: {.pf-step #surjective}
$g$ is surjective.

::: pf-proof
Let $b\in B$. Since $f$ is surjective there is $a\in A$ with $f(a)=b$; let $C$ be the class of $a$. Then $g(C)=f(a)=b$.
:::

:::

Steps [](#well-defined){.pf-ref}, [](#injective){.pf-ref} and [](#surjective){.pf-ref} show that $g$ is a well-defined injective and surjective map, that is, the required bijective correspondence of $A^*$ with $B$.
:::

:::

:::
:::
