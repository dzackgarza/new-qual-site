---
schema: qual/card@1
id: P-AGH4414FERMATCUBICHASSE
kind: problem
title: The primes where the Fermat cubic has Hasse invariant $0$ have density $\frac{1}{2}$
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
    Read Hartshorne IV.4.14 together with Proposition IV.4.21, which identifies
    the Hasse invariant with the coefficient of (xyz)^(p-1) in the (p-1)-st
    power of a homogeneous cubic equation. Cross-checked the resulting
    congruence criterion with the standard supersingularity criterion for j=0.
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
    Solutions (9 June 2019), Solution 4.4.14, printed pp. 93,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF pages are the printed
    pages. Checked against the book: Hartshorne IV.4.14, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the multinomial match $3i=3j=3k=p-1$ and the coefficient $\frac{(p-1)!}{(((p-1)/3)!)^3}$ as a unit mod $p$, and the density of the primes $2\bmod3$ as $\frac12$.
    Not checked: Yang's Solutions outside printed pp. 93; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card now carries a published-solution remark naming Yang Pi-Yeh's
    Solution 4.4.14 at printed pp. 93; it had none before. No
    step, statement or hypothesis of the card changes.
---

::: {.problem}
The Fermat curve $X: x^3+y^3=z^3$ gives a nonsingular curve in characteristic $p$ for every $p \neq 3$.
Determine the set $\mfp=\theset{p \neq 3 \st X_{(p)} \text{ has Hasse invariant } 0}$, and observe (modulo Dirichlet's theorem) that it is a set of primes of density $\frac{1}{2}$.
:::

::: {.solution}
Write the homogeneous equation as
$$
F=x^3+y^3-z^3.
$$

::: pf

::: {.pf-step #s1}

By Proposition IV.4.21, the Hasse invariant of $X_{(p)}$ is nonzero
if and only if the coefficient of
$$
(xyz)^{p-1}
$$
in $F^{p-1}$ is nonzero modulo $p$.

::: pf-proof

This is exactly Proposition IV.4.21 applied to the plane cubic $F=0$.

:::

:::

::: {.pf-step #s2}

If $p\equiv2\pmod3$, then the coefficient in step [](#s1){.pf-ref} is zero.

::: pf-proof

Every monomial occurring in
$$
(x^3+y^3-z^3)^{p-1}
$$
has each exponent divisible by $3$. For the monomial
$$
x^{p-1}y^{p-1}z^{p-1}
$$
to occur, one must therefore have
$$
3\mid p-1.
$$
If $p\equiv2\pmod3$, this is impossible. Hence the required coefficient is
zero, so the Hasse invariant vanishes.

:::

:::

::: {.pf-step #s3}

If $p\equiv1\pmod3$, then the coefficient in step [](#s1){.pf-ref} is nonzero.

::: pf-proof

Put
$$
m=\frac{p-1}{3}.
$$
There is exactly one way to obtain
$$
x^{p-1}y^{p-1}z^{p-1}=x^{3m}y^{3m}z^{3m}
$$
from the multinomial expansion: choose $x^3$, $y^3$, and $-z^3$ each
$m$ times. Its coefficient is
$$
(-1)^m\frac{(p-1)!}{(m!)^3}.
$$
Since $0<m<p$, neither $m!$ nor $(p-1)!$ is divisible by $p$. Therefore
this coefficient is nonzero in $\FF_p$, and so the Hasse invariant is
nonzero.

:::

:::

::: {.pf-step #s4}

Consequently
$$
\boxed{
\mfp=\{p\text{ prime}:p\equiv2\pmod3\}.
}
$$

::: pf-proof

The excluded prime is $p=3$. Every other prime is congruent to $1$ or $2$
modulo $3$. Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show that the Hasse invariant vanishes exactly
in the second residue class. This includes $p=2$.

:::

:::

::: {.pf-step #s5}

The set $\mfp$ has density $1/2$.

::: pf-proof

The prime number theorem for arithmetic progressions gives
$$
\pi(x;3,1)\sim\frac{x}{2\log x},
\qquad
\pi(x;3,2)\sim\frac{x}{2\log x}.
$$
Thus the primes in the two reduced residue classes modulo $3$ have equal
natural density among the primes. The single excluded prime $3$ has density
zero. Hence
$$
\delta(\mfp)=\frac{1}{\varphi(3)}=\frac12.
$$

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} determine the required set of primes and its density.

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.4.14, uses the criterion of (4.21) on the Fermat cubic: $X_{(p)}$ is supersingular exactly when $(xyz)^{p-1}$ has coefficient zero in $(x^3+y^3-z^3)^{p-1}$. A term $x^{3i}y^{3j}(-z)^{3k}$ with $i+j+k=p-1$ matches $x^{p-1}y^{p-1}z^{p-1}$ only if $3i=3j=3k=p-1$, which is impossible when $3\nmid p-1$; when $3\mid p-1$ the match is $i=j=k=\frac{p-1}{3}$ and the coefficient is $\pm\frac{(p-1)!}{(((p-1)/3)!)^3}$, a unit because neither factorial carries the prime $p$. So $X_{(p)}$ is supersingular exactly for $p\equiv2\bmod3$, and by Dirichlet that set has density $\frac12$. The printed coefficient omits the sign $(-1)^{(p-1)/3}$ that the $z$-entries contribute; it is nonzero either way, so the argument stands.
:::
