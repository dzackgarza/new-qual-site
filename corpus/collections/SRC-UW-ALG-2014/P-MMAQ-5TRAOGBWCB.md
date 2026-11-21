---
schema: qual/card@1
id: P-MMAQ-5TRAOGBWCB
kind: problem
title: $x^p-t$ is irreducible over $\FF_p(t)$ and splits as a $p$-th power
  in its splitting field
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Splitting Fields
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 2 of the 2014 Algebra Preliminary Examination (University of
    Washington, September 8, 2014), printed p. 1 of the two-page paper retained at
    assets/attachments/UW-Algebra-Qual-2014.pdf, is the statement the card answers, and the paragraph at
    the head of the solution records that the paper prints no solutions, so the argument is the card's
    own. Checked: the statement against the paper's text layer at the page named; the solution read for
    all three parts: no root of X^p - t in F_p(t), the factorization (X - alpha)^p over the splitting
    field, and the irreducibility that follows; `qualc.authoring check` on the card, and `tmp/lam.sh`
    for the numbering and the QED. Not checked: no retained solution set exists for this paper to
    compare the argument with, and no other card of the collection in this pass.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $p$ be a prime, let $\FF_p$ be the $p$-element field, and let $K=\FF_p(t)$ be the field of rational functions in $t$ with coefficients in $\FF_p$.
Consider the polynomial $f(X)=X^p-t\in K[X]$.

(a) Show that $f$ does not have a root in $K$.

(b) Let $E$ be the splitting field of $f$ over $K$.
Find the factorization of $f$ over $E$.

(c) Conclude that $f$ is irreducible over $K$.
:::

::: {.solution}

The problem is Problem 2 of the 2014 Algebra Preliminary Examination (University of Washington, September 8, 2014), printed p. 1 of the two-page paper retained at `assets/attachments/UW-Algebra-Qual-2014.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is all three parts: that $X^p-t$ has no root in $\FF_p(t)$, the factorization $(X-\alpha)^p$ over the splitting field, and the irreducibility that follows from it

::: pf

::: {.pf-step #s1}

The polynomial $f(X)=X^p-t$ has no root in $K=\FF_p(t)$.

::: pf-proof

Suppose $r\in K$ satisfies $r^p=t$. Write
$$
r=\frac{a(t)}{b(t)}
$$
with coprime $a,b\in\FF_p[t]$, $b\ne0$. Then
$$
a(t)^p=t\,b(t)^p.
$$
Let $v_t$ denote the exponent of the irreducible polynomial $t$ in a nonzero polynomial. Taking $v_t$ gives
$$
p\,v_t(a)=1+p\,v_t(b),
$$
which is impossible modulo $p$. Hence $f$ has no root in $K$.

:::

:::

::: {.pf-step #s2}

If $\alpha$ is a root of $f$ in a splitting field $E$, then
$$
f(X)=(X-\alpha)^p
$$
in $E[X]$.

::: pf-proof

We have $\alpha^p=t$. Since the characteristic is $p$, all intermediate binomial coefficients $\binom pj$ vanish in $\FF_p$, so
$$
(X-\alpha)^p=X^p-\alpha^p=X^p-t=f(X).
$$
Thus $\alpha$ is the unique root of $f$ in an algebraic closure, with multiplicity $p$.

:::

:::

::: pf-step

The polynomial $f(X)=X^p-t$ is irreducible over $K$.

::: pf-proof

Suppose $f$ were reducible in $K[X]$. Since $f$ is monic, it would have a monic factor $g\in K[X]$ of degree $r$ with
$$
1\le r\le p-1.
$$
Over the splitting field $E$, step [](#s2){.pf-ref} shows that every root of $g$ must equal $\alpha$. Hence
$$
g(X)=(X-\alpha)^r.
$$
The coefficient of $X^{r-1}$ in this polynomial is $-r\alpha$. Because $1\le r<p$, the element $r\in\FF_p$ is nonzero, hence invertible. Since $g\in K[X]$, we obtain
$$
\alpha=-r^{-1}[X^{r-1}]g\in K,
$$
contradicting step [](#s1){.pf-ref}. Therefore $f$ is irreducible over $K$.

:::

:::

:::

:::
