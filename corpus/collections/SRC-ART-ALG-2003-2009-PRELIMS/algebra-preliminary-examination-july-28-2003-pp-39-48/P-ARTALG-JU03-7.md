---
schema: qual/card@1
id: P-ARTALG-JU03-7
kind: problem
title: Removing a base-field linear factor preserves the splitting field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the arbitrary base field and the base-field root hypothesis with July 2003 problem 7 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked equality of the generated root fields, repeated roots, inseparable polynomials, and the constant quotient when the original polynomial is linear."
---

::: problem
Prove that if $F$ is a field and $g(x) \in F[x]$ has a root $\alpha \in F$, then its Galois group is the same as the Galois group of $g(x)/(x - \alpha)$.
:::

::: solution
The Galois group of a nonzero polynomial means the group of
$F$-automorphisms of its splitting field. As usual this notation
presupposes $g\ne0$. Fix an algebraic closure $\overline F$.

<1>1. The quotient $h(x)=g(x)/(x-\alpha)$ belongs to $F[x]$.

::: proof
Division by the monic linear polynomial $x-\alpha$ gives
$g=(x-\alpha)h+c$, with $h\in F[x]$ and $c\in F$.
Evaluation at $\alpha$ gives $c=g(\alpha)=0$.
Since $g\ne0$, the quotient $h$ is nonzero and
$\deg h=\deg g-1$.
:::

<1>2. The two splitting fields inside $\overline F$ are equal.

::: proof
Let $R_g$ and $R_h$ be the sets of roots in $\overline F$,
without counting multiplicities. The identity
$g=(x-\alpha)h$ implies
$$
R_g=R_h\cup\{\alpha\}.
$$
Indeed, for any $b\in\overline F$, the product
$(b-\alpha)h(b)$ vanishes exactly when one of its factors does.
Since $\alpha\in F$, adjoining it does not enlarge any extension
of $F$. The generated fields therefore satisfy
$$
F(R_g)=F(R_h,\alpha)=F(R_h).
$$
These are exactly the two splitting fields. If $\deg g=1$,
then $h$ is a nonzero constant, $R_h$ is empty, and both fields
are $F$; the same equality covers that case.
:::

<1>3. The Galois groups coincide.

::: proof
Writing the common splitting field as $L$, both groups are
literally $\operatorname{Aut}_F(L)$, with the same composition
law. No separability assumption was used. A repeated root
$\alpha$ may still belong to $R_h$, but the root-set union and
the field equality in step <1>2 remain valid.
:::
:::
