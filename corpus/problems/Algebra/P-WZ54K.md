---
schema: qual/card@1
id: P-WZ54K
kind: problem
title: $x^{p^n}-x$ is the product of monic irreducibles in $\FF_p[x]$ of degree dividing
  $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Factorization
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (an
    identity between polynomials, no repair needed), and the existing prose against a
    fresh re-derivation: x^{p^n} - x has derivative -1, so it is squarefree and its
    roots are exactly the p^n elements of F_{p^n}; a monic irreducible f of degree d
    divides it exactly when some root of f lies in F_{p^n}, which by stability of
    F_{p^n} under Frobenius is equivalent to the single condition alpha in F_{p^n}
    for one root alpha; F_p(alpha) = F_{p^d}, and F_{p^d} is contained in F_{p^n}
    exactly when d divides n; squarefreeness makes every such factor appear once, and
    no other irreducible divides it. Correct. Two points the prose passed over are now
    argued: that one root in F_{p^n} forces all roots of f there (Frobenius
    conjugates, stability of the subfield), and that the equality of polynomials
    follows from the factor list plus squarefreeness rather than from a degree count;
    the degree count p^n = sum_{d | n} d N_p(d) is kept only as a check. No source
    solution is retained for this card, so no source comparison was made. What was
    not checked: any printed source.
---

::: {.problem}
Prove that
$$
x^{p^n}-x
$$
is the product of all monic irreducible polynomials in $\FF_p[x]$ whose degrees divide $n$.
:::

::: {.solution}
Fix an algebraic closure $\Omega$ of $\FF_p$ and let $K\subseteq\Omega$ be the subfield with $p^n$ elements, so that $K=\theset{a\in\Omega:a^{p^n}=a}$.

::: pf

::: {.pf-step #roots}
$x^{p^n}-x=\prod_{a\in K}(x-a)$, and the polynomial is squarefree.

::: pf-proof
Its derivative is $p^nx^{p^n-1}-1=-1$ in characteristic $p$, so it has no repeated root in $\Omega$ and is therefore squarefree. Every $a\in K$ satisfies $a^{p^n}=a$ by definition of $K$, so the $p^n$ elements of $K$ are roots of a polynomial of degree $p^n$; a polynomial of degree $p^n$ has at most $p^n$ roots, so these are all of them and the factorization holds.
:::

:::

::: {.pf-step #criterion}
Let $f\in\FF_p[x]$ be monic and irreducible of degree $d$, with a root $\alpha\in\Omega$. Then $f$ divides $x^{p^n}-x$ if and only if $d\mid n$.

::: pf-proof
Since $f$ is irreducible with root $\alpha$, it is the minimal polynomial of $\alpha$ over $\FF_p$, and $[\FF_p(\alpha):\FF_p]=d$. Because $x^{p^n}-x=\prod_{a\in K}(x-a)$ is squarefree by step [](#roots){.pf-ref}, $f$ divides it exactly when $f$ and it share a root, that is, when some root of $f$ lies in $K$. The roots of $f$ are the Frobenius conjugates $\alpha,\alpha^p,\alpha^{p^2},\ldots$, and $K$ is stable under $a\mapsto a^p$, so either all roots of $f$ lie in $K$ or none does; hence $f\mid x^{p^n}-x$ if and only if $\alpha\in K$.

Now $\alpha\in K$ if and only if $\alpha^{p^n}=\alpha$. Since $\FF_p(\alpha)$ is a subfield of $\Omega$ with $p^d$ elements, it is $\FF_{p^d}$, and $\alpha\in\FF_{p^n}$ exactly when $\FF_{p^d}\subseteq\FF_{p^n}$, which by the subfield criterion for finite fields holds exactly when $d\mid n$. Combining the two equivalences gives $f\mid x^{p^n}-x$ iff $d\mid n$.
:::

:::

::: {.pf-step #multiplicity}
Every monic irreducible $f$ of degree $d\mid n$ divides $x^{p^n}-x$ with multiplicity exactly one, and no other monic irreducible divides it.

::: pf-proof
Multiplicity one is step [](#roots){.pf-ref}, squarefreeness. No irreducible of degree $d\nmid n$ divides it by step [](#criterion){.pf-ref}. Conversely each monic irreducible of degree dividing $n$ does divide it, again by step [](#criterion){.pf-ref}.
:::

:::

::: {.pf-step}
$x^{p^n}-x$ is the product of all monic irreducible polynomials in $\FF_p[x]$ whose degrees divide $n$.

::: pf-proof
Both sides are monic. By step [](#multiplicity){.pf-ref} the irreducible factors of $x^{p^n}-x$ in $\FF_p[x]$ are exactly the monic irreducibles of degree dividing $n$, each occurring to the first power; a monic polynomial is the product of its monic irreducible factors with their multiplicities, so $x^{p^n}-x$ equals their product. As a check on the degrees, taking degrees on both sides gives $p^n=\sum_{d\mid n}d\,N_p(d)$, where $N_p(d)$ is the number of monic irreducibles of degree $d$.
:::

:::

:::
:::
