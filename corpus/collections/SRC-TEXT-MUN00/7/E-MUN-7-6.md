---
schema: qual/card@1
id: E-MUN-7-6
kind: exercise
title: "Schroeder–Bernstein theorem and equal cardinality"
subtitle: Munkres §7.6
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
---

::: {.exercise}

We say that two sets $A$ and $B$ have the same cardinality if there is a bijection of $A$ with $B$ .

(a) Show that if $B \subset A$ and if there is an injection

$$
f: A \longrightarrow B,
$$

then A and B have the same cardinality.
[Hint: Define $A_{1} = A$, $B_{1} = B$, and for n > 1, $A_{n} = f(A_{n-1})$ and $B_{n} = f(B_{n-1})$ . (Recursive definition again!)
Note that $A_{1} \supset B_{1} \supset A_{2} \supset B_{2} \supset A_{3} \supset \cdots$ . Define a bijection $h : A \to B$ by the rule

$$
h (x) = \left\{ \begin{array}{l l} f (x) & \text { if } x \in A _ {n} - B _ {n} \text { for some } n, \\ x & \text { otherwise. } ] \end{array} \right.
$$

(b) Theorem (Schroeder-Bernstein theorem).
If there are injections $f: A \to C$ and $g: C \to A$, then $A$ and $C$ have the same cardinality.
:::
