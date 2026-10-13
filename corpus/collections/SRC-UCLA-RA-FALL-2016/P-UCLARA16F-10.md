---
schema: qual/card@1
id: P-UCLARA16F-10
kind: problem
title: Filled Julia set of $z^2-1$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Consider the quadratic polynomial $f(z)=z^2-1$ on $\mathbb C$.
We are interested in the iterates $f^n$ of $f$, defined by $f^0=\operatorname{id}_{\mathbb C}$ and
\[
f^n=\underbrace{f\circ\cdots\circ f}_{n\text{ factors}}
\]
for $n\in\mathbb N$.

(a) Find an explicit constant $M>0$ such that for each $z\in\mathbb C$ either (i) $|f^n(z)|\to\infty$ as $n\to\infty$, or (ii) $|f^n(z)|\le M$ for all $n\in\mathbb N_0$.

(b) Let $U$ be the set of all $z\in\mathbb C$ for which (i) holds and $K$ the set of all $z\in\mathbb C$ for which (ii) holds.
Show that $U$ is open and $K$ is compact without “holes”, i.e. $\mathbb C\setminus K$ has no bounded connected components.
:::

::: {.solution}
Let
\[
f(z)=z^2-1.
\]

## Part (a)

We claim that
\[
\boxed{M=2}
\]
works.

<1>1. If
\[
|w|>2,
\]
then
\[
\boxed{
|f(w)|
\ge
|w|^2-1}.
\]

::: {.proof}
By the reverse triangle inequality,
\[
|w^2-1|
\ge
\bigl||w|^2-1\bigr|
=
|w|^2-1,
\]
since \(|w|>1\).
:::

<1>2. If
\[
|w|>2,
\]
then
\[
\boxed{
|w|^2-1>\frac32|w|}.
\]

::: {.proof}
For \(r=|w|>2\),
\[
r^2-1-\frac32r
=
\left(r-2\right)\left(r+\frac12\right)
>0.
\]
:::

<1>3. Hence if
\[
|w|>2,
\]
then
\[
\boxed{
|f(w)|>\frac32|w|>2}.
\]

::: {.proof}
Combine steps <1>1--<1>2.
:::

Suppose now that for some \(N\ge0\),
\[
|f^N(z)|>2.
\]

<1>4. For every \(m\ge0\),
\[
\boxed{
|f^{N+m}(z)|
>
\left(\frac32\right)^m
|f^N(z)|}.
\]

::: {.proof}
Use induction. The case \(m=0\) is equality. If the bound holds at \(m\), then in particular
\[
|f^{N+m}(z)|>2,
\]
so step <1>3 gives
\[
|f^{N+m+1}(z)|
>
\frac32|f^{N+m}(z)|
>
\left(\frac32\right)^{m+1}|f^N(z)|.
\]
:::

<1>5. Therefore
\[
\boxed{
|f^n(z)|\to\infty}.
\]

::: {.proof}
The lower bound in step <1>4 grows geometrically to \(+\infty\).
:::

<1>6. Consequently, if the orbit does not tend to infinity, then
\[
\boxed{
|f^n(z)|\le2}
\]
for every \(n\ge0\).

::: {.proof}
If some iterate had modulus \(>2\), step <1>5 would force escape.
:::

<1>7. Thus for every \(z\in\mathbb C\), exactly one of the following holds:
- \(|f^n(z)|\to\infty\);
- \(|f^n(z)|\le2\) for all \(n\ge0\).

::: {.proof}
Step <1>5 handles any orbit that ever leaves the closed disk of radius \(2\), while step <1>6 handles every remaining orbit.
:::

<1>8. Hence
\[
\boxed{M=2}
\]
is an admissible constant.

::: {.proof}
This is exactly the dichotomy in step <1>7.
:::

## Part (b): openness and compactness

Define
\[
U
=
\{z:|f^n(z)|\to\infty\}
\]
and
\[
K
=
\{z:|f^n(z)|\le2\text{ for all }n\ge0\}.
\]

<1>9. One has
\[
\boxed{
U
=
\bigcup_{N=0}^{\infty}
\{z:|f^N(z)|>2\}}.
\]

