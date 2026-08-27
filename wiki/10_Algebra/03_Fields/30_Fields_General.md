---
order: 30
---

# General Field Theory

:::{.remark}
The most useful tricks of the trade:

- $\# \GG_m(\GF(p^k)) = p^k-1$, since every element is invertible except 0.
  You can use this to cook up strong numerical constraints on orders of elements.
  E.g. if $a^{17}=1$ in some finite field of size $p^k$, $o(a)$ divides 17 and $o(a)$ divides $p^{k}-1$, so $o(a)$ divides $\gcd(17, p^{k}-1)$.
- Multiplicativity in towers can force numerical divisibility constraints.
  E.g. if $\alpha$ is a root of any irreducible $f$, take the tower $\SF(\alpha, k)/k(\alpha)/k$: then the degree of $\min_{\alpha, k}(x)\in k[x]$ divides the degree of the extension $[\SF(\alpha, k) :  k]$.
-

:::

:::{.remark}
The most useful tricks of the trade:

- $\size \GG_m(\GF(p^k)) = p^k-1$, since every element is invertible except 0.
  You can use this to cook up strong numerical constraints on orders of elements.
  E.g. if $a^{17}=1$ in some finite field of size $p^k$, $o(a)$ divides 17 and $o(a)$ divides $p^{k}-1$, so $o(a)$ divides $\gcd(17, p^{k}-1)$.
- Multiplicativity in towers can force numerical divisibility constraints.
  E.g. if $\alpha$ is a root of any irreducible $f$, take the tower $\SF(\alpha, k)/k(\alpha)/k$: then the degree of $\min_{\alpha, k}(x)\in k[x]$ divides the degree of the extension $[\SF(\alpha, k) :  k]$.

:::

## Basics: Polynomials

[[D-BVMTZ]]

[[D-4VC6X]]

[[T-JEZZY]]

:::{.corollary}
A primitive polynomial $p\in \QQ[x]$ is irreducible $\iff p$ is irreducible in $\ZZ[x]$.

:::

## Definitions

[[D-JNCUB]]

[[PR-3X3TO]]

[[D-5FG7E]]

[[D-EOCCU]]

[[T-U3EZL]]

[[D-MN47W]]

[[D-KGF4K]]

[[D-KQFIV]]

:::{.example title="of a non-perfect field"}
Example of a non-perfect field: $\FF_p(t)$.
Use that $f(x) \da x^p - t$ is irreducible in $\FF_p(t)[x]$ but not separable.

:::

[[PR-IK6AM]]

:::{.proof}
For $\ch k = 0$, use that irreducible implies separable.

For $\ch k = p$, show that $k^p\neq k \iff$ irreducible does *not* imply separable, so there exists an inseparable irreducible.

- Supposing $k^p\neq k$, choose $a\in k$ not a $p$th power.
- Note that $f(x) \da x^p-a$ has only one root in $\bar{k}$: in a splitting field, any root $r$ satisfies $r^p=a$, so 
\[
x^p - a = x^p - r^p = (x-r)^p
.\]

- Note $f$ is irreducible: its only possible divisors are $(x-r)^m$ for $m \leq p$.
  Expanding yields 
  \[
(x-r)^m = \sum_{k=0}^m {m\choose k} x^{m-k} (-r)^{k} = x^m + {m\choose 1} x^{m-1} (-r)^m + \cdots
  ,\]
  so the coefficient of $x^{m-1}$ is $-mr \in k$.

- Thus if $(x-r)^m$ has a nontrivial divisor in $k[x]$ then $m$ must be in $k\units$, forcing $r\in k$.
  But then $r^p = a\in k$, $\contradiction$.

:::

:::{.remark title="Numerical Invariants"}
Let $K/k$ be an extension.

\[
[K: k] = \dim_{\Vect_k} K
\] 
is the dimension of $K$ as a $k\dash$vector space.
Automorphisms of fields over $K$ are defined as

