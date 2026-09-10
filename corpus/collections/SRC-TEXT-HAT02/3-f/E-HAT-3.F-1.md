---
schema: qual/card@1
id: E-HAT-3.F-1
kind: problem
title: "Reverse and double mapping telescopes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Given maps $f_i: X_i \to X_{i+1}$ for integers $i < 0$, show that the "reverse mapping telescope" obtained by gluing together the mapping cylinders of the $f_i$'s in the obvious way deformation retracts onto $X_0$.
Similarly, if maps $f_i: X_i \to X_{i+1}$ are given for all $i \in \mathbb{Z}$, show that the resulting "double mapping telescope" deformation retracts onto any of the ordinary mapping telescopes contained in it, the union of the mapping cylinders of the $f_i$'s for $i$ greater than a given number $n$.

::: {.solution}
For $i<0$, let $M_i$ be the mapping cylinder of
\[
f_i:X_i\to X_{i+1}.
\]
The reverse telescope is
\[
T^- =\cdots\cup M_{-2}\cup M_{-1},
\]
with the copy of $X_{i+1}$ at the top of $M_i$ identified with the copy at the bottom of $M_{i+1}$.

Each mapping cylinder $M_i$ deformation retracts onto its top $X_{i+1}$ by sliding points along the interval direction. These deformations are compatible with the gluing and can be performed successively on the strips
\[
M_{-1},\ M_{-2},\ldots
\]
with the time intervals chosen, for example, as
\[
[0,1/2],\ [1/2,3/4],\ [3/4,7/8],\ldots.
\]
At every time before $1$, only finitely many cylinders have been collapsed, and at time $1$ every point has been carried into $X_0$. On each compact subset only finitely many cylinders are involved, so the resulting homotopy is continuous. It fixes $X_0$ throughout. Hence
\[
T^-\simeq X_0
\]
by deformation retraction.

Now let
\[
T=\bigcup_{i\in\mathbb Z}M_i
\]
be the double telescope, and for a fixed integer $n$ let
\[
T_{\ge n}=\bigcup_{i\ge n}M_i
\]
be the ordinary right-hand telescope starting at $X_n$. The complementary left-hand part
\[
\cdots\cup M_{n-2}\cup M_{n-1}
\]
is a reverse telescope ending at $X_n$, so the preceding deformation retraction collapses it onto $X_n$ while fixing $X_n$. Extending this deformation by the identity on $T_{\ge n}$ gives a deformation retraction
\[
T\searrow T_{\ge n}.
\]
Thus the double telescope deformation retracts onto every ordinary tail telescope.
:::
