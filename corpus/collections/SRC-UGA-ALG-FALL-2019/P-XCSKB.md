---
schema: qual/card@1
id: P-XCSKB
kind: problem
title: Torsion elements form a submodule over an integral domain but not in general,
  and every module over a ring with zero-divisors has torsion
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
  - Integral Domains
relations: []
review: draft
---

::: problem
Let $R$ be a commutative ring with identity $1 \ne 0$, and let $M$ be an $R$-module. Recall that the set of torsion elements of $M$ is defined by
$$
\operatorname{tor}(M) = \{m \in M \mid \exists r \in R \setminus \{0\} \text{ such that } r m = 0\}.
$$

(a) Prove that if $R$ is an integral domain, then $\operatorname{tor}(M)$ is an $R$-submodule of $M$.

(b) Give an example where $\operatorname{tor}(M)$ is not an $R$-submodule of $M$.

(c) If $R$ has zero-divisors, prove that every non-zero $R$-module $M \ne \{0\}$ contains at least one non-zero torsion element.
:::

::: solution
**Goal:** Prove that $\operatorname{tor}(M)$ is a submodule over integral domains in (a), provide a counterexample over non-domains in (b), and prove the existence of non-zero torsion elements over rings with zero-divisors in (c).

<1>1. Part (a): $\operatorname{tor}(M)$ is an $R$-submodule when $R$ is an integral domain.
::: {.proof}
    <2>1. Non-empty: $0 \in \operatorname{tor}(M)$ since $1 \cdot 0 = 0$ and $1 \ne 0$ in $R$.
    <2>2. Closure under scalar multiplication:
        - Let $m \in \operatorname{tor}(M)$ and $r \in R$.
        - There exists $s \in R \setminus \{0\}$ such that $s m = 0$.
        - Then $s (r m) = r (s m) = r \cdot 0 = 0$ by commutativity of $R$.
        - Since $s \ne 0$, $r m \in \operatorname{tor}(M)$.
    <2>3. Closure under addition:
        - Let $m_1, m_2 \in \operatorname{tor}(M)$.
        - There exist $s_1, s_2 \in R \setminus \{0\}$ such that $s_1 m_1 = 0$ and $s_2 m_2 = 0$.
        - Multiply the sum $m_1 + m_2$ by $s_1 s_2 \in R$:
        $$(s_1 s_2)(m_1 + m_2) = s_2 (s_1 m_1) + s_1 (s_2 m_2) = s_2 \cdot 0 + s_1 \cdot 0 = 0.$$
        - Since $R$ is an integral domain and $s_1 \ne 0, s_2 \ne 0$, the product $s_1 s_2 \ne 0$.
        - Thus $m_1 + m_2 \in \operatorname{tor}(M)$.
    <2>4. Therefore $\operatorname{tor}(M)$ is an $R$-submodule of $M$.

:::

<1>2. Part (b): Counterexample where $\operatorname{tor}(M)$ is not a submodule.
::: {.proof}
    <2>1. Let $R = \mathbb{Z}/6\mathbb{Z}$ and consider $M = R = \mathbb{Z}/6\mathbb{Z}$ as a regular module over itself.
    <2>2. The element $\bar{2} \in \mathbb{Z}/6\mathbb{Z}$ is torsion: $3 \cdot \bar{2} = \bar{6} = \bar{0}$ with $\bar{3} \ne \bar{0}$, so $\bar{2} \in \operatorname{tor}(M)$.
    <2>3. The element $\bar{3} \in \mathbb{Z}/6\mathbb{Z}$ is torsion: $2 \cdot \bar{3} = \bar{6} = \bar{0}$ with $\bar{2} \ne \bar{0}$, so $\bar{3} \in \operatorname{tor}(M)$.
    <2>4. The sum is $\bar{2} + \bar{3} = \bar{5}$.
    <2>5. Since $\gcd(5, 6) = 1$, $\bar{5}$ is a unit in $\mathbb{Z}/6\mathbb{Z}$ ($\bar{5}^2 = \bar{25} = \bar{1}$).
    <2>6. For any $r \in \mathbb{Z}/6\mathbb{Z}$, $r \cdot \bar{5} = \bar{0} \implies r = r \cdot \bar{5} \cdot \bar{5} = \bar{0} \cdot \bar{5} = \bar{0}$.
    <2>7. Thus $\bar{5} \notin \operatorname{tor}(M)$, showing that $\operatorname{tor}(M)$ is not closed under addition.

:::

<1>3. Part (c): Existence of non-zero torsion elements when $R$ has zero-divisors.
::: {.proof}
    <2>1. Since $R$ has zero-divisors, there exist non-zero elements $a, b \in R \setminus \{0\}$ such that $a b = 0$.
    <2>2. Let $M \ne \{0\}$ be any non-zero $R$-module. Choose a non-zero element $m \in M \setminus \{0\}$.
    <2>3. Consider the element $b m \in M$:
    <2>4. Case 1 ($b m = 0$):
        - The element $m \in M$ is non-zero, and $b m = 0$ with $b \in R \setminus \{0\}$.
        - Thus $m$ is a non-zero torsion element of $M$.
    <2>5. Case 2 ($b m \ne 0$):
        - Define $w = b m \in M \setminus \{0\}$.
        - Compute $a w = a (b m) = (a b) m = 0 \cdot m = 0$.
        - Since $a \in R \setminus \{0\}$ and $w \ne 0$, $w = b m$ is a non-zero torsion element of $M$.
    <2>6. In both cases, $M$ contains at least one non-zero torsion element.

:::

<1>4. Conclusion:
::: {.proof}
    $\operatorname{tor}(M)$ is a submodule over integral domains, fails to be a submodule in general rings, and non-zero modules over rings with zero-divisors always contain non-zero torsion elements.
:::
:::

