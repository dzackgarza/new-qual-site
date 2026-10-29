---
schema: qual/card@1
id: P-ALGS19H
kind: problem
title: "Real subfield of cyclotomic field and powers of algebraic numbers in Q"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose $\zeta_n := e^{\frac{2\pi i}{n}} \in \CC$, and $K_n := \QQ[\zeta_n] \cap \RR$.

(a) Prove that $K_n/\QQ$ is a Galois extension.

(b) Suppose $\alpha \in K_n$, $r := \alpha^m \in \QQ$ and $m$ is the smallest such positive integer (i.e.\ $\alpha^i \notin \QQ$ for $1 \leq i < m$). Prove that $m \leq 2$.

Hint: Think about the minimal polynomial of $\alpha$ over $\QQ$.
:::

::: {.solution}

::: pf

::: pf-step

Let $L=\QQ(\zeta_n)$. Then $L/\QQ$ is Galois and
$$
\operatorname{Gal}(L/\QQ)\cong (\ZZ/n\ZZ)^\times,
$$
so its Galois group is abelian.

::: pf-proof

The field $L$ is the splitting field over $\QQ$ of the separable polynomial $x^n-1$. Its automorphisms are determined by $\zeta_n\mapsto \zeta_n^a$ for $a\in(\ZZ/n\ZZ)^\times$, giving the stated abelian Galois group.

:::

:::

::: pf-step

Complex conjugation $c\in\operatorname{Gal}(L/\QQ)$ has fixed field exactly
$$
L^{\langle c\rangle}=L\cap\RR=K_n.
$$

::: pf-proof

An element of $L$ is fixed by complex conjugation exactly when it is real.

:::

:::

::: {.pf-step #s3}

The extension $K_n/\QQ$ is Galois.

::: pf-proof

Since $\operatorname{Gal}(L/\QQ)$ is abelian, the subgroup $\langle c\rangle$ is normal. By the fundamental theorem of Galois theory, the fixed field $K_n=L^{\langle c\rangle}$ is therefore Galois over $\QQ$.

:::

:::

::: pf-step

Now suppose $\alpha\in K_n$ and $\alpha^m=r\in\QQ$, with $m$ minimal positive. If $\alpha=0$, then $m=1$. Hence assume $\alpha\ne0$.

::: pf-proof

If $\alpha=0$, then already $\alpha^1=0\in\QQ$, so the minimal positive exponent is $1$.

:::

:::

::: pf-step

Let $f\in\QQ[x]$ be the minimal polynomial of $\alpha$. Every root $\beta$ of $f$ lies in $K_n$, hence is real, and satisfies $\beta^m=r=\alpha^m$.

::: pf-proof

By step [](#s3){.pf-ref}, $K_n/\QQ$ is Galois. Therefore every $\QQ$-conjugate of $\alpha$ lies in $K_n$. Since $K_n\subseteq\RR$, every such conjugate is real. Also $f$ divides $x^m-r$, because $f(\alpha)=0$ and $\alpha^m-r=0$; hence every root $\beta$ of $f$ satisfies $\beta^m=r$.

:::

:::

::: {.pf-step #s6}

Every root $\beta$ of $f$ is equal to $\alpha$ or $-\alpha$. Thus $\deg f\le2$.

::: pf-proof

Since $\alpha\ne0$ and $\beta^m=\alpha^m$, one has $(\beta/\alpha)^m=1$. Hence $\beta/\alpha$ is an $m$-th root of unity. But both $\alpha$ and $\beta$ are real, so $\beta/\alpha\in\RR$. The only real roots of unity are $1$ and $-1$. Therefore $\beta=\pm\alpha$. Since a minimal polynomial is separable in characteristic $0$, it has at most these two distinct roots, so $\deg f\le2$.

:::

:::

::: pf-step

If $\deg f=1$, then $\alpha\in\QQ$, so $m=1$. If $\deg f=2$, then the roots of $f$ are $\alpha$ and $-\alpha$, so
$$
f(x)=x^2-\alpha^2\in\QQ[x].
$$
Hence $\alpha^2\in\QQ$, and therefore $m\le2$.

::: pf-proof

The degree-one case is immediate. In degree two, step [](#s6){.pf-ref} shows that the two distinct conjugates are $\alpha$ and $-\alpha$. Since $f$ is monic,
$$
f(x)=(x-\alpha)(x+\alpha)=x^2-\alpha^2.
$$
Because $f\in\QQ[x]$, its constant coefficient $-\alpha^2$ is rational. Thus a positive exponent at most $2$ already sends $\alpha$ into $\QQ$, so the minimal such exponent satisfies $m\le2$.

:::

:::

:::

:::
