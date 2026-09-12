---
schema: qual/card@1
id: E-MUN-7-6
kind: problem
title: Schroeder–Bernstein theorem and equal cardinality
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
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

::: {.solution}
(a) Put
\[
A_1=A,\qquad B_1=B,
\]
and for \(n>1\), define
\[
A_n=f(A_{n-1}),\qquad B_n=f(B_{n-1}).
\]
Since \(B\subset A\) and \(f\) is injective,
\[
A_1\supset B_1\supset A_2\supset B_2\supset A_3\supset\cdots.
\]
Let
\[
R=\bigcup_{n\ge1}(A_n-B_n)
\]
and define
\[
h:A\to B,
\qquad
h(x)=
\begin{cases}
f(x),&x\in R,\\x,&x\notin R.
\end{cases}
\]
This does map into \(B\): if \(x\notin R\), then in particular \(x\notin A_1-B_1=A-B\), hence \(x\in B\); if \(x\in R\), then \(f(x)\in f(A)=A_2\subset B\).

Moreover, injectivity of \(f\) gives
\[
f(A_n-B_n)=A_{n+1}-B_{n+1}.
\]
Thus \(f\) maps \(R\) bijectively onto
\[
R\cap B=\bigcup_{n\ge2}(A_n-B_n),
\]
while \(h\) is the identity on \(A-R\), which lies in \(B-R\). These two image pieces are disjoint and together equal \(B\). Hence \(h\) is bijective, so \(A\) and \(B\) have the same cardinality.

(b) Suppose there are injections
\[
f:A\to C,
\qquad
g:C\to A.
\]
Let \(B=g(C)\subset A\). The map \(g:C\to B\) is a bijection after restricting its codomain to its image. The composite
\[
g\circ f:A\to B
\]
is injective. By part (a), there is a bijection \(A\to B\). Composing with the inverse bijection \(B\to C\) induced by \(g\) yields a bijection \(A\to C\). This is the Schroeder--Bernstein theorem.
:::
