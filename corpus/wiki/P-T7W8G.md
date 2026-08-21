---
schema: qual/card@1
id: P-T7W8G
kind: problem
title: Irreducible polynomials over a field in which every element has a $p$th root
  are separable
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
solved: false
---

::: problem
Suppose every element in $F$ admits a $p$th root in $F$, and suppose $f \in F[x]$ is an irreducible polynomial which is *not* separable, so it has a repeated root in $\overline F$.

Supposing that $\gcd(f, f') = g(x)$ for any polynomial $g(x)$, this would imply that $g\divides f$.
But $f$ was assumed irreducible, so the only possibility is that in fact $g = f$.

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
Thus every irreducible polynomial is separable, which is what we wanted to show.
$\qed$
:::
