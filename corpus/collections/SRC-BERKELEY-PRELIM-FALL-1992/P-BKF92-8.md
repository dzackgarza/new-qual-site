---
schema: qual/card@1
id: P-BKF92-8
kind: problem
title: An irreducible minimal polynomial controls cyclic-subspace dimensions
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Made V a vector space over F[t]/(mu); each nonzero cyclic subspace is one
    dimensional over that field, and dim_F V is its field degree times dim_E V.
---

::: {.problem}
Let $F$ be a field, let $V$ be finite-dimensional over $F$, and let $T:V\to V$ have irreducible minimal polynomial $\mu\in F[t]$.

1. If $0\ne v\in V$ and $V_1$ is the subspace spanned by $v$ and its images under the positive powers of $T$, prove that
\[
\dim V_1=\deg\mu.
\]
2. Prove that $\deg\mu$ divides $\dim V$.
:::

::: {.solution}
Put
$$
E\coloneqq F[t]/(\mu).
$$

<1>1. The quotient $E$ is a field and
$$
\dim_F E=\deg\mu.
$$

::: {.proof}
The polynomial $\mu$ is irreducible over the field $F$, so the ideal $(\mu)$ is maximal in $F[t]$. Hence $E$ is a field. If $d=\deg\mu$, every residue class has a unique representative of degree less than $d$, so
$$
1,t,\ldots,t^{d-1}
$$
give an $F$-basis of $E$.
:::

<1>2. The vector space $V$ carries an $E$-vector-space structure defined by
$$
[p(t)]\cdot v\coloneqq p(T)v.
$$

::: {.proof}
Since $\mu$ is the minimal polynomial of $T$,
$$
\mu(T)=0.
$$
If $p\equiv q\pmod\mu$, then $p-q=\mu r$ for some $r\in F[t]$, so
$$
(p(T)-q(T))v
=
\mu(T)r(T)v
=0.
$$
Thus the action is well-defined. The vector-space axioms follow from the usual polynomial functional calculus for $T$.
:::

<1>3. If $0\ne v\in V$, then the $E$-subspace $Ev$ is one-dimensional over $E$.

::: {.proof}
The vector $v$ itself spans $Ev$ over $E$. If $\alpha\in E$ satisfies
$$
\alpha v=0
$$
and $\alpha\ne0$, then $\alpha$ is invertible because $E$ is a field. Multiplying by $\alpha^{-1}$ would give $v=0$, a contradiction. Hence $v$ is an $E$-basis of $Ev$.
:::

<1>4. The subspace $V_1$ in part 1 is exactly $Ev$.

::: {.proof}
By definition,
$$
V_1=F[T]v,
$$
the $F$-span of $v,Tv,T^2v,\ldots$. The action in step <1>2 factors $F[T]$ through the quotient $E=F[t]/(\mu)$, so its image on $v$ is precisely $Ev$.
:::

<1>5. Therefore
$$
\boxed{\dim_F V_1=\deg\mu}.
$$

::: {.proof}
By steps <1>3--<1>4, $V_1$ is one-dimensional over $E$. Thus step <1>1 gives
$$
\dim_F V_1
=
\dim_E V_1\cdot\dim_F E
=
1\cdot\deg\mu.
$$
:::

<1>6. The space $V$ is finite-dimensional over $E$.

::: {.proof}
Any finite $F$-basis of $V$ is also a finite spanning set over the larger scalar field $E$, because $F$ embeds in $E$. Hence $V$ has finite dimension over $E$.
:::

<1>7. One has
$$
\boxed{\deg\mu\mid\dim_F V}.
$$

::: {.proof}
Let
$$
r\coloneqq\dim_E V.
$$
By the dimension formula for extension of scalars and step <1>1,
$$
\dim_F V
=
r\dim_F E
=
r\deg\mu.
$$
Thus $\deg\mu$ divides $\dim_F V$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>5 proves part 1, and step <1>7 proves part 2.
:::
:::
