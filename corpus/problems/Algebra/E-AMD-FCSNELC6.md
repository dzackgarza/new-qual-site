---
schema: qual/card@1
id: E-AMD-FCSNELC6
kind: problem
title: $\GF(p^d)\leq\GF(p^n)$ iff $d$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard criterion, no repair needed; the comparison of the two finite fields
    is made inside a fixed algebraic closure, which the lead-in now states because
    the statement is otherwise comparing fields that need not be given as
    subfields of one another), and the existing prose solution against a fresh
    re-derivation: the root set of x^{p^m} - x is a subfield with exactly p^m
    elements (the derivative is -1, so the roots are distinct; Frobenius is a ring
    homomorphism in characteristic p), hence has degree m over F_p; the tower law
    in F_p <= F_{p^d} <= F_{p^n} gives n = [F_{p^n}:F_{p^d}]*d; and for d | n the
    k-fold iterate of the p^d-power map sends x^{p^d} = x to x^{p^{dk}} = x with
    n = dk. Correct. The prose assumed the root-set description without stating
    why the set is a field of the stated size; that is now step 1 with its
    reasons. No source solution is retained for this card, so no source comparison
    was made. What was not checked: any printed source.
---

::: {.exercise}
Show that $\FF_{p^d} \le \FF_{p^n} \iff d \mid n$.
:::

::: {.solution}
Fix an algebraic closure $\Omega$ of $\FF_p$ and, for $m\geq1$, let $K_m=\theset{x\in\Omega:x^{p^m}=x}$; write $\FF_{p^m}$ for $K_m$, the subfield of $\Omega$ with $p^m$ elements, so that $\FF_{p^d}\subseteq\FF_{p^n}$ is an inclusion of subfields of the common field $\Omega$.

::: pf

::: {.pf-step #subfield}
For every $m\geq1$, $K_m$ is a subfield of $\Omega$ with exactly $p^m$ elements, and $[\FF_{p^m}:\FF_p]=m$.

::: pf-proof
$K_m$ is the set of roots in $\Omega$ of $x^{p^m}-x$. That polynomial has derivative $p^m x^{p^m-1}-1=-1\neq0$ in characteristic $p$, so it has no repeated root and therefore exactly $p^m$ distinct roots in $\Omega$, the degree being $p^m$. The set of roots is closed under addition and multiplication because $x\mapsto x^{p^m}$ is a ring homomorphism — $(x+y)^{p^m}=x^{p^m}+y^{p^m}$ and $(xy)^{p^m}=x^{p^m}y^{p^m}$ in characteristic $p$ — and contains $0$ and $1$, so it is a subfield. Its degree over $\FF_p$ is $\log_p\abs{K_m}=m$ because a finite extension of degree $r$ of $\FF_p$ has $p^r$ elements.
:::

:::

::: {.pf-step #forward}
If $\FF_{p^d}\subseteq\FF_{p^n}$ then $d\mid n$.

::: pf-proof
The inclusion is an extension of finite fields, so the tower law applies to $\FF_p\subseteq\FF_{p^d}\subseteq\FF_{p^n}$:
$$n=[\FF_{p^n}:\FF_p]=[\FF_{p^n}:\FF_{p^d}]\,[\FF_{p^d}:\FF_p]=[\FF_{p^n}:\FF_{p^d}]\cdot d,$$
using step [](#subfield){.pf-ref} at both ends. Hence $d$ divides $n$.
:::

:::

::: {.pf-step #backward}
If $d\mid n$ then $\FF_{p^d}\subseteq\FF_{p^n}$.

::: pf-proof
Write $n=dk$. Let $x\in\FF_{p^d}$, so $x^{p^d}=x$. Applying the map $y\mapsto y^{p^d}$ a total of $k$ times to the equality $x^{p^d}=x$ gives $x^{p^{dk}}=x$, that is $x^{p^n}=x$, so $x\in K_n=\FF_{p^n}$ by the definition of $K_n$. Hence every element of $\FF_{p^d}$ lies in $\FF_{p^n}$.
:::

:::

::: {.pf-step}
$\FF_{p^d}\leq\FF_{p^n}$ if and only if $d\mid n$.

::: pf-proof
Step [](#forward){.pf-ref} gives one implication and step [](#backward){.pf-ref} the other, so the equivalence holds. Both directions compare the two fields inside the fixed algebraic closure $\Omega$; in a field of characteristic $p$ any two subfields with $p^d$ and $p^n$ elements are the images of $\FF_{p^d}$ and $\FF_{p^n}$ under an isomorphism into such an $\Omega$, so the conclusion does not depend on the choice of $\Omega$.
:::

:::

:::
:::
