---
schema: qual/card@1
id: P-BKF96-9
kind: problem
title: A distributive identity for gcd and lcm
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Compared prime valuations and reduced the identity to the distributive
    law min(A,max(B,C))=max(min(A,B),min(A,C)).
---

::: {.problem}
For positive integers $a,b,c$, prove that
\[
\gcd\bigl(a,\operatorname{lcm}(b,c)\bigr)
=
\operatorname{lcm}\bigl(\gcd(a,b),\gcd(a,c)\bigr).
\]
:::

::: {.solution}
Fix a prime $p$ and write
$$
A=v_p(a),
\qquad
B=v_p(b),
\qquad
C=v_p(c).
$$

<1>1. One has
$$
v_p\!\left(
\gcd\bigl(a,\operatorname{lcm}(b,c)\bigr)
\right)
=
\min\bigl(A,\max(B,C)\bigr).
$$

::: {.proof}
For positive integers,
$$
v_p(\gcd(r,s))
=
\min(v_p(r),v_p(s))
$$
and
$$
v_p(\operatorname{lcm}(r,s))
=
\max(v_p(r),v_p(s)).
$$
Apply these formulas first to $\operatorname{lcm}(b,c)$ and then to the
outer gcd.
:::

<1>2. One has
$$
v_p\!\left(
\operatorname{lcm}\bigl(\gcd(a,b),\gcd(a,c)\bigr)
\right)
=
\max\bigl(\min(A,B),\min(A,C)\bigr).
$$

::: {.proof}
Apply the same two valuation formulas, first to the two gcds and then to
the outer lcm.
:::

<1>3. For all real numbers $A,B,C$,
$$
\min\bigl(A,\max(B,C)\bigr)
=
\max\bigl(\min(A,B),\min(A,C)\bigr).
$$

::: {.proof}
Interchange $B$ and $C$ if necessary and assume
$$
B\leq C.
$$
Then
$$
\max(B,C)=C.
$$
Also
$$
\min(A,B)\leq\min(A,C),
$$
so
$$
\max\bigl(\min(A,B),\min(A,C)\bigr)
=
\min(A,C).
$$
This equals
$$
\min\bigl(A,\max(B,C)\bigr).
$$
:::

<1>4. The two integers in the statement have the same $p$-adic valuation
for every prime $p$.

::: {.proof}
Combine steps <1>1--<1>3.
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
Two positive integers are equal exactly when their $p$-adic valuations
agree for every prime $p$. Step <1>4 gives that agreement.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required identity.
:::
:::
