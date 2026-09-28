---
schema: qual/card@1
id: P-QJKMC
kind: problem
title: Jordan form of an operator on a $6$-dimensional space with $T^6=0$ and $T^5\neq
  0$, and similarity of any two such operators
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Nilpotence
  - Canonical Forms
relations: []
review: draft
---

::: {.problem}
Suppose $V$ is $6$-dimensional and $T\in\operatorname{End}(V)$ satisfies
\[
T^6=0,
\qquad
T^5\ne0.
\]

1. Determine the Jordan canonical form of $T$.
2. Show that any two such operators are similar.
:::

::: {.solution}
Because $T$ is nilpotent, every Jordan block has eigenvalue $0$. The condition $T^6=0$ says every block has size at most $6$, while $T^5\ne0$ says at least one block has size at least $6$. Hence there is a block of size exactly $6$.

Since $V$ itself has dimension $6$, that block is the whole Jordan form:
\[
J(T)=J_6(0).
\]

If $S$ is another operator satisfying the same hypotheses, then also
\[
J(S)=J_6(0).
\]
Thus there exist invertible $P,Q$ with
\[
T=PJ_6(0)P^{-1},
\qquad
S=QJ_6(0)Q^{-1}.
\]
Taking
\[
A=QP^{-1}
\]
gives
\[
ATA^{-1}=S.
\]
Hence all such operators are similar.
:::
