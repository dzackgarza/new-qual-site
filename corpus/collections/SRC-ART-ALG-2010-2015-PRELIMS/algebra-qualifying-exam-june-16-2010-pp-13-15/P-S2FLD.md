---
schema: qual/card@1
id: P-S2FLD
kind: problem
title: Whether $\QQ(\sqrt[3]{2})$ and $\QQ(\sqrt{2}+\sqrt{5})$ are splitting
  fields over $\QQ$
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
Decide whether or not each of the following fields is a splitting field over $\QQ$.

(a) $\QQ(\sqrt[3]{2})$.

(b) $\QQ(\sqrt{2} + \sqrt{5})$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The field $\QQ(\sqrt[3]{2})$ is not a splitting
field over $\QQ$.

::: pf-proof

Put $a=\sqrt[3]{2}>0$. The polynomial $T^3-2$ is
Eisenstein at two, hence irreducible over $\QQ$
[@DF04]. Its roots are $a,\zeta a,\zeta^2 a$, where
$\zeta=e^{2\pi i/3}$ is a nonreal primitive cube root
of unity. The field $\QQ(a)$ lies in $\RR$
and therefore does not contain the latter two roots.
An irreducible polynomial over $\QQ$ has a root
in this field without splitting there, so the extension
is not normal. Every splitting field over a field is
a normal extension [@DF04]. Consequently $\QQ(a)$
cannot be the splitting field of any polynomial over
$\QQ$, not just of $T^3-2$.

:::

:::

::: {.pf-step #s2}

The field $\QQ(\sqrt2+\sqrt5)$ is the splitting
field of $(T^2-2)(T^2-5)$ over $\QQ$.

::: pf-proof

Let $s=\sqrt2+\sqrt5>0$. Since
$$
(\sqrt5-\sqrt2)s=5-2=3,
$$
one has $\sqrt5-\sqrt2=3/s\in\QQ(s)$.
Adding and subtracting this identity from the definition
of $s$ gives
$$
\sqrt5=\frac{s+3/s}{2},\qquad
\sqrt2=\frac{s-3/s}{2}.
$$
Thus both radicals lie in $\QQ(s)$, and the reverse
containment is immediate from $s=\sqrt2+\sqrt5$.
Therefore
$\QQ(s)=\QQ(\sqrt2,\sqrt5)$.

The roots of $(T^2-2)(T^2-5)$ are exactly
$\sqrt2,-\sqrt2,\sqrt5,-\sqrt5$. They all belong to
this field, and the field they generate is exactly
$\QQ(\sqrt2,\sqrt5)=\QQ(s)$.
This proves that it is the asserted splitting field.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} answers part (a), and step [](#s2){.pf-ref} answers part (b).

:::

:::

:::