\[ 
\Aut_{\Fieldsover{k}}(K) \da \Aut(K/k) \da \ts{ \sigma: K \to K' \st \ro{\sigma}{k} = \id_k } 
, \] 
so lifts of the identity on $k$, and 
\[
\ts{K:k} \da \size \Aut(K/k)
.\]

If $K/k$ is finite, normal, and separable,
\[
\Gal(K/k) \da \Aut(K/k)
,\]
where in general
\[
\ts{K: k} \leq [K: k]
\]
with equality when $L/k$ is Galois.

:::

:::{.fact}
\envlist
- All fields are simple rings (no proper nontrivial ideals).
  - Thus every field morphism is either zero or injective.
- The characteristic of any field $k$ is either 0 or $p$ a prime.
- If $L/k$ is algebraic, then $\min(\alpha, L)$ divides $\min(\alpha, k)$.

:::

[[PR-ZO73V]]

## Finite Fields

[[T-QBQLM]]

[[PR-ADLQN]]

[[PR-Q2IFX]]

[[PR-32R3E]]

:::{.proof}
Every element is a root by Cauchy's theorem, and the $p^n$ roots are distinct since its derivative is identically $-1$.

:::

[[PR-73MCN]]

:::{.corollary}
$x^{p^n} - x = \prod f_i(x)$ over all irreducible monic $f_i \in \FF_p[x]$ of degree $d$ dividing $n$.

:::

:::{.proof}
$\impliedby$:

- Suppose $f$ is irreducible of degree $d$.
- Then $f \divides x^{p^d} - x$, by considering $F[x]/\gens{f}$.
- Thus $x^{p^d} - x \divides x^{p^n} - x \iff d\divides n$.

$\implies$:

- $\alpha \in \GF(p^n) \iff \alpha^{p^n} - \alpha = 0$, so every element is a root of $\phi_n$ and $\deg \min(\alpha, \FF_p) \divides n$ since $\FF_p(\alpha)$ is an intermediate extension.

- So if $f$ is an irreducible factor of $\phi_n$, $f$ is the minimal polynomial of some root $\alpha$ of $\phi_n$, so $\deg f \divides n$.

-  $\phi_n'(x) = p^nx^{p^{n-1}} \neq 0$, so $\phi_n$ is squarefree and thus has no repeated factors. So $\phi_n$ is the product of all such irreducible $f$.

:::

[[PR-DEG36]]

:::{.proof}
If \( k = \ts{ a_1, a_2, \cdots a_n } \)  then define the polynomial 
\[
f(x) \da 1 +\prod_{j=1}^n (x-a_j) \in k[x]
.\]
This has no roots in $k$.

:::

## Cyclotomic Polynomials

[[D-JX3YC]]

:::{.remark}
\envlist

- $\phi(p) = p-1$, because every number $k\leq p-1$ is coprime to $p$.
- $\phi(p^k) = p^{k} - p^{k-1}$, since there are $p^k$ total numbers less than $p^k$, most of which are coprime to $p$.
  The ones to remove are those dividing $p^k$: the only divisors of $p^k$ are $p^\ell$ for $0\leq \ell \leq k$, and $\gcd(p^k, m) = p^\ell$ 
  whenever $m=tp$ for $t = 1,2,3,\cdots,p^{k-1}$ (i.e. $m$ is divisible by some power of $p$, so the $p^{k-1}$ multiples of $p$ are possible).
- $\phi$ is multiplicative (arithmetically, so only on prime powers!)

:::

:::{.example title="Some totient values"}
\[
\phi(1) &= 1 \\
\phi(2) &= 1 \\
\phi(3) &= 2 \\
\phi(4) &= 2 \\
\phi(6) &= 2 \\
\phi(8) &= 4 \\
.\]

:::

[[D-BLV6F]]

[[D-IPR4B]]

[[PR-JLDJ6]]

:::{.fact title="computing cyclotomic polynomials, special cases and examples"}
\[
\Phi_{p}(x)   &=  x^{p-1}+x^{p-2}+\cdots+x+1 \\
\Phi_{2 p}(x) &=  x^{p-1}-x^{p-2}+\cdots-x+1 \\
\\
k\divides n \implies \Phi_{n}(x) &= \Phi_{n\over k}\left(x^{k}\right)
\\ \\
\Phi_1(z) &= z-1 \\
\Phi_2(z) &= z+1 \\
\Phi_4(z) &= z^2+1 \\
\Phi_6(z) &= z^2 -z + 1 \\
\Phi_8(z) &= z^4+1 
.\]

:::

[[PR-DCK6S]]

[[T-QX5QU]]

## Misc

[[D-FK47C]]

## Exercises

[[E-LUR7G]]

[[E-6OUJV]]

[[E-OB3LO]]

[[E-PHSV5]]
