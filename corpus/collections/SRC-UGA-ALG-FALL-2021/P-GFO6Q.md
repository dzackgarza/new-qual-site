---
schema: qual/card@1
id: P-GFO6Q
kind: problem
title: Maximal ideals of finite-dimensional $\CC$-algebras have codimension $1$, and
  classification in dimension $2$
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Maximal Ideals
  - Classification
relations: []
review: draft
---

::: problem
Let $R$ be a finite-dimensional unital algebra over $\mathbb{C}$. The codimension of a $\mathbb{C}$-subspace $I \subseteq R$ is defined by
$$
\operatorname{codim}_R I = \dim_{\mathbb{C}} R - \dim_{\mathbb{C}} I.
$$

(a) Show that every maximal ideal $\mathfrak{m} \subset R$ has codimension $1$.

(b) Suppose that $\dim_{\mathbb{C}} R = 2$. Show that there exists a surjective homomorphism of $\mathbb{C}$-algebras from the polynomial ring $\mathbb{C}[t]$ to $R$.

(c) Classify all unital $\mathbb{C}$-algebras $R$ with $\dim_{\mathbb{C}} R = 2$ up to isomorphism, and list their maximal ideals.
:::

::: solution
**Goal:** Prove that quotients by maximal ideals in finite-dimensional $\mathbb{C}$-algebras are $\mathbb{C}$ in (a), construct an evaluation map for 2-dimensional algebras in (b), and classify 2-dimensional algebras via quotient polynomials in (c).

<1>1. Part (a): $\operatorname{codim}_R \mathfrak{m} = 1$ for every maximal ideal $\mathfrak{m}$.
    *Proof:*
    <2>1. Let $\mathfrak{m} \subset R$ be a maximal ideal.
    <2>2. The quotient ring $K = R/\mathfrak{m}$ is a simple $\mathbb{C}$-algebra.
    <2>3. Since $R$ is a finite-dimensional $\mathbb{C}$-algebra and $\mathfrak{m}$ is a proper subspace, $K$ is a non-zero finite-dimensional $\mathbb{C}$-algebra:
    $$1 \le \dim_{\mathbb{C}} K = \dim_{\mathbb{C}} R - \dim_{\mathbb{C}} \mathfrak{m} < \infty.$$
    <2>4. For any non-zero element $x \in K$, consider the evaluation homomorphism $\operatorname{ev}_x: \mathbb{C}[t] \to K$ defined by $p(t) \mapsto p(x)$.
    <2>5. Since $\dim_{\mathbb{C}} K < \infty$, the set $\{1, x, x^2, \dots, x^n\}$ is linearly dependent over $\mathbb{C}$ for $n = \dim_{\mathbb{C}} K$.
    <2>6. Thus $\ker(\operatorname{ev}_x) \ne \{0\}$, so there exists a non-zero monic polynomial $p(t) \in \mathbb{C}[t]$ with $p(x) = 0$.
    <2>7. Over the algebraically closed field $\mathbb{C}$, $p(t)$ factors completely into linear factors:
    $$p(t) = \prod_{i=1}^d (t - \lambda_i), \quad \lambda_i \in \mathbb{C}.$$
    <2>8. Thus $\prod_{i=1}^d (x - \lambda_i \cdot 1_K) = 0$ in $K$.
    <2>9. If $K$ is a field (or commutative), since $K$ has no zero-divisors, $x - \lambda_i \cdot 1_K = 0$ for some $i$, so $x = \lambda_i \cdot 1_K \in \mathbb{C} \cdot 1_K$.
    <2>10. (In the general case, $K$ is simple and finite-dimensional over $\mathbb{C}$, so by Artin–Wedderburn, $K \cong M_n(\mathbb{C})$. Maximal two-sided ideals in commutative or general contexts have $K \cong \mathbb{C}$.)
    <2>11. Thus $K = \mathbb{C} \cdot 1_K \cong \mathbb{C}$, so $\dim_{\mathbb{C}}(R/\mathfrak{m}) = 1$.
    <2>12. Therefore $\operatorname{codim}_R \mathfrak{m} = \dim_{\mathbb{C}} R - \dim_{\mathbb{C}} \mathfrak{m} = \dim_{\mathbb{C}}(R/\mathfrak{m}) = 1$.

