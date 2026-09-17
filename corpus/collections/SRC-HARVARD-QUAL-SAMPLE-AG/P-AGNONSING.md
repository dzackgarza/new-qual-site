---
schema: qual/card@1
id: P-AGNONSING
kind: problem
title: Two criteria for nonsingularity of a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingularity
  - Regular Local Rings
  - Normal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's pair of questions on nonsingularity criteria and normal versus regular local rings.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Give two criteria for a curve over an algebraically closed field to be nonsingular.

What is a normal domain, and how does normality relate to regular local rings?
:::

::: {.solution}
Let $C$ be an integral curve of finite type over an algebraically closed field $k$, and let $p\in C$ be a closed point.  Put
\[
A=\mathcal O_{C,p},
\qquad
\mathfrak m=\mathfrak m_p.
\]
Since $C$ is a curve,
\[
\dim A=1.
\]

<1>1. The first criterion is intrinsic:
\[
\boxed{
p\text{ is nonsingular}
\iff
A\text{ is a regular local ring}
\iff
\dim_k\mathfrak m/\mathfrak m^2=1.
}
\]
::: {.proof}
For a Noetherian local ring $(A,\mathfrak m)$, regularity means
\[
\dim_{A/\mathfrak m}\mathfrak m/\mathfrak m^2=\dim A.
\]
Here $A/\mathfrak m=k$ because $k$ is algebraically closed and $p$ is closed, while $\dim A=1$.  Hence regularity is exactly
\[
\dim_k\mathfrak m/\mathfrak m^2=1.
\]

For a finite-type scheme over a perfect field, in particular over an algebraically closed field, regularity at a point is equivalent to smoothness there.  Thus this is precisely the nonsingularity criterion for the curve.
:::

<1>2. Equivalently, the Zariski tangent space
\[
T_pC=(\mathfrak m/\mathfrak m^2)^\vee
\]
has dimension $1$:
\[
\boxed{
p\text{ nonsingular}
\iff
\dim_kT_pC=1.
}
\]
::: {.proof}
Taking duals does not change the dimension of the finite-dimensional $k$-vector space $\mathfrak m/\mathfrak m^2$.  Apply <1>1.
:::

<1>3. The second criterion is the Jacobian criterion.  Suppose an affine neighborhood of $p$ is presented as
\[
C\cap U=V(f_1,\ldots,f_r)\subseteq\mathbb A^n_k.
\]
Let
\[
J(p)=\left(\frac{\partial f_i}{\partial x_j}(p)\right).
\]
Then
\[
\boxed{
p\text{ nonsingular}
\iff
\operatorname{rank}J(p)=n-1.
}
\]
::: {.proof}
A tangent vector $v=(v_1,\ldots,v_n)\in k^n$ lies in $T_pC$ exactly when every first-order variation of the equations vanishes:
\[
\sum_{j=1}^n
\frac{\partial f_i}{\partial x_j}(p)v_j=0
\qquad
\text{for every }i.
\]
Thus
\[
T_pC=\ker J(p),
\]
so
\[
\dim_kT_pC=n-\operatorname{rank}J(p).
\]
By <1>2, nonsingularity is equivalent to this dimension being $1$, which is equivalent to
\[
\operatorname{rank}J(p)=n-1.
\]
:::

<1>4. A domain $R$ is normal if it is integrally closed in its fraction field:
\[
\boxed{
x\in\operatorname{Frac}(R),\ x\text{ integral over }R
\Longrightarrow x\in R.
}
\]
::: {.proof}
This is the definition of a normal integral domain.
:::

<1>5. Every regular local ring is normal.
::: {.proof}
This is the standard regular-local-ring theorem.  In the one-dimensional case needed here it can be seen concretely: if $(A,\mathfrak m)$ is a one-dimensional regular local domain, then <1>1 gives
\[
\dim_k\mathfrak m/\mathfrak m^2=1.
\]
Nakayama's lemma therefore shows that
\[
\mathfrak m=(\pi)
\]
is principal.  A one-dimensional Noetherian local domain with principal maximal ideal is a discrete valuation ring.  A DVR is integrally closed, hence normal.
:::

<1>6. For a one-dimensional Noetherian local domain, the converse also holds:
\[
\boxed{
A\text{ normal}
\iff
A\text{ is a DVR}
\iff
A\text{ is regular}.
}
\]
::: {.proof}
The implication
\[
\text{DVR}\Longrightarrow\text{normal}
\]
follows from the valuation: if $x$ in the fraction field has negative valuation, then no monic polynomial with coefficients in the valuation ring can vanish at $x$, because the term of lowest valuation would be the highest power of $x$ and could not cancel.  Thus an element integral over a DVR has nonnegative valuation and lies in the DVR.

The equivalence
\[
\text{DVR}\Longleftrightarrow
\text{one-dimensional Noetherian regular local domain}
\]
is the characterization used in <1>5.

For the remaining implication, the standard one-dimensional normalization theorem says that a one-dimensional Noetherian local domain is integrally closed exactly when it is a DVR.  Applying it to a normal $A$ gives the result.
:::

<1>7. Consequently, for an integral curve over an algebraically closed field,
\[
\boxed{
C\text{ is nonsingular}
\iff
C\text{ is regular}
\iff
C\text{ is normal}.
}
\]
::: {.proof}
The curve is nonsingular exactly when all local rings at closed points are regular by <1>1.  For a one-dimensional Noetherian integral scheme, <1>6 identifies regularity with normality at every local ring.  Over the algebraically closed field, regularity is equivalent to smoothness, so these are exactly the nonsingular curves.
:::

<1>8. Q.E.D.
::: {.proof}
Steps <1>1--<1>3 give the two nonsingularity criteria, and steps <1>4--<1>7 give the requested relation between normality and regular local rings.
:::
:::
