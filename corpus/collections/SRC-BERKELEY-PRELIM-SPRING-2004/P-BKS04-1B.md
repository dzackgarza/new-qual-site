---
schema: qual/card@1
id: P-BKS04-1B
kind: problem
title: $y^2+a(x)y+b(x)$ is irreducible over $F(x)$ when $\deg a\le g$ and $\deg b=2g+1$
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Spring 2004
    prelim solutions, Problem 1B, PDF p. 6, the file named in the collection's provenance),
    which the card now cites; it previously carried no citation. Added: why F[x] a UFD with
    fraction field F(x) and f monic in y make Gauss's lemma give a factorization with
    p, q in F[x]; the comparison of coefficients p + q = a, pq = b; and the parity argument
    that distinct degrees of p and q follow from deg(pq) odd. The sheet closes with "This
    contradictions deg a(x) = g"; the card states the hypothesis as printed, deg a <= g, which
    is what the argument contradicts and what the sheet's own display uses.
---

::: {.problem}
Let $F$ be a field (of arbitrary characteristic).
Suppose $g$ is a nonnegative integer, and polynomials $a(x),b(x)\in F[x]$ satisfy $\deg a(x)\leq g$ and $\deg b(x)=2g+1$. Prove that the polynomial $y^2+a(x)y+b(x)$ is irreducible over $F(x)$.
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Spring 2004 prelim solutions, Problem 1B, PDF p. 6** (`assets/attachments/s04solution.pdf`, the file named in this collection's `provenance`): the reduction by Gauss's lemma to a factorization over $F[x]$, the parity of $\deg b$, and the degree estimate on $p+q$ are that solution's. The sheet ends the argument with "This contradictions $\deg a(x)=g$"; the card states the hypothesis it contradicts, $\deg a(x)\le g$, as printed.

Throughout $F$ is a field of arbitrary characteristic, $g\ge0$, $a,b\in F[x]$ with $\deg a\le g$ and $\deg b=2g+1$, and $f=y^2+a(x)y+b(x)\in F[x][y]$.

::: pf

::: {.pf-step #gauss}
If $f$ were reducible over $F(x)$, then $f=(y+p)(y+q)$ for some $p,q\in F[x]$.

::: pf-proof
$F[x]$ is a unique factorization domain with fraction field $F(x)$, and $f$ is monic in $y$ with coefficients in $F[x]$. A factorization over $F(x)$ into polynomials of $y$-degree $\ge1$ is, since $\deg_yf=2$, a factorization into two monic linear factors $y+p$, $y+q$ with $p,q\in F(x)$; by Gauss's lemma the polynomial factors in $F[x][y]$ with the same bidegrees, so we may take $p,q\in F[x]$.

:::

:::

::: {.pf-step #degrees}
$p q=b$ and $\deg p+\deg q=2g+1$, so $\deg p\ne\deg q$.

::: pf-proof
Expanding $(y+p)(y+q)=y^2+(p+q)y+pq$ and comparing with $f$ gives $p+q=a$ and $pq=b$. In the domain $F[x]$, $\deg(pq)=\deg p+\deg q=\deg b=2g+1$, an odd number; a sum of two nonnegative integers is odd only when the two have different parities, so in particular $\deg p\ne\deg q$.

:::

:::

::: {.pf-step #sum}
$\deg(p+q)>g$, contradicting $\deg a\le g$.

::: pf-proof
For polynomials of different degrees the leading terms cannot cancel, so $\deg(p+q)=\max(\deg p,\deg q)$. Since $\deg p+\deg q=2g+1$ by step [](#degrees){.pf-ref}, the maximum of two integers with that sum is at least half of it: $\max(\deg p,\deg q)\ge(2g+1)/2>g$. So $\deg a=\deg(p+q)>g$, contrary to the hypothesis $\deg a\le g$.

:::

:::

::: {.pf-step #conclusion}
$f=y^2+a(x)y+b(x)$ is irreducible over $F(x)$.

::: pf-proof
If $f$ were reducible over $F(x)$, step [](#gauss){.pf-ref} would produce $p,q\in F[x]$ with $p+q=a$ and $pq=b$, and step [](#sum){.pf-ref} turns that into a contradiction with $\deg a\le g$. So no factorization exists.

:::

:::

:::
:::
