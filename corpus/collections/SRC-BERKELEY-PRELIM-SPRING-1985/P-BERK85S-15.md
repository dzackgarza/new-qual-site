---
schema: qual/card@1
id: P-BERK85S-15
kind: problem
title: Cubic polynomial for $\zeta_7+\zeta_7^{-1}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Divided the seventh-cyclotomic relation by zeta^3 and expressed
    zeta^2+zeta^{-2} and zeta^3+zeta^{-3} as polynomials in
    alpha=zeta+zeta^{-1}.
---

::: {.problem}
Let
\[
\zeta=e^{2\pi i/7}
\]
and set
\[
\alpha=\zeta+\zeta^{-1}.
\]
Find a cubic polynomial with integer coefficients having $\alpha$ as a root.
:::

::: {.solution}
<1>1. Since $\zeta$ is a primitive seventh root of unity,
$$
1+\zeta+\zeta^2+\zeta^3+\zeta^4+\zeta^5+\zeta^6=0.
$$

::: {.proof}
One has $\zeta^7=1$ and $\zeta\neq1$. Hence
$$
0
=
\frac{\zeta^7-1}{\zeta-1}
=
1+\zeta+\cdots+\zeta^6.
$$
:::

<1>2. Dividing the relation in step <1>1 by $\zeta^3$ gives
$$
(\zeta^3+\zeta^{-3})
+
(\zeta^2+\zeta^{-2})
+
(\zeta+\zeta^{-1})
+1
=0.
$$

::: {.proof}
Since $\zeta^7=1$,
$$
\zeta^{-1}=\zeta^6,
\qquad
\zeta^{-2}=\zeta^5,
\qquad
\zeta^{-3}=\zeta^4.
$$
The displayed equation is exactly the divided cyclotomic relation.
:::

<1>3. In terms of $\alpha=\zeta+\zeta^{-1}$,
$$
\zeta^2+\zeta^{-2}
=
\alpha^2-2
$$
and
$$
\zeta^3+\zeta^{-3}
=
\alpha^3-3\alpha.
$$

::: {.proof}
Squaring $\alpha$ gives
$$
\alpha^2
=
\zeta^2+2+\zeta^{-2}.
$$
Similarly,
$$
\alpha^3
=
\zeta^3+3\zeta+3\zeta^{-1}+\zeta^{-3}
=
\zeta^3+\zeta^{-3}+3\alpha.
$$
Rearranging gives both identities.
:::

<1>4. The number $\alpha$ is a root of
$$
\boxed{p(x)=x^3+x^2-2x-1\in\ZZ[x]}.
$$

::: {.proof}
Substitute the identities from step <1>3 into step <1>2:
$$
(\alpha^3-3\alpha)
+
(\alpha^2-2)
+
\alpha
+1
=0.
$$
Collecting terms yields
$$
\alpha^3+\alpha^2-2\alpha-1=0.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested cubic polynomial with integer coefficients.
:::
:::