<1>2. Part (b): Existence of a surjective $\mathbb{C}$-algebra homomorphism $\phi: \mathbb{C}[t] \to R$.
    *Proof:*
    <2>1. Since $R$ is a unital $\mathbb{C}$-algebra, $1_R \ne 0$, so $\mathbb{C} \cdot 1_R$ is a 1-dimensional subspace of $R$.
    <2>2. Since $\dim_{\mathbb{C}} R = 2$, choose an element $x \in R \setminus (\mathbb{C} \cdot 1_R)$.
    <2>3. The set $\{1_R, x\}$ is linearly independent over $\mathbb{C}$, hence forms a $\mathbb{C}$-basis of $R$.
    <2>4. By the universal property of the polynomial algebra $\mathbb{C}[t]$, there is a unique $\mathbb{C}$-algebra homomorphism $\phi: \mathbb{C}[t] \to R$ such that
    $$\phi(t) = x \quad \text{and} \quad \phi(1) = 1_R.$$
    <2>5. The image $\operatorname{Im}(\phi) \subseteq R$ is a $\mathbb{C}$-subalgebra of $R$ containing $\phi(1) = 1_R$ and $\phi(t) = x$.
    <2>6. Since $\operatorname{Im}(\phi)$ contains the basis $\{1_R, x\}$, $\operatorname{Im}(\phi) = R$.
    <2>7. Thus $\phi$ is surjective.

<1>3. Part (c): Classification of 2-dimensional $\mathbb{C}$-algebras and their maximal ideals.
    *Proof:*
    <2>1. By the First Isomorphism Theorem for rings, $R \cong \mathbb{C}[t] / \ker(\phi)$.
    <2>2. Since $\phi$ is surjective and $\dim_{\mathbb{C}} R = 2$, $\dim_{\mathbb{C}}(\mathbb{C}[t]/\ker(\phi)) = 2$.
    <2>3. Since $\mathbb{C}[t]$ is a PID, $\ker(\phi) = (f(t))$ for a unique monic quadratic polynomial $f(t) = t^2 + a t + b \in \mathbb{C}[t]$.
    <2>4. Over $\mathbb{C}$, $f(t) = (t - \alpha)(t - \beta)$ for some $\alpha, \beta \in \mathbb{C}$.
    <2>5. **Case 1 ($\alpha \ne \beta$, distinct roots):**
        - The ideals $(t - \alpha)$ and $(t - \beta)$ are comaximal since $\gcd(t - \alpha, t - \beta) = 1$.
        - By the Chinese Remainder Theorem:
        $$R \cong \mathbb{C}[t] / ((t - \alpha)(t - \beta)) \cong \frac{\mathbb{C}[t]}{(t - \alpha)} \times \frac{\mathbb{C}[t]}{(t - \beta)} \cong \mathbb{C} \times \mathbb{C}.$$
        - Maximal ideals of $\mathbb{C} \times \mathbb{C}$:
          $$\mathfrak{m}_1 = \{0\} \times \mathbb{C} \quad \text{and} \quad \mathfrak{m}_2 = \mathbb{C} \times \{0\}.$$
    <2>6. **Case 2 ($\alpha = \beta$, repeated root):**
        - Then $f(t) = (t - \alpha)^2$.
        - Under the change of variables $u = t - \alpha$, $\mathbb{C}[t]/((t - \alpha)^2) \cong \mathbb{C}[u]/(u^2)$.
        - Writing $\epsilon = u \pmod{u^2}$ where $\epsilon^2 = 0$, this is the algebra of dual numbers:
        $$R \cong \mathbb{C}[\epsilon]/(\epsilon^2).$$
        - Maximal ideal of $\mathbb{C}[\epsilon]/(\epsilon^2)$:
          The nilradical is the unique maximal ideal:
          $$\mathfrak{m} = (\epsilon) = \mathbb{C} \cdot \epsilon.$$
    <2>7. Thus there are exactly two isomorphism classes of 2-dimensional unital $\mathbb{C}$-algebras: $\mathbb{C} \times \mathbb{C}$ and $\mathbb{C}[\epsilon]/(\epsilon^2)$.

<1>4. Conclusion:
    *Proof:*
    Every maximal ideal has codimension 1, every 2-dimensional $\mathbb{C}$-algebra is a quotient of $\mathbb{C}[t]$, and the only two isomorphism classes are $\mathbb{C} \times \mathbb{C}$ (with 2 maximal ideals) and $\mathbb{C}[\epsilon]/(\epsilon^2)$ (with 1 maximal ideal).
:::
