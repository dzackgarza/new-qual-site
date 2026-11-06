---
schema: qual/card@1
id: P-SMTIY
kind: problem
title: Unique $p$th roots in a field of order $p^n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Characteristic
  - Separability
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section V.5,
    exercise 3, book page 281: "If |K| = p^n, then every element of K has a unique
    pth root in K." The card states exactly this. The proof was checked: a field
    of order p^n has prime field F_p and characteristic p, so (x+y)^p = x^p + y^p
    since the intermediate binomial coefficients vanish, giving the Frobenius
    endomorphism; its kernel is a proper ideal in a field, hence 0, so it is
    injective, and an injective self-map of a finite set is bijective, which gives
    existence and uniqueness of the pth root. Complete; no defect.
---

::: {.problem}
Show that if $\cardinality{K} = p^n$, then every element of $K$ has a unique $p$th root in $K$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The Frobenius map $\varphi\colon K \to K$, $\varphi(x) = x^p$, is an injective ring homomorphism.

::: pf-proof

The field $K$ has order $p^n$, so its prime field is $\FF_p$ and $\operatorname{char}K=p$. Hence $p$ divides $\binom pk$ for $0<k<p$, so $(x + y)^p = x^p + y^p$; also $(xy)^p = x^p y^p$ and $1^p=1$. The kernel of a ring homomorphism out of a field is an ideal not containing $1$, hence $0$.

:::

:::

::: {.pf-step #s2}

$\varphi$ is bijective.

::: pf-proof

By step [](#s1){.pf-ref}, $\varphi$ is an injective map from the finite set $K$ to itself, hence surjective.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, for every $a\in K$ there is exactly one $x\in K$ with $x^p=\varphi(x)=a$.

:::

:::

:::
