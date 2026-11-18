---
schema: qual/card@1
id: E-F46JG
kind: problem
title: Every topological group is completely regular
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 33 Exercise 10, printed p. 213,
    whose printed construction -- V_{n+1}^2 inside V_n, the dyadic sets U(k/2^n) with
    U((2k+1)/2^{n+1}) = V_{n+1} U(k/2^n), the inclusion V_n U(k/2^n) inside U((k+1)/2^n), and "proceed
    as in the Urysohn lemma" -- is the skeleton the card fills in. No published solution was located:
    dbFin, "Section 33: Problem 10 Solution", https://dbfin.com/topology/munkres/chapter-4/section-33-the-urysohn-lemma/problem-10-solution/
    (read 2026-11-10; kept at tmp/sources/dbfin/section-33-the-urysohn-lemma/problem-10-solution.txt)
    runs the same construction in prose but its displayed identities are corrupted where it matters
    ("U(0) = {e} ... after that we assume U(0) = emptyset", and a final line that breaks off inside
    V_n <= U(k/2^n)), so it is not a checkable proof; Moller's S33 has no Exercise 10, Doug's World
    stops at 33.8 in this section, and Orellana's Section 33 has Exercises 1 and 3. The card's own
    proof checks the inclusion in the three cases k = 0, k odd, k even, derives the nesting and the
    closure inclusion cl(U(p)) inside U(q) for p < q from symmetry of V_n, and concludes with the
    two open sets {f < t} and {f > t}. This exercise is in the COMPLAINTS.md entry.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps the card's own proof of Munkres §33 Exercise 10, printed
    p. 213: the inclusion V_n U(k/2^n) inside U((k+1)/2^n) checked by induction in the four
    cases k = 0, k = 2j, k = 1 and k = 2j+1; nesting from e in V_n; the closure inclusion
    from symmetry of V_n and translations being homeomorphisms; and f as the infimum, with
    {f < t} a union of the U(p) and {f > t} a union of the complements of the closed U(p).
    The argument is the card's own: no checkable published solution was located, as the
    earlier note records. The printed construction needed no repair.
---

::: {.exercise}

Prove the following.

Theorem.
Every topological group is completely regular.

Proof.
Let $V_0$ be a neighborhood of the identity element $e$, in the topological group $G$.
In general, choose $V_n$ to be a neighborhood of $e$ such that $V_n \cdot V_n \subset V_{n-1}$.
Consider the set of all dyadic rationals $p$, that is, all rational numbers of the form $k/2^n$, with $k$ and $n$ integers.
For each dyadic rational $p$ in $(0, 1]$, define an open set $U(p)$ inductively as follows: $U(1) = V_0$ and $U(\tfrac{1}{2}) = V_1$.
Given $n$, if $U(k/2^n)$ is defined for $0 < k/2^n \leq 1$, define

$$
U(1/2^{n+1}) = V_{n+1},
$$

$$
U((2k+1)/2^{n+1}) = V_{n+1} \cdot U(k/2^n)
$$

for $0 < k < 2^n$.
For $p \leq 0$, let $U(p) = \varnothing$, and for $p > 1$, let $U(p) = G$.
Show that

$$
V_n \cdot U(k/2^n) \subset U((k+1)/2^n)
$$

for all $k$ and $n$.
Proceed as in the Urysohn lemma.

This exercise is adapted from [M-Z], to which the reader is referred for further results on topological groups.
:::

::: {.solution}
The argument is the card's own: it fills in the skeleton Munkres gives in §33 Exercise 10, printed p. 213 ("proceed as in the Urysohn lemma"), and no checkable published solution was located for it — dbFin's Section 33 Problem 10 prose is corrupted where it matters, as the card's earlier audit note records. Every step below is checked against the printed construction: $V_{n+1}^{2}\subset V_{n}$, the dyadic sets $U(k/2^{n})$ with $U\big((2k+1)/2^{n+1}\big)=V_{n+1}U(k/2^{n})$, and the inclusion $V_{n}U(k/2^{n})\subset U\big((k+1)/2^{n}\big)$.

