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

::: problem
Let $k$ be an algebraically closed field of characteristic $p > 0$ and let $K = k(t)$ be a purely transcendental extension in one indeterminate $t$.
Let $n \geq 1$ be any integer, and let $L$ be the splitting field of the polynomial $x^n - t$ over $K$.
It may be helpful in this problem to write $n = p^i m$ where $\gcd(m,p) = 1$.

(i) Show that $L = K(\alpha)$ where $\alpha$ is any root of $x^n - t$ in $L$.

(ii) Let $G = \mathrm{Aut}(L/K)$ be the group of all automorphisms of $L$ fixing $K$ pointwise, and let $F = \mathrm{Fix}(G)$ be the subfield of $L$ of elements fixed by $G$.
Calculate $[F : K]$.
:::
\n\n::: {.solution}\nWrite\n\[\nn=p^i m,\qquad (m,p)=1,\n\]\nand let $\alpha$ be a root of $x^n-t$.
Thus $\alpha^n=t$.\n\n<1>1. The polynomial $x^n-t$ is irreducible over $K=k(t)$, so $[K(\alpha):K]=n$.\n::: {.proof}\nView $x^n-t$ as a polynomial in $k[t][x]$.
It is Eisenstein at the prime element $t$: every nonleading coefficient is divisible by $t$, and the constant term $-t$ is not divisible by $t^2$.
Hence it is irreducible in $k[t][x]$, and therefore in $k(t)[x]$ by Gauss's lemma.\n:::\n\n<1>2. Every root of $x^n-t$ is of the form $\zeta\alpha$ with $\zeta^m=1$.
Hence the splitting field is\n\[\nL=K(\alpha).\n\]\n::: {.proof}\nBecause $k$ is algebraically closed, all $m$th roots of unity lie in $k\subset K$.
If $\zeta^m=1$, then\n\[\n(\zeta\alpha)^n=\zeta^{p^im}\alpha^n=(\zeta^m)^{p^i}t=t,\n\]\nso every $\zeta\alpha$ is a root.
Conversely, if $\beta^n=t=\alpha^n$, then\n\[\n(\beta/\alpha)^n=1.\n\]\nIn characteristic $p$, the group of $n$th roots of unity is the same as the group of $m$th roots of unity, since\n\[\nx^n-1=(x^m-1)^{p^i}.\n\]\nThus $\beta/\alpha=\zeta$ for some $\zeta^m=1$.
All roots therefore already lie in $K(\alpha)$.\n:::\n\n<1>3. The automorphism group is\n\[\nG=\operatorname{Aut}(L/K)\cong \mu_m,\n\]\nacting by $\alpha\mapsto\zeta\alpha$ for $\zeta^m=1$.
In particular $|G|=m$.\n::: {.proof}\nEvery $K$-automorphism sends $\alpha$ to another root of its irreducible polynomial, hence to $\zeta\alpha$ with $\zeta^m=1$.
Conversely, for each such $\zeta$, the assignment $\alpha\mapsto\zeta\alpha$ preserves the relation $\alpha^n=t$ and defines a $K$-automorphism of $L$.
These automorphisms are distinct.\n:::\n\n<1>4. The element\n\[\n\beta:=\alpha^m\n\]\nis fixed by $G$, and\n\[\n[K(\beta):K]=p^i.\n\]\n::: {.proof}\nFor $\sigma_\zeta\in G$,\n\[\n\sigma_\zeta(\beta)=(\zeta\alpha)^m=\alpha^m=\beta.\n\]\nAlso\n\[\n\beta^{p^i}=\alpha^{mp^i}=\alpha^n=t.\n\]\nThe polynomial $x^{p^i}-t$ is Eisenstein at $t$ in $k[t][x]$, so it is irreducible over $K$.
Hence $[K(\beta):K]=p^i$.\n:::\n\n<1>5. The fixed field is\n\[\nF=K(\beta)=K(\alpha^m),\n\]\nand therefore\n\[\n\boxed{[F:K]=p^i}.\n\]\n::: {.proof}\nBy <1>4, $K(\beta)\subseteq F$.
Moreover\n\[\n[L:K(\beta)]\n=\frac{[L:K]}{[K(\beta):K]}\n=\frac{p^im}{p^i}=m.\n\]\nSince $G$ has $m$ elements and fixes $K(\beta)$, Artin's theorem on fixed fields gives\n\[\n[L:F]=|G|=m.\n\]\nThus $F$ and $K(\beta)$ are intermediate fields of the same degree over $K$, with $K(\beta)\subseteq F$, so they are equal.\n:::\n:::\n
