---
schema: qual/card@1
id: P-ALGS11E
kind: problem
title: Splitting field of $x^n - t$ over $k(t)$ in characteristic $p$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft

audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 5 of the official UCSD Spring 2011 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Separated the separable m-part from the purely inseparable p^i-part and identified the fixed field explicitly.
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic $p > 0$ and let $K = k(t)$ be a purely transcendental extension in one indeterminate $t$.
Let $n \geq 1$ be any integer, and let $L$ be the splitting field of the polynomial $x^n - t$ over $K$.
It may be helpful in this problem to write $n = p^i m$ where $\gcd(m,p) = 1$.

(i) Show that $L = K(\alpha)$ where $\alpha$ is any root of $x^n - t$ in $L$.

(ii) Let $G = \mathrm{Aut}(L/K)$ be the group of all automorphisms of $L$ fixing $K$ pointwise, and let $F = \mathrm{Fix}(G)$ be the subfield of $L$ of elements fixed by $G$.
Calculate $[F : K]$.
:::


::: {.solution}
Write
\[
n=p^i m,\qquad (m,p)=1,
\]
and let $\alpha$ be a root of $x^n-t$.
Thus $\alpha^n=t$.

<1>1. The polynomial $x^n-t$ is irreducible over $K=k(t)$, so $[K(\alpha):K]=n$.
::: {.proof}
View $x^n-t$ as a polynomial in $k[t][x]$.
It is Eisenstein at the prime element $t$: every nonleading coefficient is divisible by $t$, and the constant term $-t$ is not divisible by $t^2$.
Hence it is irreducible in $k[t][x]$, and therefore in $k(t)[x]$ by Gauss's lemma.
:::

<1>2. Every root of $x^n-t$ is of the form $\zeta\alpha$ with $\zeta^m=1$.
Hence the splitting field is
\[
L=K(\alpha).
\]
::: {.proof}
Because $k$ is algebraically closed, all $m$th roots of unity lie in $k\subset K$.
If $\zeta^m=1$, then
\[
(\zeta\alpha)^n=\zeta^{p^im}\alpha^n=(\zeta^m)^{p^i}t=t,
\]
so every $\zeta\alpha$ is a root.
Conversely, if $\beta^n=t=\alpha^n$, then
\[
(\beta/\alpha)^n=1.
\]
In characteristic $p$, the group of $n$th roots of unity is the same as the group of $m$th roots of unity, since
\[
x^n-1=(x^m-1)^{p^i}.
\]
Thus $\beta/\alpha=\zeta$ for some $\zeta^m=1$.
All roots therefore already lie in $K(\alpha)$.
:::

<1>3. The automorphism group is
\[
G=\operatorname{Aut}(L/K)\cong \mu_m,
\]
acting by $\alpha\mapsto\zeta\alpha$ for $\zeta^m=1$.
In particular $|G|=m$.
::: {.proof}
Every $K$-automorphism sends $\alpha$ to another root of its irreducible polynomial, hence to $\zeta\alpha$ with $\zeta^m=1$.
Conversely, for each such $\zeta$, the assignment $\alpha\mapsto\zeta\alpha$ preserves the relation $\alpha^n=t$ and defines a $K$-automorphism of $L$.
These automorphisms are distinct.
:::

<1>4. The element
\[
\beta:=\alpha^m
\]
is fixed by $G$, and
\[
[K(\beta):K]=p^i.
\]
::: {.proof}
For $\sigma_\zeta\in G$,
\[
\sigma_\zeta(\beta)=(\zeta\alpha)^m=\alpha^m=\beta.
\]
Also
\[
\beta^{p^i}=\alpha^{mp^i}=\alpha^n=t.
\]
The polynomial $x^{p^i}-t$ is Eisenstein at $t$ in $k[t][x]$, so it is irreducible over $K$.
Hence $[K(\beta):K]=p^i$.
:::

<1>5. The fixed field is
\[
F=K(\beta)=K(\alpha^m),
\]
and therefore
\[
\boxed{[F:K]=p^i}.
\]
::: {.proof}
By <1>4, $K(\beta)\subseteq F$.
Moreover
\[
[L:K(\beta)]
=\frac{[L:K]}{[K(\beta):K]}
=\frac{p^im}{p^i}=m.
\]
Since $G$ has $m$ elements and fixes $K(\beta)$, Artin's theorem on fixed fields gives
\[
[L:F]=|G|=m.
\]
Thus $F$ and $K(\beta)$ are intermediate fields of the same degree over $K$, with $K(\beta)\subseteq F$, so they are equal.
:::
:::

