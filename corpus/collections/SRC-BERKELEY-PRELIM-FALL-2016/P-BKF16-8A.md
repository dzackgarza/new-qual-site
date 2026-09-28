---
schema: qual/card@1
id: P-BKF16-8A
kind: problem
title: Fields embedding in $M_2(\mathbb Q)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet. The
    necessity can be read directly from Q^2 as a vector space over the
    embedded field, while sufficiency is the regular representation of a
    quadratic extension.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked that a unital embedding restricts to the standard scalar action
    of Q, the Q-linear injection of K into Q^2 obtained from any nonzero
    vector, and faithfulness of the multiplication representation.
---

::: {.problem}
Let $M _ { 2 } ( \mathbb { Q } )$ be the ring of all $2 \times 2$ matrices with coefficients in Q. Describe all field extensions K of Q such that there is an injective ring homomorphism $K \to M _ { 2 } ( \mathbb { Q } )$ . (Note: we take the convention that a ring homomorphism maps the multiplicative identity to the multiplicative identity.)
:::

::: {.solution}
<1>1. Any unital ring homomorphism
$$
\iota:K\to M_2(\QQ)
$$
restricts on $\QQ\subset K$ to
$$
\iota(q)=qI_2.
$$

::: {.proof}
Since $\iota(1)=I_2$, additivity gives
$$
\iota(n)=nI_2
$$
for every integer $n$. If $n\ne0$, then
$$
\iota(1/n)\iota(n)=I_2,
$$
so
$$
\iota(1/n)=\frac1nI_2.
$$
Multiplicativity and additivity then give
$$
\iota(q)=qI_2
$$
for every rational $q$.
:::

<1>2. If an injective unital homomorphism
$$
\iota:K\hookrightarrow M_2(\QQ)
$$
exists, then $\QQ^2$ becomes a nonzero vector space over $K$.

::: {.proof}
Define scalar multiplication by
$$
a\cdot v\coloneqq\iota(a)v,
\qquad
a\in K,\ v\in\QQ^2.
$$
The ring-homomorphism identities give the vector-space axioms, and
$\iota(1)=I_2$ gives
$$
1\cdot v=v.
$$
Step <1>1 shows that the resulting action of the subfield $\QQ$ is the
ordinary rational scalar multiplication.
:::

<1>3. Under the hypothesis of step <1>2,
$$
[K:\QQ]\le2.
$$

::: {.proof}
Choose a nonzero vector
$$
v\in\QQ^2.
$$
The map
$$
\Phi:K\longrightarrow\QQ^2,
\qquad
a\longmapsto a\cdot v
$$
is $\QQ$-linear by step <1>1. It is injective: if
$$
\Phi(a)=a\cdot v=0
$$
and $a\ne0$, multiplication by $a^{-1}$ in the $K$-vector space would
give $v=0$, a contradiction. Hence $K$, as a $\QQ$-vector space,
injects into the $2$-dimensional $\QQ$-vector space $\QQ^2$.
Therefore
$$
[K:\QQ]\le2.
$$
:::

<1>4. Consequently, an embeddable field $K$ is either
$$
K=\QQ
$$
or a quadratic extension of $\QQ$.

::: {.proof}
By step <1>3,
$$
[K:\QQ]\in\{1,2\}.
$$
Degree $1$ means $K=\QQ$, while degree $2$ means exactly that $K/\QQ$
is quadratic.
:::

<1>5. The field $\QQ$ embeds unitally in $M_2(\QQ)$.

::: {.proof}
The map
$$
q\longmapsto qI_2
$$
is an injective unital ring homomorphism.
:::

<1>6. Every quadratic extension $K/\QQ$ embeds unitally in
$M_2(\QQ)$.

::: {.proof}
View $K$ as a $2$-dimensional vector space over $\QQ$. For
$a\in K$, let
$$
L_a:K\to K,
\qquad
x\longmapsto ax.
$$
This is $\QQ$-linear. The assignment
$$
a\longmapsto L_a
$$
satisfies
$$
L_{a+b}=L_a+L_b,
\qquad
L_{ab}=L_aL_b,
\qquad
L_1=\operatorname{Id}_K,
$$
so it is a unital ring homomorphism
$$
K\to\operatorname{End}_{\QQ}(K).
$$
It is injective because
$$
L_a=0
\quad\Longrightarrow\quad
a=L_a(1)=0.
$$
After choosing a $\QQ$-basis of the $2$-dimensional space $K$, one has
$$
\operatorname{End}_{\QQ}(K)\cong M_2(\QQ),
$$
which gives the required embedding.
:::

<1>7. Therefore the complete list is
$$
\boxed{
K=\QQ
\quad\text{or}\quad
[K:\QQ]=2.
}
$$

::: {.proof}
Step <1>4 proves necessity, while steps <1>5--<1>6 prove sufficiency.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the requested classification.
:::
:::
