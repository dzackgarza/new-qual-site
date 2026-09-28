---
schema: qual/card@1
id: P-BKF14-2B
kind: problem
title: Continuous functions on the plane bounded on every line need not be bounded
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet and its
    parabola-neighborhood counterexample.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked continuity, unboundedness along the parabola, and boundedness on
    both vertical and nonvertical affine lines for an explicit bump.
---

::: {.problem}
Either prove or describe a counterexample to the following statement: If a continuous realvalued function on the plane is bounded on all straight lines then it is bounded.
:::

::: {.solution}
Define
$$
\phi(t)\coloneqq\max\{0,1-|t|\}
$$
and
$$
f(x,y)\coloneqq x\,\phi(y-x^2).
$$

<1>1. The function $f:\RR^2\to\RR$ is continuous.

::: {.proof}
The functions $(x,y)\mapsto y-x^2$, $\phi$, and $(x,u)\mapsto xu$ are
continuous. Their composition and product therefore give a continuous
function $f$.
:::

<1>2. The function $f$ is unbounded on $\RR^2$.

::: {.proof}
Along the parabola $y=x^2$,
$$
f(x,x^2)
=
x\,\phi(0)
=
x.
$$
Hence, for example, $f(n,n^2)=n\to\infty$.
:::

<1>3. The restriction of $f$ to every vertical line is bounded.

::: {.proof}
On the line $x=c$,
$$
|f(c,y)|
=
|c|\,|\phi(y-c^2)|
\le
|c|,
$$
because $0\le\phi\le1$.
:::

<1>4. The restriction of $f$ to every nonvertical line is bounded.

::: {.proof}
Let the line be
$$
y=mx+b.
$$
If $f(x,mx+b)\ne0$, then
$$
|mx+b-x^2|<1.
$$
Consequently
$$
x^2
\le
|m|\,|x|+|b|+1.
$$
Writing $r=|x|$, this implies
$$
r^2-|m|r-(|b|+1)\le0,
$$
and hence
$$
|x|
\le
\frac{|m|+\sqrt{m^2+4(|b|+1)}}2.
$$
Since $|\phi|\le1$, every point of the line therefore satisfies
$$
|f(x,mx+b)|
\le
\frac{|m|+\sqrt{m^2+4(|b|+1)}}2.
$$
Thus the restriction to the line is bounded.
:::

<1>5. The proposed statement is false.

::: {.proof}
Steps <1>3--<1>4 show that the continuous function $f$ is bounded on
every straight line, whereas step <1>2 shows that $f$ is unbounded on
the plane.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 supplies the required counterexample.
:::
:::
