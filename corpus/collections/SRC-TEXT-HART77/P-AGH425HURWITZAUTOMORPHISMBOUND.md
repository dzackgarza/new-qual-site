---
schema: qual/card@1
id: P-AGH425HURWITZAUTOMORPHISMBOUND
kind: problem
title: A curve of genus $g \geq 2$ has at most $84(g-1)$ automorphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Genus
  - Curves
relations: []
review: draft
---

::: {.problem}
Prove the theorem of Hurwitz that a curve $X$ of genus $g \geq 2$ over a field of characteristic 0 has at most $84(g-1)$ automorphisms.

We will see later (Ex.
5.2) or (V, Ex.
1.11) that the group $G=\Aut X$ is finite.
So let $G$ have order $n$.
Then $G$ acts on the function field $K(X)$.
Let $L$ be the fixed field.
Then the field extension $L \subseteq K(X)$ corresponds to a finite morphism of curves $f: X \to Y$ of degree $n$.

a. If $P \in X$ is a ramification point, and $e_P=r$, show that $f^{-1} f(P)$ consists of exactly $n / r$ points, each having ramification index $r$.
Let $P_1, \ldots, P_s$ be a maximal set of ramification points of $X$ lying over distinct points of $Y$, and let $e_{P_i}=r_i$.
Then show that Hurwitz's theorem implies that
$$
{2 g-2 \over n } =2 g(Y)-2+\sum_{i=1}^s\left(1- {1\over r_i}\right)
$$

b. Since $g \geq 2$, the left hand side of the equation is $>0$.
Show that if $g(Y) \geq 0$, $s \geq 0$, $r_i \geq 2$, $i=1, \ldots, s$ are integers such that
$$
2g(Y)-2+\sum_{i=1}^s\left(1- {1\over r_i}\right)>0,
$$
then the minimum value of this expression is $1/42$.
Conclude that $n \leq 84(g-1)$.

See (Ex.
5.7) for an example where this maximum is achieved.
It is known that this maximum is achieved for infinitely many values of $g$ (Macbeath).
Over a field of characteristic $p>0$, the same bound holds, provided $p>g+1$, with one exception, namely the hyperelliptic curve $y^2=x^p-x$, which has $p=2g+1$ and $2p(p^2-1)$ automorphisms (Roquette).
:::
