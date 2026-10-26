---
schema: qual/card@1
id: P-NORI-GT-3-02
kind: problem
title: Cube roots of unity in $\mathbb F_p$ and the splitting field of $X^p-\omega X$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.2 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
For which primes p is there some $1 \neq \omega \in \mathbb { F } _ { p }$ such that $\omega ^ { 3 } = 1$ . For such a prime $p ,$ how many elements are there in a splitting field of $X ^ { p } - \omega X \in \mathbb { F } _ { p } [ X ]$
:::

::: pf

::: pf-step

For $p\ne3$, the multiplicative group $\mathbb F_p^\times$ is cyclic of order $p-1$.


::: pf-proof

The multiplicative group of every finite field is cyclic; for $\mathbb F_p$ its order is $p-1$.

:::

:::

::: {.pf-step #s1-2}

A nontrivial element $\omega\in\mathbb F_p$ satisfying $\omega^3=1$ exists if and only if
\[
3\mid(p-1).
\]


::: pf-proof

Such an $\omega$ has multiplicative order exactly $3$. A cyclic group of order $p-1$ contains an element of order $3$ exactly when $3$ divides $p-1$.

:::

:::

::: {.pf-step #s1-3}

The prime $p=3$ does not admit such an $\omega$.


::: pf-proof

In characteristic $3$,
\[
X^3-1=(X-1)^3,
\]
so the only cube root of unity in $\mathbb F_3$ is $1$.

:::

:::

::: {.pf-step #s1-4}

Therefore the required primes are precisely
\[
\boxed{p\equiv1\pmod3}.
\]


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} cover all primes. For a prime different from $3$, divisibility $3\mid p-1$ is equivalent to $p\equiv1\pmod3$.

:::

:::

::: {.pf-step #s1-5}

Fix such a prime $p$ and a nontrivial cube root $\omega\in\mathbb F_p$. Let
\[
f(X)=X^p-\omega X.
\]
Then $f$ is separable.


::: pf-proof

In characteristic $p$,
\[
f'(X)=pX^{p-1}-\omega=-\omega\ne0.
\]
Thus $f$ has no repeated roots.

:::

:::

::: {.pf-step #s1-6}

If $\alpha$ is a root, then
\[
\alpha^p=\omega\alpha.
\]


::: pf-proof

This is exactly the equation $f(\alpha)=0$.

:::

:::

::: {.pf-step #s1-7}

Every root satisfies
\[
\alpha^{p^3}=\alpha.
\]


::: pf-proof

Because $\omega\in\mathbb F_p$, one has $\omega^p=\omega$. Applying the $p$-power map successively to step [](#s1-6){.pf-ref} gives
\[
\alpha^{p^2}
=(\omega\alpha)^p
=\omega\alpha^p
=\omega^2\alpha,
\]
and then
\[
\alpha^{p^3}
=(\omega^2\alpha)^p
=\omega^2\alpha^p
=\omega^3\alpha
=\alpha.
\]

:::

:::

::: {.pf-step #s1-8}

Hence all roots lie in $\mathbb F_{p^3}$.


::: pf-proof

The roots of $X^{p^3}-X$ in an algebraic closure are exactly the elements of $\mathbb F_{p^3}$. Apply step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The root set
\[
V=\{x\in\mathbb F_{p^3}:x^p=\omega x\}
\]
is a one-dimensional vector space over $\mathbb F_p$, so it consists of the $p$ roots of $f$.


::: pf-proof

The equation is the kernel of the $\mathbb F_p$-linear map
\[
T(x)=x^p-\omega x.
\]
By step [](#s1-5){.pf-ref}, $f$ has exactly $p$ distinct roots in its splitting field, and step [](#s1-8){.pf-ref} puts all of them in $\mathbb F_{p^3}$. Hence $|V|=p$, so $V$ has dimension one over $\mathbb F_p$.

:::

:::

::: {.pf-step #s1-10}

If $0\ne\alpha\in V$, then the splitting field is
\[
E=\mathbb F_p(\alpha).
\]


::: pf-proof

By step [](#s1-9){.pf-ref}, every root is $c\alpha$ for some $c\in\mathbb F_p$. Thus adjoining one nonzero root adjoins every root, and conversely the splitting field contains such a root.

:::

:::

::: {.pf-step #s1-11}

The element $\alpha$ does not lie in $\mathbb F_p$.


::: pf-proof

If $\alpha\in\mathbb F_p$, then $\alpha^p=\alpha$. Step [](#s1-6){.pf-ref} would give
\[
\alpha=\omega\alpha.
\]
Since $\alpha\ne0$, this would imply $\omega=1$, contrary to the choice of $\omega$.

:::

:::

::: {.pf-step #s1-12}

Since $\alpha\in\mathbb F_{p^3}\setminus\mathbb F_p$ and $3$ is prime,
\[
\mathbb F_p(\alpha)=\mathbb F_{p^3}.
\]


::: pf-proof

The extension $\mathbb F_{p^3}/\mathbb F_p$ has degree $3$. By the tower law, an intermediate field has degree over $\mathbb F_p$ dividing $3$, hence degree $1$ or $3$. Step [](#s1-11){.pf-ref} excludes degree $1$ for $\mathbb F_p(\alpha)$.

:::

:::

::: {.pf-step #s1-13}

Therefore the splitting field has
\[
\boxed{p^3}
\]
elements.


::: pf-proof

Steps [](#s1-10){.pf-ref} through [](#s1-12){.pf-ref} identify the splitting field with $\mathbb F_{p^3}$, which by definition has $p^3$ elements.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies the primes, and step [](#s1-13){.pf-ref} gives the size of the splitting field for each such prime.

:::

:::
