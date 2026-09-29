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

::: pf

::: {.pf-step #intrinsic-criterion}
The first criterion is intrinsic:
\[
\boxed{
p\text{ is nonsingular}
\iff
A\text{ is a regular local ring}
\iff
\dim_k\mathfrak m/\mathfrak m^2=1.
}
\]

::: pf-proof
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

:::

::: {.pf-step #tangent-space-criterion}
Equivalently, the Zariski tangent space
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

::: pf-proof
Taking duals does not change the dimension of the finite-dimensional $k$-vector space $\mathfrak m/\mathfrak m^2$.  Apply step [](#intrinsic-criterion){.pf-ref}.
:::

:::

::: {.pf-step #jacobian-criterion}
The second criterion is the Jacobian criterion.  Suppose an affine neighborhood of $p$ is presented as
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

::: pf-proof
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
By step [](#tangent-space-criterion){.pf-ref}, nonsingularity is equivalent to this dimension being $1$, which is equivalent to
\[
\operatorname{rank}J(p)=n-1.
\]
:::

:::

::: {.pf-step #normal-domain-definition}
A domain $R$ is normal if it is integrally closed in its fraction field:
\[
\boxed{
x\in\operatorname{Frac}(R),\ x\text{ integral over }R
\Longrightarrow x\in R.
}
\]

::: pf-proof
This is the definition of a normal integral domain.
:::

:::

::: {.pf-step #regular-implies-normal}
Every regular local ring is normal.

::: pf-proof
This is the standard regular-local-ring theorem.  In the one-dimensional case needed here it can be seen concretely: if $(A,\mathfrak m)$ is a one-dimensional regular local domain, then step [](#intrinsic-criterion){.pf-ref} gives
\[
\dim_k\mathfrak m/\mathfrak m^2=1.
\]
Nakayama's lemma therefore shows that
\[
\mathfrak m=(\pi)
\]
is principal.  A one-dimensional Noetherian local domain with principal maximal ideal is a discrete valuation ring.  A DVR is integrally closed, hence normal.
:::

:::

::: {.pf-step #dvr-equivalence}
For a one-dimensional Noetherian local domain, the converse also holds:
\[
\boxed{
A\text{ normal}
\iff
A\text{ is a DVR}
\iff
A\text{ is regular}.
}
\]

::: pf-proof
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
is the characterization used in step [](#regular-implies-normal){.pf-ref}.

For the remaining implication, the standard one-dimensional normalization theorem says that a one-dimensional Noetherian local domain is integrally closed exactly when it is a DVR.  Applying it to a normal $A$ gives the result.
:::

:::

::: {.pf-step #nonsingular-regular-normal}
Consequently, for an integral curve over an algebraically closed field,
\[
\boxed{
C\text{ is nonsingular}
\iff
C\text{ is regular}
\iff
C\text{ is normal}.
}
\]

::: pf-proof
The curve is nonsingular exactly when all local rings at closed points are regular by step [](#intrinsic-criterion){.pf-ref}.  For a one-dimensional Noetherian integral scheme, step [](#dvr-equivalence){.pf-ref} identifies regularity with normality at every local ring.  Over the algebraically closed field, regularity is equivalent to smoothness, so these are exactly the nonsingular curves.
:::

:::

::: pf-qed
Steps [](#intrinsic-criterion){.pf-ref}, [](#tangent-space-criterion){.pf-ref} and [](#jacobian-criterion){.pf-ref} give the two nonsingularity criteria, and steps [](#normal-domain-definition){.pf-ref}, [](#regular-implies-normal){.pf-ref}, [](#dvr-equivalence){.pf-ref} and [](#nonsingular-regular-normal){.pf-ref} give the requested relation between normality and regular local rings.
:::

:::
:::
