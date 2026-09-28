---
schema: qual/card@1
id: P-BKF11-2B
kind: problem
title: When $k[x]/(x^4+6x-12)$ is a field for $k=\mathbb C,\mathbb R,\mathbb Q,\mathbb F_{2011^2}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 2B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked irreducibility over Q by Eisenstein at 3 and the finite-field
    degree argument over the quadratic extension of F_2011.
---

::: {.problem}
Let $k$ be one of the fields $\CC$, $\RR$, $\QQ$, or
$\FF_{4044121}$, where $4044121=2011^2$ and $2011$ is prime.

For which of these choices of $k$ is
$$
k[x]/(x^4+6x-12)
$$
a field?
:::

::: {.solution}
Put
$$
f(x)\coloneqq x^4+6x-12.
$$

<1>1. For any field $k$, the quotient $k[x]/(f)$ is a field if and
only if $f$ is irreducible in $k[x]$.

::: {.proof}
The polynomial ring $k[x]$ is a principal ideal domain. Hence the
principal ideal $(f)$ is maximal exactly when $f$ is irreducible.
The quotient by an ideal is a field exactly when the ideal is maximal.
:::

<1>2. The polynomial $f$ is reducible over $\CC$ and over $\RR$.

::: {.proof}
By the fundamental theorem of algebra, every complex polynomial of
positive degree has a complex root. Since $\deg f=4>1$, a linear
factor obtained from such a root makes $f$ reducible in $\CC[x]$.

Every irreducible real polynomial has degree at most $2$: nonreal
complex roots occur in conjugate pairs, giving real quadratic factors.
Since $f$ has degree $4$, it is therefore reducible in $\RR[x]$.
:::

<1>3. The polynomial $f$ is irreducible over $\QQ$.

::: {.proof}
Apply Eisenstein's criterion with the prime $3$. The prime $3$
divides every nonleading coefficient of
$$
x^4+0x^3+0x^2+6x-12,
$$
while $3\nmid1$ and $9\nmid12$. Thus $f$ is irreducible in
$\QQ[x]$.
:::

<1>4. The polynomial $f$ is reducible over $\FF_{2011^2}$.

::: {.proof}
Regard $f$ first as an element of $\FF_{2011}[x]$.

If $f$ is reducible over $\FF_{2011}$, then the same factorization
is a factorization over the extension field $\FF_{2011^2}$.

Suppose instead that $f$ is irreducible over $\FF_{2011}$. Let
$\alpha$ be a root in an algebraic closure. An irreducible polynomial
of degree $4$ over $\FF_{2011}$ has its roots in
$\FF_{2011^4}$, and
$$
\FF_{2011^2}\subset\FF_{2011^4},
\qquad
[\FF_{2011^4}:\FF_{2011^2}]=2.
$$
Consequently the minimal polynomial of $\alpha$ over
$\FF_{2011^2}$ has degree at most $2$. It divides $f$, so $f$ has a
proper factor over $\FF_{2011^2}$ and is reducible there.

Thus $f$ is reducible over $\FF_{2011^2}$ in either case.
:::

<1>5. Among the four choices, the quotient is a field exactly for
$$
\boxed{k=\QQ}.
$$

::: {.proof}
By step <1>1, the quotient is a field exactly when $f$ is
irreducible. Step <1>3 gives irreducibility over $\QQ$, whereas
steps <1>2 and <1>4 give reducibility over the other three listed
fields.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the complete list of choices of $k$.
:::
:::
