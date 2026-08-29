---
schema: qual/card@1
id: P-SMTIY
kind: problem
title: Hungerford 5.5.3
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
---

::: {.problem}
Show that if $|K| = p^n$, then every element of $K$ has a unique $p$th root in $K$.
:::

::: {.solution}
<1>1. $K$ is a finite field of characteristic $p$ (since $|K| = p^n$).
Proof: a finite field of order $p^n$ has characteristic $p$.

<1>2. The Frobenius map $\varphi : K \to K$, $\varphi(x) = x^p$, is a field homomorphism.
Proof: $(x + y)^p = x^p + y^p$ in characteristic $p$ (freshman's dream), and $(xy)^p = x^p y^p$.

<1>3. $\varphi$ is injective (it is a field homomorphism, so its kernel is an ideal, hence $0$).
Proof: <1>2 (a nonzero field homomorphism is injective).

<1>4. Since $K$ is finite, $\varphi$ is surjective (an injective map from a finite set to itself is bijective).
Proof: <1>3 and finiteness.

<1>5. Hence every element $a \in K$ has a $p$th root: there is $x \in K$ with $x^p = a$.
Proof: <1>4 (surjectivity of $\varphi$).

<1>6. The root is unique: if $x^p = y^p$, then $(x - y)^p = x^p - y^p = 0$, so $x - y = 0$ (since $K$ is a field, hence an integral domain), i.e. $x = y$.
Proof: <1>2 and the domain property.

<1>7. Hence every element of $K$ has a unique $p$th root.
Proof: <1>5 and <1>6.

<1>8. Q.E.D.
Proof: <1>7.
:::
