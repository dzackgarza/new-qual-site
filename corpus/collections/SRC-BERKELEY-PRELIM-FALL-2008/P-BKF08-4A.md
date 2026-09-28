---
schema: qual/card@1
id: P-BKF08-4A
kind: problem
title: Holomorphic antiderivatives of $z^n/(1+z^2)$ on $\lvert z\rvert>1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 4A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Laurent expansion on the exterior annulus and the exact
    condition under which its z^{-1} coefficient occurs.
---

::: {.problem}
For which integer values of $n$ (positive, negative, or zero) is there a holomorphic function defined for $\abs{z}>1$ whose derivative is
$$
\frac{z^n}{1+z^2}?
$$
:::

::: {.solution}
Put
$$
\Omega\coloneqq\{z\in\CC:\abs{z}>1\},
\qquad
f_n(z)\coloneqq\frac{z^n}{1+z^2}.
$$

<1>1. On $\Omega$ one has the Laurent expansion
$$
f_n(z)
=\sum_{m=0}^{\infty}(-1)^m z^{n-2-2m}.
$$

::: {.proof}
For $\abs{z}>1$, one has $\abs{z^{-2}}<1$, so the geometric series gives
$$
\frac1{1+z^{-2}}
=\sum_{m=0}^{\infty}(-1)^m z^{-2m}.
$$
Since
$$
f_n(z)=\frac{z^{n-2}}{1+z^{-2}},
$$
multiplication by $z^{n-2}$ gives the claimed Laurent expansion. The
geometric series converges uniformly on compact subsets of $\Omega$.
:::

<1>2. A holomorphic function on $\Omega$ has a holomorphic primitive on
$\Omega$ if and only if the coefficient of $z^{-1}$ in its Laurent series
is zero.

::: {.proof}
If
$$
F(z)=\sum_{j\in\ZZ}a_jz^j
$$
is holomorphic on $\Omega$, then termwise differentiation gives
$$
F'(z)=\sum_{j\in\ZZ}j a_j z^{j-1}.
$$
The coefficient of $z^{-1}$ in $F'$ is zero, since it could only come from
$j=0$, whose derivative vanishes.

Conversely, let
$$
g(z)=\sum_{j\in\ZZ}c_jz^j
$$
be holomorphic on $\Omega$ with $c_{-1}=0$. Then the Laurent series
$$
G(z)=\sum_{j\ne-1}\frac{c_j}{j+1}z^{j+1}
$$
converges locally uniformly on the same annulus and may be differentiated
termwise there. Hence $G$ is holomorphic on $\Omega$ and $G'=g$.
:::

<1>3. The Laurent expansion in step <1>1 has a $z^{-1}$ term if and only
if $n$ is a positive odd integer.

::: {.proof}
The exponent of the $m$-th term is $n-2-2m$. It equals $-1$ exactly when
$$
m=\frac{n-1}{2}.
$$
Such an integer $m\ge0$ exists exactly when $n$ is odd and $n\ge1$.
:::

<1>4. The required integer values are
$$
\boxed{n<0\quad\text{or}\quad n\text{ is even}}.
$$

::: {.proof}
By step <1>2, $f_n$ has a holomorphic primitive on $\Omega$ exactly when
its $z^{-1}$ Laurent coefficient vanishes. Step <1>3 says that the
coefficient is nonzero exactly for the positive odd integers. The
complement of those integers is precisely the set displayed above.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives exactly the requested values of $n$.
:::
:::
