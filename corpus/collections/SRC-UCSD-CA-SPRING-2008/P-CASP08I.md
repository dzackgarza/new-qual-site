---
schema: qual/card@1
id: P-CASP08I
kind: problem
title: A self-map of a bounded region with $f(a)=a$ and $f'(a)=1$ is the identity
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Taylor Series
relations: []
review: draft
---

::: {.problem}
Let $G$ be an open and bounded region in the plane. Suppose that $f(z)$ is analytic in $G$, $f(G) \subset G$, and that there exists $a \in G$ with $f(a) = a$ and $f'(a) = 1$. Show that $f(z)$ is the identity $f(z) \equiv z$.

Hint: First, show that it suffices to prove the statement when $0 \in G$ and $a = 0$. Then, suppose that the Taylor series of $f(z) - z$ at $a = 0$ is not identically zero. Consider the $n$th iterate $f^n := f \circ f \circ \cdots \circ f$ ($n$ times) and compute the first nonvanishing term in the Taylor series of $f^n(z) - z$ at $a = 0$.
:::

::: {.solution}
::: pf

::: {.pf-step #normalize}
It suffices to treat $a=0$.

::: pf-proof
Let $\tau(z)=z-a$. Then $\tilde G=\tau(G)$ is a bounded region containing $0$, and $\tilde f=\tau\circ f\circ\tau^{-1}$ maps $\tilde G$ into itself with $\tilde f(0)=0$ and $\tilde f'(0)=1$. If $\tilde f$ is the identity, so is $f$.
:::

:::

::: {.pf-step #iterate}
Suppose $f(z)-z$ is not identically $0$ near $0$, and write $f(z)=z+a_kz^k+O(z^{k+1})$ with $k\ge2$ and $a_k\ne0$. Then $f^n(z)=z+na_kz^k+O(z^{k+1})$ for every $n\ge1$.

::: pf-proof
Induction on $n$. If it holds for $n$, then
$$
f^{n+1}(z)=f^n(z)+a_k\bigl(f^n(z)\bigr)^k+O\bigl((f^n(z))^{k+1}\bigr)
=z+na_kz^k+a_kz^k+O(z^{k+1}),
$$
because $f^n(z)=z+O(z^2)$.
:::

:::

::: {.pf-step #cauchy}
$n\abs{a_k}\le R/r^k$ for every $n$, where $G\subset B(0,R)$ and $\overline{B(0,r)}\subset G$.

::: pf-proof
$f^n$ maps $G$ into $G\subset B(0,R)$, so $\abs{f^n}\le R$ on $\abs{z}=r$. By step [](#iterate){.pf-ref} the $k$th Taylor coefficient of $f^n$ at $0$ is $na_k$, and Cauchy's estimate bounds it by $R/r^k$.
:::

:::

::: pf-qed
Letting $n\to\infty$ in step [](#cauchy){.pf-ref} forces $a_k=0$, a contradiction. Hence $f(z)=z$ near $0$, and by the identity theorem on the region $G$, $f(z)\equiv z$. With step [](#normalize){.pf-ref} this proves the claim for every $a$.
:::

:::
:::
