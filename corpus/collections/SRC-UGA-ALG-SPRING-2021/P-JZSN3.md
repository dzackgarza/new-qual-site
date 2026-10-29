---
schema: qual/card@1
id: P-JZSN3
kind: problem
title: $x^p-a$ is irreducible in characteristic $p$ if $a$ is not a $p$th power
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Characteristic
  - Polynomials
relations: []
review: draft
---
::: {.problem}
Let $p$ be a prime number and let $F$ be a field of characteristic $p$.

Show that if $a \in F$ is not a $p$-th power in $F$, then the polynomial $f(x) = x^p - a$ is irreducible in $F[x]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $\alpha$ is a root of $x^p-a$ in an algebraic closure of $F$, then $x^p-a=(x-\alpha)^p$.

::: pf-proof

::: pf-step

Let $K$ be a splitting field of $f(x) = x^p - a$ over $F$.

:::

::: pf-step

In $K$, there exists a root $\alpha \in K$ such that $\alpha^p = a$.

:::

::: pf-step

Because $\operatorname{char}(F) = p$, the Frobenius map $t \mapsto t^p$ is an endomorphism, so
    $$(x - \alpha)^p = x^p - \alpha^p = x^p - a = f(x).$$

:::

::: pf-step

Thus in $K[x]$, $f(x)$ factors completely as $f(x) = (x - \alpha)^p$.

:::

:::

:::

::: {.pf-step #s2}

If $x^p-a$ were reducible in $F[x]$, it would have a monic factor $(x-\alpha)^k$ with $1\leq k<p$.

::: pf-proof

::: pf-step

Suppose for contradiction that $f(x)$ is reducible in $F[x]$.

:::

::: pf-step

Then there exists a monic irreducible factor $g(x) \in F[x]$ of $f(x)$ with degree $k = \deg g$ satisfying $1 \le k < p$.

:::

::: pf-step

In $K[x]$, $g(x)$ divides $f(x) = (x - \alpha)^p$.

:::

::: pf-step

Because $K[x]$ is a unique factorization domain and $x - \alpha$ is the only irreducible factor of $f(x)$ in $K[x]$, $g(x)$ must be of the form:

:::

$$g(x) = (x - \alpha)^k.$$

:::

:::

::: {.pf-step #s3}

Any factor $(x-\alpha)^k\in F[x]$ with $1\leq k<p$ forces $\alpha\in F$.

::: pf-proof

::: pf-step

Expanding $g(x) = (x - \alpha)^k$, its constant term is $(-1)^k \alpha^k$.

:::

::: pf-step

Since $g(x) \in F[x]$, all its coefficients lie in $F$, so $(-1)^k \alpha^k \in F$.

:::

::: pf-step

Since $-1 \in F$, $\alpha^k \in F$.

:::

::: pf-step

Because $p$ is prime and $1 \le k < p$, $\gcd(k, p) = 1$.

:::

::: pf-step

By Bézout's identity, there exist integers $u, v \in \ZZ$ such that
    $$u k + v p = 1.$$

:::

::: pf-step

Express $\alpha \in K$ using this identity:
    $$\alpha = \alpha^1 = \alpha^{u k + v p} = (\alpha^k)^u \cdot (\alpha^p)^v = (\alpha^k)^u \cdot a^v.$$

:::

::: pf-step

Since $\alpha^k \in F$ and $a \in F$, and $F$ is a field, the product $(\alpha^k)^u a^v$ lies in $F$.

:::

::: pf-step

Thus $\alpha \in F$.

:::

:::

:::

::: {.pf-step #s4}

The polynomial $x^p-a$ is irreducible over $F$.

::: pf-proof

::: pf-step

Since $\alpha \in F$, the element $a = \alpha^p$ is a $p$-th power of an element of $F$.

:::

::: pf-step

This contradicts the hypothesis that $a$ is not a $p$-th power in $F$.

:::

::: pf-step

Therefore $f(x) = x^p - a$ has no factors of degree $k$ with $1 \le k < p$, so $f(x)$ is irreducible in $F[x]$.

:::

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the assertion using steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::
