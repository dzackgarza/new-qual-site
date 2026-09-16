---
schema: qual/card@1
id: P-S2FLD
kind: problem
title: Whether $\mathbb{Q}(\sqrt[3]{2})$ and $\mathbb{Q}(\sqrt{2}+\sqrt{5})$ are splitting
  fields over $\mathbb{Q}$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared both fields with June 2010 Fields 4 on PDF page 15, including the cube root and the sum of square roots."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked nonnormality as an obstruction to being any splitting field, and explicitly recovered both radicals from their sum to identify the second splitting field."
---

::: {.problem}
Decide whether or not each of the following fields is a splitting field over $\mathbb{Q}$.

a. $\mathbb{Q}(\sqrt[3]{2})$.

b. $\mathbb{Q}(\sqrt{2} + \sqrt{5})$.
:::

::: {.solution}
<1>1. The field $\mathbb Q(\sqrt[3]{2})$ is not a splitting
field over $\mathbb Q$.

::: {.proof}
Put $a=\sqrt[3]{2}>0$. The polynomial $T^3-2$ is
Eisenstein at two, hence irreducible over $\mathbb Q$
[@DF04]. Its roots are $a,\zeta a,\zeta^2 a$, where
$\zeta=e^{2\pi i/3}$ is a nonreal primitive cube root
of unity. The field $\mathbb Q(a)$ lies in $\mathbb R$
and therefore does not contain the latter two roots.
An irreducible polynomial over $\mathbb Q$ has a root
in this field without splitting there, so the extension
is not normal. Every splitting field over a field is
a normal extension [@DF04]. Consequently $\mathbb Q(a)$
cannot be the splitting field of any polynomial over
$\mathbb Q$, not just of $T^3-2$.
:::

<1>2. The field $\mathbb Q(\sqrt2+\sqrt5)$ is the splitting
field of $(T^2-2)(T^2-5)$ over $\mathbb Q$.

::: {.proof}
Let $s=\sqrt2+\sqrt5>0$. Since
$$
(\sqrt5-\sqrt2)s=5-2=3,
$$
one has $\sqrt5-\sqrt2=3/s\in\mathbb Q(s)$.
Adding and subtracting this identity from the definition
of $s$ gives
$$
\sqrt5=\frac{s+3/s}{2},\qquad
\sqrt2=\frac{s-3/s}{2}.
$$
Thus both radicals lie in $\mathbb Q(s)$, and the reverse
containment is immediate from $s=\sqrt2+\sqrt5$.
Therefore
$\mathbb Q(s)=\mathbb Q(\sqrt2,\sqrt5)$.

The roots of $(T^2-2)(T^2-5)$ are exactly
$\sqrt2,-\sqrt2,\sqrt5,-\sqrt5$. They all belong to
this field, and the field they generate is exactly
$\mathbb Q(\sqrt2,\sqrt5)=\mathbb Q(s)$.
This proves that it is the asserted splitting field.
:::
:::
