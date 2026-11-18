---
schema: qual/card@1
id: E-CFNT7
kind: problem
title: Countable unions in Baire spaces
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: "Solutions to exercises for Mathematics 205A" (University
    of California, Riverside, Fall 2014), Part 3, section "III.3: Implications of completeness", answer to
    Munkres §48 Exercise 1 (printed p. 298) on the set's own printed p. 6 (in tmp/sources/munkres-solutions-ucr-math205-gentop.pdf,
    PDF p. 47; the file names no author, so the course and the file are the attribution). Checked against
    Munkres, Topology (2000), §48 Exercise 1, printed p. 298, with the definition of a Baire space and of a
    nowhere dense set in §48: the answer is the set's one sentence, that if the interior of the closure of each
    B_n were empty then each B_n would be nowhere dense and X would be of the first category. The card writes
    the same argument, adding the observation that the union of the closures is X because the B_n cover X, and
    the nonemptiness of X is what makes the open set X itself the witness required by the definition. Nothing
    needed correction.
---

::: {.exercise}

Let $X$ equal the countable union $\bigcup B_n$.
Show that if $X$ is a nonempty Baire space, at least one of the sets $\overline{B}_n$ has a nonempty interior.
:::

::: {.solution}

The argument is that of the retained set **"Yougi", *Munkres Chapter 8* (2025), §48 Exercise 1** (`tmp/sources/yougi-2025-munkres-chapter-8.md`), which states the same three lines; the intermediate identifications it compresses are written out below. The card's earlier prose carried no citation, so this one is added. The statement was checked against Munkres, *Topology* (2000), §48 Exercise 1, printed p. 298, with the definition of a Baire space on printed p. 295. Closures and interiors are taken in $X$.

::: pf

::: {.pf-step #union-of-closures}
$\bigcup_{n}\overline{B_{n}}=X$.

:::: pf-proof

::: {.pf-step #inclusions}
$X\subset\bigcup_{n}\overline{B_{n}}$ and $\bigcup_{n}\overline{B_{n}}\subset X$.

::: pf-proof
Each $B_{n}$ is contained in its closure, so $X=\bigcup_{n}B_{n}\subset\bigcup_{n}\overline{B_{n}}$. Conversely each $\overline{B_{n}}$ is a closed subset of $X$ containing $B_{n}\subset X$; a closure in $X$ of a subset of $X$ lies in $X$, so the union lies in $X$.
:::

:::

::: {.pf-step}
The two inclusions of step [](#inclusions){.pf-ref} give the equality.

::: pf-proof
Two sets, each contained in the other, are equal.
:::

:::

::::

:::

::: {.pf-step #supposition}
Suppose, for contradiction, that every $\overline{B_{n}}$ has empty interior in $X$.

::: pf-proof
This is the negation of the conclusion, which asserts that some $\overline{B_{n}}$ has a nonempty interior.
:::

:::

::: {.pf-step #empty-interior}
Under the supposition of step [](#supposition){.pf-ref} the union $\bigcup_{n}\overline{B_{n}}$ has empty interior in $X$.

::: pf-proof
Each $\overline{B_{n}}$ is closed in $X$ and, by the supposition, has empty interior; the defining condition of a Baire space (§48, printed p. 295) is that the union of any countable collection of closed sets with empty interior has empty interior, and $\theset{\overline{B_{n}}}$ is such a collection.
:::

:::

::: {.pf-step #nonempty-interior}
$\bigcup_{n}\overline{B_{n}}$ has interior $X$, which is nonempty.

::: pf-proof
By step [](#union-of-closures){.pf-ref} the union is $X$. A space is open in itself, so $X$ is an open subset of $X$ contained in $X$, and the interior of $X$ in $X$, being the union of all open subsets of $X$ contained in $X$, contains $X$ and hence equals $X$. The hypothesis says $X$ is nonempty, so this interior is not the empty set.
:::

:::

::: pf-step
Therefore some $\overline{B_{n}}$ has a nonempty interior.

::: pf-proof
Step [](#empty-interior){.pf-ref} says the union has empty interior under the supposition of step [](#supposition){.pf-ref}, while step [](#nonempty-interior){.pf-ref} says its interior is the nonempty set $X$; this is a contradiction, so the supposition is false and at least one $\overline{B_{n}}$ has nonempty interior.
:::

:::

:::

:::
