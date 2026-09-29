---
schema: qual/card@1
id: P-ALGS15B
kind: problem
title: $K \otimes_F F[x]/(f)$; tensor product of simple extensions in characteristic zero
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
(a) Let $K/F$ be a field extension and let $f \in F[x]$.
If $A = F[x]/(f)$, show that $K \otimes_F A \cong K[x]/(f)$ as $F$-algebras.

(b) Again let $K/F$ be a field extension, assume that $\mathrm{char}\, F = 0$, and let $\alpha, \beta \in K$ be algebraic over $F$.
Let $F_1 = F(\alpha)$ and $F_2 = F(\beta)$.
Consider the $F$-algebra $R = F_1 \otimes_F F_2$.
Show that $R$ is isomorphic as a ring to a direct product of finitely many fields.
:::

::: {.solution}
**(a).**

::: pf

::: pf-step
$A = F[x]/(f)$, so $K \otimes_F A = K \otimes_F (F[x]/(f))$.

::: pf-proof
definition of $A$.
:::

:::

::: {.pf-step #p1-s2}
$K \otimes_F F[x] \cong K[x]$ (tensoring the polynomial ring with $K$ gives the polynomial ring over $K$).

::: pf-proof
$K \otimes_F F[x] \cong K[x]$ via $k \otimes x^n \mapsto k x^n$.
:::

:::

::: {.pf-step #p1-s3}
$K \otimes_F (F[x]/(f)) \cong (K \otimes_F F[x])/(K \otimes_F (f)) \cong K[x]/(f)$.

::: pf-proof
tensor product is right-exact, so $K \otimes_F (F[x]/(f)) \cong (K \otimes_F F[x])/(\operatorname{im}(K \otimes_F (f)))$, and the image of $(f)$ is the ideal $(f)$ in $K[x]$.
:::

:::

::: {.pf-step #p1-s4}
Hence $K \otimes_F A \cong K[x]/(f)$ as $F$-algebras.

::: pf-proof
step [](#p1-s2){.pf-ref} and step [](#p1-s3){.pf-ref}.
:::

:::

:::

**(b).**

::: pf

::: {.pf-step #p2-s1}
$F_1 = F(\alpha) \cong F[x]/(m_\alpha)$ and $F_2 = F(\beta) \cong F[x]/(m_\beta)$, where $m_\alpha, m_\beta$ are the minimal polynomials.

::: pf-proof
simple algebraic extensions.
:::

:::

::: pf-step
$R = F_1 \otimes_F F_2 \cong F[x]/(m_\alpha) \otimes_F F[x]/(m_\beta) \cong F_1[x]/(m_\beta)$.

::: pf-proof
step [](#p2-s1){.pf-ref} and part (a) (with $K = F_1$, $f = m_\beta$).
:::

:::

::: {.pf-step #p2-s3}
Over $F_1$, the polynomial $m_\beta$ factors as $m_\beta = p_1^{e_1} \cdots p_r^{e_r}$ into distinct irreducibles $p_i$ (with $e_i = 1$ since $\operatorname{char} F = 0$ implies separability).

::: pf-proof
$m_\beta$ is separable (characteristic $0$), so it has no repeated irreducible factors.
:::

:::

::: {.pf-step #p2-s4}
By the Chinese remainder theorem, $F_1[x]/(m_\beta) \cong \prod_{i=1}^{r} F_1[x]/(p_i)$.

::: pf-proof
step [](#p2-s3){.pf-ref} (the $p_i$ are pairwise coprime).
:::

:::

::: {.pf-step #p2-s5}
Each $F_1[x]/(p_i)$ is a field (since $p_i$ is irreducible).

::: pf-proof
quotient of a polynomial ring by an irreducible polynomial is a field.
:::

:::

::: {.pf-step #p2-s6}
Hence $R \cong \prod_{i=1}^{r} F_1[x]/(p_i)$ is a direct product of finitely many fields.

::: pf-proof
step [](#p2-s4){.pf-ref} and step [](#p2-s5){.pf-ref}.
:::

:::

::: pf-qed
step [](#p1-s4){.pf-ref} (a) and step [](#p2-s6){.pf-ref} (b).
:::

:::
:::
