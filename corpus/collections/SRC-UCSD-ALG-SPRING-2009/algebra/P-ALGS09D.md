---
schema: qual/card@1
id: P-ALGS09D
kind: problem
title: "Galois group of the splitting field of sqrt(2 + sqrt(2)) over Q"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $\alpha = \sqrt{2 + \sqrt{2}}$ in $\mathbb{C}$ and let $f$ be the minimal polynomial of $\alpha$ over $\mathbb{Q}$.
Let $E$ be the splitting field for $f$ over $\mathbb{Q}$.
Determine the Galois group $\operatorname{Gal}(E/\mathbb{Q})$.
:::

::: {.solution}
<1>1. $\alpha^2 = 2 + \sqrt{2}$, so $\alpha$ satisfies $(\alpha^2 - 2)^2 = 2$, i.e. $\alpha^4 - 4\alpha^2 + 2 = 0$.
::: {.proof}
square both sides.
:::

<1>2. $f(x) = x^4 - 4x^2 + 2$ is irreducible over $\QQ$.
::: {.proof}
it is Eisenstein at $p = 2$ (leading coefficient $1$, all other coefficients divisible by $2$, constant term $2$ not divisible by $4$).
:::

<1>3. Hence $f$ is the minimal polynomial of $\alpha$ and $[\QQ(\alpha) : \QQ] = 4$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. The roots of $f$ are $\pm \sqrt{2 \pm \sqrt{2}}$.
::: {.proof}
solving $x^2 = 2 \pm \sqrt{2}$.
:::

<1>5. The splitting field is $E = \QQ(\sqrt{2 + \sqrt{2}}, \sqrt{2 - \sqrt{2}})$.
::: {.proof}
<1>4.
:::

<1>6. $E = \QQ(\zeta_8)$, the cyclotomic field of $8$-th roots of unity.
::: {.proof}
$\sqrt{2 + \sqrt{2}} = 2\cos(\pi/8)$ and $\sqrt{2 - \sqrt{2}} = 2\sin(\pi/8)$, so $E$ contains $\zeta_8 = \cos(\pi/4) + i\sin(\pi/4)$; conversely $\zeta_8$ generates these.
:::

<1>7. $\operatorname{Gal}(\QQ(\zeta_8)/\QQ) \cong (\ZZ/8\ZZ)^\times$.
::: {.proof}
standard cyclotomic Galois theory.
:::

<1>8. $(\ZZ/8\ZZ)^\times = \{1, 3, 5, 7\} \cong \ZZ/2 \times \ZZ/2$.
::: {.proof}
the units modulo $8$ form the Klein four-group.
:::

<1>9. Hence $\operatorname{Gal}(E/\QQ) \cong \ZZ/2 \times \ZZ/2$.
::: {.proof}
<1>7 and <1>8.
:::

<1>10. Q.E.D.
::: {.proof}
<1>9.
:::
:::
