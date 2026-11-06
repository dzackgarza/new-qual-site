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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 6, problem 7
    (assets/attachments/UCSD_290_F14_sheet6.pdf, printed page 259), from the
    checked-in extraction and a 300 dpi render, which resolves the five
    sequences the extraction garbles: 0 -> Z_2 -> G -> Z -> 0, 0 -> Z -> G ->
    Z_2 -> 0, 0 -> Z -alpha-> Z + Z -> Z + Z_2 -> 0, 0 -> G -> Z -alpha-> Z ->
    Z_2 -> 0, and 0 -> Z_3 -> G -> Z_2 -> Z -alpha-> Z -> 0. The card displays
    these five and adds the first request, to write a long exact sequence as
    short exact sequences, which is the printed opening sentence. No repair was
    needed.
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

Write $\ZZ_n=\ZZ/n\ZZ$, and for an exact sequence with differentials
$d_i\colon A_i\to A_{i-1}$ put $Z_i=\ker d_i=\operatorname{im}d_{i+1}$ and
$B_i=\operatorname{im}d_i$.

::: pf

::: {.pf-step #short}

A long exact sequence breaks into the short exact sequences $0\to B_i\to
A_i\to B_{i-1}\to0$ for all $i$.

::: pf-proof

Let $d\colon A_{i+1}\to A_i$ and $d'\colon A_i\to A_{i-1}$ be consecutive
differentials. Exactness at $A_i$ says $\ker d'=\operatorname{im}d$, that is
$B_{i-1}=B_i$ as subgroups of $A_i$ in the appropriate sense: the composite of
$d$ followed by $d'$ is zero, so $\operatorname{im}d\subseteq\ker d'$, and the
equality is exactness. Hence the inclusion $B_i\hookrightarrow A_i$ followed
by the quotient map $A_i\to A_i/B_i=A_i/\ker
d'\cong\operatorname{im}d'=B_{i-1}$ is a short exact sequence.

:::

:::

::: {.pf-step #free-splitting}

A short exact sequence of abelian groups whose quotient is free splits.

::: pf-proof

This is the last part of sheet 6 problem 6: a basis of the quotient lifts
through the surjection and extends by linearity to a section, which gives the
splitting.

:::

:::

::: {.pf-step #casea}

(a) $G\cong\ZZ_2\oplus\ZZ$, and the sequence is the direct sum sequence.

::: pf-proof

The map $G\to\ZZ$ is surjective onto a free group, so by step
[](#free-splitting){.pf-ref} it has a section and $G\cong\ZZ_2\oplus\ZZ$ with
the given inclusion and projection up to isomorphism of sequences.

:::

:::

::: {.pf-step #caseb}

(b) Either $G\cong\ZZ\oplus\ZZ_2$, when the extension splits, or $G\cong\ZZ$
with the inclusion $\ZZ\to G$ multiplication by $2$ and $G\to\ZZ_2$ reduction
modulo $2$.

::: pf-proof

Let $e$ generate the image of the injection $\ZZ\to G$ and let $t\in G$ map to
the nonzero element of $\ZZ_2$. Then $2t\in\ker(G\to\ZZ_2)=\ZZ e$, so $2t=ke$
for an integer $k$, and replacing $t$ by $t+me$ changes $k$ to $k+2m$; so $k$
is determined modulo $2$. If $k$ is even, $t'=t-(k/2)e$ is an element of order
$2$ mapping onto the generator of $\ZZ_2$, so $G=\ZZ e\oplus\ZZ
t'\cong\ZZ\oplus\ZZ_2$. If $k$ is odd, $e'=t-((k-1)/2)e$ satisfies $2e'=e$, so
$e'$ generates $G$ and the sequence becomes $\ZZ\xrightarrow{2}\ZZ\to\ZZ_2$ up
to signs.

:::

:::

::: {.pf-step #casec}

(c) $\alpha(1)=(u,v)$ with $\gcd(u,v)=2$; after an automorphism of $\ZZ^2$,
$\alpha(1)=(2,0)$ and $G$ is not part of the data.

::: pf-proof

The cokernel of $\alpha\colon\ZZ\to\ZZ^2$ is $\ZZ^2/\langle(u,v)\rangle$,
which is $\ZZ\oplus\ZZ/d$ with $d=\gcd(u,v)$, by the argument that an
automorphism of $\ZZ^2$ carries $(u,v)$ to $(d,0)$. The target
$\ZZ\oplus\ZZ_2$ therefore forces $d=2$, and every such pair gives the stated
sequence. There is no unknown group in (c); the only unknown is the map, and
up to automorphisms of the source and target it is $1\mapsto(2,0)$.

:::

:::

::: {.pf-step #cased}

(d) $\alpha$ is multiplication by $\pm2$ and $G=0$.

::: pf-proof

The cokernel of multiplication by $k$ on $\ZZ$ is $\ZZ_k$, and the sequence
requires $\ZZ_k=\ZZ_2$, so $k=\pm2$. Exactness at the middle $\ZZ$ gives
$G=\ker\alpha$, and multiplication by $\pm2$ on $\ZZ$ is injective, so $G=0$.

:::

:::

::: {.pf-step #casee}

(e) $\alpha$ is multiplication by $\pm1$, $G\cong\ZZ_6$, the map $\ZZ_2\to\ZZ$
is zero, and the map $G\to\ZZ_2$ is surjective.

::: pf-proof

The last map $\ZZ\xrightarrow{\alpha}\ZZ$ is surjective, so $\alpha$ is
multiplication by $\pm1$ and $\ker\alpha=0$; exactness at the second $\ZZ$
then makes the map $\ZZ_2\to\ZZ$ zero, and exactness at $\ZZ_2$ makes
$G\to\ZZ_2$ surjective. Exactness at $G$ then gives
$\operatorname{im}(\ZZ_3\to G)=\ker(G\to\ZZ_2)$, so $\abs G=3\cdot2=6$; the
abelian groups of order $6$ are $\ZZ_6$ alone, so $G\cong\ZZ_6$ and $\ZZ_3\to
G$ is the inclusion of the unique subgroup of order $3$.

:::

:::

:::


:::
