---
schema: qual/card@1
id: E-MUN-5-4
kind: problem
title: Bijections between finite and countable product spaces
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 4; restored part (f) to the printed map X^A -> X^B for A subset B.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (f) did not say what the retained printing says. Munkres, Topology (2000), §5
    Exercise 4(f), printed p. 39, reads "If A is a subset of B, find an injective map
    m : (A^omega)^n -> B^omega", read on the page image as well as in the text layer.
    The card stated instead "m : X^A -> X^B", and its earlier note called that the
    printed map. Dan Whitman's manual (printed p. 71) records why both readings exist:
    the older printings say X^A -> X^B, which the text never defines, and the printing
    retained here was changed. The statement now follows the retained printing; the
    older reading is recorded here rather than silently dropped.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 5.4,
    printed pp. 71-73 (tmp/sources/munkres-solutions-whitman.pdf). Parts (a)-(e) are his.
    Part (f) now proves the map the retained printing asks for: interleave the n
    sequences x_1, ..., x_n by the bijection k = (j-1)n + i between Z_+ and
    Z_+ x {1, ..., n}; injectivity is that bijection's uniqueness. The previous proof of
    the X^A -> X^B reading, which padded with a chosen point, is superseded.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the six constructions, which is what Queue D asks for on this card. Each part is a step: the injective ones are justified by reading back the coordinates the construction preserves, the bijective ones by exhibiting the inverse as a splitting or an interleaving, and part (f) carries the division-algorithm argument that makes its index map well defined as well as injective. The choice of the padding point x_0 is made in prose before the proof, as it is used in three parts. Statement re-read against Munkres, Topology (2000), §5 Exercise 4, printed p. 39, and the six constructions against Dan Whitman's set, Exercise 5.4, printed pp. 71-73. No statement repair.
---

::: {.exercise}

Let $m, n \in \ZZ_{+}$ . Let $X \neq \varnothing$ .

(a) If $m \leq n$, find an injective map $f: X^m \to X^n$ .

(b) Find a bijective map $g: X^m \times X^n \to X^{m+n}$ .

(c) Find an injective map $h: X^n \to X^\omega$ .

(d) Find a bijective map $k: X^n \times X^\omega \to X^\omega$ .

(e) Find a bijective map $l: X^{\omega} \times X^{\omega} \to X^{\omega}$ .

(f) If $A \subset B$, find an injective map $m: (A^{\omega})^{n} \to B^{\omega}$ .
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.4, printed pp. 71--73** (`tmp/sources/munkres-solutions-whitman.pdf`); the six constructions are his, part (f) being the interleaving he writes with the division algorithm. The statement is Munkres, *Topology*, 2nd ed. (2000), §5 Exercise 4, printed p. 39.

Choose once and for all a point $x_0\in X$, which exists because $X\ne\varnothing$.

::: pf

::: {.pf-step #part-a}
(a) If $m\le n$, the map $f:X^m\to X^n$ with $f(x_1,\dots,x_m)=(x_1,\dots,x_m,x_0,\dots,x_0)$, the last $n-m$ coordinates equal to $x_0$, is injective.

::: pf-proof
The first $m$ coordinates of $f(x)$ are $x$ again, so $f(x)=f(x')$ gives $x=x'$; the padding coordinates are irrelevant to that reading.
:::

:::

::: {.pf-step #part-b}
(b) Concatenation, $g\bigl((x_1,\dots,x_m),(y_1,\dots,y_n)\bigr)=(x_1,\dots,x_m,y_1,\dots,y_n)$, is a bijection $X^m\times X^n\to X^{m+n}$.

::: pf-proof
Its inverse is the map that splits an $(n+m)$-tuple $z$ after its $m$-th coordinate, sending $z$ to $\bigl((z_1,\dots,z_m),(z_{m+1},\dots,z_{m+n})\bigr)$; the two composites are the identities on $X^m\times X^n$ and on $X^{m+n}$ respectively.
:::

:::

::: {.pf-step #part-c}
(c) The map $h:X^n\to X^\omega$ with $h(x_1,\dots,x_n)=(x_1,\dots,x_n,x_0,x_0,\dots)$ is injective.

::: pf-proof
The first $n$ coordinates of $h(x)$ are the entries of $x$, so $h(x)=h(x')$ implies $x=x'$.
:::

:::

::: {.pf-step #part-d}
(d) The map $k\bigl((x_1,\dots,x_n),(y_1,y_2,\dots)\bigr)=(x_1,\dots,x_n,y_1,y_2,\dots)$ is a bijection $X^n\times X^\omega\to X^\omega$.

::: pf-proof
Its inverse sends a sequence $z\in X^\omega$ to the pair consisting of $(z_1,\dots,z_n)$ and the tail $(z_{n+1},z_{n+2},\dots)$; both composites are identities, so $k$ is bijective.
:::

:::

::: {.pf-step #part-e}
(e) The interleaving $l\bigl((x_1,x_2,\dots),(y_1,y_2,\dots)\bigr)=(x_1,y_1,x_2,y_2,\dots)$ is a bijection $X^\omega\times X^\omega\to X^\omega$.

::: pf-proof
Its inverse sends $z\in X^\omega$ to the pair of its odd-indexed and even-indexed terms, $(z_1,z_3,z_5,\dots)$ and $(z_2,z_4,z_6,\dots)$; the two composites are the identities on the respective products, so $l$ is bijective.
:::

:::

::: {.pf-step #part-f}
(f) For $A\subset B$ the map $m:(A^\omega)^n\to B^\omega$ defined by $m(x)_k=x_i(j)$, where $k=(j-1)n+i$ with $i\in\{1,\dots,n\}$ and $j\in\ZZ_+$, is injective.

::: pf-proof
Every $k\in\ZZ_+$ has exactly one such expression: dividing $k-1$ by $n$ gives a quotient $j-1\ge0$ and a remainder $i-1$ with $0\le i-1<n$, so $j\in\ZZ_+$ and $i\in\{1,\dots,n\}$, and both are determined by $k$. Hence $m(x)$ is a well-defined sequence, and each of its terms $x_i(j)$ lies in $A\subset B$, so $m(x)\in B^\omega$. If $x\ne x'$, then $x_i\ne x'_i$ for some $i$, so $x_i(j)\ne x'_i(j)$ for some $j$, and at the index $k=(j-1)n+i$ the sequences $m(x)$ and $m(x')$ differ. So $m$ is injective, and the six constructions are (a)--(f).
:::

:::

:::
:::
