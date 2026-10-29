---
schema: qual/card@1
id: P-VGN3T
kind: problem
title: '$\ZZ[\sqrt{-5}]$ is not a PID: units $\pm 1$, and $3$ irreducible but not prime'
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Integral Domains
  - Principal Ideal Domains
relations: []
review: draft
---
::: {.problem}
For a commutative ring $R$, let $U(R) = R^\times$ denote the group of units in $R$. Recall that in an integral domain $R$, a non-zero, non-unit element $r \in R$ is called *irreducible* if whenever $r = x y$ with $x, y \in R$, then either $x \in U(R)$ or $y \in U(R)$. A non-zero, non-unit element $r \in R$ is called *prime* in $R$ if $r \mid a b \implies r \mid a \text{ or } r \mid b$.

Consider the ring $R = \ZZ[\sqrt{-5}] = \{a + b \sqrt{-5} \mid a, b \in \ZZ\} \subset \CC$.

(a) Prove that $R$ is an integral domain.

(b) Show that $U(R) = \{\pm 1\}$.

(c) Show that $3$, $2 + \sqrt{-5}$, and $2 - \sqrt{-5}$ are irreducible in $R$.

(d) Show that $3$ is not prime in $R$.

(e) Conclude that $R$ is not a principal ideal domain (PID).
:::

::: {.solution}
Put $u=\sqrt{-5}$ and define the norm $N:R\to\ZZ_{\geq0}$ by $N(a+bu)=(a+bu)(a-bu)=a^2+5b^2$.

::: pf

::: {.pf-step #s1}

The ring $R$ is an integral domain, and the norm is multiplicative.

::: pf-proof

For integers $a,b,c,d$, the product $(a+bu)(c+du)=(ac-5bd)+(ad+bc)u$ belongs to $R$, and $R$ is closed under subtraction and contains $1$. Hence $R$ is a unital subring of the field $\CC$, so it is an integral domain. Complex conjugation preserves $R$ and is multiplicative. Therefore $N(\alpha\beta)=\alpha\beta\overline{\alpha\beta}=(\alpha\overline\alpha)(\beta\overline\beta)=N(\alpha)N(\beta)$ for all $\alpha,\beta\in R$.

:::

:::

::: {.pf-step #s2}

The units of $R$ are
\[
\boxed{R^\times=\{1,-1\}}.
\]

::: pf-proof

If $\alpha$ is a unit, multiplicativity of $N$ from step [](#s1){.pf-ref} gives $N(\alpha)N(\alpha^{-1})=1$, so $N(\alpha)=1$. For $\alpha=a+bu$ this is $a^2+5b^2=1$, forcing $b=0$ and $a=\pm1$. Conversely, both $1$ and $-1$ are units.

:::

:::

::: {.pf-step #s3}

The elements $3$, $2+u$, and $2-u$ are irreducible in $R$.

::: pf-proof

Each of the three elements has norm $9$ and is consequently a nonzero nonunit by step [](#s2){.pf-ref}. No element of $R$ has norm $3$: the equation $a^2+5b^2=3$ forces $b=0$ and then $a^2=3$, which has no integral solution. In any factorization $\alpha=\beta\gamma$ of one of these elements, step [](#s1){.pf-ref} yields $N(\beta)N(\gamma)=9$. Both norms are positive integers, and neither equals $3$; therefore one equals $1$. By step [](#s2){.pf-ref}, its corresponding factor is a unit. Hence each $\alpha$ is irreducible.

:::

:::

::: {.pf-step #s4}

The irreducible element $3$ is not prime.

::: pf-proof

The product $(2+u)(2-u)=4-u^2=9$ is divisible by $3$. If $3$ divided either $2+u$ or $2-u$ in $R$, comparison of the integer coefficients of $1$ would give $3a=2$ for some $a\in\ZZ$, an impossibility. Thus $3$ divides their product but neither factor.

:::

:::

::: {.pf-step #s5}

The ring $R$ is not a PID.

::: pf-proof

In a PID every irreducible element $p$ is prime: if $p\mid ab$ and $p\nmid a$, irreducibility forces $(p,a)=R$; Bézout's identity gives $rp+sa=1$, and multiplication by $b$ shows $p\mid b$. If $R$ were a PID, the irreducible element $3$ from step [](#s3){.pf-ref} would therefore be prime, contradicting step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} establish parts (a)--(e), respectively.

:::

:::

:::
