---
schema: qual/card@1
id: P-MMAQ-NMHZVYS2AS
kind: problem
title: Length of a module, composition series, and additivity of length along exact
  sequences
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
- Give definitions of the following terms:

  (i) a finite length (left) module, (ii) a composition series for a module, and (iii) the length of a module,

- Let $l(M)$ denote the length of a module $M$.
  Prove that if `\begin{align*} 0\rightarrow M_1\rightarrow M_2\rightarrow\dots\rightarrow M_n\rightarrow 0 .\end{align*}`{=tex}

  is an exact sequence of modules of finite length, then `\begin{align*} \sum_{i=1}^n(-1)^i l(M_i)=0.\end{align*}`{=tex}
:::

::: {.solution}

::: pf

::: pf-step

A module $M$ has **finite length** if it admits a finite composition series.
A **composition series** is a finite chain
\[
0=M_0\subsetneq M_1\subsetneq\cdots\subsetneq M_r=M
\]
of submodules such that every quotient $M_i/M_{i-1}$ is simple.
The **length** $l(M)$ is the number $r$ of simple factors in a composition series.

::: pf-proof

By the Jordan--Hölder theorem, any two composition series of a finite-length module have the same number of factors, so $l(M)$ is well-defined.

:::

:::

::: {.pf-step #s2}

If
\[
0\longrightarrow A\longrightarrow B\xrightarrow{\pi} C\longrightarrow0
\]
is a short exact sequence of finite-length modules, then
\[
l(B)=l(A)+l(C).
\]

::: pf-proof

Identify $A$ with its image in $B$. Choose composition series
\[
0=A_0\subsetneq A_1\subsetneq\cdots\subsetneq A_r=A
\]
and
\[
0=C_0\subsetneq C_1\subsetneq\cdots\subsetneq C_s=C.
\]
Then
\[
0=A_0\subsetneq\cdots\subsetneq A_r=A
=\pi^{-1}(C_0)
\subsetneq\pi^{-1}(C_1)
\subsetneq\cdots\subsetneq\pi^{-1}(C_s)=B
\]
is a composition series for $B$. Indeed,
\[
\pi^{-1}(C_j)/\pi^{-1}(C_{j-1})\cong C_j/C_{j-1}
\]
for each $j$, while the factors below $A$ are the factors of the chosen composition series of $A$. Hence the series has $r+s$ factors.

:::

:::

::: {.pf-step #s3}

For the exact sequence
\[
0\to M_1\xrightarrow{d_1}M_2\xrightarrow{d_2}\cdots\xrightarrow{d_{n-1}}M_n\to0,
\]
set
\[
I_i=\operatorname{im}(d_i)\quad(1\le i\le n-1),
\qquad I_0=I_n=0.
\]
Then for every $1\le i\le n$ there is a short exact sequence
\[
0\longrightarrow I_{i-1}\longrightarrow M_i\longrightarrow I_i\longrightarrow0.
\]

::: pf-proof

Exactness gives
\[
\ker(d_i)=\operatorname{im}(d_{i-1})=I_{i-1}
\]
for $1<i<n$. At the two ends, injectivity of $M_1\to M_2$ gives $I_0=0=\ker d_1$, while exactness at $M_n$ gives $I_{n-1}=M_n$ and hence the final short exact sequence
\[
0\to I_{n-1}\to M_n\to0.
\]
The first isomorphism theorem gives $M_i/I_{i-1}\cong I_i$.

:::

:::

::: {.pf-step #s4}

Therefore
\[
l(M_i)=l(I_{i-1})+l(I_i)
\qquad(1\le i\le n).
\]

::: pf-proof

Apply step [](#s2){.pf-ref} to the short exact sequences in step [](#s3){.pf-ref}.

:::

:::

::: pf-step

The alternating sum of the lengths vanishes:
\[
\sum_{i=1}^n(-1)^i l(M_i)=0.
\]

::: pf-proof

Using step [](#s4){.pf-ref},
\[
\begin{aligned}
\sum_{i=1}^n(-1)^i l(M_i)
&=\sum_{i=1}^n(-1)^i l(I_{i-1})
 +\sum_{i=1}^n(-1)^i l(I_i)\\
&=-\sum_{j=0}^{n-1}(-1)^j l(I_j)
 +\sum_{j=1}^{n}(-1)^j l(I_j).
\end{aligned}
\]
All interior terms cancel, and the two endpoint terms vanish because $I_0=I_n=0$ and $l(0)=0$.

:::

:::

:::

:::