::: {.proof}
If \(z\in U\), then eventually \(|f^N(z)|>2\). Conversely, if some iterate has modulus \(>2\), step <1>5 gives escape.
:::

<1>10. For each \(N\),
\[
\{z:|f^N(z)|>2\}
\]
is open.

::: {.proof}
The iterate \(f^N\) is a polynomial, hence continuous, and
\[
\{w:|w|>2\}
\]
is open.
:::

<1>11. Therefore
\[
\boxed{U\text{ is open}.}
\]

::: {.proof}
Use steps <1>9--<1>10 and closure of open sets under arbitrary unions.
:::

<1>12. One has
\[
\boxed{
K=\mathbb C\setminus U}.
\]

::: {.proof}
Part (a), step <1>7, gives the exact dichotomy between escape and boundedness by \(2\).
:::

<1>13. Hence
\[
\boxed{K\text{ is closed}.}
\]

::: {.proof}
It is the complement of the open set \(U\).
:::

<1>14. Also,
\[
\boxed{
K\subseteq\{z:|z|\le2\}}.
\]

::: {.proof}
The defining condition for \(K\) includes the case \(n=0\):
\[
|f^0(z)|=|z|\le2.
\]
:::

<1>15. Therefore
\[
\boxed{K\text{ is compact}.}
\]

::: {.proof}
The set \(K\) is closed by step <1>13 and bounded by step <1>14. Apply Heine--Borel in \(\mathbb C\cong\mathbb R^2\).
:::

## No bounded components of the complement

Suppose, toward a contradiction, that \(V\) is a bounded connected component of
\[
\mathbb C\setminus K=U.
\]

<1>16. The boundary of \(V\) satisfies
\[
\boxed{
\partial V\subseteq K}.
\]

::: {.proof}
Since \(V\) is a connected component of the open set \(U\), no boundary point of \(V\) can lie in \(U\). Indeed, if \(z_0\in\partial V\cap U\), then because \(U\) is open there is a connected disk
\[
D(z_0,\rho)\subseteq U.
\]
Because \(z_0\in\partial V\), this disk meets \(V\). Thus the disk and \(V\) lie in the same connected component of \(U\), forcing \(z_0\in V\), contradiction. Hence
\[
\partial V\subseteq\mathbb C\setminus U=K.
\]
:::

<1>17. For every \(n\ge0\) and every \(z\in\partial V\),
\[
\boxed{
|f^n(z)|\le2}.
\]

::: {.proof}
By step <1>16,
\[
z\in K,
\]
and this is the defining property of \(K\).
:::

<1>18. For each fixed \(n\), the maximum modulus principle gives
\[
\boxed{
|f^n(z)|\le2}
\]
for every \(z\in V\).

::: {.proof}
The domain \(V\) is bounded, and the polynomial \(f^n\) is holomorphic on a neighborhood of \(\overline V\) and continuous there. By step <1>17, its modulus is at most \(2\) on \(\partial V\). The maximum modulus principle therefore gives the same bound throughout \(V\).
:::

<1>19. Hence every \(z\in V\) satisfies
\[
|f^n(z)|\le2
\]
for all \(n\ge0\).

::: {.proof}
Step <1>18 holds for each \(n\).
:::

<1>20. Therefore
\[
V\subseteq K.
\]

::: {.proof}
Step <1>19 is exactly the defining condition for membership in \(K\).
:::

<1>21. This contradicts
\[
V\subseteq U=\mathbb C\setminus K.
\]

::: {.proof}
A set cannot be contained simultaneously in \(K\) and its complement.
:::

<1>22. Therefore \(U\) has no bounded connected components.

::: {.proof}
The assumption of a bounded connected component led to the contradiction in step <1>21.
:::

<1>23. Equivalently,
\[
\boxed{
K\text{ has no holes}.}
\]

::: {.proof}
By definition in the problem, “no holes” means that \(\mathbb C\setminus K\) has no bounded connected components.
:::

<1>24. Q.E.D.

::: {.proof}
Step <1>8 proves part (a); steps <1>11 and <1>15 prove openness of \(U\) and compactness of \(K\); step <1>23 proves that \(K\) has no holes.
:::
:::
