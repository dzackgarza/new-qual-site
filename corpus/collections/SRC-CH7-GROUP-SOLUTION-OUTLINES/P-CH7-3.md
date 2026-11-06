---
schema: qual/card@1
id: P-CH7-3
kind: problem
title: Cosets of $3\ZZ$ in $\ZZ$
classification:
  areas: [algebra]
  topics:
    - Cosets and Lagrange's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Gallian, Contemporary Abstract Algebra, seventh edition (2010),
    Chapter 7, Cosets and Lagrange's Theorem, exercise 3, printed page 149 (PDF
    page 164 of tmp/sources/Gallian-Contemporary-Abstract-Algebra-7e.pdf,
    untracked). The printed exercise reads: "Let H = {0, +-3, +-6, +-9, ...}.
    Find all the left cosets of H in Z." The card states exactly this and the
    index locator, exercise 3, is the printed number.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The card carried the list H, 1 + H, 2 + H with a parenthetical appeal to the
    division algorithm and no proof that the list is complete or that the three
    cosets are distinct. The solution written here establishes both: the
    division algorithm puts every integer in one of the three cosets, and any
    two of 0, 1, 2 differ by less than 3 so their cosets cannot coincide.
---

::: {.problem}
Let $H = \{0, \pm 3, \pm 6, \pm 9, \ldots\}$. Find all the left cosets of $H$ in $\ZZ$.
:::

::: {.solution}

$H=3\ZZ$, and the left cosets are $H$, $1+H$ and $2+H$.

::: pf

::: {.pf-step #h-is-3z}

$H=\{0,\pm3,\pm6,\dots\}=3\ZZ$ is a subgroup of $\ZZ$.

::: pf-proof

$H$ is the set of integer multiples of $3$, it contains $0$, and the difference
of two multiples of $3$ is a multiple of $3$, so $H$ is a subgroup of the
additive group $\ZZ$ (the one-step subgroup test).

:::

:::

::: {.pf-step #complete}

Every integer lies in $H$, $1+H$ or $2+H$.

::: pf-proof

By the division algorithm, for $a\in\ZZ$ there are $q$ and $r$ with
$a=3q+r$ and $0\le r<3$, so $r\in\{0,1,2\}$ and $3q\in H$. Hence
$a\in r+H\subseteq\{H,1+H,2+H\}$. So these three cosets cover $\ZZ$.

:::

:::

::: {.pf-step #distinct}

The three cosets are distinct.

::: pf-proof

Suppose $r+H=r'+H$ with $r,r'\in\{0,1,2\}$ and $r\neq r'$. Then
$r'-r\in H$, so $r'-r=3k$ for some integer $k$. But $0<|r'-r|\le 2$, and no
nonzero integer of absolute value at most $2$ is a multiple of $3$. So
$r=r'$, and the three cosets are pairwise different. Together with step
[](#complete){.pf-ref} this gives exactly the three left cosets $H$, $1+H$,
$2+H$.

:::

:::

:::

:::
