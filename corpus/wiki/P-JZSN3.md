---
schema: qual/card@1
id: P-JZSN3
kind: problem
title: "Let $p$ be a prime number and let $F$ be a field of characteristic $p$\u2026"
classification:
  areas:
  - algebra
  topics:
  - irreducibility-criteria
  - characteristic
  - polynomials
relations: []
review: draft
---
Let $p$ be a prime number and let $F$ be a field of characteristic $p$.
Show that if $a\in F$ is not a $p$th power in $F$, then $x^p-a \in F[x]$ is irreducible.


:::{.strategy}
\envlist

- Contradiction: go to splitting field, apply Freshman's dream.
- Use that this polynomial is ramified, and its only factors are $(x-a)$.
:::


:::{.solution title="Likely the 'right' solution"}
\envlist

- Suppose $a$ is not a $p$th power in $F$, then $f(x) \da x^p-a$ has no roots in $F$.
- Toward a contradiction, suppose $f$ is reducible in $F[x]$.
- In $\SF(f)$, since $\ch F = p$ we have $f(x) = (x-\zeta)^p$ for some $\zeta = a^{1\over p}$.
  - So if $f$ is reducible in $F[x]$, we have $f(x) = p_1(x) p_2(x)$ where $p(x) = (x-\zeta)^q\in F[x]$ for some $1\leq q < p$, since these are the only factors of $f$.
  - The claim is that $\zeta\in F$ as well, which is a contradiction since $\zeta$ is a $p$th root of $a$.
- We have $x^q-\zeta^q \in F[x]$, so $\zeta^q\in F$.
- We know $a = \zeta^p\in F$, and thus $\zeta^{d} = \zeta\in F$ for $d \da \gcd(p, n) = 1$. $\contradiction$
  - Why this is true: write $d = \gcd(p, n)$ in $\ZZ$ to obtain $d = tp + sn$ for some $t, s$.
  - Then $\zeta^d = \zeta^{tp+sn} = (\zeta^p)^t \cdot (\zeta^n)^s \in F$.
:::


:::{.strategy title="for an alternative solution"}
\envlist

- By contrapositive, show that $f(x) \da x^p-a \in \FF[x]$ reducible $\implies a$ is a $p$th power in $\FF$.
- Eventually show $a^\ell = b^p$ for some $\ell\in \NN$ and some $b\in \FF$, then $\gcd(\ell, p) = 1$ forces $b=a$ and $\ell=p$.
- Use the fact that the constant term of any $g\in \FF[x]$ is actually in $\FF$.
:::

:::{.concept}
\envlist

- Reducible: $f\in \FF[x]$ is reducible iff there exists $g, h\in \FF[x]$ nonconstant with $f = g h$. 
  - Importantly, this factorization needs to happen in $\FF[x]$, since we can *always* find such factorizations in the splitting field $\SF(f)[x]$.

- Bezout's identity: $\gcd(p, q) = d \implies$ there exist $s,t\in \ZZ$ such that 
\[
sp + tq = d
.\]

:::

:::{.solution}
\envlist

- WTS: $f(x) \da x^p - a\in \FF[x]$ reducible $\implies f$ has a root in the *base field* $\FF$.
- Write $f(x) = g(x) h(x)$ and factor $f(x) = \prod_{i=1}^p (x- r_i) \in \SF(f)[x]$ where the $r_i$ are not necessarily distinct roots.
- WLOG, $g(x) = \prod_{i=1}^\ell (x-r_i)$ for some $1\leq \ell \leq p-1$, i.e. rearrange the factors so that $g$ is the first $\ell$ of them.
  - $\ell \neq 1, p$ since $f$ is reducible, making $g, h$ nonconstant.

- Set $R_\ell \da \prod_{i=1}^\ell r_i$, which is the constant term in $g$, so $R_\ell \in \FF$ since $g\in \FF[x]$.

- Each $r_i$ is a root of $f$, so $r_i^p - a = 0$ for all $i$, so $r_i^p = a$.

- Trick: what is the $p$th power of $R_\ell$?
\[
R_\ell^p 
&\da \qty{ \prod_{i=1}^\ell}^p \\
&= \prod_{i=1}^\ell r_i^p \\
&= \prod_{i=1}^\ell a \\
&= a^\ell
,\]
  so $R_\ell^p = a^\ell$.

- Use Bezout: $\gcd(\ell, p) = 1$ since $p$ is prime, so write $tp + s\ell = 1$ for some $t,s\in \ZZ$

- Use this to build a root of $f$ that's in $\FF$: write
\[
a &= a^1\\
&= a^{tp + s\ell} \\
&= a^{tp} a^{s\ell} \\
&=a^{tp} (a^\ell)^s\\
&= a^{tp} (R_\ell^p)^s \\
&= (a^t R_\ell^s)^p \\
&\da \beta^p
,\]
  so $a = \beta^p$.

  - Check $\beta\in \FF$: use that $R_\ell \in \FF$ since it was a constant term of a polynomial in $\FF[x]$, $a\in \FF$ by assumption, and fields are closed under taking powers and products.



:::



