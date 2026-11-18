---
schema: qual/card@1
id: E-MUN-7-2
kind: problem
title: Bijections in the countability proofs for $\QQ$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §7 Exercise 2 and Examples 1 and 2 of §7,
    printed pp. 44-46; the card states the book's two formulas, f(n) = 2n for n > 0 and
    -2n+1 for n <= 0, and f(x,y) = (x+y-1,y) into A = {y <= x} composed with
    g(x,y) = x(x-1)/2 + y, exactly as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.2,
    printed pp. 81-84 (tmp/sources/munkres-solutions-whitman.pdf). He checks each of the
    three maps separately; the card writes the explicit inverses f^{-1} and F^{-1} and
    the consecutive-block count for g, which is his argument that the blocks
    x(x-1)/2 + 1, ..., x(x+1)/2 partition Z_+. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the map of Example 1 with injectivity
    and surjectivity, the two maps of Example 2 with the image in A, the inverse of F and
    the consecutive blocks of G, and the conclusion for each. Read the book's text at
    tmp/sources/munkres-2000-topology.md, which prints f: Z -> Z_+ with f(n) = 2n for
    n > 0 and -2n+1 for n <= 0, F(x,y) = (x+y-1,y) and G(x,y) = (1/2)(x-1)x + y: the
    card's formulas are the printed ones. Re-read the retained solution at the cited
    pages, Whitman Exercise 7.2 printed pp. 81-84; the argument is unchanged.
---

::: {.exercise}

Show that the maps $f$ and $g$ of Examples 1 and 2 are bijections.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.2, printed pp. 81--84** (`tmp/sources/munkres-solutions-whitman.pdf`); the three maps checked are the book's Examples 1 and 2, and the inverse formulas and the block count for $g$ are his argument written out.

The book's Example 1 is the map $f:\ZZ\to\ZZ_{+}$ with $f(n)=2n$ for $n>0$ and $f(n)=-2n+1$ for $n\le0$; Example 2 is the pair of maps
$$
F:\ZZ_{+}^{2}\to A,\quad F(x,y)=(x+y-1,y),
\qquad
G:A\to\ZZ_{+},\quad G(x,y)=\frac{x(x-1)}{2}+y,
$$
where $A=\{(x,y)\in\ZZ_{+}^{2}\mid y\le x\}$.

::: pf

::: {.pf-step #example-one}
$f$ is a bijection $\ZZ\to\ZZ_{+}$.

::: pf-proof
Injectivity and surjectivity, separately.

::: {.pf-step #f-injective}
$f$ is injective.

::: pf-proof
Let $f(m)=f(n)$. If $m,n>0$ then $2m=2n$, so $m=n$. If $m,n\le0$ then $-2m+1=-2n+1$, so again $m=n$. In the remaining case one of $m,n$ is positive and the other is not: say $n>0$ and $m\le0$, so $f(n)=2n$ is even and $f(m)=-2m+1$ is odd, and the two are unequal, contrary to $f(m)=f(n)$. So $f(m)=f(n)$ forces $m=n$.
:::

:::

::: {.pf-step #f-surjective}
$f$ is surjective, hence $f$ is a bijection.

::: pf-proof
Let $k\in\ZZ_{+}$. If $k$ is even, then $k=2n$ with $n=k/2>0$, and $f(n)=k$. If $k$ is odd, then $k=2j-1$ with $j=(k+1)/2\ge1$, so $n=1-j\le0$ satisfies $f(n)=-2(1-j)+1=2j-1=k$. So $k$ has a preimage, and surjectivity together with step [](#f-injective){.pf-ref} makes $f$ a bijection.
:::

:::

:::

:::

::: {.pf-step #example-two-first}
$F(x,y)=(x+y-1,y)$ is a bijection $\ZZ_{+}^{2}\to A$.

::: pf-proof
The image lies in $A$ and the displayed formula is a two-sided inverse.

::: {.pf-step #F-into}
$F$ maps $\ZZ_{+}^{2}$ into $A$ and is injective.

::: pf-proof
For $(x,y)\in\ZZ_{+}^{2}$ one has $x\ge1$, so the first coordinate $x+y-1\ge y$: thus $F(x,y)\in A$. If $F(x,y)=F(x',y')$, then $y=y'$ from the second coordinates and $x+y-1=x'+y'-1$ from the first, whence $x=x'$.
:::

:::

::: {.pf-step #F-onto}
$F$ is surjective onto $A$, hence a bijection.

::: pf-proof
Let $(u,v)\in A$, so $u\ge v\ge1$. Put $x=u-v+1\ge1$ and $y=v\ge1$. Then $(x,y)\in\ZZ_{+}^{2}$ and $F(x,y)=(u-v+1+v-1,\,v)=(u,v)$. So $F$ is onto $A$, and with step [](#F-into){.pf-ref} it is a bijection.
:::

:::

:::

:::

::: {.pf-step #example-two-second}
$G(x,y)=\frac{x(x-1)}{2}+y$ is a bijection $A\to\ZZ_{+}$.

::: pf-proof
The values of $G$ on $A$ fall into consecutive blocks, one for each $x$.

::: {.pf-step #G-blocks}
For fixed $x\ge1$, as $y$ runs over $1,\dots,x$ the values $G(x,y)$ are exactly the block $\frac{x(x-1)}{2}+1,\dots,\frac{x(x+1)}{2}$.

::: pf-proof
For $1\le y\le x$ the value $G(x,y)=\frac{x(x-1)}{2}+y$ runs over those $x$ consecutive integers, increasing by $1$ each step, from $\frac{x(x-1)}{2}+1$ up to $\frac{x(x-1)}{2}+x=\frac{x(x+1)}{2}$.
:::

:::

::: {.pf-step #G-bijective}
$G$ is a bijection $A\to\ZZ_{+}$.

::: pf-proof
The block of step [](#G-blocks){.pf-ref} ends at $\frac{x(x+1)}{2}$ and the next block, for $x+1$, begins at $\frac{(x+1)x}{2}+1$, which is one more; the first block begins at $1$. So the blocks for $x=1,2,3,\dots$ are pairwise disjoint and together exhaust $\ZZ_{+}$, and within a block $G$ is strictly increasing in $y$ and injective in $x$ because distinct $x$ give distinct blocks. Hence every positive integer is the value of $G$ at exactly one point of $A$, which is the bijectivity of $G$.
:::

:::

:::

:::

:::
:::
