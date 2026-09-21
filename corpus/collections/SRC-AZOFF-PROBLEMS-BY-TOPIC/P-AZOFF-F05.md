---
schema: qual/card@1
id: P-AZOFF-F05
kind: problem
title: Entire functions with a pole at $\infty$ are polynomials
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Laurent expansions and singularities, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Wrote the Taylor series of the entire function at zero and viewed
    f(1/w) near w=0. A pole at infinity is exactly a pole of f(1/w) at zero,
    which permits only finitely many negative Laurent powers and at least one;
    hence f is a nonconstant polynomial. Conversely a degree-d polynomial
    has a pole of order d at infinity.
---

::: {.problem}
Find all entire functions which have poles at $\infty$
:::

::: {.solution}
<1>1. Let
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n
$$
be entire. Near infinity, use the coordinate
$$
w=\frac1z.
$$
Then
$$
f(1/w)
=
\sum_{n=0}^{\infty}a_nw^{-n}
$$
for every $w\neq0$.

::: {.proof}
Because $f$ is entire, its Taylor series at $0$ has infinite radius of
convergence. Substituting $z=1/w$ for $w\neq0$ gives the displayed Laurent
series about $w=0$.
:::

<1>2. If $f$ has a pole at $\infty$, then $f$ is a nonconstant polynomial.

::: {.proof}
By definition, $f$ has a pole at $\infty$ exactly when
$$
w\longmapsto f(1/w)
$$
has a pole at $w=0$. A Laurent series at a pole has only finitely many
negative-power terms. By step <1>1, the coefficient of $w^{-n}$ is $a_n$.
Hence there is an integer $d\geq0$ such that
$$
a_n=0
$$
for every $n>d$. Thus
$$
f(z)=\sum_{n=0}^{d}a_nz^n
$$
is a polynomial.

Since the singularity at infinity is a pole rather than removable, the
principal part of $f(1/w)$ is nonzero. Therefore some $a_n$ with $n\geq1$
is nonzero, so the polynomial is nonconstant.
:::

<1>3. Every nonconstant polynomial has a pole at $\infty$.

::: {.proof}
Let
$$
p(z)=a_0+a_1z+\cdots+a_dz^d,
\qquad
d\geq1,
\qquad
a_d\neq0.
$$
Then
$$
p(1/w)
=
a_0+a_1w^{-1}+\cdots+a_dw^{-d}.
$$
Its Laurent series at $w=0$ has highest negative power $w^{-d}$ with
nonzero coefficient $a_d$. Hence $w=0$ is a pole of order $d$ for
$p(1/w)$, so $p$ has a pole of order $d$ at $\infty$.
:::

<1>4. The complete list is the set of all nonconstant polynomials.

::: {.proof}
Step <1>2 shows that every entire function with a pole at infinity is a
nonconstant polynomial, and step <1>3 shows that every nonconstant
polynomial has such a pole.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested classification.
:::
:::
