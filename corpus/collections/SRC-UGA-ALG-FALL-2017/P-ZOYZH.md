---
schema: qual/card@1
id: P-ZOYZH
kind: problem
title: Commutative unital simple rings are fields, and $M_n(k)$ is simple
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Ideals
  - Semisimplicity
relations: []
review: draft
---

::: problem
A ring $R$ is called *simple* if its only two-sided ideals are $\{0\}$ and $R$.

(a) Suppose $R$ is a commutative ring with identity $1 \ne 0$. Prove that $R$ is simple if and only if $R$ is a field.

(b) Let $k$ be a field and $n \ge 1$. Show that the ring $M_n(k)$ of $n \times n$ matrices with entries in $k$ is a simple ring.
:::

::: solution
**Goal:** Prove that commutative unital simple rings are fields in (a), and that matrix rings $M_n(k)$ over a field are simple in (b) using matrix units.

<1>1. Part (a): $R$ is simple if and only if $R$ is a field.
    *Proof:*
    <2>1. Forward direction ($\implies$):
        - Assume $R$ is simple, commutative, with $1 \ne 0$.
        - Let $x \in R \setminus \{0\}$ be a non-zero element.
        - The principal ideal $(x) = R x = \{r x \mid r \in R\}$ is an ideal of $R$.
        - Since $x = 1 \cdot x \in (x)$ and $x \ne 0$, the ideal $(x) \ne \{0\}$.
        - Because $R$ is simple, the only non-zero ideal is $R$, so $(x) = R$.
        - Since $1 \in R = (x)$, there exists $y \in R$ such that $y x = 1$.
        - By commutativity, $x y = y x = 1$, so $x$ is a unit in $R$.
        - Since every non-zero element of $R$ is invertible, $R$ is a field.
    <2>2. Reverse direction ($\impliedby$):
        - Assume $R$ is a field.
        - Let $I \subseteq R$ be an ideal such that $I \ne \{0\}$.
        - Choose a non-zero element $x \in I \setminus \{0\}$.
        - Since $R$ is a field, $x^{-1} \in R$.
        - Since $I$ is an ideal, $1 = x^{-1} x \in I$.
        - For every $r \in R$, $r = r \cdot 1 \in I$, so $I = R$.
        - Thus the only ideals of $R$ are $\{0\}$ and $R$, proving $R$ is simple.

<1>2. Part (b): $M_n(k)$ is a simple ring.
    *Proof:*
    <2>1. Let $I \subseteq M_n(k)$ be a non-zero two-sided ideal.
    <2>2. Matrix units: For $1 \le i, j \le n$, let $E_{i j} \in M_n(k)$ denote the standard matrix unit with 1 in the $(i, j)$-entry and 0 elsewhere.
    <2>3. Multiplication rule for matrix units:
    $$E_{p q} E_{r s} = \delta_{q r} E_{p s} = \begin{cases} E_{p s} & \text{if } q = r, \\ 0 & \text{if } q \ne r. \end{cases}$$
    <2>4. Non-zero entry extraction:
        - Since $I \ne \{0\}$, choose a non-zero matrix $A = (a_{p q}) \in I \setminus \{0\}$.
        - There exist indices $r, c \in \{1, \dots, n\}$ such that $a_{r c} \ne 0$.
        - Since $k$ is a field, the scalar $a_{r c} \in k^\times$ has an inverse $a_{r c}^{-1} \in k$.
    <2>5. Generation of all matrix units:
        - For any desired indices $i, j \in \{1, \dots, n\}$, compute the product:
        $$E_{i r} A E_{c j} = E_{i r} \left( \sum_{p=1}^n \sum_{q=1}^n a_{p q} E_{p q} \right) E_{c j} = \sum_{p, q} a_{p q} (E_{i r} E_{p q}) E_{c j} = \sum_{q} a_{r q} E_{i q} E_{c j} = a_{r c} E_{i j}.$$
        - Since $A \in I$ and $I$ is a two-sided ideal, $E_{i r} A E_{c j} \in I$, so $a_{r c} E_{i j} \in I$.
        - Multiplying by the central element $a_{r c}^{-1} I_n \in M_n(k)$ gives
        $$E_{i j} = (a_{r c}^{-1} I_n)(a_{r c} E_{i j}) \in I \quad \text{for all } 1 \le i, j \le n.$$
    <2>6. Inclusion of the identity:
        - The $n \times n$ identity matrix $I_n$ is the sum of diagonal matrix units:
        $$I_n = \sum_{i=1}^n E_{i i} \in I.$$
    <2>7. Full ring equality:
        - For any matrix $M \in M_n(k)$, $M = M I_n \in I$, so $I = M_n(k)$.
        - Thus the only two-sided ideals of $M_n(k)$ are $\{0\}$ and $M_n(k)$, so $M_n(k)$ is simple.

<1>3. Conclusion:
    *Proof:*
    Commutative unital simple rings are fields, and $M_n(k)$ is a simple ring.
:::
