---
schema: qual/card@1
id: P-AGH4413SUPERSINGULARJATTHIRTEEN
kind: problem
title: The unique $j$ with vanishing Hasse invariant when $p=13$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.13 with the preceding Hasse-invariant formula and
    the Legendre j-formula. Cross-checked the Legendre Hasse polynomial
    formula against MIT 18.783 notes.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
If $p=13$, there is just one value of $j$ for which the Hasse invariant of the corresponding curve is 0. Find it.
Answer: $j=5 \pmod{13}$.
:::

::: {.solution}
Work over the algebraically closed field $k$ of characteristic $13$.

<1>1. For the Legendre curve
$$
E_\lambda:
\qquad
y^2=x(x-1)(x-\lambda),
\qquad
\lambda\ne0,1,
$$
the Hasse invariant vanishes exactly when
$$
S_{13}(\lambda)=0,
$$
where
$$
\boxed{
S_{13}(T)
=
1+10T+4T^2+10T^3+4T^4+10T^5+T^6
}
$$
in $\FF_{13}[T]$.

::: {.proof}
For an odd prime $p$ and
$$
E:y^2=f(x)
$$
with $f$ a monic cubic, the Hasse invariant is the coefficient of
$x^{p-1}$ in
$$
f(x)^{(p-1)/2}.
$$
For
$$
f(x)=x(x-1)(x-\lambda)
$$
this coefficient is, up to the sign
$(-1)^{(p-1)/2}$,
$$
S_p(\lambda)
=
\sum_{i=0}^{(p-1)/2}
\binom{(p-1)/2}{i}^2\lambda^i.
$$
Here $(p-1)/2=6$, so the sign is $1$.  Reducing
$$
\binom60^2,\binom61^2,\ldots,\binom66^2
$$
modulo $13$ gives
$$
1,10,4,10,4,10,1,
$$
which is the displayed polynomial.
:::

<1>2. In $\FF_{13}[T]$ one has the identity
$$
\boxed{
256(T^2-T+1)^3
-5T^2(T-1)^2
=
-4S_{13}(T).
}
$$

::: {.proof}
Since $256\equiv9\pmod{13}$, direct expansion of the left-hand side gives
$$
-4T^6-T^5-3T^4-T^3-3T^2-T-4.
$$
On the other hand,
$$
-4S_{13}(T)
=
-4T^6-T^5-3T^4-T^3-3T^2-T-4
$$
in $\FF_{13}[T]$.
:::

<1>3. Every elliptic curve in characteristic $13$ whose Hasse invariant
vanishes has
$$
\boxed{j=5}.
$$

::: {.proof}
Over the algebraically closed field $k$, every elliptic curve is isomorphic
to a Legendre curve $E_\lambda$: its three nonzero points of order $2$ give
three distinct branch points, which can be moved to $0,1,\lambda$.

For such a curve, step <1>1 gives
$$
S_{13}(\lambda)=0.
$$
Also
$$
S_{13}(0)=S_{13}(1)=1,
$$
so a root of $S_{13}$ is never $0$ or $1$.  Dividing the identity in step
<1>2 by
$$
\lambda^2(\lambda-1)^2
$$
and using Hartshorne's Legendre formula
$$
j(E_\lambda)
=
256\frac{(\lambda^2-\lambda+1)^3}
{\lambda^2(\lambda-1)^2}
$$
therefore gives
$$
j(E_\lambda)=5.
$$
:::

<1>4. There exists an elliptic curve with vanishing Hasse invariant in
characteristic $13$.

::: {.proof}
The polynomial $S_{13}$ has degree $6$, so it has a root
$\lambda\in k$ because $k$ is algebraically closed.  Step <1>3 shows that
$\lambda\ne0,1$, so $E_\lambda$ is smooth, and step <1>1 says its Hasse
invariant vanishes.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 shows that no $j$-value other than $5$ can occur, while step
<1>4 shows that this value is attained.
:::
:::
