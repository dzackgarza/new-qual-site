---
schema: qual/card@1
id: P-KOSSD
kind: problem
title: A normal subgroup of coprime order and index is the unique subgroup of that
  order
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Sixteen steps asserted their claim with no
    justification and the card is now three steps each deriving its claim. The first takes Bézout's identity
    for the coprime pair $(n, m) = (\cardinality{N}, [G:N])$, noting that $G/N$ is a group of order $[G:N]$
    because $N$ is normal. The second proves that a subgroup $K$ of order $n$ lies in $N$: Lagrange in $K$
    gives $x^n = e$, Lagrange in $G/N$ gives $x^m \in N$, and $ns + mt = 1$ writes $x = (x^m)^t$, which is in
    $N$ since a subgroup is closed under powers; the integer exponents, which may be negative, are the point
    the card had left implicit. The third concludes $K = N$ from the inclusion and the equality of finite
    cardinalities, which is the uniqueness. The four-step Bézout argument, the nine fragments of the
    containment argument and the three fragments of the equality argument are gone, the display that sat
    between a step and the closing fences now stands inside its proof, and the closing pf-qed, which only
    named the step that answers the question, is removed. Sources are cited by numbered statement:
    Bézout's identity, Lagrange's theorem, and the definition of the index as the order of the quotient.
    No page reference is written in the body of this card or in the event above. The statement is
    unchanged. The collection retains the UGA algebra qualifying exam of Spring 2020 and no solution
    sheet, so the argument is the card's own.
---
::: {.problem}
Let $N$ be a normal subgroup of a finite group $G$ such that the order of $N$ and the index of $N$ in $G$ are relatively prime ($\gcd(\cardinality{N}, [G : N]) = 1$).

Prove that $N$ is the unique subgroup of $G$ of order $\cardinality{N}$.
:::

::: {.solution}

::: pf

::: {.pf-step #bezout}

There are integers $s, t$ with $\cardinality{N}s + [G:N]t = 1$.

::: pf-proof
Since $N \trianglelefteq G$ the quotient $G/N$ is a group, of order $[G:N] = \cardinality{G/N}$. With $n = \cardinality{N}$ and $m = [G:N]$, the hypothesis is $\gcd(n,m) = 1$, and Bézout's identity for a coprime pair of integers supplies $s, t \in \ZZ$ with $ns + mt = 1$.
:::

:::

::: {.pf-step #containment}

Every subgroup $K \leq G$ with $\cardinality{K} = \cardinality{N}$ is contained in $N$.

::: pf-proof
Let $n = \cardinality{N}$ and $m = [G:N]$, so $ns + mt = 1$ by the preceding step, and let $K \le G$ have $\cardinality{K} = n$. For $x \in K$ Lagrange's theorem in the group $K$ makes the order of $x$ divide $\abs{K} = n$, so $x^n = e$; and Lagrange's theorem in $G/N$ makes the order of the coset $xN$ divide $\abs{G/N} = m$, so $(xN)^m = x^m N$ is the identity coset $N$, that is $x^m \in N$. Since $ns + mt = 1$ with $s, t \in \ZZ$,
$$x = x^1 = x^{ns+mt} = (x^n)^s\,(x^m)^t = e\,(x^m)^t = (x^m)^t,$$
and $(x^m)^t \in N$ because $x^m \in N$ and $N$ is closed under powers. Hence $x \in N$; since $x$ was an arbitrary element of $K$, the inclusion $K \subseteq N$ follows.
:::

:::

::: {.pf-step #equality}

Every subgroup $K$ of order $\cardinality{N}$ equals $N$, so $N$ is the unique subgroup of that order.

::: pf-proof
Let $K \le G$ have $\cardinality{K} = \cardinality{N} = n$. The preceding step gives $K \subseteq N$, and $n$ is finite, so a subset of $N$ with as many elements as $N$ is all of $N$. Hence $K = N$, and every subgroup of order $n$ is that one subgroup.
:::

:::

:::
:::
