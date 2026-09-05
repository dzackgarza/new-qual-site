---
schema: qual/card@1
id: P-LZ5CZ
kind: problem
title: $H_i(T,B)$ for a torus and the boundary of an embedded disk
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 8 of the official UGA Spring 2018 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the inclusion B->T is nullhomotopic through the embedded disk and used the full relative long exact sequence in degrees 2, 1, and 0.
---

::: problem
Let $D$ be a closed disk embedded in the torus
\[
T=S^1\times S^1,
\]
and let $X$ be the result of removing the interior of $D$ from $T$.
Let $B$ be the boundary of $X$, i.e. the circle boundary of the original closed disk $D$.
Compute $H_i(T,B)$ for all $i$.
:::

::: {.solution}
All homology groups below have coefficients in $\ZZ$.
Since $B\cong S^1$ and $T\cong S^1\times S^1$,
\[
H_i(B)\cong
\begin{cases}
\ZZ,&i=0,1,\\
0,&\text{otherwise},
\end{cases}
\qquad
H_i(T)\cong
\begin{cases}
\ZZ,&i=0,2,\\
\ZZ^2,&i=1,\\
0,&\text{otherwise}.
\end{cases}
\]

<1>1. The inclusion
\[
j:B\hookrightarrow T
\]
induces the zero map
\[
j_*:H_1(B)\longrightarrow H_1(T).
\]
::: {.proof}
The circle $B$ is the boundary of the embedded disk $D\subset T$.
Hence the inclusion $j:B\hookrightarrow T$ extends over the disk:
\[
\begin{array}{ccc}
B&\hookrightarrow&D\\
&\searrow j&\downarrow\\
&&T.
\end{array}
\]
Since $D$ is contractible, the inclusion $B\to T$ is nullhomotopic.
Therefore it induces the zero homomorphism on positive-dimensional homology, in particular on $H_1$.
:::

<1>2. One has
\[
H_2(T,B)\cong\ZZ^2.
\]
::: {.proof}
The degree-$2$ portion of the long exact sequence of the pair $(T,B)$ is
\[
H_2(B)
\longrightarrow
H_2(T)
\longrightarrow
H_2(T,B)
\longrightarrow
H_1(B)
\xrightarrow{j_*}
H_1(T).
\]
Using $H_2(B)=0$, $H_2(T)\cong\ZZ$, $H_1(B)\cong\ZZ$, and <1>1 gives a short exact sequence
\[
0\longrightarrow\ZZ
\longrightarrow H_2(T,B)
\longrightarrow\ZZ
\longrightarrow0.
\]
Since $\ZZ$ is free abelian, this sequence splits.
Thus
\[
H_2(T,B)\cong\ZZ\oplus\ZZ.
\]
:::

<1>3. One has
\[
H_1(T,B)\cong\ZZ^2
\qquad\text{and}\qquad
H_0(T,B)=0.
\]
::: {.proof}
The next part of the long exact sequence is
\[
H_1(B)
\xrightarrow{j_*}
H_1(T)
\longrightarrow
H_1(T,B)
\longrightarrow
H_0(B)
\longrightarrow
H_0(T)
\longrightarrow
H_0(T,B)
\longrightarrow0.
\]
Both $B$ and $T$ are path-connected, so the inclusion induces an isomorphism
\[
H_0(B)\xrightarrow{\cong}H_0(T).
\]
By <1>1, the preceding map $j_*:H_1(B)\to H_1(T)$ is zero.
Exactness therefore forces
\[
H_1(T)\xrightarrow{\cong}H_1(T,B),
\]
so
\[
H_1(T,B)\cong\ZZ^2.
\]
Exactness at $H_0(T)$ and the fact that $H_0(B)\to H_0(T)$ is surjective give
\[
H_0(T,B)=0.
\]
:::

<1>4. For every $i\ge3$,
\[
H_i(T,B)=0.
\]
::: {.proof}
For $i\ge3$, both $H_i(T)$ and $H_{i-1}(B)$ vanish.
The long exact sequence of the pair therefore forces $H_i(T,B)=0$.
:::

<1>5. Hence
\[
\boxed{
H_i(T,B)\cong
\begin{cases}
\ZZ^2,&i=1,2,\\
0,&\text{otherwise}.
\end{cases}}
\]
::: {.proof}
Combine <1>2, <1>3, and <1>4.
:::
:::
