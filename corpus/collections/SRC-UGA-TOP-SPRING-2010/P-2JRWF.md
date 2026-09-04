---
schema: qual/card@1
id: P-2JRWF
kind: problem
title: Every map homotopic to $f\vee g:X\vee Y\to X\vee Y$ has a fixed point
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: problem
Let $X$ and $Y$ be finite connected simplicial complexes and let $f : X \to Y$ and $g : Y \to X$ be basepoint-preserving maps.

Show that no matter how you homotope $f \lor g : X \lor Y \to X \lor Y$, there will always be a fixed point.
:::

::: {.solution}
Put
\[
F=f\vee g:X\vee Y\longrightarrow X\vee Y,
\]
where $F$ sends the $X$-summand into the $Y$-summand by $f$ and the $Y$-summand into the $X$-summand by $g$.

<1>1. For every $n\ge1$,
\[
H_n(X\vee Y;\QQ)
\cong
H_n(X;\QQ)\oplus H_n(Y;\QQ).
\]
::: {.proof}
Since $X$ and $Y$ are connected and are wedged at a point, reduced homology satisfies
\[
\widetilde H_n(X\vee Y;\QQ)
\cong
\widetilde H_n(X;\QQ)\oplus\widetilde H_n(Y;\QQ).
\]
For $n\ge1$, reduced and unreduced homology agree.
:::

<1>2. For every $n\ge1$, the trace of
\[
F_*:H_n(X\vee Y;\QQ)\longrightarrow H_n(X\vee Y;\QQ)
\]
is zero.
::: {.proof}
With respect to the decomposition in <1>1, the map $F_*$ has block form
\[
F_*
=
\begin{pmatrix}
0 & g_*\\
f_* & 0
\end{pmatrix}.
\]
Indeed, the $X$-summand is sent into $Y$ and the $Y$-summand is sent into $X$.
Both diagonal blocks are zero, so
\[
\operatorname{tr}(F_*|H_n)=0.
\]
:::

<1>3. On degree-zero homology,
\[
F_*:H_0(X\vee Y;\QQ)\longrightarrow H_0(X\vee Y;\QQ)
\]
is the identity and has trace $1$.
::: {.proof}
Because $X$ and $Y$ are connected, their wedge $X\vee Y$ is connected.
Thus
\[
H_0(X\vee Y;\QQ)\cong\QQ.
\]
Every self-map of a connected space induces the identity on $H_0$ with these coefficients.
:::

<1>4. The Lefschetz number of $F$ is
\[
L(F)=1.
\]
::: {.proof}
By definition,
\[
L(F)=\sum_{n\ge0}(-1)^n
\operatorname{tr}\bigl(F_*:H_n(X\vee Y;\QQ)\to H_n(X\vee Y;\QQ)\bigr).
\]
The degree-zero term is $1$ by <1>3, and every positive-degree trace is zero by <1>2. Therefore $L(F)=1$.
:::

<1>5. Every map $H:X\vee Y\to X\vee Y$ homotopic to $F$ also has Lefschetz number $1$.
::: {.proof}
Homotopic maps induce the same maps on homology.
Hence $H_*=F_*$ in every degree, so
\[
L(H)=L(F)=1
\]
by <1>4.
:::

<1>6. Every map homotopic to $f\vee g$ has a fixed point.
::: {.proof}
After subdividing if necessary so that the wedge point is a vertex, $X\vee Y$ is a finite simplicial complex.
Let $H$ be homotopic to $F$.
By <1>5,
\[
L(H)=1\ne0.
\]
The Lefschetz fixed-point theorem therefore implies that $H$ has a fixed point.
:::
:::