Throughout, $G$ is a topological group with identity $e$; $\mathcal{D}$ is the set of dyadic rationals; $U(p)=\varnothing$ for $p\le0$ and $U(p)=G$ for $p>1$; and $V_{n}$ is a symmetric open neighbourhood of $e$ with $V_{n+1}^{2}\subset V_{n}$ for $n\ge0$, such a $V_{n+1}$ existing at each stage because multiplication is continuous at $(e,e)$ and inversion is continuous.

::: pf

::: {.pf-step #step-inclusion}
For all $n\ge0$ and $0\le k<2^{n}$, $\;V_{n}U(k/2^{n})\subset U\big((k+1)/2^{n}\big)$.

:::: pf-proof

::: {.pf-step #base}
The case $n=0$.

::: pf-proof
Here $k=0$ and $U(0)=\varnothing$, so $V_{0}U(0)=\varnothing\subset U(1)$.
:::

:::

::: {.pf-step #induction}
If the inclusion holds at level $n$, it holds at level $n+1$.

::: pf-proof
Let $0\le k<2^{n+1}$. If $k=0$ then $V_{n+1}U(0)=\varnothing\subset U(1/2^{n+1})$. If $k=2j$ with $1\le j<2^{n}$, then $U(2j/2^{n+1})=U(j/2^{n})$ and the defining relation $U\big((2j+1)/2^{n+1}\big)=V_{n+1}U(j/2^{n})$ gives $V_{n+1}U(k/2^{n+1})=U\big((k+1)/2^{n+1}\big)$. If $k=1$, then $V_{n+1}U(1/2^{n+1})=V_{n+1}V_{n+1}=V_{n+1}^{2}\subset V_{n}=U(1/2^{n})=U\big((k+1)/2^{n+1}\big)$. If $k=2j+1$ with $j\ge1$, then $U\big((2j+1)/2^{n+1}\big)=V_{n+1}U(j/2^{n})$ and
$$
V_{n+1}U\big((2j+1)/2^{n+1}\big)=V_{n+1}^{2}U(j/2^{n})\subset V_{n}U(j/2^{n})\subset U\big((j+1)/2^{n}\big)=U\big((k+1)/2^{n+1}\big),
$$
the second inclusion being the hypothesis at level $n$, which applies because $1\le j<2^{n}$.
:::

:::

::: {.pf-step}
The inclusion holds for all $n$ and $k$.

::: pf-proof
Steps [](#base){.pf-ref} and [](#induction){.pf-ref} are the base and the induction step.
:::

:::

:::

:::

::: {.pf-step #nesting}
$U(p)\subset U(q)$ for dyadic $0\le p\le q\le1$.

::: pf-proof
It suffices, by finitely many applications, to treat adjacent dyadics $p=k/2^{n}$ and $q=(k+1)/2^{n}$ at a common level $n$, since any two dyadics lie at a common level and intermediate levels can be inserted. For those, $e\in V_{n}$ gives $U(p)\subset V_{n}U(p)\subset U(q)$ by step [](#step-inclusion){.pf-ref}.
:::

:::

::: {.pf-step #closure}
$\overline{U(p)}\subset U(q)$ for dyadic $0<p<q\le1$.

::: pf-proof
Choose a level $n$ and adjacent dyadics $r$, $r+2^{-n}$ with $p\le r<r+2^{-n}\le q$; this is possible because the dyadics of a sufficiently fine level are spaced $2^{-n}$ apart throughout $(0,1]$. Then $U(p)\subset U(r)$ by step [](#nesting){.pf-ref}. Let $z\in\overline{U(r)}$. The set $V_{n}z$ is a neighbourhood of $z$, because $V_{n}$ is a neighbourhood of $e$ and left translation is a homeomorphism, so $V_{n}z$ meets $U(r)$; say $vz=u$ with $v\in V_{n}$ and $u\in U(r)$. Since $V_{n}$ is symmetric, $v^{-1}\in V_{n}$, so $z=v^{-1}u\in V_{n}U(r)\subset U(r+2^{-n})\subset U(q)$ by step [](#step-inclusion){.pf-ref} and step [](#nesting){.pf-ref}. Hence $\overline{U(p)}\subset\overline{U(r)}\subset U(q)$.
:::

:::

::: {.pf-step #f-function}
Define $f(z)=\inf\{p\in\mathcal{D}\mid z\in U(p)\}$. Then $f:G\to[0,1]$ is well defined, and $\{f<t\}$ and $\{f>t\}$ are open for every real $t$.

:::: pf-proof

::: {.pf-step #f-well-defined}
$f(z)$ is a real number in $[0,1]$ for every $z$.

::: pf-proof
The set in the infimum is nonempty, because $U(p)=G\ni z$ for every dyadic $p>1$, and it is bounded below by $0$, because $U(p)=\varnothing$ for $p\le0$. So the infimum exists; it is $\ge0$ and $\le1$, since $z\in U(1)=V_{0}$ gives $f(z)\le1$.
:::

:::

::: {.pf-step #f-lower}
$\{f<t\}$ is open for every real $t$.

::: pf-proof
If $z\in U(p)$ with $p\in\mathcal{D}$ and $p<t$, then $f(z)\le p<t$. Conversely, if $f(z)<t$, then by the definition of infimum there is $p$ in the set with $p<t$, and then $z\in U(p)$. So $\{f<t\}=\bigcup\{U(p)\mid p\in\mathcal{D},\ p<t\}$, a union of open sets.
:::

:::

::: {.pf-step #f-upper}
$\{f>t\}$ is open for every real $t$.

::: pf-proof
Let $t$ be real. If $z\notin\overline{U(p)}$ for some dyadic $p>t$, then $z\notin U(q)$ for every dyadic $q\le p$, by step [](#nesting){.pf-ref}, so $f(z)\ge p>t$. Conversely, if $f(z)>t$, choose a dyadic $p$ with $t<p<f(z)$; if $z\in\overline{U(p)}$ then step [](#closure){.pf-ref} with any dyadic $q$ satisfying $p<q<f(z)$ would put $z\in U(q)$, contradicting $f(z)\le q<f(z)$. So $z\notin\overline{U(p)}$. Hence $\{f>t\}=\bigcup\{G-\overline{U(p)}\mid p\in\mathcal{D},\ p>t\}$, a union of open sets.
:::

:::

::: {.pf-step}
$f$ is well defined and the two families of sets are open.

::: pf-proof
Steps [](#f-well-defined){.pf-ref}, [](#f-lower){.pf-ref} and [](#f-upper){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #values}
$f$ is continuous, $f(e)=0$, and $f=1$ on $G-V_{0}$.

::: pf-proof
The rays $(-\infty,t)$ and $(t,+\infty)$ form a subbasis for the topology of $\RR$, and their preimages $\{f<t\}$ and $\{f>t\}$ are open by step [](#f-function){.pf-ref}, so $f$ is continuous (Theorem 18.1). For every $n$ one has $e\in V_{n}=U(2^{-n})$, so $f(e)\le2^{-n}$ for every $n$ and $f(e)=0$. If $z\notin V_{0}=U(1)$ then $z\notin U(p)$ for every dyadic $p\le1$, by step [](#nesting){.pf-ref}, so the set in the definition of $f(z)$ consists of numbers exceeding $1$ and $f(z)=1$.
:::

:::

::: {.pf-step #separation}
For each closed $A\subset G$ and each $x\notin A$ there is a continuous $g:G\to[0,1]$ with $g(x)=0$ and $g(A)=\{1\}$, and points of $G$ are closed.

::: pf-proof
The set $x^{-1}A$ is closed, being the image of the closed set $A$ under the homeomorphism $z\mapsto x^{-1}z$ (Supplementary Exercise TG.4), and $e\notin x^{-1}A$. Choose $V_{0}$ an open neighbourhood of $e$ with $V_{0}\cap x^{-1}A=\varnothing$, and build the $V_{n}$ and $f$ as above. Put $g(z)=f(x^{-1}z)$; it is continuous, as a composite of $f$ with a homeomorphism, and $g(x)=f(e)=0$, while for $a\in A$ one has $x^{-1}a\in x^{-1}A\subset G-V_{0}$, so $g(a)=f(x^{-1}a)=1$. Finally a topological group is $T_{1}$ by definition, so its points are closed.
:::

:::

::: {.pf-step}
$G$ is completely regular.

::: pf-proof
Munkres defines complete regularity by the two properties of step [](#separation){.pf-ref}: points are closed, and each point can be separated from each neighbourhood of it by a continuous map to $[0,1]$. Step [](#values){.pf-ref} and step [](#separation){.pf-ref} provide them.
:::

:::

:::
:::
