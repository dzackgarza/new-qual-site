---
schema: qual/card@1
id: P-5YZPH
kind: problem
title: A $p$-subgroup acting on the cosets of a Sylow $p$-subgroup has a length-one
  orbit iff it lies in a conjugate
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, with the two facts the prose used
    silently now stated: that the left multiplication h . xP = hxP is an action, so that the
    orbit-stabilizer theorem applies, and that p does not divide [G:P] because P is a Sylow
    p-subgroup. Checked the equivalence chain in the second part: hxP = xP iff x^{-1}hx P = P iff
    x^{-1}hx in P, and conjugating x^{-1}Hx contained in P gives H contained in xPx^{-1}. The
    statement is unchanged, including its two parts and the left-translation wording; the card
    says the argument is its own.
---

::: {.problem}
Let $G$ be a finite group, $H$ a $p\dash$subgroup, and $P$ a Sylow $p\dash$subgroup for $p$ a prime.
Let $H$ act on the left cosets of $P$ in $G$ by left translation.

Prove that there is an orbit under this action of length 1.

Prove that $xP$ is an orbit of length 1 $\iff H$ is contained in $xP\inverseof{x}$.
:::

::: {.solution}
The number of cosets $[G:P]$ is prime to $p$, while every $H$-orbit is $[H:H_{xP}]$, a power of $p$; so the orbits of size $>1$ contribute a multiple of $p$ and at least one orbit must have size $1$. A coset $xP$ is fixed by all of $H$ exactly when $x^{-1}Hx\le P$. The argument is this card's own: the checkout retains no solution set for this exam.

::: pf

::: {.pf-step #count}
$\abs{G/P}=[G:P]$ is not divisible by $p$.

::: pf-proof
$P$ is a Sylow $p$-subgroup, so $p\nmid[G:P]$: writing $\abs G=p^am$ with $p\nmid m$, one has $\abs P=p^a$ and $[G:P]=m$.
:::

:::


::: {.pf-step #orbits}
The left action of $H$ on $X=G/P$ has orbits of size $[H:H_{xP}]$, each a power of $p$.

::: pf-proof
For $xP\in X$ the stabilizer is $H_{xP}=\{h\in H:hxP=xP\}$, a subgroup of $H$, and the orbit-stabilizer theorem gives $\abs{H\cdot xP}=[H:H_{xP}]$. Since $H$ is a $p$-subgroup, $\abs H$ is a power of $p$, and so is every divisor of it, that is, every index $[H:H_{xP}]$. (The action is by left multiplication, $h\cdot xP=hxP$, and $h_1(h_2xP)=(h_1h_2)xP$ with $exP=xP$, so it is an action.)
:::

:::


::: {.pf-step #exist}
There is an orbit of length $1$.

::: pf-proof
$X$ is the disjoint union of its orbits, so $\abs X$ is the sum of the orbit sizes. By step [](#orbits){.pf-ref} each orbit size is a power of $p$, so each orbit of size $>1$ is divisible by $p$. If no orbit had size $1$, then $\abs X$ would be a sum of terms each divisible by $p$, hence divisible by $p$, contradicting step [](#count){.pf-ref}. Therefore some orbit has size $1$.
:::

:::


::: {.pf-step #fixpoint}
For a coset $xP$, $xP$ has orbit of length $1$ if and only if $H\subseteq xPx^{-1}$.

::: pf-proof
The orbit of $xP$ has length $1$ exactly when $h\cdot xP=xP$ for every $h\in H$, that is $hxP=xP$ for all $h$. Now $hxP=xP$ if and only if $x^{-1}hxP=P$, i.e. $x^{-1}hx\in P$, since $P$ is a subgroup and $gP=P$ is equivalent to $g\in P$. So the condition is $x^{-1}hx\in P$ for every $h\in H$, which says $x^{-1}Hx\subseteq P$. Conjugating by $x$ gives $H\subseteq xPx^{-1}$, using that conjugation is an automorphism and $(x^{-1})^{-1}=x$.
:::

:::


::: {.pf-step #conclusion}
Both assertions of the problem hold.

::: pf-proof
Step [](#exist){.pf-ref} gives an orbit of length $1$, and step [](#fixpoint){.pf-ref} identifies the cosets with orbit of length $1$ as those with $H\subseteq xPx^{-1}$; together these are the two claims.
:::

:::

:::
:::
