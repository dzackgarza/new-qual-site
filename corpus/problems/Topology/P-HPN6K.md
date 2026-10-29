---
schema: qual/card@1
id: P-HPN6K
kind: problem
title: Open and closed subsets of $\RR$; $\RR^n\not\cong\RR$; closure of a product
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Closure
  - Homeomorphisms
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source (Topology Week 1 Preliminaries workshop sheet) lists the five sets under 'Determine if the following subsets of R are opened, closed, both, or neither'; that lead-in was lost, and the title was the first list item. The lead-in is restored, and n in Z^{>=0} in the sets 1/n is corrected to n >= 1, since 1/0 is undefined."
---

::: {.problem}
(a) Determine whether each of the following subsets of $\RR$ is open, closed, both, or neither:

- $\ZZ$;
- $\theset{1}$;
- $\theset{p \in \ZZ^{\geq 0} \st p\text{ is prime}}$;
- $\theset{ {1\over n} \st n\in \ZZ^{\geq 1}}$;
- $\theset{ {1\over n} \st n\in \ZZ^{\geq 1}} \union \theset{0}$.

(b) Prove that $\RR^n$ is not homeomorphic to $\RR$ for any $n\geq 2$.

(c) Is it true that the closure of a product is the product of the closures?
:::

::: {.solution}

::: pf

::: pf-step

(a) The sets $\ZZ$, $\theset{1}$, the primes, and $\theset{1/n}\cup\theset{0}$ are closed and not open; the set $\theset{1/n \st n\ge1}$ is neither open nor closed.

::: pf-proof

None of the five sets is open, because each is nonempty and contains no interval.
A subset $S\subseteq\RR$ with no accumulation point in $\RR$ is closed. The sets $\ZZ$, $\theset{1}$, and the primes are subsets of $\ZZ$, any two of whose points are at distance at least $1$, so a bounded interval meets them in finitely many points and they have no accumulation points.
The only accumulation point of $\theset{1/n \st n\ge1}$ is $0$, because $1/n\to0$ and every interval around a point $x\ne0$ of length less than $\abs{x}/2$ contains finitely many $1/n$. Hence $\theset{1/n}\cup\theset{0}$ contains all its accumulation points and is closed, while $\theset{1/n}$ misses the accumulation point $0$ and is not closed.

:::

:::

::: pf-step

(b) For every $n\ge2$, $\RR^n$ is not homeomorphic to $\RR$.

::: pf-proof

If $h:\RR^n\to\RR$ were a homeomorphism, then deleting any point $x$ would give a homeomorphism $\RR^n\setminus\{x\}\cong\RR\setminus\{h(x)\}$. For $n\ge2$, $\RR^n\setminus\{x\}$ is path-connected, while $\RR\setminus\{h(x)\}$ has two connected components, a contradiction.

:::

:::

::: pf-step

(c) Yes: for arbitrary subsets $A\subseteq X$ and $B\subseteq Y$,
$$\boxed{\overline{A\times B}^{\,X\times Y}=\overline A^{\,X}\times\overline B^{\,Y}.}$$

::: pf-proof

If $(x,y)$ lies in the left closure, continuity of the projections gives $x\in\overline A$ and $y\in\overline B$. Conversely, if $x\in\overline A$ and $y\in\overline B$, every basic neighborhood $U\times V$ of $(x,y)$ meets $A\times B$ because $U\cap A\ne\varnothing$ and $V\cap B\ne\varnothing$.

:::

:::

:::

:::
