---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-10
kind: problem
title: 'A continuous real function cannot take every value exactly twice'
classification:
  areas:
  - real-analysis
  topics:
  - continuity
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
([KRD10, 5.6.H]) Show that a continuous function $f:\mathbb R\to\mathbb R$ cannot take on every real value exactly twice.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Suppose, toward a contradiction, that every real value is taken exactly twice.
<1>2. Pick two preimages of one value.
Proof: fix any $x_0$; let $a < b$ be the two points with $f(a) = f(b) = f(x_0)$ (exactly two exist by assumption).
<1>3. On $[a,b]$, $f$ attains a maximum $M$ at some $x^* \in [a,b]$ and a minimum $m$ at $x_* \in [a,b]$ (extreme value theorem).
<1>4. $M$ is attained only at $a$ and $b$ (or $f \equiv f(a)$, impossible).
Proof: if $x^* \in (a,b)$ and $M > f(a)$, then for every $y \in (f(a), M)$, the intermediate value theorem gives a preimage of $y$ in $(a, x^*)$ and another in $(x^*, b)$ — at least two preimages of $y$ inside $(a,b)$, so exactly two, both in $(a,b)$, for uncountably many $y$.
Now consider $y = f(a)$: by IVT on $[x^*, b]$ (since $f(x^*) = M > f(a) = f(b)$), there is $z \in (x^*, b)$ with $f(z) = f(a)$, giving three preimages $a, z, b$ of $f(a)$ — contradiction.
Hence either $M = f(a)$ or $x^* \in \{a, b\}$; in either case $f \le f(a)$ on $[a,b]$, with $f(a)$ attained at $a, b$ and nowhere in $(a,b)$ (else a third preimage).
<1>5. By symmetry, the minimum is $m = f(a)$ as well.
Proof: applying <1>4 to $-f$ (or repeating the argument with min), $f \ge f(a)$ on $[a,b]$.
<1>6. Contradiction.
Proof: <1>4 gives $f \le f(a)$ on $[a,b]$ and <1>5 gives $f \ge f(a)$ on $[a,b]$; hence $f \equiv f(a)$ on $[a,b]$, so the value $f(a)$ is taken uncountably many times — contradicting "exactly twice".
<1>7. Q.E.D.
:::
