---
schema: qual/card@1
id: P-BKF10-2B
kind: problem
title: Galois group of $x^5-10x+5$ over $\mathbb Q$ is $S_5$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 2B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked Eisenstein irreducibility, the transitive-action/Cauchy
    argument for a 5-cycle, the exact real-root count, and complex
    conjugation as a transposition.
---

::: {.problem}
Show that the splitting field of
$$
x^5-10x+5
$$
over $\QQ$ has Galois group the symmetric group $S_5$ on five points.

You may assume that any subgroup of $S_5$ containing a $5$-cycle and a $2$-cycle is all of $S_5$.
:::

::: {.solution}
Put
$$
p(x)\coloneqq x^5-10x+5,
$$
let $L$ be its splitting field over $\QQ$, and set
$$
G\coloneqq\operatorname{Gal}(L/\QQ).
$$

<1>1. The polynomial $p$ is irreducible over $\QQ$.

::: {.proof}
Eisenstein's criterion applies at the prime $5$: every nonleading
coefficient is divisible by $5$, while the constant term $5$ is not
divisible by $25$. Hence $p$ is irreducible in $\QQ[x]$.
:::

<1>2. The group $G\le S_5$ contains a $5$-cycle.

::: {.proof}
Because $p$ is irreducible of degree $5$, $G$ acts transitively on its
five roots. If $\alpha$ is one root, orbit--stabilizer gives
$$
\abs{G}=5\abs{G_\alpha},
$$
so $5\mid\abs{G}$. By Cauchy's theorem, $G$ contains an element of order
$5$. Viewed as a permutation of five roots, any permutation of order
$5$ is a $5$-cycle.
:::

<1>3. The polynomial $p$ has at least three distinct real roots.

::: {.proof}
One has
$$
\lim_{x\to-\infty}p(x)=-\infty,
\qquad
p(0)=5>0,
$$
so the intermediate value theorem gives a negative real root. Also
$$
p(0)=5>0>p(1)=-4,
$$
so there is a root in $(0,1)$. Finally,
$$
p(1)=-4<0,
\qquad
\lim_{x\to\infty}p(x)=\infty,
$$
so there is a real root greater than $1$. These three intervals are
disjoint, so the roots are distinct.
:::

<1>4. The polynomial $p$ has at most three distinct real roots.

::: {.proof}
Its derivative is
$$
p'(x)=5x^4-10=5(x^4-2),
$$
which has exactly two real zeros, namely
$\pm2^{1/4}$. If $p$ had four distinct real roots, Rolle's theorem would
produce at least three distinct real zeros of $p'$, a contradiction.
:::

<1>5. Exactly three roots of $p$ are real, and the other two form one
nonreal complex-conjugate pair.

::: {.proof}
Steps <1>3 and <1>4 give exactly three distinct real roots. Since the
base field has characteristic $0$, the irreducible polynomial $p$ is
separable, so all five roots are distinct. The remaining two roots are
nonreal. Because $p$ has real coefficients, nonreal roots occur in
complex-conjugate pairs, so those two roots are conjugate to each other.
:::

<1>6. The group $G$ contains a transposition.

::: {.proof}
Complex conjugation preserves $L$, because it permutes the roots of the
real polynomial $p$, and it fixes $\QQ$. Hence its restriction to $L$
is an element of $G$. By step <1>5, it fixes the three real roots and
interchanges the two nonreal roots. Thus its permutation on the five
roots is a transposition.
:::

<1>7. Therefore
$$
\boxed{G\cong S_5}.
$$

::: {.proof}
Step <1>2 gives a $5$-cycle in $G$, and step <1>6 gives a $2$-cycle.
By the group-theoretic fact allowed in the problem, any subgroup of
$S_5$ containing both is all of $S_5$. Hence $G=S_5$ in its action on
the five roots.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 proves the required Galois-group identification.
:::
:::
