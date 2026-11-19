---
schema: qual/card@1
id: P-IMVV7
kind: problem
title: 'Permutations, combinations, and the number of injections from a $k$-set to an $n$-set'
classification:
  areas:
    - prelim
  topics:
    - Combinatorics
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Structured the definitions and counts into numbered steps. The three counts are now derived
      rather than stated: the multiplication principle for the ordered list of a permutation, the
      division by k! because each k-element subset has exactly k! orderings, and the bijection
      between injections and ordered lists of k distinct elements of the codomain. No source text is
      retained for this preliminary examination, so the statement is the one stored and nothing was
      checked against a printed page.
---

::: {.problem}
Let $k$ and $n$ be positive integers with $k \le n$.
Give the definitions for the permutations and for the combinations of $k$ elements from an $n$-element set, and state formulas for the numbers of these.
Derive a formula for the number of one-to-one functions from a $k$-element set to an $n$-element set.
:::

::: {.solution}

The definitions and the argument are the card's own; the card is an examination problem and no source text or solution set is retained for it.

Throughout $k$ and $n$ are positive integers with $k\leq n$, and sets are finite.

::: pf

::: {.pf-step #perm}
A permutation of $k$ elements chosen from an $n$-element set is an ordered list of $k$ distinct elements of it, and their number is $P(n,k)=n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}$.

::: pf-proof
An ordered list $(y_{1},\dots,y_{k})$ of distinct elements is built by choosing $y_{1}$ in $n$ ways, then $y_{2}$ among the $n-1$ elements left, and so on, down to $y_{k}$ with $n-k+1$ choices; the multiplication principle gives the product. The product equals $\frac{n!}{(n-k)!}$ because $n!=n(n-1)\cdots(n-k+1)\cdot(n-k)!$.
:::

:::

::: {.pf-step #comb}
A combination of $k$ elements from an $n$-element set is a $k$-element subset, and their number is $\binom{n}{k}=\frac{n!}{k!\,(n-k)!}$.

::: pf-proof
Each $k$-element subset $S$ gives exactly $k!$ ordered lists of its elements, by step [](#perm){.pf-ref} with $n=k$, and every ordered list of $k$ distinct elements arises from exactly one subset. So $P(n,k)=k!\binom{n}{k}$, giving $\binom{n}{k}=P(n,k)/k!=\frac{n!}{k!(n-k)!}$.
:::

:::

::: {.pf-step #injections}
The number of injective functions from a $k$-element set $X$ to an $n$-element set $Y$ is $\frac{n!}{(n-k)!}$.

::: pf-proof
Fix an ordering $x_{1},\dots,x_{k}$ of $X$. A function $f\colon X\to Y$ is determined by the tuple $\bigl(f(x_{1}),\dots,f(x_{k})\bigr)$, and $f$ is injective exactly when the entries of that tuple are distinct: if two entries agree then two distinct points have the same image, and conversely distinct images at distinct points give injectivity. The map $f\mapsto\bigl(f(x_{1}),\dots,f(x_{k})\bigr)$ is therefore a bijection from the set of injections onto the set of ordered lists of $k$ distinct elements of $Y$, whose number is $P(n,k)$ by step [](#perm){.pf-ref}. Hence the number of injections is $P(n,k)=\frac{n!}{(n-k)!}$.
:::

:::

::: {.pf-step}
The three answers are $P(n,k)=n!/(n-k)!$ for permutations, $\binom{n}{k}=n!/(k!(n-k)!)$ for combinations, and $n!/(n-k)!$ for injective functions.

::: pf-proof
Steps [](#perm){.pf-ref}, [](#comb){.pf-ref} and [](#injections){.pf-ref}; the third count coincides with the first, as it must, an injective function from a $k$-element set being the same thing as an ordered list of $k$ distinct images.
:::

:::

:::

:::
