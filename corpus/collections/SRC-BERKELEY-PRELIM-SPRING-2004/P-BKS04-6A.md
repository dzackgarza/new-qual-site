---
schema: qual/card@1
id: P-BKS04-6A
kind: problem
title: Integers $a,b$ with $\ZZ[x]/(x^2+ax+b)\cong\ZZ\times\ZZ$
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
    Restructured into numbered steps for issue #2: reducibility forced by being a domain, the prime-by-prime
    obstruction to $c-d$, the converse by the Chinese remainder theorem, and the resulting list of pairs. The
    argument is the retained packet's (problem 6A of `assets/attachments/s04solution.pdf`), read again for
    this pass and unchanged.
---

::: {.problem}
For which pairs of integers $(a,b)$ is the quotient ring $\ZZ[x]/(x^2+ax+b)$ isomorphic (as a ring) to the direct product of rings $\ZZ\times\ZZ$?
:::

::: {.solution}
The retained solution set is the **Berkeley Spring 2004 preliminary solution packet** (`assets/attachments/s04solution.pdf`, extracted text at `assets/attachments/s04solution_extracted.md`), problem 6A; the argument below is its, split into steps. Write $A=\ZZ[x]/(x^{2}+ax+b)$ and $B=\ZZ\times\ZZ$; the answer is the pairs $(a,b)=(-(2n+1),\,n(n+1))$ with $n\in\ZZ$.

::: pf

::: {.pf-step #reducible}
If $A\cong B$ then $x^{2}+ax+b=(x-c)(x-d)$ with $c,d\in\ZZ$.

::: pf-proof
$B=\ZZ\times\ZZ$ is not a domain, since $(1,0)(0,1)=(0,0)$ with both factors nonzero. If $x^{2}+ax+b$ were irreducible in the unique factorization domain $\ZZ[x]$, it would be prime, so the ideal it generates would be prime and $A$ would be a domain; that is impossible. Hence the quadratic factors, and since it is monic the factors are monic of degree one with integer constant terms, which is the displayed form with $c,d\in\ZZ$.
:::

:::

::: {.pf-step #difference}
$c-d=\pm1$.

::: pf-proof
Suppose a prime $p$ divides $c-d$. Then reducing the isomorphism $A\cong B$ modulo $p$ gives
$$
A/pA\cong B/pB,\qquad\text{that is}\qquad \FF_{p}[x]/(\overline{x-c})^{2}\cong\FF_{p}\times\FF_{p},
$$
because $x^{2}+ax+b\equiv(x-c)(x-d)\equiv(x-\bar c)^{2}$ modulo $p$ when $\bar c=\bar d$. The left ring has a nonzero element whose square is zero, namely $x-\bar c$, while a product of fields has no such element: if $(u,v)^{2}=(0,0)$ then $u=v=0$. This contradicts the isomorphism, so no prime divides $c-d$, and $c-d=\pm1$ because $c-d\ne0$ is an integer with no prime divisor only when it is $\pm1$.
:::

:::

::: {.pf-step #converse}
If $c-d=\pm1$ and $x^{2}+ax+b=(x-c)(x-d)$, then $A\cong B$.

::: pf-proof
The ideals $(x-c)$ and $(x-d)$ of $\ZZ[x]$ are comaximal: their sum contains $(x-c)-(x-d)=d-c=\pm1$, so it is the unit ideal. Comaximal ideals satisfy $IJ=I\cap J$, and the Chinese remainder theorem then gives
$$
\frac{\ZZ[x]}{((x-c)(x-d))}\cong\frac{\ZZ[x]}{(x-c)}\times\frac{\ZZ[x]}{(x-d)} .
$$
Each factor is isomorphic to $\ZZ$: division by the monic $x-c$ gives every class a unique representative $r\in\ZZ$, since $g=q(x)(x-c)+r$ with $r=g(c)$. So $A\cong\ZZ\times\ZZ=B$.
:::

:::

::: {.pf-step}
The pairs are exactly those with $x^{2}+ax+b=(x-n)(x-(n+1))$, that is $(a,b)=(-(2n+1),\,n(n+1))$ for $n\in\ZZ$.

::: pf-proof
By steps [](#reducible){.pf-ref} and [](#difference){.pf-ref}, $A\cong B$ forces $x^{2}+ax+b=(x-c)(x-d)$ with $\abs{c-d}=1$, and then $a=-(c+d)$, $b=cd$. Writing $n=\min\{c,d\}$ gives $c,d=\{n,n+1\}$, hence $a=-(2n+1)$ and $b=n(n+1)$. Conversely for such a pair the quadratic is $(x-n)(x-(n+1))$ with the two roots differing by $1$, so step [](#converse){.pf-ref} gives $A\cong B$. That is the asserted set of pairs.
:::

:::

:::
:::
