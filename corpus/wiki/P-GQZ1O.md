---
schema: qual/card@1
id: P-GQZ1O
kind: problem
title: The torsion subset of a module over an integral domain is a submodule
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
  - Integral Domains
relations: []
review: draft
---

::: problem
Suppose $R$ is a domain, $M$ an $R\dash$module, and let
$$
T(M) = \theset{m \in M \suchthat rm = 0 \text{ for some $r\neq 0 \in R$}}.
$$

Then $T(R)$ is a submodule iff for all $r\in R$ and all $m,n\in T(M)$ we have $rm + n \in T(M)$.

So pick annihilators $a_m, a_n \neq 0 \in R$ where $a_m m = 0$ and $a_n n = 0$.

Since $a_m \neq 0$ and $a_n \neq 0$, the product $a_m a_n \neq 0$ **because $R$ is a domain**.

Since $0 \in T(M)$, we can suppose $rm+n \neq 0$ (otherwise this is in $T(M)$ trivially).
Then

\[
\begin{align*}
a_m a_n (rm + n) 
&= a_m a_n r m + a_m a_n n \\
&=r a_n (a_m m) + a_m (a_n n) \\
&= r a_n 0 + a_m 0 \\
&= 0
.\end{align*}
\]

where the commutativity of $r, a_n, a_m$ follows from the fact that these are all elements of $R$, which is a domain, and in particular is commutative.
$\qed$
:::
