---
schema: qual/card@1
id: P-MMAQ-CAEXKRPGEP
kind: problem
title: Units and maximal ideals of $C[0,1]$
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Consider the ring `\begin{align*} S=C[0,1]=\{f:[0,1]\rightarrow\mathbb R:f\text{ is continuous}\} .\end{align*}`{=tex}

with the usual operations of addition and multiplication of functions.

- What are the invertible elements of $S$?

- For $a\in[0,1]$, define $I_a=\{f\in S:f(a)=0\}$.
  Show that $I_a$ is a maximal ideal of $S$.

- Show that the elements of any proper ideal of $S$ have a common zero, i.e., if $I$ is a proper ideal of $S$, then there exists $a\in[0,1]$ such that $f(a)=0$ for all $f\in I$.
  Conclude that every maximal ideal of $S$ is of the form $I_a$ for some $a\in[0,1]$.

  > **Hint**: As $[0,1]$ is compact, every open cover of $[0,1]$ contains a finite subcover.
:::

::: {.solution}
<1>1. A function $f\in S$ is invertible if and only if
\[
f(x)\ne0\qquad\text{for every }x\in[0,1].
\]
::: {.proof}
If $f$ is invertible, choose $g\in S$ with $fg=1$. Then for every $x$,
\[
f(x)g(x)=1,
\]
so $f(x)\ne0$.

Conversely, suppose $f$ is nowhere zero. Then
\[
g(x)=\frac1{f(x)}
\]
is continuous on $[0,1]$, because reciprocal is continuous on $\mathbb R\setminus\{0\}$ and $f([0,1])\subseteq\mathbb R\setminus\{0\}$. Hence $g\in S$ and $fg=1$.
:::

<1>2. For each $a\in[0,1]$, the set $I_a$ is a maximal ideal of $S$.
::: {.proof}
Consider evaluation at $a$,
\[
\operatorname{ev}_a:S\longrightarrow\mathbb R,
\qquad
\operatorname{ev}_a(f)=f(a).
\]
This is a surjective ring homomorphism, since every real number is the value at $a$ of the corresponding constant function. Its kernel is exactly
\[
\ker(\operatorname{ev}_a)=I_a.
\]
Therefore the first isomorphism theorem gives
\[
S/I_a\cong\mathbb R.
\]
Because $\mathbb R$ is a field, $I_a$ is maximal.
:::

<1>3. Let $I\subsetneq S$ be a proper ideal. Then the elements of $I$ have a common zero.
::: {.proof}
Suppose not. Then for every $x\in[0,1]$ there exists $f_x\in I$ such that
\[
f_x(x)\ne0.
\]
By continuity of $f_x$, there is an open neighborhood $U_x$ of $x$ on which $f_x$ is nowhere zero. The family $\{U_x:x\in[0,1]\}$ is an open cover of $[0,1]$. By compactness, choose finitely many points $x_1,\dots,x_n$ such that
\[
[0,1]=U_{x_1}\cup\cdots\cup U_{x_n}.
\]
Set
\[
h=f_{x_1}^2+\cdots+f_{x_n}^2.
\]
Since each $f_{x_i}\in I$ and $I$ is an ideal, $h\in I$.

For every $y\in[0,1]$, some $U_{x_i}$ contains $y$, so $f_{x_i}(y)\ne0$. Hence
\[
h(y)=\sum_{i=1}^n f_{x_i}(y)^2>0.
\]
Thus $h$ is nowhere zero, so by <1>1 it is a unit of $S$. Since $h\in I$, the ideal $I$ contains a unit, hence $I=S$, contradicting that $I$ is proper. Therefore there exists $a\in[0,1]$ with
\[
f(a)=0\qquad\text{for every }f\in I.
\]
:::

<1>4. Every maximal ideal of $S$ is $I_a$ for some $a\in[0,1]$.
::: {.proof}
Let $M$ be maximal. By <1>3, there exists $a\in[0,1]$ such that every $f\in M$ vanishes at $a$. Hence
\[
M\subseteq I_a.
\]
By <1>2, $I_a$ is a proper maximal ideal. Since $M$ is maximal and is contained in the proper ideal $I_a$, we must have
\[
M=I_a.
\]
:::
:::
