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
---

::: problem
(a) Let $K/F$ be a field extension and let $f \in F[x]$.
If $A = F[x]/(f)$, show that $K \otimes_F A \cong K[x]/(f)$ as $F$-algebras.

(b) Again let $K/F$ be a field extension, assume that $\mathrm{char}\, F = 0$, and let $\alpha, \beta \in K$ be algebraic over $F$.
Let $F_1 = F(\alpha)$ and $F_2 = F(\beta)$.
Consider the $F$-algebra $R = F_1 \otimes_F F_2$.
Show that $R$ is isomorphic as a ring to a direct product of finitely many fields.
:::

::: {.solution}
**(a).**

<1>1. $A = F[x]/(f)$, so $K \otimes_F A = K \otimes_F (F[x]/(f))$.
Proof: definition of $A$.

<1>2. $K \otimes_F F[x] \cong K[x]$ (tensoring the polynomial ring with $K$ gives the polynomial ring over $K$).
Proof: $K \otimes_F F[x] \cong K[x]$ via $k \otimes x^n \mapsto k x^n$.

<1>3. $K \otimes_F (F[x]/(f)) \cong (K \otimes_F F[x])/(K \otimes_F (f)) \cong K[x]/(f)$.
Proof: tensor product is right-exact, so $K \otimes_F (F[x]/(f)) \cong (K \otimes_F F[x])/(\operatorname{im}(K \otimes_F (f)))$, and the image of $(f)$ is the ideal $(f)$ in $K[x]$.

<1>4. Hence $K \otimes_F A \cong K[x]/(f)$ as $F$-algebras.
Proof: <1>2 and <1>3.

**(b).**

<1>1. $F_1 = F(\alpha) \cong F[x]/(m_\alpha)$ and $F_2 = F(\beta) \cong F[x]/(m_\beta)$, where $m_\alpha, m_\beta$ are the minimal polynomials.
Proof: simple algebraic extensions.

<1>2. $R = F_1 \otimes_F F_2 \cong F[x]/(m_\alpha) \otimes_F F[x]/(m_\beta) \cong F_1[x]/(m_\beta)$.
Proof: <1>1 and part (a) (with $K = F_1$, $f = m_\beta$).

<1>3. Over $F_1$, the polynomial $m_\beta$ factors as $m_\beta = p_1^{e_1} \cdots p_r^{e_r}$ into distinct irreducibles $p_i$ (with $e_i = 1$ since $\operatorname{char} F = 0$ implies separability).
Proof: $m_\beta$ is separable (characteristic $0$), so it has no repeated irreducible factors.

<1>4. By the Chinese remainder theorem, $F_1[x]/(m_\beta) \cong \prod_{i=1}^{r} F_1[x]/(p_i)$.
Proof: <1>3 (the $p_i$ are pairwise coprime).

<1>5. Each $F_1[x]/(p_i)$ is a field (since $p_i$ is irreducible).
Proof: quotient of a polynomial ring by an irreducible polynomial is a field.

<1>6. Hence $R \cong \prod_{i=1}^{r} F_1[x]/(p_i)$ is a direct product of finitely many fields.
Proof: <1>4 and <1>5.

<1>7. Q.E.D.
Proof: <1>4 (a) and <1>6 (b).
:::
