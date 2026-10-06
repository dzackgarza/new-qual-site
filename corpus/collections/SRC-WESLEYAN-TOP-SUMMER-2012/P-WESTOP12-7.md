---
schema: qual/card@1
id: P-WESTOP12-7
kind: problem
title: Simple connectivity of subspaces and fundamental groups of retracts
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Prove or disprove each statement:

1. If $A\subset X$ and $X$ is simply connected, then $A$ is simply connected.
2. If $r:X\to A$ is a retraction, then
   \[
   r_*:\pi_1(X)\to\pi_1(A)
   \]
   is surjective.
:::

::: {.solution}
<1>1. Statement (1) is false.

::: {.proof}
Take
\[
X=D^2
\]
and
\[
A=\partial D^2=S^1.
\]
The disk is contractible, hence simply connected:
\[
\pi_1(D^2)=0.
\]

But
\[
\pi_1(S^1)\cong\mathbb Z\ne0.
\]
Thus
\[
A\subset X,
\]
with $X$ simply connected, while $A$ is not simply connected.
:::

<1>2. Statement (2) is true.

::: {.proof}
Let
\[
r:X\to A
\]
be a retraction, and let
\[
i:A\hookrightarrow X
\]
be the inclusion.
By definition of retraction,
\[
r\circ i
=
\operatorname{id}_A.
\]

Choose a basepoint
\[
a_0\in A.
\]
Then
\[
i:(A,a_0)\to(X,a_0)
\]
and
\[
r:(X,a_0)\to(A,a_0)
\]
are pointed maps, because
\[
r(a_0)=a_0.
\]

Functoriality of the fundamental group gives
\[
r_*\circ i_*
=
(r\circ i)_*
=
(\operatorname{id}_A)_*
=
\operatorname{id}_{\pi_1(A,a_0)}.
\]

Hence $r_*$ has a right inverse
\[
i_*.
\]
Any map with a right inverse is surjective.
Therefore
\[
\boxed{
r_*:\pi_1(X,a_0)\twoheadrightarrow\pi_1(A,a_0).
}
\]
:::

<1>3. The final answers are
\[
\boxed{
\begin{array}{c|cc}
\text{statement}&1&2\\
\hline
\text{true?}&\mathrm{no}&\mathrm{yes}
\end{array}
}
\]

::: {.proof}
Step <1>1 gives a counterexample to statement (1), and step <1>2 proves
statement (2).
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 records the complete answer.
:::
:::
