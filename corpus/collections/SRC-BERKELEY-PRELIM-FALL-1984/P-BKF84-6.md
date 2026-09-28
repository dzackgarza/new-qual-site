---
schema: qual/card@1
id: P-BKF84-6
kind: problem
title: A distributive identity for gcd and lcm
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the identity prime by prime using the distributive law for minimum and maximum of the three valuations.
---

::: {.problem}
For nonzero integers $a,b,c$, prove that
\[
\gcd\bigl(a,\operatorname{lcm}(b,c)\bigr)
=
\operatorname{lcm}\bigl(\gcd(a,b),\gcd(a,c)\bigr).
\]
:::

::: {.solution}
<1>1. Fix a prime $p$ and set
$$
\alpha=v_p(a),
\qquad
\beta=v_p(b),
\qquad
\gamma=v_p(c),
$$
where the valuations are taken on the absolute values of the nonzero
integers.

::: {.proof}
For nonzero integers, prime factorization gives
$$
v_p(\gcd(r,s))
=
\min\{v_p(r),v_p(s)\}
$$
and
$$
v_p(\operatorname{lcm}(r,s))
=
\max\{v_p(r),v_p(s)\}.
$$
:::

<1>2. The exponent of $p$ on the left-hand side is
$$
\min\bigl(\alpha,\max(\beta,\gamma)\bigr).
$$

::: {.proof}
Apply the two valuation formulas from step <1>1 first to
$\operatorname{lcm}(b,c)$ and then to its gcd with $a$.
:::

<1>3. The exponent of $p$ on the right-hand side is
$$
\max\bigl(\min(\alpha,\beta),\min(\alpha,\gamma)\bigr).
$$

::: {.proof}
Apply the gcd formula separately to $(a,b)$ and $(a,c)$ and then apply
the lcm formula to the resulting two integers.
:::

<1>4. For all real numbers $\alpha,\beta,\gamma$,
$$
\min\bigl(\alpha,\max(\beta,\gamma)\bigr)
=
\max\bigl(\min(\alpha,\beta),\min(\alpha,\gamma)\bigr).
$$

::: {.proof}
If $\beta\leq\gamma$, then the left-hand side is
$$
\min(\alpha,\gamma).
$$
Also
$$
\min(\alpha,\beta)
\leq
\min(\alpha,\gamma),
$$
so the right-hand side is the same number. The case
$\gamma\leq\beta$ is symmetric.
:::

<1>5. Therefore
$$
\boxed{
\gcd\bigl(a,\operatorname{lcm}(b,c)\bigr)
=
\operatorname{lcm}\bigl(\gcd(a,b),\gcd(a,c)\bigr)
}.
$$

::: {.proof}
By steps <1>2--<1>4, the two positive integers in the displayed formula
have the same $p$-adic valuation for every prime $p$. Uniqueness of
prime factorization therefore makes them equal.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the desired identity.
:::
:::
