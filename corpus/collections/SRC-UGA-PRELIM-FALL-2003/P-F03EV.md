---
schema: qual/card@1
id: P-F03EV
kind: problem
title: Eigenvectors for distinct eigenvalues are linearly independent
classification:
  areas:
  - prelim
  topics:
  - Eigenvalues
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
    Restructured as a Lamport proof of the same two parts, with the one hypothesis the statement leaves
    implicit made explicit: the scalars must form a field, since the elimination step divides by the
    nonzero scalar mu - lambda, and over a ring with zero divisors the conclusion can fail. The definition
    of part (a) is also given in its kernel form, which is what the rest of the argument uses. No published
    solution located; the card keeps its own argument and says so.
---

::: {.problem}
Let $A$ be an $n \times n$ matrix.

a) Define what is meant by the eigenvalues and eigenvectors of $A$.

b) Show that if $v$ and $w$ are eigenvectors of $A$ corresponding to distinct eigenvalues $\lambda$ and $\mu$, then $v$ and $w$ are linearly independent.
:::

::: {.solution}

No published solution was located for this preliminary examination problem; the argument is the card's own and is the standard one-line elimination.

The statement was checked against the Fall 2003 UGA preliminary examination collection holding this card. Throughout $A$ is an $n\times n$ matrix with entries in a field $K$ --- the field hypothesis is what makes $\mu-\lambda$ invertible for distinct $\lambda,\mu$, and the argument below uses exactly that --- and a vector is an element of $K^{n}$.

::: pf

::: {.pf-step #definition}

(a) A scalar $\lambda\in K$ is an *eigenvalue* of $A$ when $Av=\lambda v$ for some nonzero $v\in K^{n}$, and such a nonzero $v$ is an *eigenvector* of $A$ belonging to $\lambda$.

::: pf-proof

This is the definition the part asks for. Equivalently, $\lambda$ is an eigenvalue exactly when $\ker(A-\lambda I)\neq\theset{0}$, the nonzero vectors of that kernel being the eigenvectors belonging to $\lambda$.

:::

:::

::: {.pf-step #b}

(b) If $v$ and $w$ are eigenvectors of $A$ belonging to distinct eigenvalues $\lambda\neq\mu$, then $v$ and $w$ are linearly independent.

:::: pf-proof

Let $av+bw=0$ be a linear relation and show both coefficients vanish.

::: {.pf-step #data}

$v\neq0$, $w\neq0$, $Av=\lambda v$ and $Aw=\mu w$.

::: pf-proof

A vector is an eigenvector only if it is nonzero, and the eigenvalue equations are the hypothesis of the part.

:::

:::

::: {.pf-step #applied}

If $av+bw=0$ with $a,b\in K$, then $a\lambda v+b\mu w=0$.

::: pf-proof

Apply $A$ to the relation $av+bw=0$ and use linearity together with the eigenvalue equations: $0=A(av+bw)=aAv+bAw=a\lambda v+b\mu w$.

:::

:::

::: {.pf-step #eliminate}

$b(\mu-\lambda)w=0$, hence $b=0$.

::: pf-proof

Subtract $\lambda$ times $av+bw=0$ from $a\lambda v+b\mu w=0$: the $v$-terms cancel and leave $b(\mu-\lambda)w=0$. Since $\mu\neq\lambda$ the scalar $\mu-\lambda$ is nonzero, and in a field every nonzero element is invertible; multiplying by its inverse gives $bw=0$, and $w\neq0$ forces $b=0$.

:::

:::

::: {.pf-step #coefficient}

$a=0$.

::: pf-proof

With $b=0$ the relation $av+bw=0$ reads $av=0$, and $v\neq0$ gives $a=0$.

:::

:::

::: pf-step

The only linear relation between $v$ and $w$ has both coefficients zero, so they are linearly independent.

::: pf-proof

Steps [](#eliminate){.pf-ref} and [](#coefficient){.pf-ref} show that any $a,b$ with $av+bw=0$ satisfy $a=b=0$, which is the definition of linear independence for the pair.

:::

:::

::::

:::

::: pf-step

Both parts hold.

::: pf-proof

Part [](#definition){.pf-ref} gives the definitions asked for in (a), and part [](#b){.pf-ref} the independence of eigenvectors belonging to distinct eigenvalues, which is (b).

:::

:::

:::

:::
