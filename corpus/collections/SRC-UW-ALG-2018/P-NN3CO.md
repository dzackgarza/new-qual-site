---
schema: qual/card@1
id: P-NN3CO
kind: problem
title: Galois group of $\QQ(\sqrt{2+\sqrt{2}})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The statement is the UW 2018 algebra exam question recorded for this collection; the
    retained exam file lists it in the field-theory section. No retained solution set covers
    it, so the argument on the card is its own.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured the card's own argument into numbered steps, with the conclusion unchanged
    (the group is cyclic of order 4; note it is not the Klein four-group, since the
    automorphism taking alpha to beta has square alpha -> -alpha). The step "there exists an
    automorphism sending alpha to beta" is now justified: substituting a root of the minimal
    polynomial into Q(alpha) gives a Q-embedding of K into C, whose image is the splitting
    field of f, hence K itself. The count of automorphisms is given by the degree, which the
    irreducible minimal polynomial supplies.
---

::: {.problem}
Show that the field extension $\QQ\subset\QQ[\sqrt{2+\sqrt{2}}]$ is Galois and determine its Galois group.
:::

::: {.solution}

The question is the UW 2018 algebra exam's, as this collection records it; no retained
solution set covers it, so the argument below is the card's own, restructured as numbered
steps.

Let $\alpha=\sqrt{2+\sqrt{2}}$ and $K=\QQ(\alpha)\subseteq\RR$, and put
$f(x)=x^{4}-4x^{2}+2$.

::: pf

::: {.pf-step #minimal}

$f$ is the minimal polynomial of $\alpha$ over $\QQ$, and $[K:\QQ]=4$.

::: pf-proof

Squaring $\alpha^{2}=2+\sqrt2$ gives $(\alpha^{2}-2)^{2}=2$, that is
$\alpha^{4}-4\alpha^{2}+2=0$, so $\alpha$ is a root of $f$. The polynomial $f$ is monic with
integer coefficients, and Eisenstein's criterion applies at the prime $2$: $2$ divides both
$-4$ and $2$, $2^{2}=4$ does not divide $2$, and $2$ does not divide the leading coefficient
$1$. So $f$ is irreducible over $\QQ$, and being monic and irreducible with $\alpha$ as a
root it is the minimal polynomial of $\alpha$; hence $[K:\QQ]=\deg f=4$.

:::

:::

::: {.pf-step #roots}

$f$ has exactly the four roots $\pm\alpha,\pm\beta$, where $\beta=\sqrt{2-\sqrt2}$.

::: pf-proof

Setting $y=x^{2}$, $f$ becomes $y^{2}-4y+2$, whose roots are $y=2\pm\sqrt2$ by the quadratic
formula. Both are positive, so each has two real square roots, and $x^{2}=2\pm\sqrt2$ gives
$x=\pm\sqrt{2+\sqrt2}=\pm\alpha$ and $x=\pm\sqrt{2-\sqrt2}=\pm\beta$ — four distinct values,
which exhaust the roots of a quartic.

:::

:::

::: {.pf-step #splitting-field}

$K$ contains $\beta$, hence all four roots of $f$; so $K$ is the splitting field of $f$ over
$\QQ$ and $K/\QQ$ is Galois.

::: pf-proof

$\alpha\neq0$ and $\alpha\beta=\sqrt{(2+\sqrt2)(2-\sqrt2)}=\sqrt{4-2}=\sqrt2$, so
$\beta=\sqrt2/\alpha$. Moreover $\sqrt2=\alpha^{2}-2\in K$. Hence
$\beta=(\alpha^{2}-2)/\alpha\in K$, and with it $-\beta\in K$; $\pm\alpha\in K$ by definition
of $K$. So $K$ contains all roots of $f$ by step [](#roots){.pf-ref}, that is $K$ is the
splitting field of $f$ over $\QQ$. A splitting field over a field of characteristic $0$ is a
separable normal extension, that is Galois.

:::

:::

::: {.pf-step #automorphisms}

For each root $\gamma$ of $f$ there is exactly one $\sigma\in\Gal(K/\QQ)$ with
$\sigma(\alpha)=\gamma$; consequently $\cardinality{\Gal(K/\QQ)}=4$.

::: pf-proof

As $f$ is the minimal polynomial of $\alpha$ (step [](#minimal){.pf-ref}), sending $\alpha$ to
a root $\gamma$ defines a ring homomorphism $\QQ[\alpha]\to\CC$ fixing $\QQ$; its kernel is a
proper ideal of the field $\QQ[\alpha]$, hence $0$, so it is injective, and it extends to the
fraction field $K$. Its image is $\QQ(\gamma)$, which by step [](#splitting-field){.pf-ref}
lies in $K$ and contains $K$ (symmetrically), so the image is $K$ and the embedding is an
automorphism of $K$. Distinct roots give distinct images of $\alpha$, so the four roots give
four distinct automorphisms, and there are no others since an automorphism must send $\alpha$
to a root of its minimal polynomial. Hence the group has $4$ elements, matching $[K:\QQ]=4$.

:::

:::

::: {.pf-step #cyclic}

The automorphism $\sigma$ with $\sigma(\alpha)=\beta$ has order $4$, so
$\Gal(K/\QQ)=\langle\sigma\rangle\cong\ZZ_{4}$.

::: pf-proof

Such a $\sigma$ exists by step [](#automorphisms){.pf-ref}. Since $\alpha^{2}-2=\sqrt2$,
$\sigma(\sqrt2)=\sigma(\alpha)^{2}-2=\beta^{2}-2=(2-\sqrt2)-2=-\sqrt2$. Then
$\sigma(\beta)=\sigma(\sqrt2/\alpha)=\sigma(\sqrt2)/\sigma(\alpha)=-\sqrt2/\beta=-\alpha$,
using $\sqrt2/\beta=\alpha$. Applying $\sigma$ again:
$\sigma^{2}(\alpha)=-\alpha$, $\sigma^{3}(\alpha)=-\beta$, $\sigma^{4}(\alpha)=\alpha$. So
$\sigma^{4}$ fixes the generator $\alpha$ of $K$ and is the identity, while
$\sigma^{2}(\alpha)=-\alpha\ne\alpha$, so $\sigma$ has order $4$. A group of order $4$ with an
element of order $4$ is cyclic, so $\Gal(K/\QQ)=\langle\sigma\rangle\cong\ZZ_{4}$.

:::

:::

:::

:::
