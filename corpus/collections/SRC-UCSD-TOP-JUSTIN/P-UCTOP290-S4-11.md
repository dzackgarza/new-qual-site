---
schema: qual/card@1
id: P-UCTOP290-S4-11
kind: problem
title: Rank of a cyclic-kernel subgroup of a free group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    Read sheet 4, Problems 11 and 14 against the extraction and PDF
    page image. Problem 14 is the n=4 instance of Problem 11.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 4, problems 11 and 14
    (assets/attachments/UCSD_290_F14_sheet4.pdf, printed page 254), from the
    checked-in extraction and a 300 dpi render. Problem 11 asks for the cover
    realising the kernel of F_2 -> Z_3 sending both generators to 1, for a proof
    that the kernel is free on 4 generators, and for the rank when Z_3 is
    replaced by Z_n; problem 14 is the Z_4 case and asks for rank 5. The card is
    the collection's appearance of both problems (index.md records problem 14
    here) and states both, so no repair was needed. Not checked: whether the
    sheet intends one answer for problem 11 or two separate answers, since
    problem 14 repeats the Z_4 case verbatim as its own question.
---

::: {.problem}
Let $F_2=\langle a,b\rangle$, and let
$\theta:F_2\to\ZZ/3$ send both $a$ and $b$ to $1$.
Construct the cover of $S^1\vee S^1$ corresponding to
$H=\ker\theta$ and show that $H$ is free of rank $4$.
If $\ZZ/3$ is replaced by $\ZZ/n$, what is the rank?
In particular, construct the cover for $\ZZ/4$ and show that
its kernel is free of rank $5$.
:::

::: {.solution}

Write $\ZZ/n$ additively and $F_2=\langle a,b\rangle$.

::: pf

::: {.pf-step #cover}

For every $n\ge1$ there is a connected $n$-sheeted covering graph $\Gamma_n$
of $S^1\vee S^1$ with vertices the elements $i\in\ZZ/n$ and, at each vertex,
one $a$-edge and one $b$-edge from $i$ to $i+1$; the subgroup it defines at
the vertex $0$ is $\ker\theta$ for $\theta\colon F_2\to\ZZ/n$ sending both
generators to $1$, and the cover is regular with deck group $\ZZ/n$.

::: pf-proof

Right translation by $+1$ is a bijection of $\ZZ/n$, so every vertex has
exactly one incoming and one outgoing edge of each label, which makes the
labelled graph a covering of $S^1\vee S^1$; it is connected because the
$a$-edges alone form a cycle through every vertex, and it has $n$ vertices,
hence $n$ sheets. Lifting a word from the vertex $0$ moves the vertex by the
total exponent sum of the word modulo $n$, so a loop based at $0$ closes up
exactly when that sum is $0$, which is the kernel of $\theta$. A kernel is
normal, so the cover is regular, and its deck group is
$F_2/\ker\theta\cong\ZZ/n$.

:::

:::

::: {.pf-step #rank}

The subgroup $H=\ker\theta$ is free of rank $n+1$.

::: pf-proof

$\Gamma_n$ is a connected graph with $n$ vertices and $2n$ edges, so its
fundamental group at any vertex is free on $1-n+2n=n+1$ generators, namely the
edges outside a spanning tree; a free group of rank $n+1$ cannot be generated
by fewer elements, so the displayed count is the rank of $H$.

:::

:::

::: {.pf-step #three}

For $n=3$, $\Gamma_3$ is the three-vertex graph with $a$-edges and $b$-edges
both running $0\to1\to2\to0$, and $H$ is free of rank $4$, with basis $a^3$,
$ba^{-1}$, $aba^{-2}$, $a^2b$ at the vertex $0$.

::: pf-proof

With $n=3$ the two families of edges coincide, so this is the left diagram of
sheet 4 problem 7 read as a cover of the wedge; the spanning tree
$0\xrightarrow{a}1\xrightarrow{a}2$ and the four edges outside it give the
four listed words, and step [](#rank){.pf-ref} says $4$ is the rank, so they
are a basis.

:::

:::

::: {.pf-step #four}

For $n=4$, $\Gamma_4$ has the four vertices $0,1,2,3$ with an $a$-edge and a
$b$-edge from $i$ to $i+1$ modulo $4$, eight edges in all, and the kernel
$\ker(F_2\to\ZZ/4)$ is free of rank $5$.

::: pf-proof

Step [](#cover){.pf-ref} gives the graph and step [](#rank){.pf-ref} gives the
rank $1-4+8=5$; explicitly, the four $a$-edges form a spanning tree, so the
edges outside it are the four $b$-edges $i\to i+1$ together with the $a$-edge
$3\to0$, and the resulting basis at $0$ is $a^4$ together with $a^ib a^{-i-1}$
for $i=0,1,2,3$.

:::

:::

:::


:::
