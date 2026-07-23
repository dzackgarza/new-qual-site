---
schema: qual/card@1
id: P-5KZDX
kind: problem
title: "Definition: A field $F$ is *perfect* if every irreducible polynomial $\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Definition: A field $F$ is *perfect* if every irreducible polynomial $f(x) \in F[x]$ is separable in $\overline{F}[x]$.

Note that since $F$ is a finite field, $p$ must be a prime.

## $\implies:$

Suppose all irreducible polynomials in $F[x]$ are separable.
Then let $a\in K$ be arbitrary, we will show that there exists some $\beta \in K$ such that $\beta^p = a$.

Given such an $a$, define the polynomial
$$
f(x) = x^p - a \in F[x].
$$

Note that $f$ is *not* separable, since $f'(x) = px^{p-1} = 0$ since $\mathrm{char}(F) = p$, which means (by assumption) that $f$ must be *reducible*.

Thus we can write $f(x) = g(x)h(x)$ where $g \in F[x]$ is some irreducible factor that divides $f$.

Noting that if $\beta \in \overline{F}$ is a any root of $f$, then
$$
f(\beta) = 0 \implies \beta^p = a \implies f(x) = x^p - a = x^p - \beta^p = (x-\beta)^p,
$$

and so $\beta$ is necessarily a multiple root.

Moreover, since $g\divides f$, we must have $g(x) = (x-\beta)^\ell$ for some $1 \leq \ell \leq p$.

But then we can expand $g$ using the binomial formula:
$$
g(x) = (x - \beta)^\ell = \sum_{k=1}^\ell {\ell \choose k}x^{\ell-k}(-\beta)^k = x^\ell + \cdots + (-\beta)^\ell \in F[x].
$$

But since every coefficient must be in $F$, we must have $\beta^\ell \in F$. We know that $\beta^p = a \in F$ as well, but since $p$ is prime, $\gcd(p, \ell) = 1$.

We can thus find $s, t \in \ZZ$ such that $ps + t\ell = 1$. But then

$$
\beta = \beta^1 = \beta^{ps + t\ell} = \beta^{st} \beta^{t\ell} = (\beta^\ell)^s (\beta^p)^t,
$$

where since $\beta^\ell, \beta^p \in F$, the entire RHS is in $F$, and thus the LHS $\beta\in F$ as well.

But then $\alpha = \beta^p$ where $\beta \in F$, which is exactly what we wanted to show.

## $\impliedby$:

Suppose every element in $F$ admits a $p$th root in $F$, and suppose $f \in F[x]$ is an irreducible polynomial which is *not* separable, so it has a repeated root in $\overline F$.

Supposing that $\gcd(f, f') = g(x)$ for any polynomial $g(x)$, this would imply that $g\divides f$. But $f$ was assumed irreducible, so the only possibility is that in fact $g = f$.

But if $\gcd(f, f') = f$, since $\deg f' < f$, we can not have $f \divides f'$ unless $f'$ is identically zero.

If we thus write
\[
\begin{align*}
f(x) &= \sum_{k=0}^n c_k x^k, \\
f'(x) &= \sum_{k=1}^n k c_k x^{k-1} \\
&\equiv 0
,\end{align*}
\]

then for each $k$ we must have $c_k = 0$ or $k = 0$ in $F$, i.e. $c_k = 0$ or $p \divides k$.

Thus the only possible nonzero terms in $f$ must come from coefficients of $x^{kp}$ for each $k$ such that $1 \leq kp \leq n$, i.e.
$$
f(x) = c_0 + c_p x^p + c_{2p} x^{2p} + \cdots
$$

But this says we can write $f(x) \definedas g(x^p)$, where
$$
g(x) = c_0 + c_p x + c_{2p} x^2 + \cdots
$$

and furthermore, we can now use the assumption that $F$ is perfect to write $c_i = b_i^p$ for each $i$, yielding

\[
\begin{align*}
g(x) &= b_0^p + b_p^p x^2 + b_{2p}^p x^{2} + \cdots \\
.\end{align*}
\]
and thus
\[
\begin{align*}
f(x) &= g(x^p) \\
&= b_0^p + b_p^p x^{p} + b_{2p}^p x^{2p} + \cdots \\
&= (b_0 + b_p x + b_{2p} x^2)^p \\
&\definedas \left( j(x) \right)^p
,\end{align*}
\]

from which it follows that $j \divides f$ in $F[x]$. 
But since $f$ was irreducible, this is a contradiction, and so $f$ could not have had a repeated root. 
Thus every irreducible polynomial is separable, which is what we wanted to show. $\qed$

