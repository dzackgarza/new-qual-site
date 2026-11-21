---
schema: qual/card@1
id: P-OWMPB
kind: problem
title: A polynomial $g$ with $g(T)=0$ is irreducible iff $k(T)$ is invertible for
  every nonzero $k$ of lower degree
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Irreducibility Criteria
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: that I is nonzero (n^2 + 1 powers of T are linearly dependent in the
    n^2-dimensional matrix algebra) and principal, so I = (m_T) with m_T dividing g; that m_T
    is nonconstant, so an irreducible g in I forces m_T to be an associate rather than merely a
    divisor; the coprimality of k and g with the reason a common factor of positive degree is
    excluded; and both directions of the equivalence as separate steps. Not claimed: a retained
    solution set; the provenance names the examination.
---

::: {.problem}
Let $F$ be a field and $T$ an $n\times n$ matrix with entries in $F$.
Let $I$ be the ideal consisting of all polynomials $f\in F[x]$ such that $f(T) =0$.

Show that the following statements are equivalent about a polynomial $g\in I$:

a. $g$ is irreducible.

b. If $k\in F[x]$ is nonzero and of degree strictly less than $g$, then $k(T)$ is an invertible matrix.
:::

::: {.solution}
The statement is the one printed on this card; no retained solution set covers it — the collection's `provenance` names the Fall 2014 algebra examination, which carries no solutions — so the argument below is the card's own, and it is the card's previous prose with the identity $I=(m_T)$ and the coprimality step justified.

Throughout $F$ is a field, $T\in M_n(F)$, $I=\theset{f\in F[x]:f(T)=0}$, $m_T$ the minimal polynomial of $T$, and (a), (b) are the stated conditions on $g\in I$.

::: pf

::: {.pf-step #ideal}
$I$ is a nonzero ideal of $F[x]$ and $I=(m_T)$.

::: pf-proof
$I$ is the kernel of the ring homomorphism $F[x]\to M_n(F)$, $f\mapsto f(T)$, hence an ideal. It is nonzero: the powers $I,T,T^2,\dots,T^{n^2}$ are $n^2+1$ vectors in the $n^2$-dimensional space $M_n(F)$, so a nontrivial linear relation $\sum_{j\le n^2}c_jT^j=0$ gives a nonzero polynomial in $I$. Since $F[x]$ is a principal ideal domain, $I=(m)$ for a unique monic $m$, which is by definition the minimal polynomial $m_T$. Thus $m_T$ generates $I$ and divides every element of $I$, in particular $g$.

:::

:::

::: {.pf-step #a-implies-m}
If $g$ is irreducible then $m_T$ is an associate of $g$.

::: pf-proof
$m_T\mid g$ by step [](#ideal){.pf-ref}, and $m_T$ is nonconstant because $T$ satisfies no nonzero constant polynomial. An irreducible $g$ factors only as a unit times $g$ or a unit times $1$, so $m_T=cg$ with $c\in F^\times$, and in particular $\deg m_T=\deg g$.

:::

:::

::: {.pf-step #a-implies-b}
If $g$ is irreducible, every nonzero $k$ with $\deg k<\deg g$ has $k(T)$ invertible.

::: pf-proof
$\gcd(k,g)=1$: a common divisor of positive degree would be a nonunit divisor of the irreducible $g$, impossible since $\deg k<\deg g$ rules out $k$ being an associate of $g$. By Bézout in $F[x]$ there are $a,b$ with $ak+bg=1$; evaluating at $T$ and using $g(T)=0$ gives $a(T)k(T)=I_n$. Polynomials in $T$ commute, so $k(T)a(T)=I_n$ too, and $k(T)$ is invertible with inverse $a(T)$.

:::

:::

::: {.pf-step #b-implies-a}
If (b) holds then $g$ is irreducible.

::: pf-proof
$g$ is nonconstant, lying in $I$. Suppose $g=uv$ with $u,v$ nonconstant; then $\deg u,\deg v<\deg g$ and both are nonzero, so by (b) both $u(T)$ and $v(T)$ are invertible. But $0=g(T)=u(T)v(T)$ is a product of invertible matrices, hence invertible, a contradiction. So $g$ admits no such factorisation and is irreducible.

:::

:::

::: {.pf-step #conclusion}
(a) and (b) are equivalent.

::: pf-proof
Step [](#a-implies-b){.pf-ref} gives (a) implies (b), and step [](#b-implies-a){.pf-ref} gives (b) implies (a).

:::

:::

:::
:::
