---
schema: qual/card@1
id: E-7PAHX
kind: problem
title: Principal parts of $P/Q$ at simple and double poles
classification:
  areas:
  - complex-analysis
  topics:
  - Principal Parts
  - Poles
  - Residues
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $P, Q$ be polynomials with no common zeros. Assume $a$ is a root of
$Q$.
Find the principal part of $P/Q$ at $z=a$ in terms of $P$ and $Q$ if $a$ is 

(1) a simple root, and 
(2) a double root.

:::

::: {.solution}
Since $P(a)\neq0$, a root of $Q$ of order $m$ is a pole of $P/Q$ of order $m$.

(1) Write $Q(z)=(z-a)R(z)$ with $R$ a polynomial and $R(a)=Q'(a)\neq0$. Then $P/R$ is holomorphic near $a$, and
\[
{P(z) \over Q(z) } = {1\over z-a} {P(z) \over R(z)} 
= {1\over z-a}\qty{{P(a)\over R(a)} + \bigo(z-a)}
,\]
so the principal part at $a$ is
\[
\boxed{{P(a)\over Q'(a)}\,{1\over z-a}}
.\]

(2) Write $Q(z)=(z-a)^2R(z)$ with $R(a)\neq0$. Differentiating, $Q''(a)=2R(a)$ and $Q'''(a)=6R'(a)$. The function $h\coloneqq P/R$ is holomorphic near $a$, and
\[
{P(z) \over Q(z) } = {h(z)\over (z-a)^2} = {h(a) \over (z-a)^2} + {h'(a)\over z-a} + \bigo(1)
.\]
Here
\[
h(a)={P(a)\over R(a)}={2P(a)\over Q''(a)},
\qquad
h'(a)={P'(a)R(a)-P(a)R'(a)\over R(a)^2}={2P'(a)\over Q''(a)}-{2P(a)Q'''(a)\over 3Q''(a)^2}
,\]
so the principal part at $a$ is
\[
\boxed{{2P(a)\over Q''(a)}\,{1\over (z-a)^2}+\qty{{2P'(a)\over Q''(a)}-{2P(a)Q'''(a)\over 3Q''(a)^2}}{1\over z-a}}
.\]
:::
