---
schema: qual/card@1
id: P-CH7-1
kind: problem
title: Cosets of the Klein four-subgroup in $A_4$
classification:
  areas: [algebra]
  topics:
    - Cosets and Lagrange's Theorem
relations: []
review: draft
audit:
  - event: source-checked
    by: claude-opus-5
    date: 2026-09-16
    note: Wrote the statement in math mode and added a remark that Table 5.1, which the solution's alpha labels refer to, is not in the source; page 1 of Ch7Sltns.pdf.
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      The solution was extraction residue in spaced-out notation, with no argument for why three
      cosets suffice. Rewritten as a structured proof and re-checked: $H$ is the Klein four-group
      inside $A_4$, of order $4$ in a group of order $12$, so the index is $3$ by Lagrange; and
      each product was recomputed by following the permutations from the right, giving
      $(123)H=\{(123),(134),(243),(142)\}$ and $(132)H=\{(132),(234),(124),(143)\}$, which agree
      with the card's earlier lists. Added: Lagrange's count, the disjointness of the three sets and
      their exhaustion of $A_4$, and the two sample products worked out. The remark on table 5.1's
      labels is unchanged. The statement is Gallian Chapter 7 Exercise 1; the collection's
      provenance is the textbook, so no retained solution set covers it.
  - event: source-corrected
    by: claude
    date: 2026-11-19
    note: >-
      The card said no retained solution set covers the exercise, and that is false: the collection's
      own outline is retained in this repository as `assets/attachments/Ch7Sltns.pdf`, and its
      entry "# 1" is this exercise. The rendered sentence now cites it and says what the card
      adds. Found by screening the residue's absence claims against the attachments, after two Munkres
      cards were found making the same false claim; no step of the proof changed.
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      Read in the retained scan `tmp/sources/Gallian-Contemporary-Abstract-Algebra-7e.pdf`: the left
      cosets of the Klein four-subgroup in $A_4$ are Chapter 7 Exercise 1, printed p. 149 (page 163 of
      the file, whose running head is p. 149). The printed words are the card's statement, and the
      number the card already carried is the book's. The page is now named in the solution's opening
      sentence. Not checked in this pass: the proof, which the edit does not touch.
---

::: {.problem}
Let $H = \{(1), (12)(34), (13)(24), (14)(23)\}$. Find the left cosets of $H$ in $A_4$ (using table 5.1).
:::

::: {.solution}
The collection retains its solution outline as `assets/attachments/Ch7Sltns.pdf`, whose entry "# 1" is this exercise and lists the same three cosets. In the seventh edition the exercise is printed as **Chapter 7 Exercise 1 on p. 149**, where the printed words are the card's statement; the outline and the book number it the same. The card verifies each product and the exhaustion of $A_4$, and the wording below is its own. Write $H=\{(1),(12)(34),(13)(24),(14)(23)\}$.

::: pf

::: {.pf-step #index}
$H$ is a subgroup of $A_4$ of order $4$, so it has exactly three left cosets, and they partition $A_4$.

::: pf-proof
$H$ consists of the identity and the three elements of cycle type $2+2$, all of which are even, so $H\subseteq A_4$; it is closed under multiplication and inverses, being the Klein four-group. $\abs{A_4}=\frac{1}{2}\cdot 4!=12$ and $\abs{H}=4$, so by Lagrange's theorem the index is $12/4=3$, and the left cosets of a subgroup partition the group.
:::

:::

::: {.pf-step #coset-one}
$(123)H=\{(123),(134),(243),(142)\}$.

::: pf-proof
Multiply $(123)$ on the left by each element of $H$ in turn:
$$
(123)(1)=(123),\quad (123)(12)(34)=(134),\quad (123)(13)(24)=(243),\quad (123)(14)(23)=(142),
$$
each product computed by following the two permutations from the right; for instance $(123)(12)(34)$ sends $1\mapsto2\mapsto3$, $3\mapsto4\mapsto4$, $4\mapsto3\mapsto1$ and $2\mapsto1\mapsto2$, which is the cycle $(134)$. The four products are distinct, as they must be, left multiplication being injective.
:::

:::

::: {.pf-step #coset-two}
$(132)H=\{(132),(234),(124),(143)\}$.

::: pf-proof
Similarly,
$$
(132)(1)=(132),\quad (132)(12)(34)=(234),\quad (132)(13)(24)=(124),\quad (132)(14)(23)=(143).
$$
For example $(132)(13)(24)$ sends $1\mapsto3\mapsto2$, $2\mapsto4\mapsto4$, $4\mapsto2\mapsto1$ and $3\mapsto1\mapsto3$, which is the cycle $(124)$.
:::

:::

::: {.pf-step}
$\boxed{H\cup(123)H\cup(132)H=A_4}$, so the left cosets of $H$ in $A_4$ are $H$, $(123)H$ and $(132)H$.

::: pf-proof
By step [](#index){.pf-ref} the left cosets number three and partition the $12$ elements of $A_4$; steps [](#coset-one){.pf-ref} and [](#coset-two){.pf-ref} exhibit two of them besides $H$, each of four elements, and the displayed four sets are pairwise distinct — $H$ contains $(1)$, and the two others contain only $3$-cycles with, respectively, starting letter $1$ and starting letter $1$ reversed, so no element occurs twice. Twelve elements in three disjoint sets of four exhaust $A_4$.
:::

:::

:::
:::

::: {.remark}
The labels $\alpha_1, \ldots, \alpha_{12}$ are the names of the elements of $A_4$ in table 5.1 of the textbook.
:::
