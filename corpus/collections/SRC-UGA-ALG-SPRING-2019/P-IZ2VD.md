---
schema: qual/card@1
id: P-IZ2VD
kind: problem
title: Irreducibles of degree $d$ over $\FF_p$ divide $x^{p^d}-x$, and divide $x^{p^n}-x$
  only if $d$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Field Extensions
relations: []
review: draft
---

Let $F = \FF_p$ , where $p$ is a prime number.

a.
Show that if $\pi(x) \in F[x]$ is irreducible of degree $d$, then $\pi(x)$ divides $x^{p^d} - x$.

b.
Show that if $\pi(x) \in F[x]$ is an irreducible polynomial that divides $x^{p^n} - x$, then $\deg \pi(x)$ divides $n$.

:::{.concept}
\envlist

- Go to a field extension.
  - Orders of multiplicative groups for finite fields are known.
- $\GF(p^n)$ is the splitting field of $x^{p^n} - x \in \FF_p[x]$.
- $x^{p^d} - x \divides x^{p^n} - x \iff d \divides n$
- $\GF(p^d) \leq \GF(p^n) \iff d\divides n$
- $x^{p^n} - x = \prod f_i(x)$ over all irreducible monic $f_i$ of degree $d$ dividing $n$.

:::

:::{.solution}
\envlist

:::{.proof}
We can consider the quotient $K = \displaystyle{\frac{\FF_p[x]}{\generators{\pi(x)}}}$, which since $\pi(x)$ is irreducible is an extension of $\FF_p$ of degree $d$ and thus a field of size $p^d$ with a natural quotient map of rings $\rho: \FF_p[x] \to K$.

Since $K\units$ is a group of size $p^d-1$, we know that for any $y \in K\units$, we have by Lagrange's theorem that the order of $y$ divides $p^d-1$ and so $y^{p^d} = y$.

So every element in $K$ is a root of $q(x) = x^{p^d}-x$.

Since $\rho$ is a ring morphism, we have

\[
\rho(q(x)) = \rho(x^{p^d} - x) &= \rho(x)^{p^d} - \rho(x)
= 0 \in K \\
&\iff q(x) \in \ker \rho \\
&\iff q(x) \in \generators{\pi(x)} \\
&\iff \pi(x) \divides q(x) = x^{p^d}-x
,\]
  where we've used that "to contain is to divide" in the last step.


:::

:::{.proof}

:::{.claim}
$\pi(x)$ divides $x^{p^n}-x \iff \deg \pi$ divides $n$.
:::

:::{.proof}
Let $L \cong \GF(p^n)$ be the splitting field of $\phi_n(x) \definedas x^{p^n}-x$; then since $\pi \divides \phi_n$ by assumption, $\pi$ splits in $L$.
Let $\alpha \in L$ be any root of $\pi$; then there is a tower of extensions $\FF_p \leq \FF_p(\alpha) \leq L$.

Then $\FF_p \leq \FF_p(\alpha) \leq L$, and so
\[
n &= [L: \FF_p] \\
&= [L: \FF_p(\alpha)]~[\FF_p(\alpha): \FF_p] \\
&= \ell d
,\]

for some $\ell \in \ZZ^{\geq 1}$, so $d$ divides $n$.

:::

:::{.proof}
$\impliedby$:
If $d\divides n$, use the fact (claim) that $x^{p^n} - x = \prod f_i(x)$ over all irreducible monic $f_i$ of degree $d$ dividing $n$. 
So $f = f_i$ for some $i$.

:::

:::

:::

