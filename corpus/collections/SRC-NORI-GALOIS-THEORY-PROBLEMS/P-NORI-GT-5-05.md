---
schema: qual/card@1
id: P-NORI-GT-5-05
kind: problem
title: Degree of $F(a^{1/p^n})$ over a field with $p^n$-th roots of unity
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5.5 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the degree formulas, moved the source hint to a hint block, and removed the following section note, against Problem 5.5 on pp. 4-5 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $p$ be a prime, let $n$ be a natural number, and let $F$ be a field that contains a primitive $p^n$-th root of unity.
Let $a \in F$.
Show that if $\deg(F(a^{1/p})/F) > 1$, then $\deg(F(a^{1/p^n})/F) = p^n$.
:::

::: {.hint}
Let $E = F(b)$ where $b^{p^n} = a$.
Is $E$ a Galois extension of $F$?

Let $u = p^{n-1}$ and let $c = b^u$.
Does a $F$-automorphism $\sigma$ of $F(c)$ extend to an $F$-automorphism of $F(b)$?
:::

::: {.solution}

Choose $b$ with $b^{p^n}=a$, and set
$$
E=F(b),\qquad c=b^{p^{n-1}}.
$$
Then $c^p=a$, so $F(c)=F(a^{1/p})$.

::: pf

::: {.pf-step #s1-1}

The extension $F(c)/F$ is Galois of degree $p$.


::: pf-proof

Because $F$ contains a primitive $p^n$-th root of unity, it contains all $p$-th roots of unity. Hence every root of
$$
X^p-a
$$
has the form $\xi c$ with $\xi\in\mu_p\subseteq F$, so all roots lie in $F(c)$. Also $\operatorname{char}F\neq p$, since a field of characteristic $p$ has no nontrivial $p$-power roots of unity. Thus $X^p-a$ is separable, and $F(c)/F$ is Galois.

Every $F$-automorphism of $F(c)$ sends $c$ to $\xi c$ for some $\xi\in\mu_p$. Therefore $\Gal(F(c)/F)$ injects into the cyclic group $\mu_p$, so its order divides $p$. The hypothesis $[F(c):F]>1$ excludes the trivial group. Hence
$$
[F(c):F]=\abs{\Gal(F(c)/F)}=p.
$$

:::

:::

::: {.pf-step #s1-2}

The extension $E/F$ is Galois, and every $F$-automorphism of $F(c)$ extends to an $F$-automorphism of $E$.


::: pf-proof

Let $\zeta\in F$ be a primitive $p^n$-th root of unity. Every root of
$$
X^{p^n}-a
$$
has the form $\zeta^j b$, and therefore lies in $E=F(b)$. Since $\operatorname{char}F\neq p$, this polynomial is separable. Thus $E/F$ is finite Galois.

For a finite Galois extension, every $F$-embedding of an intermediate field into $E$ extends to an element of the full Galois group. Hence the restriction map
$$
\Gal(E/F)\longrightarrow \Gal(F(c)/F)
$$
is surjective.

:::

:::

::: {.pf-step #s1-3}

There exists $\sigma\in\Gal(E/F)$ such that, when
$$
\sigma(b)=\zeta^k b,
$$
the integer $k$ is not divisible by $p$.


::: pf-proof

By step [](#s1-1){.pf-ref}, $\Gal(F(c)/F)$ has order $p$, so choose a nonidentity automorphism
$$
\tau\in\Gal(F(c)/F).
$$
By step [](#s1-2){.pf-ref}, $\tau$ extends to some $\sigma\in\Gal(E/F)$.

Since $\sigma(b)$ is another root of $X^{p^n}-a$, there is an integer $k$ such that
$$
\sigma(b)=\zeta^k b.
$$
Then
$$
\sigma(c)=\sigma\left(b^{p^{n-1}}\right)
=\zeta^{k p^{n-1}}c.
$$
Because $\sigma\restrict_{F(c)}=\tau$ is nonidentity, the factor $\zeta^{k p^{n-1}}$ is not $1$. Since $\zeta$ has order $p^n$, this is equivalent to $p\nmid k$.

:::

:::

::: {.pf-step #s1-4}

The automorphism $\sigma$ from step [](#s1-3){.pf-ref} has order $p^n$.


::: pf-proof

For every integer $m\geq 1$,
$$
\sigma^m(b)=\zeta^{km}b,
$$
because $\sigma$ fixes $\zeta\in F$. Hence $\sigma^m=\operatorname{id}_E$ only if
$$
\zeta^{km}=1.
$$
By step [](#s1-3){.pf-ref}, $p\nmid k$, so $\zeta^k$ is again a primitive $p^n$-th root of unity. Its order is therefore $p^n$, and consequently $\sigma$ has order $p^n$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{[F(a^{1/p^n}):F]=p^n}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $E/F$ is Galois, and every element of $\Gal(E/F)$ sends $b$ to $\zeta^j b$ for some $j$. Thus
$$
\Gal(E/F)\hookrightarrow \mu_{p^n},
$$
so
$$
\abs{\Gal(E/F)}\leq p^n.
$$
By step [](#s1-4){.pf-ref}, $\Gal(E/F)$ contains an element of order $p^n$, so its order is at least $p^n$. Therefore
$$
[E:F]=\abs{\Gal(E/F)}=p^n.
$$
Since $E=F(b)=F(a^{1/p^n})$, this is the required degree.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required equality.

:::

:::

:::
