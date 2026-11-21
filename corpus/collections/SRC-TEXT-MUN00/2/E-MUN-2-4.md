---
schema: qual/card@1
id: E-MUN-2-4
kind: problem
title: Composition of functions and injectivity and surjectivity
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 4; the stored statement matches.
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
    Read against Munkres, Topology (2000), §2 Exercise 4, printed p. 21; parts (a)-(f)
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 2.4,
    printed pp. 15-16 (tmp/sources/munkres-solutions-whitman.pdf). His conclusions in
    (c) and (e) are the card's - injectivity of the composite forces the first map
    injective only, surjectivity forces the second surjective only - and his Theorem
    2.4.1 is the summary (f). The card's two counterexamples use {0} into {0,1} where he
    uses {1,2} into {1,2,3}; both are correct, and the card's is the smaller.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the six parts, which is what Queue D asks for on this card. Parts (b)-(e) are separate steps, the counterexample is given once in (c) and reused in (e), and (f) is the summary step, as Whitman's Theorem 2.4.1 states it. Statement re-read against Munkres, Topology (2000), §2 Exercise 4, printed p. 21; the conclusions and the summary against Dan Whitman's set, Exercise 2.4, printed pp. 15-16. The card's smaller counterexample ({0} into {0,1} with a constant map) is correct and is kept in place of his {1,2} into {1,2,3}. No statement repair.
---

::: {.exercise}

Let $f: A \to B$ and $g: B \to C$ .

(a) If $C_0 \subset C$, show that $(g \circ f)^{-1}(C_0) = f^{-1}(g^{-1}(C_0))$ .

(b) If $f$ and $g$ are injective, show that $g \circ f$ is injective.

(c) If $g \circ f$ is injective, what can you say about injectivity of $f$ and $g$ ?

(d) If $f$ and $g$ are surjective, show that $g \circ f$ is surjective.

(e) If $g \circ f$ is surjective, what can you say about surjectivity of $f$ and $g$ ?

(f) Summarize your answers to (b)-(e) in the form of a theorem.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 2.4** (`tmp/sources/munkres-solutions-whitman.pdf`); his summary of (b)--(e) is his Theorem 2.4.1, reproduced as step [](#summary){.pf-ref}, and his examples for (c) and (e) are replaced by the smaller ones below. The statement is Munkres, *Topology*, 2nd ed. (2000), §2 Exercise 4.

::: pf

::: {.pf-step #preimage}
(a) For $C_0\subset C$, $\;(g\circ f)^{-1}(C_0)=f^{-1}\bigl(g^{-1}(C_0)\bigr)$.

::: pf-proof
For $a\in A$ the following are equivalent: $a\in(g\circ f)^{-1}(C_0)$; $(g\circ f)(a)=g(f(a))\in C_0$; $f(a)\in g^{-1}(C_0)$; $a\in f^{-1}\bigl(g^{-1}(C_0)\bigr)$. Each line is the definition of a preimage, so the two sets have the same elements.
:::

:::

::: {.pf-step #comp-injective}
(b) If $f$ and $g$ are injective, then $g\circ f$ is injective.

::: pf-proof
If $g(f(a_1))=g(f(a_2))$, injectivity of $g$ gives $f(a_1)=f(a_2)$, and injectivity of $f$ gives $a_1=a_2$.
:::

:::

::: {.pf-step #composite-injective-forces-first}
(c) If $g\circ f$ is injective, then $f$ is injective; nothing follows about $g$.

::: pf-proof
If $f(a_1)=f(a_2)$ then $g(f(a_1))=g(f(a_2))$, so $a_1=a_2$ by injectivity of $g\circ f$. For the second clause, let $f:\{0\}\to\{0,1\}$ be the inclusion and $g:\{0,1\}\to\{*\}$ the constant map; then $g\circ f$ is injective because its domain is a singleton, while $g$ is not injective. So an injective composite does not force $g$ to be injective.
:::

:::

::: {.pf-step #comp-surjective}
(d) If $f$ and $g$ are surjective, then $g\circ f$ is surjective.

::: pf-proof
Given $c\in C$, surjectivity of $g$ gives $b\in B$ with $g(b)=c$, and surjectivity of $f$ gives $a\in A$ with $f(a)=b$; then $(g\circ f)(a)=c$.
:::

:::

::: {.pf-step #composite-surjective-forces-second}
(e) If $g\circ f$ is surjective, then $g$ is surjective; nothing follows about $f$.

::: pf-proof
Every $c\in C$ equals $g(f(a))$ for some $a\in A$, so $c$ is the image under $g$ of $f(a)\in B$. For the second clause, the same inclusion $f:\{0\}\to\{0,1\}$ and constant map $g:\{0,1\}\to\{*\}$ have surjective composite, since $*$ is hit, while $f$ is not surjective.
:::

:::

::: {.pf-step #summary}
(f) The theorem: the composite of injective maps is injective, and injectivity of a composite forces its first factor injective; the composite of surjective maps is surjective, and surjectivity of a composite forces its second factor surjective. Consequently the composite of bijections is a bijection, and a composite that is a bijection forces the first factor injective and the second surjective.

::: pf-proof
The four assertions about injectivity and surjectivity are steps [](#comp-injective){.pf-ref}, [](#composite-injective-forces-first){.pf-ref}, [](#comp-surjective){.pf-ref} and [](#composite-surjective-forces-second){.pf-ref}. A bijection is an injective and surjective map, so the composite of two bijections is both, hence a bijection; and if $g\circ f$ is a bijection then it is injective, so $f$ is injective, and it is surjective, so $g$ is surjective. This is part (f) and the last of the six parts.
:::

:::

:::
:::
