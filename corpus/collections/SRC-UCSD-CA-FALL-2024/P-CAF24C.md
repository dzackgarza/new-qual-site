---
schema: qual/card@1
id: P-CAF24C
kind: problem
title: Bound and value at $1/3$ imply no zeros in $|z|<1/7$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $f : \mathbb{D} \to \mathbb{C}$ be holomorphic.
Assume that

(i) $|f(z)| < 2$ for all $z \in \mathbb{D}$,

(ii) $f\!\left(\dfrac{1}{3}\right) = 1$.

Show that $f$ has no zeros in the disc $|z| < \dfrac{1}{7}$.
:::

::: {.solution}
<1>1. Suppose for contradiction that $f(a) = 0$ for some $a$ with $|a| < 1/7$.
::: {.proof}
assume a zero exists in the given disc.
:::

<1>2. Define the automorphism $\phi_a(z) = \frac{z - a}{1 - \bar a z}$ of $\DD$, and set $g = f \circ \phi_a^{-1}$.
::: {.proof}
$\phi_a$ is a disk automorphism sending $a$ to $0$.
:::

<1>3. $g$ is holomorphic on $\DD$ with $|g| < 2$ and $g(0) = 0$.
::: {.proof}
$g(0) = f(\phi_a^{-1}(0)) = f(a) = 0$, and $|g| < 2$ since $|f| < 2$.
:::

<1>4. By the Schwarz lemma, $|g(w)| \le 2|w|$ for all $w \in \DD$.
::: {.proof}
apply the Schwarz lemma to $g/2$ (a holomorphic self-map of $\DD$ with $g(0)/2 = 0$).
:::

<1>5. Let $w_0 = \phi_a(1/3) = \frac{1/3 - a}{1 - a/3}$.
::: {.proof}
definition.
:::

<1>6. Then $1 = f(1/3) = g(w_0)$, so $|g(w_0)| = 1 \le 2|w_0|$, giving $|w_0| \ge 1/2$.
::: {.proof}
<1>4 and the hypothesis $f(1/3) = 1$.
:::

<1>7. But $|w_0| = \left|\frac{1/3 - a}{1 - a/3}\right| < \frac{1/3 + 1/7}{1 - 1/21} = \frac{10/21}{20/21} = \frac{1}{2}$.
::: {.proof}
$|a| < 1/7$, so $|1/3 - a| < 1/3 + 1/7 = 10/21$ and $|1 - a/3| > 1 - 1/21 = 20/21$.
:::

<1>8. Contradiction.
::: {.proof}
<1>6 says $|w_0| \ge 1/2$ but <1>7 says $|w_0| < 1/2$.
:::

<1>9. Hence $f$ has no zeros in $|z| < 1/7$.
::: {.proof}
<1>1–<1>8.
:::

<1>10. Q.E.D.
::: {.proof}
<1>9.
:::
:::
