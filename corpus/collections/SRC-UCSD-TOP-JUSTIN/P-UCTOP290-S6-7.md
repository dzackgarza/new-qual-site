---
schema: qual/card@1
id: P-UCTOP290-S6-7
kind: problem
title: Five exact sequences of abelian groups
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 7 from the PDF page image to resolve the maps garbled in extraction.
---

::: {.problem}
Express a long exact sequence as short exact sequences
of kernels and images. Then determine the unknown
abelian group $G$ and map $\alpha$ as far as possible
in each exact sequence:
$$
\begin{aligned}
\text{(a)}\quad&0\to\ZZ_2\to G\to\ZZ\to0,\\
\text{(b)}\quad&0\to\ZZ\to G\to\ZZ_2\to0,\\
\text{(c)}\quad&0\to\ZZ\xrightarrow{\alpha}\ZZ^2
  \to\ZZ\oplus\ZZ_2\to0,\\
\text{(d)}\quad&0\to G\to\ZZ\xrightarrow{\alpha}
  \ZZ\to\ZZ_2\to0,\\
\text{(e)}\quad&0\to\ZZ_3\to G\to\ZZ_2
  \to\ZZ\xrightarrow{\alpha}\ZZ\to0.
\end{aligned}
$$
:::

::: {.solution}

For an exact sequence with differentials
$d_i:A_i\to A_{i-1}$, exactness gives
$\ker d_i=\operatorname{im}d_{i+1}$.
Thus each middle term fits into
$$
0\to\operatorname{im}d_{i+1}
\to A_i\to\operatorname{im}d_i\to0.
$$

(a) The quotient is free, so the sequence
splits. Thus $G\cong\ZZ_2\oplus\ZZ$,
with the standard inclusion and projection
up to isomorphism of sequences.

(b) Choose a generator $e$ of the injected
$\ZZ$ and a lift $t$ of the nonzero element
of $\ZZ_2$. Then $2t=ke$ for some integer
$k$. Replacing $t$ by $t+me$ changes $k$
by an even integer. If $k$ is even, the
sequence splits and $G\cong\ZZ\oplus\ZZ_2$.
If $k$ is odd, $G\cong\ZZ$, with the
inclusion given, up to signs, by
multiplication by $2$ and the quotient
map given by reduction modulo $2$.

(c) Write $\alpha(1)=(u,v)$. Its cokernel
has torsion subgroup $\ZZ_{\gcd(u,v)}$.
The stated cokernel therefore requires
$\gcd(u,v)=2$. Conversely every such
vector gives the stated exact sequence.
After an automorphism of $\ZZ^2$,
$\alpha(1)=(2,0)$.

(d) The cokernel of multiplication by
an integer $k$ on $\ZZ$ is $\ZZ_k$.
Thus $\alpha$ is multiplication by
$+2$ or $-2$, and $G=\ker\alpha=0$.

(e) The last map is surjective, so
$\alpha$ is multiplication by $+1$
or $-1$. Its kernel is zero; exactness
makes $\ZZ_2\to\ZZ$ the zero map and
$G\to\ZZ_2$ surjective. Thus $G$
has order $6$. As an abelian group of
order $6$, it is $\ZZ_6$.
:::
