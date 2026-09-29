---
schema: qual/card@1
id: P-BKS09-4B
kind: problem
title: Inverses in $\mathbb Q(\alpha)$ are polynomials in $\alpha$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed its minimal-polynomial Bezout argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked irreducibility, coprimality with H, and evaluation of the Bezout identity at alpha.
---

::: {.problem}
Consider a polynomial expression $H ( \alpha ) = A + B \alpha + C \alpha ^ { 2 } + \cdot \cdot \cdot + D \alpha ^ { N }$ with rational coefficients A, $B , C , \ldots , D$ , where α is an algebraic number, in other words a root of some polynomial with rational coefficients.
Prove that if $H ( \alpha ) \neq 0$ , then the reciprocal $1 / H ( \alpha )$ can be expressed as a polynomial in α with rational coefficients.
:::

::: {.solution}
Let $m(x)\in\QQ[x]$ be the minimal polynomial of $\alpha$ over $\QQ$.

::: pf

::: {.pf-step #m-h-coprime}
The polynomials $m$ and $H$ are relatively prime in $\QQ[x]$.

::: pf-proof
The minimal polynomial $m$ is irreducible over $\QQ$. Hence any common
divisor of $m$ and $H$ is either a nonzero constant or an associate of $m$.
If $m$ divided $H$, then evaluating at $\alpha$ would give
$$
H(\alpha)=0,
$$
contrary to the hypothesis. Therefore
$$
\gcd(m,H)=1.
$$
:::

:::

::: {.pf-step #bezout-identity}
There exist polynomials $U,V\in\QQ[x]$ such that
$$
U(x)m(x)+V(x)H(x)=1.
$$

::: pf-proof
By step [](#m-h-coprime){.pf-ref}, $m$ and $H$ are relatively prime. Bézout's identity in the
Euclidean domain $\QQ[x]$ therefore gives the stated polynomials $U$ and
$V$.
:::

:::

::: {.pf-step #reciprocal-formula}
The reciprocal of $H(\alpha)$ is a polynomial in $\alpha$ with
rational coefficients, namely
$$
\boxed{\frac{1}{H(\alpha)}=V(\alpha)}.
$$

::: pf-proof
Evaluate the identity in step [](#bezout-identity){.pf-ref} at $x=\alpha$. Since
$$
m(\alpha)=0,
$$
one obtains
$$
V(\alpha)H(\alpha)=1.
$$
The hypothesis $H(\alpha)\neq0$ permits division by $H(\alpha)$, giving
the displayed formula. Since $V\in\QQ[x]$, this has exactly the required
form.
:::

:::

::: pf-qed
Step [](#reciprocal-formula){.pf-ref} is the required conclusion.
:::

:::

:::
