---
schema: qual/card@1
id: E-IP1R7
kind: problem
title: The plane minus countably many points is path connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 9, printed p. 158, with the hint;
    the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.9, PDF p. 6. Through each point pass
    uncountably many lines and only countably many meet the countable set, so two lines
    avoiding it and meeting each other join the two points inside the complement.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Assume that $\RR$ is uncountable.
Show that if $A$ is a countable subset of $\RR^2$, then $\RR^2 - A$ is path connected.
[Hint: How many lines are there passing through a given point of $\RR^2$?]
:::

::: {.solution}

The two-line argument is **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.9, PDF p. 6 (`tmp/sources/munkres-solutions-positron-ch3.pdf`), and the statement was checked against Munkres, *Topology* (2000), §24 Exercise 9, printed p. 158, with Exercise 8(d) on the same page and the definition of path connectedness on printed p. 155. The line count is made explicit below: it does not follow from each line meeting $A$ in at most $\cardinality{A}$ points, since there are uncountably many lines, but from each such line being determined by one point of $A$.

For $p=(p_{1},p_{2})\in\RR^{2}$ and $t\in\RR$ let
$$
L_{t}(p)\coloneqq\theset{(s,p_{2}+t(s-p_{1}))\mid s\in\RR},
$$
the line through $p$ of slope $t$.

::: pf

::: {.pf-step #uncountably-many}
For every $p\in\RR^{2}$ there are uncountably many lines through $p$.

::: pf-proof
If $t\neq t'$ then the point $(p_{1}+1,p_{2}+t)$ lies in $L_{t}(p)$ and not in $L_{t'}(p)$, whose points all satisfy $y-p_{2}=t'(x-p_{1})$; so $t\mapsto L_{t}(p)$ is an injective map from $\RR$ into the set of lines through $p$. Since $\RR$ is uncountable by hypothesis, that set is uncountable.
:::

:::

::: {.pf-step #countably-many-meet-A}
If $p\in\RR^{2}-A$, then only countably many lines through $p$ meet $A$.

::: pf-proof
For $a\in A$ the point $a$ differs from $p$, so exactly one line contains both $p$ and $a$; write it $\ell(p,a)$. Given any line $\ell$ through $p$ that meets $A$, pick $a\in\ell\cap A$; then $\ell$ contains $p$ and $a$, so $\ell=\ell(p,a)$. Thus $a\mapsto\ell(p,a)$ maps the countable set $A$ onto the set of lines through $p$ meeting $A$, and a surjective image of a countable set is countable by Theorem 7.1 (printed p. 45).
:::

:::

::: {.pf-step #line-avoiding-A}
For each $x\in\RR^{2}-A$ there is a line $L$ through $x$ with $L\cap A=\varnothing$.

::: pf-proof
By steps [](#uncountably-many){.pf-ref} and [](#countably-many-meet-A){.pf-ref}, the lines through $x$ are uncountable while only countably many of them meet $A$. The difference of an uncountable set and a countable one is nonempty, for otherwise the uncountable set would be the union of two countable sets and hence countable.
:::

:::

::: {.pf-step #second-line}
For $x,y\in\RR^{2}-A$ there are lines $L\ni x$ and $M\ni y$ with $L\cap A=M\cap A=\varnothing$ and $L$ not parallel to $M$.

::: pf-proof
Choose $L$ as in step [](#line-avoiding-A){.pf-ref}. Among the lines through $y$, only countably many meet $A$ by step [](#countably-many-meet-A){.pf-ref}, and exactly one is parallel to $L$; these together are countably many, while step [](#uncountably-many){.pf-ref} gives uncountably many lines through $y$. Choosing $M$ outside both families gives the two properties.
:::

:::

::: {.pf-step #lines-path-connected}
Every line in $\RR^{2}$ is path connected.

::: pf-proof
For fixed $p,t$ the map $s\mapsto(s,p_{2}+t(s-p_{1}))$ is a homeomorphism of $\RR$ onto $L_{t}(p)$ with inverse $(u,v)\mapsto u$, and the vertical lines are homeomorphic to $\RR$ by $(p_{1},s)\mapsto s$. The space $\RR$ is path connected, since $u,v\in\RR$ are joined by the continuous path $s\mapsto(1-s)u+sv$, and path connectedness is preserved by continuous maps (§24, printed p. 155).
:::

:::

::: pf-step
Therefore $\RR^{2}-A$ is path connected.

::: pf-proof
Let $x,y\in\RR^{2}-A$ and take $L,M$ as in step [](#second-line){.pf-ref}. Since $L$ and $M$ are not parallel they meet in exactly one point $z$, and $z\in L$ gives $z\notin A$; so $L\cup M\subset\RR^{2}-A$. Both are path connected by step [](#lines-path-connected){.pf-ref} and they meet in $z$, so their union is path connected by §24 Exercise 8(d) (printed p. 158). As $x\in L$ and $y\in M$, the points $x$ and $y$ are joined by a path in $\RR^{2}-A$, and $x,y$ were arbitrary.
:::

:::

:::

:::
