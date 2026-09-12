---
schema: qual/card@1
id: E-SMI-8000E-NR8
kind: problem
title: Contractions of ideals along ring maps
classification:
  areas:
  - algebra
  topics:
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the contraction, induced-map, and primality statements with the local 8000e PDF and extraction, Noetherian-rings problem 8."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Verified contraction is an ideal, computed the kernel of the induced quotient map, and pulled primality back along the ring map."
---

::: {.exercise}
If $f: R \to S$ is a ring map and $I$ an ideal of $S$, then $f^{-1}(I)$ is an ideal of $R$, the induced map $R/f^{-1}(I) \to S/I$ is injective, and $f^{-1}(I)$ is prime if $I$ is prime.
:::


::: solution
Let
$$
J=f^{-1}(I)=\{r\in R:f(r)\in I\}.
$$

<1>1. The contraction $J$ is an ideal of $R$.
::: proof
Since $0\in I$,
$$
0\in J.
$$
If $a,b\in J$, then $f(a),f(b)\in I$, so
$$
f(a-b)=f(a)-f(b)\in I,
$$
and hence $a-b\in J$.
If $r\in R$ and $a\in J$, then
$$
f(ra)=f(r)f(a)\in I
$$
because $I$ is an ideal of $S$. Thus $ra\in J$. Therefore $J$ is an ideal.
:::

<1>2. The induced map $R/J\to S/I$ is injective.
::: proof
Define
$$
\overline f:R/J\longrightarrow S/I,
\qquad
r+J\longmapsto f(r)+I.
$$
If $r-r'\in J$, then
$$
f(r-r')\in I,
$$
so $f(r)+I=f(r')+I$; hence $\overline f$ is well defined. It is plainly a
ring homomorphism.

Its kernel is
$$
\begin{aligned}
\ker\overline f
&=\{r+J:f(r)\in I\}\\
&=\{r+J:r\in J\}\\
&=0.
\end{aligned}
$$
Thus
$$
\boxed{R/f^{-1}(I)\hookrightarrow S/I.}
$$
:::

<1>3. If $I$ is prime, then $f^{-1}(I)$ is prime.
::: proof
Assume $I$ is prime. Because ring maps preserve $1$, if
$$
1\in f^{-1}(I),
$$
then $1=f(1)\in I$, impossible since $I$ is proper. Thus $f^{-1}(I)$ is
proper.

If
$$
ab\in f^{-1}(I),
$$
then
$$
f(a)f(b)=f(ab)\in I.
$$
Primality of $I$ gives
$$
f(a)\in I\quad\text{or}\quad f(b)\in I,
$$
so
$$
a\in f^{-1}(I)\quad\text{or}\quad b\in f^{-1}(I).
$$
Hence $f^{-1}(I)$ is prime.
:::
:::
