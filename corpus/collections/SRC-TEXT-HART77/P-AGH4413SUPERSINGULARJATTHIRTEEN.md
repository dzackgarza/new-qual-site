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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.4.13, printed p. 93,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.4.13, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed $h_{13}$ from $\binom6i^2$ mod $13$; its factorisation into three irreducible quadratics over $\FF_{13}$; that $j=0$ only at $4,10$ and $j=1728$ only at $2,7,12$; the identity $256(\lambda^2-\lambda+1)^3-5\lambda^2(\lambda-1)^2\equiv-4h_{13}$ mod $13$; and $\#E(\FF_{13})=14$ with $j=5$ for $y^2=x^3+4x+7$.
    Not checked: Yang's Solutions outside printed p. 93; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card now carries a published-solution remark naming Yang Pi-Yeh's
    Solution 4.4.13 at printed p. 93; it had none before. No
    step, statement or hypothesis of the card changes.
---

::: {.problem}
If $p=13$, there is just one value of $j$ for which the Hasse invariant of the corresponding curve is 0. Find it.
Answer: $j=5 \pmod{13}$.
:::

::: {.solution}
Work over the algebraically closed field $k$ of characteristic $13$.

::: pf

::: {.pf-step #s1}

For the Legendre curve
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

::: pf-proof

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

:::

::: {.pf-step #s2}

In $\FF_{13}[T]$ one has the identity
$$
\boxed{
256(T^2-T+1)^3
-5T^2(T-1)^2
=
-4S_{13}(T).
}
$$

::: pf-proof

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

:::

::: {.pf-step #s3}

Every elliptic curve in characteristic $13$ whose Hasse invariant
vanishes has
$$
\boxed{j=5}.
$$

::: pf-proof

Over the algebraically closed field $k$, every elliptic curve is isomorphic
to a Legendre curve $E_\lambda$: its three nonzero points of order $2$ give
three distinct branch points, which can be moved to $0,1,\lambda$.

For such a curve, step [](#s1){.pf-ref} gives
$$
S_{13}(\lambda)=0.
$$
Also
$$
S_{13}(0)=S_{13}(1)=1,
$$
so a root of $S_{13}$ is never $0$ or $1$.  Dividing the identity in step
[](#s2){.pf-ref} by
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

:::

::: {.pf-step #s4}

There exists an elliptic curve with vanishing Hasse invariant in
characteristic $13$.

::: pf-proof

The polynomial $S_{13}$ has degree $6$, so it has a root
$\lambda\in k$ because $k$ is algebraically closed.  Step [](#s3){.pf-ref} shows that
$\lambda\ne0,1$, so $E_\lambda$ is smooth, and step [](#s1){.pf-ref} says its Hasse
invariant vanishes.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} shows that no $j$-value other than $5$ can occur, while step
[](#s4){.pf-ref} shows that this value is attained.

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.4.13, printed p. 93, computes the Hasse invariant of the Legendre curve in characteristic $13$ as $h_{13}(\lambda)=\sum_{i=0}^{6}\binom{6}{i}^2\lambda^i=\lambda^6+10\lambda^5+4\lambda^4+10\lambda^3+4\lambda^2+10\lambda+1$, which is right --- $\binom{6}{i}^2$ is $1,36,225,400,225,36,1$, i.e. $1,10,4,10,4,10,1$ mod $13$ --- and argues that its six roots carry a single $j$-invariant: the five transforms $\lambda\mapsto\frac1\lambda,1-\lambda,\frac{1}{1-\lambda},\frac{\lambda}{\lambda-1},\frac{\lambda-1}{\lambda}$ preserve $j$, hence carry roots to roots, so the roots are one $\Sigma_3$-orbit provided no root has $j=0$ (where the orbit has size three) or $j=1728$ (size two). The two computations that exclude those cases are garbled as printed --- one line opens a bracket it does not close and carries a stray ')' --- but the claim is true: $j=0$ at $\lambda=4,10$ and $j=1728$ at $\lambda=2,7,\tfrac12$, and $h_{13}$ vanishes at none of them, its six roots being the roots of the three irreducible quadratics $\lambda^2-6\lambda+1$, $\lambda^2-\lambda+3$ and $\lambda^2+4\lambda-4$ over $\FF_{13}$. The conclusion was checked here as well: $256(\lambda^2-\lambda+1)^3-5\lambda^2(\lambda-1)^2\equiv-4h_{13}(\lambda)\pmod{13}$ coefficient by coefficient, so $j\equiv5$ at every root; and the model curve $y^2=x^3+4x+7$ has exactly $14$ points over $\FF_{13}$, i.e. trace $0$ and supersingular, with $j\equiv5$.
:::
