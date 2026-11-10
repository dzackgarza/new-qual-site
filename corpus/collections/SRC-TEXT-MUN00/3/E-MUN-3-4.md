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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.4, printed pp. 20--21** (`tmp/sources/munkres-solutions-whitman.pdf`); the three checks and the map $g$ below are his.

(a) *Reflexive.* For $a\in A$, $f(a)=f(a)$, so $a\sim a$.

*Symmetric.* If $a\sim b$ then $f(a)=f(b)$, hence $f(b)=f(a)$ and $b\sim a$.

*Transitive.* If $a\sim b$ and $b\sim c$ then $f(a)=f(b)=f(c)$, hence $a\sim c$.

(b) Each equivalence class is nonempty, since it contains its members; and the classes partition $A$. Define
$$
g: A^*\longrightarrow B,
\qquad
g(C)=f(a)\quad\text{for any } a\in C .
$$
This is well defined: if $a,a'\in C$ then $a\sim a'$, so $f(a)=f(a')$.

*Injective.* If $g(C)=g(D)$, choose $c\in C$ and $d\in D$; then $f(c)=f(d)$, so $c\sim d$ and $d$ lies in the class of $c$, which is $C$. Hence $d\in C\cap D$, and since distinct classes are disjoint, $C=D$.

*Surjective.* Let $b\in B$. Since $f$ is surjective there is $a\in A$ with $f(a)=b$; let $C$ be the class of $a$. Then $g(C)=f(a)=b$.

Hence $g$ is a bijection of $A^*$ with $B$.
:::
