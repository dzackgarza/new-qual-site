---
schema: qual/card@1
id: P-NORI-GT-4-10
kind: problem
title: Invariants of $X\mapsto X+1$ on $F(X)$ in characteristic $p$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.10 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let F be a field of characteristic $p > 0$ . With $\sigma$ as in the previous problem, show that $F ( X )$ is a Galois extension of $F ( X ) ^ { \sigma }$ of degree $p .$

Do you know what $F [ X ] ^ { \sigma }$ and $F ( X ) ^ { \sigma }$ are?
:::

::: {.solution}
Let
$$
L=F(X)
$$
and let
$$
\sigma(f(X))=f(X+1).
$$

<1>1. The automorphism $\sigma$ has order exactly $p$.

::: {.proof}
For every integer $r\ge0$,
$$
\sigma^r(X)=X+r.
$$
In characteristic $p$,
$$
\sigma^p(X)=X+p=X,
$$
so $\sigma^p=\operatorname{id}_L$.
If $0<r<p$, then the image of $r$ in $F$ is nonzero, so
$$
\sigma^r(X)=X+r\ne X.
$$
Thus the order is exactly $p$.
:::

<1>2. By Artin's fixed-field theorem,
$$
\boxed{L/L^\sigma\text{ is Galois of degree }p}
$$
and
$$
\operatorname{Gal}(L/L^\sigma)=\langle\sigma\rangle.
$$

::: {.proof}
The finite cyclic group
$$
G=\langle\sigma\rangle
$$
has order $p$ by step <1>1 and acts faithfully on $L$. Artin's theorem gives
$$
[L:L^G]=|G|=p
$$
and identifies the full Galois group with $G$. Since $L^G=L^\sigma$, the claim follows.
:::

<1>3. The element
$$
Y=X^p-X
$$
is fixed by $\sigma$.

::: {.proof}
In characteristic $p$,
$$
(X+1)^p=X^p+1.
$$
Therefore
$$
\sigma(Y)
=(X+1)^p-(X+1)
=X^p+1-X-1
=Y.
$$
:::

<1>4. Hence
$$
F(Y)\subseteq L^\sigma.
$$

::: {.proof}
Step <1>3 shows that $Y$ is fixed, and every element of $F$ is fixed. Therefore every rational function in $Y$ with coefficients in $F$ is fixed by $\sigma$.
:::

<1>5. The element $X$ is algebraic over $F(Y)$ of degree at most $p$.

::: {.proof}
It satisfies
$$
X^p-X-Y=0.
$$
Thus $X$ is a root of the degree-$p$ polynomial
$$
T^p-T-Y\in F(Y)[T].
$$
Since
$$
L=F(Y)(X),
$$
one obtains
$$
[L:F(Y)]\le p.
$$
:::

<1>6. One has
$$
\boxed{F(X)^\sigma=F(X^p-X)}.
$$

::: {.proof}
By step <1>4,
$$
F(Y)\subseteq L^\sigma\subseteq L.
$$
The tower law gives
$$
[L:F(Y)]
=[L:L^\sigma][L^\sigma:F(Y)].
$$
By step <1>2, the first factor is $p$, while step <1>5 gives
$$
[L:F(Y)]\le p.
$$
Hence equality must hold throughout and
$$
[L^\sigma:F(Y)]=1.
$$
Thus $L^\sigma=F(Y)$.
:::

<1>7. The ring $F[X]$ is generated as an $F[Y]$-module by
$$
1,X,\ldots,X^{p-1}.
$$

::: {.proof}
The relation
$$
X^p=X+Y
$$
allows every power $X^m$ with $m\ge p$ to be reduced recursively to an $F[Y]$-linear combination of lower powers. Hence every polynomial in $X$ lies in the $F[Y]$-span of the displayed elements.
:::

<1>8. The elements
$$
1,X,\ldots,X^{p-1}
$$
are linearly independent over $F(Y)$, and therefore over $F[Y]$.

::: {.proof}
Step <1>6 and step <1>2 give
$$
[F(X):F(Y)]=p.
$$
Since $F(X)=F(Y)(X)$, the minimal polynomial of $X$ over $F(Y)$ has degree $p$. Therefore the standard powers
$$
1,X,\ldots,X^{p-1}
$$
are linearly independent over $F(Y)$.
:::

<1>9. Thus
$$
F[X]
=
F[Y]\oplus F[Y]X\oplus\cdots\oplus F[Y]X^{p-1}.
$$

::: {.proof}
Spanning is step <1>7 and directness is step <1>8.
:::

<1>10. The polynomial invariants are
$$
\boxed{F[X]^\sigma=F[X^p-X]}.
$$

::: {.proof}
The inclusion
$$
F[Y]\subseteq F[X]^\sigma
$$
follows from step <1>3.

Conversely, if
$$
f\in F[X]^\sigma,
$$
then by step <1>6,
$$
f\in F(Y).
$$
Write the unique decomposition from step <1>9:
$$
f=b_0(Y)+b_1(Y)X+\cdots+b_{p-1}(Y)X^{p-1}
$$
with $b_i(Y)\in F[Y]$. Since $f$ also lies in $F(Y)$, linear independence over $F(Y)$ from step <1>8 forces
$$
b_1=\cdots=b_{p-1}=0.
$$
Hence $f=b_0(Y)\in F[Y]$.
:::

<1>11. Therefore
$$
\boxed{
F[X]^\sigma=F[X^p-X],
\qquad
F(X)^\sigma=F(X^p-X).
}
$$

::: {.proof}
Combine steps <1>6 and <1>10.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>2 proves the Galois-degree assertion, and step <1>11 identifies both invariant rings requested in the problem.
:::
:::
