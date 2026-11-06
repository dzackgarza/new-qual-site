---
schema: qual/card@1
id: P-5AMY7
kind: problem
title: Irreducible polynomials of degrees 7 and 14 over $\FF_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (two
    existence questions, no repair needed), and the existing prose solution against
    a fresh re-derivation: F_{p^n}^x is cyclic, a generator alpha satisfies
    F_p(alpha) = F_{p^n}, so its minimal polynomial is irreducible of degree n and
    exists for every n; the degree identity p^n = sum over d | n of d*N_p(d) holds
    because x^{p^n} - x is separable and equals the product of the distinct monic
    irreducibles whose degree divides n (an irreducible of degree d dividing it
    exactly when d | n, by F_{p^d} <= F_{p^n}); Mobius inversion gives the closed
    form; and the two specialisations are (p^7 - p)/7 and
    (p^14 - p^7 - p^2 + p)/14, both positive. Correct. The prose stated the Mobius
    formula without deriving it; the structured proof derives the degree identity
    it inverts, which is the only substantive addition. No source solution is
    retained for this card, so no source comparison was made. What was not
    checked: any printed source.
---

::: {.problem}
Can you have a degree 7 irreducible polynomial over $\FF_p$? How about a degree 14 irreducible polynomial?
:::

::: {.solution}
Throughout, $p$ is a prime and $N_p(n)$ denotes the number of monic irreducible polynomials of degree $n$ over $\FF_p$; fix an algebraic closure $\Omega$ of $\FF_p$ and let $\FF_{p^n}\subseteq\Omega$ be its subfield with $p^n$ elements.

::: pf

::: {.pf-step #exists-all}
For every $n\geq1$ there is a monic irreducible polynomial of degree $n$ over $\FF_p$; in particular of degrees $7$ and $14$.

::: pf-proof
$\FF_{p^n}^\times$ is a finite subgroup of the multiplicative group of a field, hence cyclic; let $\alpha$ generate it. Then $\FF_p(\alpha)$ contains every polynomial in $\alpha$ with coefficients in $\FF_p$, in particular every power $\alpha^k$, that is, every nonzero element of $\FF_{p^n}$, and also $0$; so $\FF_p(\alpha)=\FF_{p^n}$ and $[\FF_p(\alpha):\FF_p]=n$. The minimal polynomial of $\alpha$ over $\FF_p$ is monic, irreducible, and of degree $[\FF_p(\alpha):\FF_p]=n$. Taking $n=7$ and $n=14$ gives the two polynomials asked for.
:::

:::

::: {.pf-step #degree-count}
$p^n=\sum_{d\mid n}d\cdot N_p(d)$ for every $n\geq1$.

::: pf-proof
Over $\Omega$ the polynomial $x^{p^n}-x$ has derivative $-1$, so it has no repeated roots. By Lagrange's theorem in $\FF_{p^n}^\times$, every element satisfies $x^{p^n}=x$: a nonzero element has $x^{p^n-1}=1$ because the group has order $p^n-1$, and $0$ satisfies the equation trivially. So the roots include all $p^n$ elements of $\FF_{p^n}$, which is the degree of the polynomial, and being as many as the degree they are all of them. Hence $x^{p^n}-x=\prod_{a\in\FF_{p^n}}(x-a)$.

A monic irreducible $f\in\FF_p[x]$ of degree $d$ divides $x^{p^n}-x$ exactly when $d\mid n$: if $f$ divides it, a root $\beta$ of $f$ lies in $\FF_{p^n}$, so $\FF_p(\beta)\subseteq\FF_{p^n}$ and $d=[\FF_p(\beta):\FF_p]$ divides $[\FF_{p^n}:\FF_p]=n$ by the tower law; conversely if $d\mid n$ then $\FF_{p^d}\subseteq\FF_{p^n}$, and a root of $f$ lies in $\FF_{p^d}$, hence in $\FF_{p^n}$, hence is a root of $x^{p^n}-x$. Since $x^{p^n}-x$ is separable, it is the product of the distinct monic irreducibles whose degree divides $n$, and each such $f$ of degree $d$ contributes $d$ to the degree. Comparing degrees gives the identity.
:::

:::

::: {.pf-step #mobius}
$N_p(n)=\frac1n\sum_{d\mid n}\mu(d)\,p^{n/d}$, where $\mu$ is the Möbius function.

::: pf-proof
This is Möbius inversion applied to the identity of step [](#degree-count){.pf-ref}: writing $F(n)=p^n$ and $G(d)=d\,N_p(d)$, the identity reads $F(n)=\sum_{d\mid n}G(d)$, and Möbius inversion gives $G(n)=\sum_{d\mid n}\mu(d)F(n/d)$, that is $nN_p(n)=\sum_{d\mid n}\mu(d)p^{n/d}$.
:::

:::

::: {.pf-step #seven}
$N_p(7)=\frac{p^7-p}{7}$ and $N_p(7)>0$.

::: pf-proof
The divisors of $7$ are $1$ and $7$, with $\mu(1)=1$ and $\mu(7)=-1$, so step [](#mobius){.pf-ref} gives $N_p(7)=\frac17\bigl(p^7-p\bigr)$. Since $p\geq2$ we have $p^7>p$, so the numerator is positive, and $N_p(7)$ is a count, hence a positive integer; so a monic irreducible of degree $7$ exists.
:::

:::

::: {.pf-step}
$N_p(14)=\frac{p^{14}-p^7-p^2+p}{14}$ and $N_p(14)>0$.

::: pf-proof
The divisors of $14$ are $1,2,7,14$ with $\mu=1,-1,-1,1$ respectively, so step [](#mobius){.pf-ref} gives $N_p(14)=\frac1{14}\bigl(p^{14}-p^7-p^2+p\bigr)$. The numerator equals $p\bigl(p^{13}-p^{6}-p+1\bigr)$, and $p^{13}-p^6-p+1>0$ for $p\geq2$ because $p^{13}>p^6+p$; being a count it is a positive integer, so a monic irreducible of degree $14$ exists. Hence the answer to both questions is yes.
:::

:::

:::
:::
