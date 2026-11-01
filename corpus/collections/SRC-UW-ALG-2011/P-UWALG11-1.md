---
schema: qual/card@1
id: P-UWALG11-1
kind: problem
title: 'Two elements of order $n$ in $\operatorname{PGL}_2(\CC)$: one is conjugate to a power of the other'
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2011`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved, in fact with $m=1$: a lift of an element of order $n$ satisfies $\hat A^n=\lambda I$ with
    $\lambda\ne0$, hence is diagonalisable, and the ratio of its eigenvalues is a primitive $n$-th
    root of unity; so every element of order $n$ in $\operatorname{PGL}_2(\CC)$ is conjugate to the
    class of $\operatorname{diag}(\zeta,1)$, and two such are conjugate to each other. Nothing is
    left in outline.
---
---

::: {.problem}
Let $\GL_2(\CC)$ be the general linear group of $2\times2$ complex matrices, let $H$ be the subgroup of $\GL_2(\CC)$ consisting of non-zero multiples of the identity matrix, and let $\operatorname{PGL}_2(\CC)$ be the quotient group $\GL_2(\CC)/H$.

Let $A,B\in\operatorname{PGL}_2(\CC)$, and assume that both elements have order $n$.
Prove that there exist $C\in\operatorname{PGL}_2(\CC)$ and a positive integer $m$ such that
$$
CBC^{-1}=A^m.
$$
:::

::: {.solution}

Let $\pi:\GL_2(\CC)\to\operatorname{PGL}_2(\CC)=\GL_2(\CC)/\CC^\times$ be the quotient map.

::: pf

::: {.pf-step #s1}

If $A\in\operatorname{PGL}_2(\CC)$ has order $n$, then any lift $\hat A\in\GL_2(\CC)$ satisfies $\hat A^n=\lambda I$ for some $\lambda\in\CC^\times$, hence $\hat A$ is diagonalisable.

::: {.pf-proof}

$\pi(\hat A^n)=\pi(\hat A)^n=A^n=1$, so $\hat A^n\in\ker\pi=\CC^\times I$, say $\hat A^n=\lambda I$. The scalar $\lambda$ is nonzero because $\hat A$ is invertible.

The polynomial $T^n-\lambda$ has nonzero constant term, so $0$ is not a root and its roots are distinct: its derivative is $nT^{n-1}$, whose only root is $0$, and $\lambda\ne0$. A matrix annihilated by a polynomial with distinct roots is diagonalisable.

:::

:::

::: {.pf-step #s2}

With $\hat A$ diagonalisable, write $\hat A\sim\operatorname{diag}(\mu_1,\mu_2)$; then $\zeta=\mu_1/\mu_2$ is a primitive $n$-th root of unity.

::: {.pf-proof}

From $\hat A^n=\lambda I$ and diagonalisability, $\mu_i^n=\lambda$ for $i=1,2$, so $(\mu_1/\mu_2)^n=1$: $\zeta$ is an $n$-th root of unity.

If $\zeta$ had order $d<n$, then $\mu_1^d=\mu_2^d$, so
$$
\hat A^d\sim\operatorname{diag}(\mu_1^d,\mu_2^d)=\mu_2^d\,I,
$$
that is $\hat A^d\in\CC^\times I$, so $A^d=1$ in $\operatorname{PGL}_2(\CC)$, contradicting that $A$ has order exactly $n$. Hence $\zeta$ is a primitive $n$-th root of unity.

:::

:::

::: {.pf-step #s3}

Consequently every element of order $n$ in $\operatorname{PGL}_2(\CC)$ is conjugate to the class of $\operatorname{diag}(\zeta,1)$ for a primitive $n$-th root $\zeta$, and any two such classes for the same $n$ are conjugate.

::: {.pf-proof}

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\hat A\sim\operatorname{diag}(\mu_1,\mu_2)$ with $\mu_1/\mu_2=\zeta$ primitive. Multiplying by the scalar $\mu_2^{-1}$, which does not change the class in $\operatorname{PGL}_2$,
$$
A=\pi(\hat A)=\pi\bigl(\operatorname{diag}(\zeta,1)\bigr).
$$
Since conjugation by a matrix commutes with $\pi$, and any two diagonal matrices with the same ratio of eigenvalues are conjugate in $\GL_2$, all elements of order $n$ are conjugate to one another.

:::

:::

::: {.pf-step #s4}

Conclusion: taking $C$ with $CBC^{-1}=A$, one has $CBC^{-1}=A^1$, so the assertion holds with $m=1$.

::: {.pf-proof}

$A$ and $B$ both have order $n$, so by step [](#s3){.pf-ref} both are conjugate to the class of $\operatorname{diag}(\zeta,1)$; conjugacy is an equivalence relation, so there is $C\in\operatorname{PGL}_2(\CC)$ with $CBC^{-1}=A$. Taking $m=1$ gives $CBC^{-1}=A^m$.

Note that the conclusion is stronger than asked: no choice of $m\ne1$ is ever needed, and the real content is the classification of finite-order elements of $\operatorname{PGL}_2(\CC)$ up to conjugacy, in which the order $n$ determines the conjugacy class completely.

:::

:::

:::

:::
