---
schema: qual/card@1
id: P-BKS11-2A
kind: problem
title: Minimal polynomial of $2\cos(2\pi/7)$ and non-constructibility
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 1 of the retained Spring 2011 solution PDF and independently reviewed the cyclotomic and mod-2 irreducibility argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the cubic relation, irreducibility over Q, and the tower-law obstruction to a 2-power-degree overfield.
---

::: {.problem}
Find an irreducible polynomial over the integers with $2 \cos ( 2 \pi / 7 )$ as a root, and use this to show that it is not contained in any extension of the rational numbers of degree a power of 2.
:::

::: {.solution}
Set
$$
\zeta\coloneqq e^{2\pi i/7}
$$
and
$$
\alpha\coloneqq\zeta+\zeta^{-1}
=
2\cos(2\pi/7).
$$

<1>1. The number $\alpha$ satisfies
$$
\alpha^3+\alpha^2-2\alpha-1=0.
$$

::: {.proof}
Expanding gives
$$
\alpha^2
=
\zeta^2+2+\zeta^{-2}
$$
and
$$
\alpha^3
=
\zeta^3+3\zeta+3\zeta^{-1}+\zeta^{-3}.
$$
Therefore
$$
\begin{aligned}
\alpha^3+\alpha^2-2\alpha-1
&=
\zeta^3+\zeta^2+\zeta+1
+\zeta^{-1}+\zeta^{-2}+\zeta^{-3}\\
&=
\zeta^{-3}
\left(
1+\zeta+\zeta^2+\zeta^3+\zeta^4+\zeta^5+\zeta^6
\right).
\end{aligned}
$$
Since $\zeta$ is a nontrivial seventh root of unity,
$$
1+\zeta+\cdots+\zeta^6=0.
$$
:::

<1>2. The polynomial
$$
p(t)\coloneqq t^3+t^2-2t-1
$$
is irreducible over $\QQ$.

::: {.proof}
The polynomial is primitive. Modulo $2$ it becomes
$$
\overline p(t)=t^3+t^2+1\in\FF_2[t].
$$
One has
$$
\overline p(0)=1
$$
and
$$
\overline p(1)=1+1+1=1
$$
in $\FF_2$. Thus the cubic $\overline p$ has no root in $\FF_2$.
A cubic over a field is reducible exactly when it has a linear factor,
equivalently a root. Hence $\overline p$ is irreducible over $\FF_2$.
Gauss's lemma then implies that $p$ is irreducible over $\QQ$.
:::

<1>3. The minimal polynomial of $\alpha$ over $\QQ$ is
$$
\boxed{t^3+t^2-2t-1},
$$
and
$$
[\QQ(\alpha):\QQ]=3.
$$

::: {.proof}
Step <1>1 shows that $p(\alpha)=0$, while step <1>2 shows that $p$ is
irreducible over $\QQ$. Since $p$ is monic, it is the minimal polynomial
of $\alpha$.
:::

<1>4. The number $\alpha$ is not contained in any finite extension
$K/\QQ$ whose degree is a power of $2$.

::: {.proof}
Suppose
$$
\alpha\in K
$$
and
$$
[K:\QQ]=2^r.
$$
Then
$$
\QQ\subseteq\QQ(\alpha)\subseteq K.
$$
By the tower formula and step <1>3,
$$
[K:\QQ]
=
[K:\QQ(\alpha)]
[\QQ(\alpha):\QQ]
=
3[K:\QQ(\alpha)].
$$
Thus $3$ divides $2^r$, which is impossible.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 supplies the required irreducible polynomial, and step <1>4 gives
the degree obstruction.
:::
:::
